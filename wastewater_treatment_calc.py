"""
污泥处理系统参数计算器 - Wastewater Treatment Parameter Calculator

三个核心参数的动态计算和验证：
- MLSS (Mixed Liquor Suspended Solids)：混合液悬浮固体浓度 (mg/L)
- Equivalent Flow (EQ)：等效流量 (L/s)
- Solids Loading Rate (SLR)：固体负荷率 (kg/h/m²)

公式关系：
    SLR = (MLSS / 1,000) × (EQ × 3.6) / 面积(m²)
    简化为：SLR (kg/h/m²) = MLSS (mg/L) × EQ (L/s) × 3.6 / (1000 × 面积)
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class WastewaterParams:
    """污泥处理参数类"""
    mlss: Optional[float] = None  # mg/L
    equivalent_flow: Optional[float] = None  # L/s
    slr: Optional[float] = None  # kg/h/m²
    area: float = 1.0  # 默认面积 1 m²（用于标准化计算）


class WastewaterCalculator:
    """污泥处理系统参数计算器"""

    # 安全范围定义（基于行业经验）
    SAFETY_RANGES = {
        'mlss': {'min': 2000, 'max': 5400, 'optimal': (3000, 4500)},
        'slr': {'min': 3.0, 'max': 24.0, 'optimal': (8.0, 16.0)},
        'equivalent_flow': {'min': 60, 'max': 170, 'optimal': (90, 130)},
    }

    def __init__(self, area: float = 1.0):
        """
        初始化计算器

        Args:
            area: 处理单元面积 (m²)，默认为 1 m²
        """
        self.area = area

    def calculate_slr(self, mlss: float, equivalent_flow: float) -> float:
        """
        计算固体负荷率 (SLR)

        公式: SLR = (MLSS / 1000) × (EQ × 3.6) / 面积

        Args:
            mlss: 混合液悬浮固体浓度 (mg/L)
            equivalent_flow: 等效流量 (L/s)

        Returns:
            固体负荷率 (kg/h/m²)
        """
        return (mlss / 1000) * (equivalent_flow * 3.6) / self.area

    def calculate_mlss(self, slr: float, equivalent_flow: float) -> float:
        """
        根据 SLR 和等效流量推导 MLSS

        Args:
            slr: 固体负荷率 (kg/h/m²)
            equivalent_flow: 等效流量 (L/s)

        Returns:
            混合液悬浮固体浓度 (mg/L)
        """
        return (slr * self.area * 1000) / (equivalent_flow * 3.6)

    def calculate_equivalent_flow(self, mlss: float, slr: float) -> float:
        """
        根据 MLSS 和 SLR 推导等效流量

        Args:
            mlss: 混合液悬浮固体浓度 (mg/L)
            slr: 固体负荷率 (kg/h/m²)

        Returns:
            等效流量 (L/s)
        """
        return (slr * self.area * 1000) / (mlss * 3.6)

    def validate_parameter(self, param_name: str, value: float) -> dict:
        """
        验证参数是否在安全范围内

        Args:
            param_name: 参数名称 ('mlss', 'slr', 'equivalent_flow')
            value: 参数值

        Returns:
            包含验证结果的字典
        """
        ranges = self.SAFETY_RANGES.get(param_name)
        if not ranges:
            return {'error': f'未知参数: {param_name}'}

        status = 'normal'
        if value < ranges['min']:
            status = 'too_low'
        elif value > ranges['max']:
            status = 'too_high'
        elif ranges['optimal'][0] <= value <= ranges['optimal'][1]:
            status = 'optimal'

        return {
            'parameter': param_name,
            'value': value,
            'min': ranges['min'],
            'max': ranges['max'],
            'optimal': ranges['optimal'],
            'status': status,
            'safe': ranges['min'] <= value <= ranges['max']
        }

    def check_operating_point(self, mlss: float, equivalent_flow: float) -> dict:
        """
        检查某个运行点是否在安全范围内

        Args:
            mlss: 混合液悬浮固体浓度 (mg/L)
            equivalent_flow: 等效流量 (L/s)

        Returns:
            包含完整验证信息的字典
        """
        slr = self.calculate_slr(mlss, equivalent_flow)

        mlss_check = self.validate_parameter('mlss', mlss)
        flow_check = self.validate_parameter('equivalent_flow', equivalent_flow)
        slr_check = self.validate_parameter('slr', slr)

        # 判断整体状态
        all_safe = mlss_check['safe'] and flow_check['safe'] and slr_check['safe']

        return {
            'mlss': mlss_check,
            'equivalent_flow': flow_check,
            'slr': slr_check,
            'calculated_slr': slr,
            'overall_safe': all_safe,
            'recommendations': self._generate_recommendations(mlss_check, flow_check, slr_check)
        }

    def _generate_recommendations(self, mlss_check: dict, flow_check: dict, slr_check: dict) -> list:
        """生成运行建议"""
        recommendations = []

        if not mlss_check['safe']:
            if mlss_check['status'] == 'too_low':
                recommendations.append('⚠️ MLSS 过低：污泥浓度不足，处理效率可能下降')
            else:
                recommendations.append('⚠️ MLSS 过高：污泥可能缺氧，沉降性差')

        if not flow_check['safe']:
            if flow_check['status'] == 'too_low':
                recommendations.append('⚠️ 等效流量过低：设备未充分利用')
            else:
                recommendations.append('⚠️ 等效流量过高：设备可能过载')

        if not slr_check['safe']:
            if slr_check['status'] == 'too_low':
                recommendations.append('⚠️ 固体负荷过低：能耗浪费')
            else:
                recommendations.append('⚠️ 固体负荷过高：处理不彻底，出水可能不达标')

        if not recommendations:
            recommendations.append('✓ 所有参数在安全范围内，运行状态良好')

        return recommendations

    def generate_operating_range_table(self) -> list:
        """生成完整的运行范围参考表"""
        mlss_values = list(range(2000, 5600, 200))
        flow_values = list(range(60, 175, 5))

        # 创建交叉表数据
        data = []
        for flow in flow_values:
            row = {'Equivalent (L/s)': flow}
            for mlss in mlss_values:
                slr = self.calculate_slr(mlss, flow)
                row[f'MLSS {mlss}'] = f'{slr:.2f}'
            data.append(row)

        return data


# 使用示例函数
def example_usage():
    """演示使用示例"""
    calc = WastewaterCalculator(area=1.0)

    print("=" * 70)
    print("污泥处理系统参数计算器 - Wastewater Treatment Parameter Calculator")
    print("=" * 70)

    # 示例 1: 检查一个特定的运行点
    print("\n【示例 1】检查运行点：MLSS=3500 mg/L, EQ=100 L/s")
    print("-" * 70)
    result = calc.check_operating_point(mlss=3500, equivalent_flow=100)

    print(f"\nMLSS 验证:")
    print(f"  值: {result['mlss']['value']} mg/L")
    print(f"  范围: {result['mlss']['min']} - {result['mlss']['max']} mg/L")
    print(f"  最优: {result['mlss']['optimal']} mg/L")
    print(f"  状态: {result['mlss']['status']} {'✓' if result['mlss']['safe'] else '✗'}")

    print(f"\n等效流量 验证:")
    print(f"  值: {result['equivalent_flow']['value']} L/s")
    print(f"  范围: {result['equivalent_flow']['min']} - {result['equivalent_flow']['max']} L/s")
    print(f"  最优: {result['equivalent_flow']['optimal']} L/s")
    print(f"  状态: {result['equivalent_flow']['status']} {'✓' if result['equivalent_flow']['safe'] else '✗'}")

    print(f"\n固体负荷率 (计算结果):")
    print(f"  值: {result['calculated_slr']:.2f} kg/h/m²")
    print(f"  范围: {result['slr']['min']} - {result['slr']['max']} kg/h/m²")
    print(f"  最优: {result['slr']['optimal']} kg/h/m²")
    print(f"  状态: {result['slr']['status']} {'✓' if result['slr']['safe'] else '✗'}")

    print(f"\n整体状态: {'✓ 安全' if result['overall_safe'] else '✗ 需要调整'}")
    print(f"\n建议:")
    for rec in result['recommendations']:
        print(f"  {rec}")

    # 示例 2: 参数反推
    print("\n\n【示例 2】参数反推：已知 SLR=12 kg/h/m², EQ=90 L/s, 求 MLSS")
    print("-" * 70)
    mlss_calculated = calc.calculate_mlss(slr=12, equivalent_flow=90)
    print(f"推导的 MLSS: {mlss_calculated:.0f} mg/L")

    # 验证反推结果
    slr_verify = calc.calculate_slr(mlss_calculated, 90)
    print(f"验证: SLR = {slr_verify:.2f} kg/h/m² (应该≈12)")

    # 示例 3: 生成运行范围表
    print("\n\n【示例 3】运行范围参考表 (部分)")
    print("-" * 70)
    table_data = calc.generate_operating_range_table()
    for i, row in enumerate(table_data[:10]):
        print(row)

    print("\n" + "=" * 70)
    print("计算完成！")
    print("=" * 70)


if __name__ == '__main__':
    example_usage()

