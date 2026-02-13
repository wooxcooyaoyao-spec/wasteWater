"""
污泥处理系统参数计算工具 - 使用演示脚本

这个脚本演示如何使用 WasteWaterTool 工具包进行污泥处理参数的计算和分析。

使用方法：
    python use_wastewater_tool.py

该脚本会：
1. 演示基础参数计算
2. 检查运行点安全性
3. 生成 Excel 对比分析报告
4. 生成敏感性分析报告
"""

import sys
from pathlib import Path

# 添加当前目录到路径，以便导入模块
tool_dir = Path(__file__).parent
sys.path.insert(0, str(tool_dir))

from wastewater_treatment_calc import WastewaterCalculator
from excel_handler import ExcelDataHandler


def print_header(title: str):
    """打印格式化的标题"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_basic_calculation():
    """演示 1：基础参数计算"""
    print_header("演示 1：基础参数计算")

    calc = WastewaterCalculator(area=1.0)

    print("\n【场景】已知 MLSS=3500 mg/L，EQ=100 L/s，计算 SLR")
    print("-" * 70)

    mlss = 3500
    flow = 100
    slr = calc.calculate_slr(mlss, flow)

    print(f"输入参数:")
    print(f"  MLSS = {mlss} mg/L")
    print(f"  Equivalent Flow = {flow} L/s")
    print(f"\n计算结果:")
    print(f"  SLR = {slr:.2f} kg/h/m²")

    return calc


def demo_safety_check(calc):
    """演示 2：运行安全性检查"""
    print_header("演示 2：运行安全性检查")

    test_cases = [
        (3500, 100, "基准运行"),
        (3800, 110, "高浓度高流量"),
        (2500, 150, "低浓度高流量"),
        (4200, 60, "高浓度低流量"),
    ]

    print("\n检查不同运行场景的安全性:\n")

    for mlss, flow, scenario in test_cases:
        check = calc.check_operating_point(mlss, flow)
        status = "✓ 安全" if check['overall_safe'] else "✗ 需要调整"

        print(f"【{scenario}】")
        print(f"  MLSS={mlss} mg/L, EQ={flow} L/s")
        print(f"  SLR={check['calculated_slr']:.2f} kg/h/m²")
        print(f"  状态: {status}")

        if not check['overall_safe']:
            print(f"  问题:")
            for rec in check['recommendations']:
                print(f"    {rec}")
        print()


def demo_parameter_deduction(calc):
    """演示 3：参数反推"""
    print_header("演示 3：参数反推")

    print("\n【场景 1】已知 SLR=12 kg/h/m²，EQ=90 L/s，求 MLSS")
    print("-" * 70)
    mlss_result = calc.calculate_mlss(slr=12, equivalent_flow=90)
    print(f"推导的 MLSS = {mlss_result:.0f} mg/L")

    # 验证
    slr_verify = calc.calculate_slr(mlss_result, 90)
    print(f"验证: SLR = {slr_verify:.2f} kg/h/m² (应≈12)")

    print("\n【场景 2】已知 MLSS=3500 mg/L，SLR=10 kg/h/m²，求 EQ")
    print("-" * 70)
    flow_result = calc.calculate_equivalent_flow(mlss=3500, slr=10)
    print(f"推导的 EQ = {flow_result:.2f} L/s")

    # 验证
    slr_verify2 = calc.calculate_slr(3500, flow_result)
    print(f"验证: SLR = {slr_verify2:.2f} kg/h/m² (应≈10)")


def demo_excel_analysis():
    """演示 4：生成 Excel 分析报告"""
    print_header("演示 4：生成 Excel 分析报告")

    handler = ExcelDataHandler()

    # 获取相对路径
    tool_dir = Path(__file__).parent
    data_dir = tool_dir / "data"
    output_dir = tool_dir / "output"

    print(f"\n数据目录: {data_dir}")
    print(f"输出目录: {output_dir}")

    # 检查数据文件是否存在
    excel_file = data_dir / "MLSS浓度表.xlsx"
    if not excel_file.exists():
        print(f"\n⚠️ 数据文件不存在: {excel_file}")
        print("跳过 Excel 分析...")
        return

    print(f"\n✓ 找到数据文件: {excel_file}")

    # 生成对比分析
    print("\n生成对比分析...")
    variations = {
        '基准运行': {'mlss': 3500, 'flow': 100},
        '高流量运行': {'mlss': 3500, 'flow': 120},
        '高浓度运行': {'mlss': 4000, 'flow': 100},
        '超高负荷': {'mlss': 4500, 'flow': 150},
        '低负荷': {'mlss': 2800, 'flow': 80},
    }

    handler.create_comparison_excel(
        str(output_dir / "参数对比分析.xlsx"),
        variations
    )

    # 生成敏感性分析
    print("生成敏感性分析...")
    handler.create_sensitivity_analysis(
        str(output_dir / "敏感性分析.xlsx"),
        base_mlss=3500,
        base_flow=100
    )

    print(f"\n✓ Excel 报告已生成到: {output_dir}")


def demo_parameter_design():
    """演示 5：参数设计场景"""
    print_header("演示 5：参数设计 - 寻找最优参数组合")

    calc = WastewaterCalculator(area=1.0)

    print("\n【设计目标】")
    print("  目标 SLR: 12 kg/h/m²（中等负荷）")
    print("  流量范围: 80-120 L/s")
    print("  找出所有满足条件的 MLSS 值")
    print("-" * 70)

    target_slr = 12
    flow_range = [80, 90, 100, 110, 120]

    print("\n可行的参数组合:\n")
    print(f"{'EQ (L/s)':<12} {'MLSS (mg/L)':<15} {'SLR (kg/h/m²)':<18} {'状态':<15}")
    print("-" * 70)

    for flow in flow_range:
        mlss = calc.calculate_mlss(slr=target_slr, equivalent_flow=flow)
        check = calc.check_operating_point(mlss, flow)
        status = "✓ 可行" if check['overall_safe'] else "✗ 不可行"

        print(f"{flow:<12} {mlss:<15.0f} {target_slr:<18.2f} {status:<15}")

    print("\n结论: 流量在 80-120 L/s 范围内，通过调整 MLSS，")
    print("      都可以达到 12 kg/h/m² 的目标负荷率。")


def demo_system_status_report():
    """演示 6：系统状态报告"""
    print_header("演示 6：系统运行状态快速检查")

    calc = WastewaterCalculator(area=1.0)

    print("\n当前系统参数:")
    print("  MLSS = 3600 mg/L")
    print("  EQ = 105 L/s")
    print("-" * 70)

    check = calc.check_operating_point(3600, 105)

    print(f"\n参数详细信息:\n")

    # MLSS 检查
    print(f"【MLSS 浓度】")
    print(f"  当前值: {check['mlss']['value']} mg/L")
    print(f"  安全范围: {check['mlss']['min']} - {check['mlss']['max']} mg/L")
    print(f"  最优范围: {check['mlss']['optimal'][0]} - {check['mlss']['optimal'][1]} mg/L")
    print(f"  状态: {check['mlss']['status']}")

    # 流量检查
    print(f"\n【等效流量】")
    print(f"  当前值: {check['equivalent_flow']['value']} L/s")
    print(f"  安全范围: {check['equivalent_flow']['min']} - {check['equivalent_flow']['max']} L/s")
    print(f"  最优范围: {check['equivalent_flow']['optimal'][0]} - {check['equivalent_flow']['optimal'][1]} L/s")
    print(f"  状态: {check['equivalent_flow']['status']}")

    # SLR 检查
    print(f"\n【固体负荷率】")
    print(f"  当前值: {check['calculated_slr']:.2f} kg/h/m²")
    print(f"  安全范围: {check['slr']['min']} - {check['slr']['max']} kg/h/m²")
    print(f"  最优范围: {check['slr']['optimal'][0]} - {check['slr']['optimal'][1]} kg/h/m²")
    print(f"  状态: {check['slr']['status']}")

    # 整体评价
    print(f"\n【系统整体评价】")
    print(f"  安全性: {'✓ 安全运行' if check['overall_safe'] else '✗ 需要调整'}")
    print(f"\n建议:")
    for rec in check['recommendations']:
        print(f"  {rec}")


def main():
    """主函数"""
    print("\n" + "=" * 70)
    print("  污泥处理系统参数计算工具 - 使用演示")
    print("  Wastewater Treatment Parameter Calculator - Demo")
    print("=" * 70)

    print("\n工具特性:")
    print("  ✓ 参数自动计算和验证")
    print("  ✓ 安全范围自动检查")
    print("  ✓ 智能运行建议")
    print("  ✓ Excel 报告生成")
    print("  ✓ 敏感性分析")

    # 运行演示
    calc = demo_basic_calculation()
    demo_safety_check(calc)
    demo_parameter_deduction(calc)
    demo_parameter_design()
    demo_system_status_report()
    demo_excel_analysis()

    # 总结
    print_header("使用总结")
    print("""
工具提供了多种使用方式：

1. 【Python 代码集成】
   from wastewater_treatment_calc import WastewaterCalculator
   calc = WastewaterCalculator()
   check = calc.check_operating_point(3500, 100)

2.【Excel 报告生成】
   handler.create_comparison_excel('output.xlsx', variations)

3.【实时参数检查】
   支持快速验证当前运行参数是否在安全范围内

4.【参数设计】
   根据目标 SLR，反推所需的 MLSS 或流量

更多详情请查看: doc/使用指南.md
    """)

    print("=" * 70)
    print("演示完成！\n")


if __name__ == '__main__':
    main()

