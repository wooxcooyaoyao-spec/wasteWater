"""
污泥处理系统参数计算与分析工具包

包含以下模块：
1. wastewater_treatment_calc - 核心计算引擎
2. excel_handler - Excel 数据处理和分析
3. xlwings_integration - Excel 交互式功能

快速开始：
---------

# 基础计算
from wastewater_treatment_calc import WastewaterCalculator

calc = WastewaterCalculator(area=1.0)
slr = calc.calculate_slr(mlss=3500, equivalent_flow=100)
print(f"SLR = {slr} kg/h/m²")

# 检查运行点
check = calc.check_operating_point(3500, 100)
print(f"安全: {check['overall_safe']}")

# Excel 数据处理
from excel_handler import ExcelDataHandler

handler = ExcelDataHandler('MLSS浓度表.xlsx')
handler.create_comparison_excel('对比分析.xlsx', {
    '基准': {'mlss': 3500, 'flow': 100},
    '高负荷': {'mlss': 4000, 'flow': 120},
})

# xlwings 集成
from xlwings_integration import WastewaterExcelFunctions

functions = WastewaterExcelFunctions()
result = functions.check_safety(3500, 100)
"""

__version__ = "1.0.0"
__all__ = [
    'WastewaterCalculator',
    'ExcelDataHandler',
    'WastewaterExcelFunctions',
]

from excel_handler import ExcelDataHandler
from wastewater_treatment_calc import WastewaterCalculator

# xlwings_integration 是可选的，只在需要时导入
try:
    from xlwings_integration import WastewaterExcelFunctions
except ImportError:
    # 如果 xlwings 未安装，WastewaterExcelFunctions 将不可用
    WastewaterExcelFunctions = None

