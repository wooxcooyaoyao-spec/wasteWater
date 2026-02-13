# 快速开始指南

> 5 分钟快速上手污泥处理系统参数计算工具

## 安装

```bash
pip install openpyxl
```

## 三种使用方式

### 🟢 方式 1：运行演示脚本（推荐初学者）

```bash
# 在项目根目录下
python use_wastewater_tool.py
```

✅ 会自动演示所有功能

---

### 🟡 方式 2：Python 代码调用（推荐开发者）

#### 快速计算

```python
from wastewater_treatment_calc import WastewaterCalculator

calc = WastewaterCalculator()

# 计算 SLR
slr = calc.calculate_slr(mlss=3500, equivalent_flow=100)
print(f"SLR = {slr:.2f} kg/h/m²")  # 输出: SLR = 1260.00 kg/h/m²
```

#### 检查安全性

```python
# 检查参数是否安全
check = calc.check_operating_point(3500, 100)

if check['overall_safe']:
    print("✓ 安全运行")
else:
    print("✗ 需要调整:")
    for rec in check['recommendations']:
        print(f"  {rec}")
```

#### 参数反推

```python
# 已知目标 SLR，反推 MLSS
mlss = calc.calculate_mlss(slr=12, equivalent_flow=90)
print(f"需要 MLSS: {mlss:.0f} mg/L")
```

---

### 🔵 方式 3：生成 Excel 报告

```python
from excel_handler import ExcelDataHandler

handler = ExcelDataHandler()

# 定义多个运行方案
scenarios = {
    '方案 A': {'mlss': 3500, 'flow': 100},
    '方案 B': {'mlss': 3800, 'flow': 110},
    '方案 C': {'mlss': 4000, 'flow': 120},
}

# 生成对比 Excel
handler.create_comparison_excel('output/对比分析.xlsx', scenarios)

# 生成敏感性分析
handler.create_sensitivity_analysis('output/敏感性分析.xlsx')
```

---

## 核心概念

| 参数 | 单位 | 范围 | 最优 | 含义 |
|------|------|------|------|------|
| MLSS | mg/L | 2000-5400 | 3000-4500 | 污泥浓度 |
| EQ | L/s | 60-170 | 90-130 | 等效流量 |
| SLR | kg/h/m² | 3-24 | 8-16 | 处理负荷 |

**公式**：`SLR = (MLSS/1000) × (EQ×3.6) / 面积`

---

## 常见场景

### 场景 1：验证当前参数

```python
calc = WastewaterCalculator()

# 获取实时参数
current_mlss = 3600
current_flow = 105

# 检查安全性
check = calc.check_operating_point(current_mlss, current_flow)
print(f"SLR: {check['calculated_slr']:.2f} kg/h/m²")
print(f"安全: {check['overall_safe']}")
```

### 场景 2：设计目标参数

```python
calc = WastewaterCalculator()

# 目标：SLR=12 kg/h/m², EQ≤100 L/s
target_slr = 12
target_flow = 100

# 计算所需 MLSS
required_mlss = calc.calculate_mlss(target_slr, target_flow)

# 验证
check = calc.check_operating_point(required_mlss, target_flow)
if check['overall_safe']:
    print(f"✓ 可以设置 MLSS={required_mlss:.0f} mg/L")
else:
    print("✗ 无法达成目标")
```

### 场景 3：对比多方案

```python
from excel_handler import ExcelDataHandler

handler = ExcelDataHandler()

# 3 种运行策略
plans = {
    '节能': {'mlss': 2800, 'flow': 80},
    '标准': {'mlss': 3500, 'flow': 100},
    '高效': {'mlss': 4200, 'flow': 130},
}

# 生成对比报告
handler.create_comparison_excel('plans.xlsx', plans)
print("✓ 对比报告已生成：plans.xlsx")
```

---

## API 速查表

### WastewaterCalculator

```python
from wastewater_treatment_calc import WastewaterCalculator

calc = WastewaterCalculator(area=1.0)

# 计算方法
slr = calc.calculate_slr(mlss, equivalent_flow)
mlss = calc.calculate_mlss(slr, equivalent_flow)
flow = calc.calculate_equivalent_flow(mlss, slr)

# 验证方法
check = calc.check_operating_point(mlss, equivalent_flow)
validation = calc.validate_parameter('mlss', value)
```

### ExcelDataHandler

```python
from excel_handler import ExcelDataHandler

# 初始化（默认查找 data 目录）
handler = ExcelDataHandler()

# 或指定数据目录
handler = ExcelDataHandler('path/to/data.xlsx')

# Excel 方法
handler.create_comparison_excel(output_path, scenarios_dict)
handler.create_sensitivity_analysis(output_path, base_mlss, base_flow)
handler.load_excel(excel_path)
```

---

## 返回值示例

### check_operating_point() 返回

```python
{
    'mlss': {
        'value': 3500,
        'min': 2000,
        'max': 5400,
        'optimal': (3000, 4500),
        'status': 'optimal',
        'safe': True
    },
    'equivalent_flow': { ... },
    'slr': { ... },
    'calculated_slr': 1260.0,
    'overall_safe': True/False,
    'recommendations': ['建议 1', '建议 2']
}
```

---

## 文件位置

```
WasteWaterTool/
├── data/MLSS浓度表.xlsx       ← 输入数据
├── output/                    ← 输出文件（自动生成）
├── doc/使用指南.md           ← 详细文档
├── README.md                  ← 工具说明
└── *.py                       ← 源代码
```

---

## 故障排除

| 问题 | 解决方案 |
|------|--------|
| 模块导入错误 | `pip install openpyxl` |
| 找不到 data 文件 | 确保 `data/MLSS浓度表.xlsx` 存在 |
| Excel 打不开 | 更新 openpyxl：`pip install --upgrade openpyxl` |
| 计算结果异常 | 检查单位（MLSS: mg/L, EQ: L/s） |

---

## 下一步

1. ✅ 运行 `python use_wastewater_tool.py` 查看演示
2. ✅ 查看 `doc/使用指南.md` 了解更多
3. ✅ 尝试在自己的项目中集成使用
4. ✅ 生成 Excel 报告用于决策支持

---

**需要帮助？** 查看详细文档：`doc/使用指南.md`

