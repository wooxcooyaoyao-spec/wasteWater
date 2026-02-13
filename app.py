"""
污泥处理系统参数计算工具 - Streamlit 前端应用

功能：
1. 查看原始 Excel 数据
2. 参数计算工具
3. 参数对比分析
4. 敏感性分析
"""

import sys
from pathlib import Path

import pandas as pd
# 多语言支持
import streamlit as st

# 初始化语言和当前页面
if "language" not in st.session_state:
    st.session_state.language = "zh"
if "current_page" not in st.session_state:
    st.session_state.current_page = 0  # 默认首页

# 添加当前目录到路径
tool_dir = Path(__file__).parent
sys.path.insert(0, str(tool_dir))

# 导入翻译管理器
from i18n.translations import translation_manager

# 翻译函数
def t(key):
    """获取翻译文本"""
    return translation_manager.get(key, st.session_state.language)

from wastewater_treatment_calc import WastewaterCalculator

# ============================================================================
# 页面配置
# ============================================================================

st.set_page_config(
    page_title="污泥处理计算工具",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# 样式定制
# ============================================================================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2ca02c;
        border-bottom: 2px solid #2ca02c;
        padding-bottom: 0.5rem;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# 侧边栏导航
# ============================================================================

# 语言切换 - 使用回调函数保持页面位置
def set_language(lang):
    st.session_state.language = lang

st.sidebar.write("****")
col1, col2, col3 = st.sidebar.columns(3)
with col1:
    st.button("🇨🇳 中文", on_click=set_language, args=("zh",), key="btn_zh")
with col2:
    st.button("🇦🇺 English", on_click=set_language, args=("en",), key="btn_en")
with col3:
    st.button("🇮🇳 हिन्दी", on_click=set_language, args=("hi",), key="btn_hi")

col1, col2, col3 = st.sidebar.columns(3)
with col1:
    st.button("🇪🇸 Español", on_click=set_language, args=("es",), key="btn_es")
with col2:
    st.button("🇩🇪 Deutsch", on_click=set_language, args=("de",), key="btn_de")
with col3:
    st.button("🇸🇪 Svenska", on_click=set_language, args=("sv",), key="btn_sv")

st.sidebar.markdown("---")
st.sidebar.title(t("nav_menu"))

# 生成动态导航选项
page_options = [
    (" " + t("home"), "home"),
    (" " + t("calculator"), "calculator"),
    (" " + t("data"), "data"),
    (" " + t("comparison"), "comparison"),
    (" " + t("sensitivity"), "sensitivity"),
]
page_labels = [label for label, _ in page_options]
page_values = [value for _, value in page_options]

page_index = st.sidebar.radio(
    t("select_func"),
    range(len(page_labels)),
    format_func=lambda i: page_labels[i],
    index=st.session_state.current_page
)
page = page_values[page_index]
# 保存当前页面到 session_state
st.session_state.current_page = page_index

st.sidebar.markdown("---")
st.sidebar.title(t("help"))
st.sidebar.info(t("quick_guide"))

# ============================================================================
# 页面：首页
# ============================================================================

if page == "home":
    st.markdown(f'<h1 class="main-header">{t("title")}</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <h3>{t("calculator_feature")}</h3>
            <p>{t("calculator_desc")}</p>
            <ul>
                <li>{t("feature_slr")}</li>
                <li>{t("feature_mlss")}</li>
                <li>{t("feature_flow")}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <h3>{t("data_feature")}</h3>
            <p>{t("data_desc")}</p>
            <ul>
                <li>{t("feature_table")}</li>
                <li>{t("feature_export")}</li>
                <li>{t("feature_search")}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-box">
            <h3>{t("analysis_feature")}</h3>
            <p>{t("analysis_desc")}</p>
            <ul>
                <li>{t("feature_comparison")}</li>
                <li>{t("feature_sensitivity")}</li>
                <li>{t("feature_report")}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 核心参数说明
    st.markdown(f'<h3 class="section-header">{t("core_params")}</h3>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        **{t("param_mlss")}**
        - {t("unit_mg_l")}
        - {t("range_safe")}: 2,000 - 5,400 mg/L
        - {t("range_optimal")}: 3,000 - 4,500 mg/L
        """)

    with col2:
        st.markdown(f"""
        **{t("param_eq")}**
        - {t("unit_l_s")}
        - {t("range_safe")}: 60 - 170 L/s
        - {t("range_optimal")}: 90 - 130 L/s
        """)

    with col3:
        st.markdown(f"""
        **{t("param_slr")}**
        - {t("unit_kg_h_m2")}
        - {t("range_safe")}: 3.0 - 24.0 kg/h/m²
        - {t("range_optimal")}: 8.0 - 16.0 kg/h/m²
        """)

    st.markdown("---")

    # 计算公式
    st.markdown(f'<h3 class="section-header">{t("formula")}</h3>', unsafe_allow_html=True)
    st.latex(r"""
    SLR = \frac{MLSS}{1000} \times \frac{EQ \times 3.6}{Area}
    """)
    st.markdown(t("formula_explanation"))
    st.markdown(f"- {t('formula_coefficient')}")
    st.markdown(f"- {t('formula_mg_kg')}")
    st.markdown(f"- {t('formula_area')}")

# ============================================================================
# 页面 2：计算工具
# ============================================================================

elif page == "calculator":
    st.markdown(f'<h2 class="section-header">{t("calc_tool_title")}</h2>', unsafe_allow_html=True)

    # 计算器初始化
    calc = WastewaterCalculator(area=1.0)

    st.info(t("calc_hint"))

    # 计算模式选择
    col1, col2 = st.columns(2)
    with col1:
        mode_options = [t("mode_slr"), t("mode_mlss"), t("mode_flow")]
        calc_mode_index = st.radio(
            t("select_mode"),
            range(len(mode_options)),
            format_func=lambda i: mode_options[i],
            horizontal=False
        )
        calc_mode = mode_options[calc_mode_index]

    # 处理面积设置
    with col2:
        area = st.number_input(
            t("area_label"),
            min_value=0.1,
            max_value=100.0,
            value=1.0,
            step=0.1
        )
        calc = WastewaterCalculator(area=area)

    st.markdown("---")

    # 根据模式进行计算
    if calc_mode_index == 0:  # 计算 SLR
        st.markdown(f'<h3 class="section-header">{t("mode_calc_slr")}</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            mlss = st.number_input(
                t("label_mlss"),
                min_value=0.0,
                max_value=10000.0,
                value=3500.0,
                step=100.0
            )

        with col2:
            eq = st.number_input(
                t("label_flow"),
                min_value=0.0,
                max_value=500.0,
                value=100.0,
                step=5.0
            )

        # 计算
        if st.button(t("btn_calculate"), key="calc_slr"):
            slr = calc.calculate_slr(mlss, eq)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(t("result_label"), f"{slr:.2f} {t('result_slr_unit')}", delta=None)

            # 安全性检查
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = t("status_safe") if check['overall_safe'] else t("status_adjust")
                st.metric(t("status_label"), status, delta=None)

            # 状态详情
            with col3:
                slr_status = check['slr']['status']
                status_map = {
                    'optimal': t("status_optimal"),
                    'normal': t("status_normal"),
                    'too_low': t("status_low"),
                    'too_high': t("status_high")
                }
                st.metric(t("slr_status"), status_map.get(slr_status, slr_status), delta=None)

            st.markdown("---")

            # 详细分析
            st.markdown(f'<h4>{t("detailed_analysis")}</h4>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            with col1:
                mlss_status = check['mlss']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(mlss_status, '⚪')
                st.write(f"{status_emoji} **MLSS**: {check['mlss']['value']:.0f} mg/L")
                st.write(f"   {t('state_label')}{status_map.get(mlss_status, mlss_status)}")

            with col2:
                eq_status = check['equivalent_flow']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(eq_status, '⚪')
                st.write(f"{status_emoji} **Flow**: {check['equivalent_flow']['value']:.2f} L/s")
                st.write(f"   {t('state_label')}{status_map.get(eq_status, eq_status)}")

            with col3:
                slr_status = check['slr']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(slr_status, '⚪')
                st.write(f"{status_emoji} **SLR**: {check['slr']['value']:.2f} kg/h/m²")
                st.write(f"   {t('state_label')}{status_map.get(slr_status, slr_status)}")

            st.markdown("---")

            # 建议
            if check['recommendations']:
                st.markdown(f'<h4>{t("recommendations")}</h4>', unsafe_allow_html=True)
                for rec_key in check['recommendations']:
                    st.info(t(rec_key))

    elif calc_mode_index == 1:  # 计算 MLSS
        st.markdown(f'<h3 class="section-header">{t("mode_calc_mlss")}</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            slr = st.number_input(
                t("label_slr"),
                min_value=0.0,
                max_value=100.0,
                value=12.0,
                step=0.5
            )

        with col2:
            eq = st.number_input(
                t("label_flow"),
                min_value=0.0,
                max_value=500.0,
                value=100.0,
                step=5.0
            )

        if st.button(t("btn_calculate"), key="calc_mlss"):
            mlss = calc.calculate_mlss(slr, eq)

            col1, col2 = st.columns(2)
            with col1:
                st.metric(t("result_label"), f"{mlss:.0f} mg/L", delta=None)

            # 验证结果
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = t("status_safe") if check['overall_safe'] else t("status_adjust")
                st.metric(t("status_label"), status, delta=None)

            if check['recommendations']:
                st.markdown(f'<h4>{t("recommendations")}</h4>', unsafe_allow_html=True)
                for rec_key in check['recommendations']:
                    st.info(t(rec_key))

    else:  # 计算流量
        st.markdown(f'<h3 class="section-header">{t("mode_calc_flow")}</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            mlss = st.number_input(
                t("label_mlss"),
                min_value=0.0,
                max_value=10000.0,
                value=3500.0,
                step=100.0
            )

        with col2:
            slr = st.number_input(
                t("label_slr"),
                min_value=0.0,
                max_value=100.0,
                value=12.0,
                step=0.5
            )

        if st.button(t("btn_calculate"), key="calc_flow"):
            eq = calc.calculate_equivalent_flow(mlss, slr)

            col1, col2 = st.columns(2)
            with col1:
                st.metric(t("result_label"), f"{eq:.2f} L/s", delta=None)

            # 验证结果
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = t("status_safe") if check['overall_safe'] else t("status_adjust")
                st.metric(t("status_label"), status, delta=None)

            if check['recommendations']:
                st.markdown(f'<h4>{t("recommendations")}</h4>', unsafe_allow_html=True)
                for rec_key in check['recommendations']:
                    st.info(t(rec_key))

# ============================================================================
# 页面：数据查看
# ============================================================================

elif page == "data":
    st.markdown(f'<h2 class="section-header">{t("data_view_title")}</h2>', unsafe_allow_html=True)

    st.info(t("data_hint"))

    # 查找数据文件
    data_dir = tool_dir / "data"
    excel_file = data_dir / "MLSS浓度表.xlsx"

    if excel_file.exists():
        try:
            # 读取 Excel 文件
            df = pd.read_excel(excel_file, sheet_name=0, header=None)

            # 填充 NaN 值，防止 Arrow 转换错误
            df = df.fillna("")

            # 将所有数据转换为字符串类型，确保兼容性
            df = df.astype(str)

            st.markdown(f'<h3 class="section-header">{t("table_data")}</h3>', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, height=400)

            st.markdown("---")

            # 数据统计
            st.markdown(f'<h3 class="section-header">{t("data_stats")}</h3>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(t("stat_rows"), len(df))
            with col2:
                st.metric(t("stat_cols"), len(df.columns))
            with col3:
                st.metric(t("stat_points"), len(df) * len(df.columns))

            st.markdown("---")

            # 下载选项
            st.markdown(f'<h3 class="section-header">{t("data_export")}</h3>', unsafe_allow_html=True)

            # 转换为 CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label=t("btn_download_csv"),
                data=csv,
                file_name="MLSS浓度表.csv",
                mime="text/csv"
            )

            # 转换为 Excel
            try:
                from openpyxl import Workbook
                buffer = pd.ExcelWriter("temp.xlsx", engine='openpyxl')
                df.to_excel(buffer, index=False)
                st.success(t("excel_available"))
            except:
                st.warning(t("excel_warning"))

        except Exception as e:
            st.error(f"{t('read_excel_failed')} {str(e)}")

    else:
        st.error(f"{t('file_not_found')} {excel_file}")
        st.info(f"{t('expected_location')} {excel_file}")

# ============================================================================
# 页面：参数对比
# ============================================================================

elif page == "comparison":
    st.markdown(f'<h2 class="section-header">{t("comparison_title")}</h2>', unsafe_allow_html=True)

    st.info(t("comparison_hint"))

    # 输入方案数量
    num_schemes = st.number_input(
        t("num_schemes"),
        min_value=2,
        max_value=10,
        value=3,
        step=1
    )

    schemes = {}

    st.markdown(f'<h3 class="section-header">{t("scheme_definition")}</h3>', unsafe_allow_html=True)

    cols = st.columns(num_schemes)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"**{t('scheme_num')} {i+1}**")
            scheme_name = st.text_input(f"{t('scheme_name')} {i+1}", value=f"{t('scheme_num')}{i+1}", key=f"name_{i}")
            mlss = st.number_input(f"MLSS {i+1} (mg/L)", value=3500.0 + i*200, step=100.0, key=f"mlss_{i}")
            eq = st.number_input(f"Flow {i+1} (L/s)", value=100.0 + i*10, step=5.0, key=f"eq_{i}")
            schemes[scheme_name] = {'mlss': mlss, 'flow': eq}

    if st.button(t("btn_generate_report")):
        st.markdown(f'<h3 class="section-header">{t("comparison_result")}</h3>', unsafe_allow_html=True)

        calc = WastewaterCalculator(area=1.0)
        comparison_data = []

        status_map = {
            'optimal': t("status_optimal"),
            'normal': t("status_normal"),
            'too_low': t("status_low"),
            'too_high': t("status_high")
        }

        for scheme_name, params in schemes.items():
            mlss = params['mlss']
            eq = params['flow']
            slr = calc.calculate_slr(mlss, eq)
            check = calc.check_operating_point(mlss, eq)

            comparison_data.append({
                t("column_scheme"): scheme_name,
                t("column_mlss"): f"{mlss:.0f}",
                t("column_flow"): f"{eq:.1f}",
                t("column_slr"): f"{slr:.2f}",
                t("column_mlss_status"): status_map.get(check['mlss']['status'], ''),
                t("column_flow_status"): status_map.get(check['equivalent_flow']['status'], ''),
                t("column_slr_status"): status_map.get(check['slr']['status'], ''),
                t("column_overall"): t("status_safe") if check['overall_safe'] else t("status_adjust")
            })

        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True)

        # 对比可视化
        st.markdown(f'<h3 class="section-header">{t("viz_title")}</h3>', unsafe_allow_html=True)

        plot_data = []
        for scheme_name, params in schemes.items():
            mlss = params['mlss']
            eq = params['flow']
            slr = calc.calculate_slr(mlss, eq)
            plot_data.append({
                t("column_scheme"): scheme_name,
                'MLSS': mlss,
                'Flow': eq,
                'SLR': slr
            })

        df_plot = pd.DataFrame(plot_data)

        col1, col2 = st.columns(2)

        with col1:
            st.bar_chart(df_plot.set_index(t("column_scheme"))[['MLSS']])

        with col2:
            st.bar_chart(df_plot.set_index(t("column_scheme"))[['Flow']])

# ============================================================================
# 页面：敏感性分析
# ============================================================================

else:  # 敏感性分析
    st.markdown(f'<h2 class="section-header">{t("sensitivity_title")}</h2>', unsafe_allow_html=True)

    st.info(t("sensitivity_hint"))

    # 基础参数设置
    col1, col2 = st.columns(2)
    with col1:
        base_mlss = st.number_input(
            t("label_base_mlss"),
            min_value=1000.0,
            max_value=6000.0,
            value=3500.0,
            step=100.0
        )

    with col2:
        base_eq = st.number_input(
            t("label_base_flow"),
            min_value=30.0,
            max_value=200.0,
            value=100.0,
            step=5.0
        )

    st.markdown("---")

    # 分析类型选择
    analysis_options = [t("analysis_mlss"), t("analysis_flow")]
    analysis_type_index = st.radio(
        t("select_analysis"),
        range(len(analysis_options)),
        format_func=lambda i: analysis_options[i],
        horizontal=True
    )
    analysis_type = analysis_options[analysis_type_index]

    if st.button(t("btn_generate_sensitivity")):
        calc = WastewaterCalculator(area=1.0)

        st.markdown(f'<h3 class="section-header">{t("sensitivity_result")}</h3>', unsafe_allow_html=True)

        if analysis_type_index == 0:  # MLSS 敏感性分析
            # MLSS 变化，固定 Flow
            mlss_range = range(2000, 5600, 200)
            slr_values = []

            for mlss in mlss_range:
                slr = calc.calculate_slr(mlss, base_eq)
                slr_values.append(slr)

            # 创建数据框
            df_sensitivity = pd.DataFrame({
                t("column_mlss"): mlss_range,
                t("column_slr"): slr_values
            })

            # 绘制图表
            st.line_chart(df_sensitivity.set_index(t("column_mlss")))

            # 显示数据表
            st.markdown(f'<h4>{t("data_table")}</h4>', unsafe_allow_html=True)
            st.dataframe(df_sensitivity, use_container_width=True)

        else:  # Flow 敏感性分析
            # Flow 变化，固定 MLSS
            eq_range = range(60, 180, 10)
            slr_values = []

            for eq in eq_range:
                slr = calc.calculate_slr(base_mlss, eq)
                slr_values.append(slr)

            # 创建数据框
            df_sensitivity = pd.DataFrame({
                t("column_flow"): eq_range,
                t("column_slr"): slr_values
            })

            # 绘制图表
            st.line_chart(df_sensitivity.set_index(t("column_flow")))

            # 显示数据表
            st.markdown(f'<h4>{t("data_table")}</h4>', unsafe_allow_html=True)
            st.dataframe(df_sensitivity, use_container_width=True)

# ============================================================================
# 页脚
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;">
    <p>污泥处理系统参数计算工具 v1.0.0 | Powered by Streamlit</p>
    <p>© 2026 WasteWaterTool | 保留所有权利</p>
</div>
""", unsafe_allow_html=True)

