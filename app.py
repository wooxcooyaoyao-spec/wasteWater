"""
污泥处理系统参数计算工具 - Streamlit 前端应用

功能：
1. 查看原始 Excel 数据
2. 参数计算工具
3. 参数对比分析
4. 敏感性分析
"""

# 多语言支持
import streamlit as st

# 初始化语言
if "language" not in st.session_state:
    st.session_state.language = "zh"

# 简单的翻译字典（最小集合）
TEXTS = {
    "zh": {
        "title": "💧 污泥处理系统参数计算工具",
        "nav_menu": "🚀 导航菜单",
        "help": "📚 帮助",
        "home": "📊 首页",
        "calculator": "🔧 计算工具",
        "data": "📈 数据查看",
        "comparison": "🔀 参数对比",
        "sensitivity": "📉 敏感性分析",
    },
    "en": {
        "title": "💧 Wastewater Treatment System Parameter Calculator",
        "nav_menu": "🚀 Navigation Menu",
        "help": "📚 Help",
        "home": "📊 Home",
        "calculator": "🔧 Calculator",
        "data": "📈 Data View",
        "comparison": "🔀 Comparison",
        "sensitivity": "📉 Sensitivity",
    }
}

def t(key):
    """获取翻译文本"""
    lang = st.session_state.get("language", "zh")
    return TEXTS.get(lang, TEXTS["zh"]).get(key, key)
import pandas as pd
from pathlib import Path
import sys

# 添加当前目录到路径
tool_dir = Path(__file__).parent
sys.path.insert(0, str(tool_dir))

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

# 语言切换
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("🇨🇳 中文"):
        st.session_state.language = "zh"
        st.rerun()
with col2:
    if st.button("🇬🇧 English"):
        st.session_state.language = "en"
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.title(t("nav_menu"))
page = st.sidebar.radio(
    "选择功能",
    ["📊 首页", "🔧 计算工具", "📈 数据查看", "🔀 参数对比", "📉 敏感性分析"]
)

st.sidebar.markdown("---")
st.sidebar.title(t("help"))
st.sidebar.info("""
### 快速指南

**计算工具**
- 输入 MLSS、流量或 SLR
- 快速计算其他参数
- 自动检查安全性

**数据查看**
- 查看原始参考数据
- 支持搜索和筛选

**参数对比**
- 对比多个运行方案
- 评估安全性

**敏感性分析**
- 分析参数变化影响
""")

# ============================================================================
# 页面 1：首页
# ============================================================================

if page == "📊 首页":
    st.markdown(f'<h1 class="main-header">{t("title")}</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-box">
            <h3>🔧 计算工具</h3>
            <p>快速计算参数，包括：</p>
            <ul>
                <li>SLR 固体负荷率</li>
                <li>MLSS 浓度</li>
                <li>等效流量</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-box">
            <h3>📊 数据查看</h3>
            <p>查看和导出数据：</p>
            <ul>
                <li>原始参考表</li>
                <li>数据导出</li>
                <li>数据搜索</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
            <h3>📈 分析工具</h3>
            <p>深度分析功能：</p>
            <ul>
                <li>参数对比</li>
                <li>敏感性分析</li>
                <li>报告导出</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # 核心参数说明
    st.markdown('<h3 class="section-header">核心参数说明</h3>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **MLSS（混合液悬浮固体浓度）**
        - 单位：mg/L
        - 安全范围：2,000 - 5,400 mg/L
        - 最优范围：3,000 - 4,500 mg/L
        """)

    with col2:
        st.markdown("""
        **EQ（等效流量）**
        - 单位：L/s
        - 安全范围：60 - 170 L/s
        - 最优范围：90 - 130 L/s
        """)

    with col3:
        st.markdown("""
        **SLR（固体负荷率）**
        - 单位：kg/h/m²
        - 安全范围：3.0 - 24.0 kg/h/m²
        - 最优范围：8.0 - 16.0 kg/h/m²
        """)

    st.markdown("---")

    # 计算公式
    st.markdown('<h3 class="section-header">计算公式</h3>', unsafe_allow_html=True)
    st.latex(r"""
    SLR = \frac{MLSS}{1000} \times \frac{EQ \times 3.6}{面积}
    """)
    st.markdown("其中：")
    st.markdown("- 3.6：秒/小时的换算系数")
    st.markdown("- 1000：mg 到 kg 的换算系数")
    st.markdown("- 面积（m²）：处理单元面积，默认为 1")

# ============================================================================
# 页面 2：计算工具
# ============================================================================

elif page == "🔧 计算工具":
    st.markdown('<h2 class="section-header">参数计算工具</h2>', unsafe_allow_html=True)

    # 计算器初始化
    calc = WastewaterCalculator(area=1.0)

    st.info("💡 选择要计算的参数，输入已知值，系统将自动计算其他参数并检查安全性")

    # 计算模式选择
    col1, col2 = st.columns(2)
    with col1:
        calc_mode = st.radio(
            "选择计算模式",
            ["计算 SLR", "计算 MLSS", "计算流量"],
            horizontal=False
        )

    # 处理面积设置
    with col2:
        area = st.number_input(
            "处理面积 (m²)",
            min_value=0.1,
            max_value=100.0,
            value=1.0,
            step=0.1
        )
        calc = WastewaterCalculator(area=area)

    st.markdown("---")

    # 根据模式进行计算
    if calc_mode == "计算 SLR":
        st.markdown('<h3 class="section-header">模式：计算 SLR</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            mlss = st.number_input(
                "MLSS 浓度 (mg/L)",
                min_value=0.0,
                max_value=10000.0,
                value=3500.0,
                step=100.0
            )

        with col2:
            eq = st.number_input(
                "等效流量 (L/s)",
                min_value=0.0,
                max_value=500.0,
                value=100.0,
                step=5.0
            )

        # 计算
        if st.button("🔄 计算", key="calc_slr"):
            slr = calc.calculate_slr(mlss, eq)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("计算结果", f"{slr:.2f} kg/h/m²", delta=None)

            # 安全性检查
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = "✓ 安全" if check['overall_safe'] else "✗ 需要调整"
                st.metric("运行状态", status, delta=None)

            # 状态详情
            with col3:
                slr_status = check['slr']['status']
                status_map = {
                    'optimal': '🟢 最优',
                    'normal': '🟡 正常',
                    'too_low': '🔵 过低',
                    'too_high': '🔴 过高'
                }
                st.metric("SLR 状态", status_map.get(slr_status, slr_status), delta=None)

            st.markdown("---")

            # 详细分析
            st.markdown('<h4>详细状态分析</h4>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            with col1:
                mlss_status = check['mlss']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(mlss_status, '⚪')
                st.write(f"{status_emoji} **MLSS**: {check['mlss']['value']:.0f} mg/L")
                st.write(f"   状态：{status_map.get(mlss_status, mlss_status)}")

            with col2:
                eq_status = check['equivalent_flow']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(eq_status, '⚪')
                st.write(f"{status_emoji} **Flow**: {check['equivalent_flow']['value']:.2f} L/s")
                st.write(f"   状态：{status_map.get(eq_status, eq_status)}")

            with col3:
                slr_status = check['slr']['status']
                status_emoji = {'optimal': '🟢', 'normal': '🟡', 'too_low': '🔵', 'too_high': '🔴'}.get(slr_status, '⚪')
                st.write(f"{status_emoji} **SLR**: {check['slr']['value']:.2f} kg/h/m²")
                st.write(f"   状态：{status_map.get(slr_status, slr_status)}")

            st.markdown("---")

            # 建议
            if check['recommendations']:
                st.markdown('<h4>💡 运行建议</h4>', unsafe_allow_html=True)
                for rec in check['recommendations']:
                    st.info(rec)

    elif calc_mode == "计算 MLSS":
        st.markdown('<h3 class="section-header">模式：计算 MLSS</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            slr = st.number_input(
                "SLR (kg/h/m²)",
                min_value=0.0,
                max_value=100.0,
                value=12.0,
                step=0.5
            )

        with col2:
            eq = st.number_input(
                "等效流量 (L/s)",
                min_value=0.0,
                max_value=500.0,
                value=100.0,
                step=5.0
            )

        if st.button("🔄 计算", key="calc_mlss"):
            mlss = calc.calculate_mlss(slr, eq)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("计算结果", f"{mlss:.0f} mg/L", delta=None)

            # 验证结果
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = "✓ 安全" if check['overall_safe'] else "✗ 需要调整"
                st.metric("运行状态", status, delta=None)

            if check['recommendations']:
                st.markdown('<h4>💡 运行建议</h4>', unsafe_allow_html=True)
                for rec in check['recommendations']:
                    st.info(rec)

    else:  # 计算流量
        st.markdown('<h3 class="section-header">模式：计算流量</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            mlss = st.number_input(
                "MLSS 浓度 (mg/L)",
                min_value=0.0,
                max_value=10000.0,
                value=3500.0,
                step=100.0
            )

        with col2:
            slr = st.number_input(
                "SLR (kg/h/m²)",
                min_value=0.0,
                max_value=100.0,
                value=12.0,
                step=0.5
            )

        if st.button("🔄 计算", key="calc_flow"):
            eq = calc.calculate_equivalent_flow(mlss, slr)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("计算结果", f"{eq:.2f} L/s", delta=None)

            # 验证结果
            check = calc.check_operating_point(mlss, eq)
            with col2:
                status = "✓ 安全" if check['overall_safe'] else "✗ 需要调整"
                st.metric("运行状态", status, delta=None)

            if check['recommendations']:
                st.markdown('<h4>💡 运行建议</h4>', unsafe_allow_html=True)
                for rec in check['recommendations']:
                    st.info(rec)

# ============================================================================
# 页面 3：数据查看
# ============================================================================

elif page == "📈 数据查看":
    st.markdown('<h2 class="section-header">原始数据查看</h2>', unsafe_allow_html=True)

    st.info("💡 此页面展示 MLSS 浓度表的原始数据")

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

            st.markdown('<h3 class="section-header">表格数据</h3>', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True, height=400)

            st.markdown("---")

            # 数据统计
            st.markdown('<h3 class="section-header">数据统计</h3>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("表格行数", len(df))
            with col2:
                st.metric("表格列数", len(df.columns))
            with col3:
                st.metric("数据点数", len(df) * len(df.columns))

            st.markdown("---")

            # 下载选项
            st.markdown('<h3 class="section-header">数据导出</h3>', unsafe_allow_html=True)

            # 转换为 CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 下载为 CSV",
                data=csv,
                file_name="MLSS浓度表.csv",
                mime="text/csv"
            )

            # 转换为 Excel
            try:
                from openpyxl import Workbook
                buffer = pd.ExcelWriter("temp.xlsx", engine='openpyxl')
                df.to_excel(buffer, index=False)
                st.success("✓ Excel 导出功能可用")
            except:
                st.warning("⚠️ Excel 导出需要额外依赖")

        except Exception as e:
            st.error(f"❌ 读取 Excel 文件失败: {str(e)}")

    else:
        st.error(f"❌ 找不到数据文件: {excel_file}")
        st.info(f"期望位置：{excel_file}")

# ============================================================================
# 页面 4：参数对比
# ============================================================================

elif page == "🔀 参数对比":
    st.markdown('<h2 class="section-header">参数对比分析</h2>', unsafe_allow_html=True)

    st.info("💡 对比多个运行方案，找到最优解决方案")

    # 输入方案数量
    num_schemes = st.number_input(
        "方案数量",
        min_value=2,
        max_value=10,
        value=3,
        step=1
    )

    schemes = {}

    st.markdown('<h3 class="section-header">方案定义</h3>', unsafe_allow_html=True)

    cols = st.columns(num_schemes)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"**方案 {i+1}**")
            scheme_name = st.text_input(f"方案名称 {i+1}", value=f"方案{i+1}", key=f"name_{i}")
            mlss = st.number_input(f"MLSS {i+1} (mg/L)", value=3500.0 + i*200, step=100.0, key=f"mlss_{i}")
            eq = st.number_input(f"Flow {i+1} (L/s)", value=100.0 + i*10, step=5.0, key=f"eq_{i}")
            schemes[scheme_name] = {'mlss': mlss, 'flow': eq}

    if st.button("📊 生成对比报告"):
        st.markdown('<h3 class="section-header">对比结果</h3>', unsafe_allow_html=True)

        calc = WastewaterCalculator(area=1.0)
        comparison_data = []

        for scheme_name, params in schemes.items():
            mlss = params['mlss']
            eq = params['flow']
            slr = calc.calculate_slr(mlss, eq)
            check = calc.check_operating_point(mlss, eq)

            comparison_data.append({
                '方案': scheme_name,
                'MLSS (mg/L)': f"{mlss:.0f}",
                'Flow (L/s)': f"{eq:.1f}",
                'SLR (kg/h/m²)': f"{slr:.2f}",
                'MLSS状态': check['mlss']['status'],
                'Flow状态': check['equivalent_flow']['status'],
                'SLR状态': check['slr']['status'],
                '整体安全': "✓ 安全" if check['overall_safe'] else "✗ 需要调整"
            })

        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True)

        # 对比可视化
        st.markdown('<h3 class="section-header">参数可视化</h3>', unsafe_allow_html=True)

        plot_data = []
        for scheme_name, params in schemes.items():
            mlss = params['mlss']
            eq = params['flow']
            slr = calc.calculate_slr(mlss, eq)
            plot_data.append({
                '方案': scheme_name,
                'MLSS': mlss,
                'Flow': eq,
                'SLR': slr
            })

        df_plot = pd.DataFrame(plot_data)

        col1, col2 = st.columns(2)

        with col1:
            st.bar_chart(df_plot.set_index('方案')[['MLSS']])

        with col2:
            st.bar_chart(df_plot.set_index('方案')[['Flow']])

# ============================================================================
# 页面 5：敏感性分析
# ============================================================================

else:  # 敏感性分析
    st.markdown('<h2 class="section-header">敏感性分析</h2>', unsafe_allow_html=True)

    st.info("💡 分析参数变化对结果的影响")

    # 基础参数设置
    col1, col2 = st.columns(2)
    with col1:
        base_mlss = st.number_input(
            "基础 MLSS (mg/L)",
            min_value=1000.0,
            max_value=6000.0,
            value=3500.0,
            step=100.0
        )

    with col2:
        base_eq = st.number_input(
            "基础 Flow (L/s)",
            min_value=30.0,
            max_value=200.0,
            value=100.0,
            step=5.0
        )

    st.markdown("---")

    # 分析类型选择
    analysis_type = st.radio(
        "选择分析类型",
        ["MLSS 敏感性分析", "Flow 敏感性分析"],
        horizontal=True
    )

    if st.button("📉 生成敏感性分析图"):
        calc = WastewaterCalculator(area=1.0)

        st.markdown('<h3 class="section-header">敏感性分析结果</h3>', unsafe_allow_html=True)

        if analysis_type == "MLSS 敏感性分析":
            # MLSS 变化，固定 Flow
            mlss_range = range(2000, 5600, 200)
            slr_values = []

            for mlss in mlss_range:
                slr = calc.calculate_slr(mlss, base_eq)
                slr_values.append(slr)

            # 创建数据框
            df_sensitivity = pd.DataFrame({
                'MLSS (mg/L)': mlss_range,
                'SLR (kg/h/m²)': slr_values
            })

            # 绘制图表
            st.line_chart(df_sensitivity.set_index('MLSS (mg/L)'))

            # 显示数据表
            st.markdown('<h4>数据表</h4>', unsafe_allow_html=True)
            st.dataframe(df_sensitivity, use_container_width=True)

        else:
            # Flow 变化，固定 MLSS
            eq_range = range(60, 180, 10)
            slr_values = []

            for eq in eq_range:
                slr = calc.calculate_slr(base_mlss, eq)
                slr_values.append(slr)

            # 创建数据框
            df_sensitivity = pd.DataFrame({
                'Flow (L/s)': eq_range,
                'SLR (kg/h/m²)': slr_values
            })

            # 绘制图表
            st.line_chart(df_sensitivity.set_index('Flow (L/s)'))

            # 显示数据表
            st.markdown('<h4>数据表</h4>', unsafe_allow_html=True)
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

