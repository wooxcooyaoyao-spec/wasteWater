"""
xlwings 集成模块 - 在 Excel 中直接使用污泥处理参数计算

这个模块提供了 xlwings 的自定义函数，可以在 Excel 中直接调用
"""

try:
    import xlwings as xw
    XLWINGS_AVAILABLE = True
except ImportError:
    XLWINGS_AVAILABLE = False
    print("⚠️ xlwings 未安装，部分功能不可用")

from wastewater_treatment_calc import WastewaterCalculator


class WastewaterExcelFunctions:
    """污泥处理 Excel 自定义函数类"""

    def __init__(self):
        self.calculator = WastewaterCalculator(area=1.0)

    @staticmethod
    def calculate_slr(mlss: float, equivalent_flow: float, area: float = 1.0) -> float:
        """
        Excel 函数：计算 SLR

        使用方式（在 Excel 中）:
            =calculate_slr(3500, 100, 1.0)

        Args:
            mlss: MLSS 浓度 (mg/L)
            equivalent_flow: 等效流量 (L/s)
            area: 面积 (m²)，默认 1

        Returns:
            固体负荷率 (kg/h/m²)
        """
        calculator = WastewaterCalculator(area=area)
        return round(calculator.calculate_slr(mlss, equivalent_flow), 2)

    @staticmethod
    def calculate_mlss(slr: float, equivalent_flow: float, area: float = 1.0) -> float:
        """
        Excel 函数：计算 MLSS

        使用方式（在 Excel 中）:
            =calculate_mlss(12, 100, 1.0)
        """
        calculator = WastewaterCalculator(area=area)
        return round(calculator.calculate_mlss(slr, equivalent_flow), 0)

    @staticmethod
    def calculate_flow(mlss: float, slr: float, area: float = 1.0) -> float:
        """
        Excel 函数：计算等效流量

        使用方式（在 Excel 中）:
            =calculate_flow(3500, 12, 1.0)
        """
        calculator = WastewaterCalculator(area=area)
        return round(calculator.calculate_equivalent_flow(mlss, slr), 2)

    @staticmethod
    def check_safety(mlss: float, equivalent_flow: float) -> str:
        """
        Excel 函数：检查运行点是否安全

        使用方式（在 Excel 中）:
            =check_safety(3500, 100)

        Returns:
            "✓ 安全" 或 "✗ 需要调整"
        """
        calculator = WastewaterCalculator(area=1.0)
        check = calculator.check_operating_point(mlss, equivalent_flow)
        return '✓ 安全' if check['overall_safe'] else '✗ 需要调整'

    @staticmethod
    def get_slr_status(mlss: float, equivalent_flow: float) -> str:
        """
        Excel 函数：获取 SLR 状态

        Returns:
            "optimal", "normal", "too_low", "too_high"
        """
        calculator = WastewaterCalculator(area=1.0)
        check = calculator.check_operating_point(mlss, equivalent_flow)
        return check['slr']['status']

    @staticmethod
    def get_recommendations(mlss: float, equivalent_flow: float) -> str:
        """
        Excel 函数：获取运行建议

        Returns:
            建议文本（用 | 分隔多条建议）
        """
        calculator = WastewaterCalculator(area=1.0)
        check = calculator.check_operating_point(mlss, equivalent_flow)
        return ' | '.join(check['recommendations'])


def register_xlwings_functions():
    """
    注册 xlwings 自定义函数

    使用方式：
    1. 确保 xlwings 已安装: pip install xlwings
    2. 在 Excel 中启用 Python 宏（需要 Excel 365 或 xlwings Server）
    3. 调用此函数以注册所有自定义函数
    """
    if not XLWINGS_AVAILABLE:
        print("✗ xlwings 未安装，无法注册函数")
        return

    @xw.func
    def CalcSLR(mlss, equivalent_flow, area=1.0):
        """计算 SLR"""
        return WastewaterExcelFunctions.calculate_slr(mlss, equivalent_flow, area)

    @xw.func
    def CalcMLSS(slr, equivalent_flow, area=1.0):
        """计算 MLSS"""
        return WastewaterExcelFunctions.calculate_mlss(slr, equivalent_flow, area)

    @xw.func
    def CalcFlow(mlss, slr, area=1.0):
        """计算流量"""
        return WastewaterExcelFunctions.calculate_flow(mlss, slr, area)

    @xw.func
    def CheckSafety(mlss, equivalent_flow):
        """检查安全性"""
        return WastewaterExcelFunctions.check_safety(mlss, equivalent_flow)

    @xw.func
    def GetSLRStatus(mlss, equivalent_flow):
        """获取 SLR 状态"""
        return WastewaterExcelFunctions.get_slr_status(mlss, equivalent_flow)

    @xw.func
    def GetRecommendations(mlss, equivalent_flow):
        """获取建议"""
        return WastewaterExcelFunctions.get_recommendations(mlss, equivalent_flow)

    print("✓ xlwings 自定义函数已注册")


def create_interactive_dashboard():
    """创建交互式仪表板 Excel 文件"""
    if not XLWINGS_AVAILABLE:
        print("✗ xlwings 未安装")
        return

    wb = xw.Book()
    ws = wb.sheets[0]
    ws.name = "污泥处理计算器"

    # 标题
    ws['A1'] = '污泥处理系统实时计算器'
    ws['A1'].font = xw.Font(name='Microsoft YaHei', bold=True, size=18)

    # 输入区域
    ws['A3'] = '输入参数'
    ws['A3'].font = xw.Font(bold=True, size=12)

    ws['A4'] = 'MLSS (mg/L):'
    ws['B4'] = 3500

    ws['A5'] = 'Equivalent Flow (L/s):'
    ws['B5'] = 100

    ws['A6'] = '处理面积 (m²):'
    ws['B6'] = 1

    # 计算结果区域
    ws['A8'] = '计算结果'
    ws['A8'].font = xw.Font(bold=True, size=12)

    ws['A9'] = 'SLR (kg/h/m²):'
    ws['B9'] = '=IFERROR((B4/1000)*(B5*3.6)/B6, "Error")'

    ws['A10'] = '运行安全状态:'
    ws['B10'] = '=IF(AND(B4>=2000, B4<=5400, B5>=60, B5<=170, B9>=3, B9<=24), "✓ 安全", "✗ 需要调整")'

    # 详细状态
    ws['A12'] = '详细状态分析'
    ws['A12'].font = xw.Font(bold=True, size=12)

    ws['A13'] = 'MLSS 状态:'
    ws['B13'] = '=IF(B4<2000, "过低", IF(B4>5400, "过高", IF(AND(B4>=3000, B4<=4500), "最优", "正常")))'

    ws['A14'] = '流量状态:'
    ws['B14'] = '=IF(B5<60, "过低", IF(B5>170, "过高", IF(AND(B5>=90, B5<=130), "最优", "正常")))'

    ws['A15'] = 'SLR 状态:'
    ws['B15'] = '=IF(B9<3, "过低", IF(B9>24, "过高", IF(AND(B9>=8, B9<=16), "最优", "正常")))'

    # 调整列宽
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 30

    # 保存
    from pathlib import Path
    tool_dir = Path(__file__).parent
    file_path = tool_dir / "污泥处理实时计算器.xlsx"
    wb.save(str(file_path))
    print(f"✓ 交互式仪表板已创建: {file_path}")


# 使用示例
def main():
    """主函数"""
    print("=" * 70)
    print("xlwings 集成模块 - 污泥处理参数计算")
    print("=" * 70)

    # 演示 Python 函数调用
    print("\n【Python 函数调用示例】")
    print("-" * 70)

    functions = WastewaterExcelFunctions()

    mlss = 3500
    flow = 100

    slr = functions.calculate_slr(mlss, flow)
    print(f"计算 SLR: MLSS={mlss} mg/L, Flow={flow} L/s")
    print(f"  结果: SLR = {slr} kg/h/m²")

    safety = functions.check_safety(mlss, flow)
    print(f"\n安全性检查: {safety}")

    recommendations = functions.get_recommendations(mlss, flow)
    print(f"\n运行建议:\n  {recommendations}")

    # 创建 Excel 仪表板
    if XLWINGS_AVAILABLE:
        print("\n【创建 Excel 仪表板】")
        print("-" * 70)
        try:
            create_interactive_dashboard()
        except Exception as e:
            print(f"✗ 创建仪表板失败: {e}")


if __name__ == '__main__':
    main()

