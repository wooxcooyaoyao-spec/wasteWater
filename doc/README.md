# 污泥处理系统参数计算工具包

> 一个专为自来水处理污泥处理环节设计的参数计算和分析工具

## 📋 功能特性

- ✅ **参数计算**：自动计算 MLSS、流量、SLR 的相互转换
- ✅ **安全性检查**：自动验证参数是否在安全范围内
- ✅ **智能建议**：根据参数状态给出针对性的调整建议
- ✅ **Excel 处理**：读取原始数据，生成分析报告
- ✅ **对比分析**：支持多个运行场景的并行对比
- ✅ **敏感性分析**：分析参数变化对结果的影响
- ✅ **相对路径设计**：工具可独立部署到任意位置
- ✅ **🌐 Web 应用**：基于 Streamlit 的友好 Web 界面
- ✅ **📊 数据可视化**：参数对比和敏感性分析图表

## 📁 目录结构

```
WasteWaterTool/
├── data/                           # 📊 原始数据目录
│   └── MLSS浓度表.xlsx            # 输入的 Excel 表格
├── output/                         # 📈 生成的分析结果
│   ├── 参数对比分析.xlsx
│   └── 敏感性分析.xlsx
├── doc/                            # 📖 文档目录
│   └── 使用指南.md                # 详细使用说明
├── wastewater_treatment_calc.py   # 🧮 核心计算引擎
├── excel_handler.py                # 📑 Excel 处理模块
├── xlwings_integration.py         # 🔗 Excel 集成（可选）
├── __init__.py                     # 包初始化
└── README.md                       # 本文件
```

## 🚀 快速开始

### 方案 A：Web 应用（推荐初学者）

最简单的使用方式，打开即用！

#### macOS/Linux:
```bash
chmod +x run_streamlit.sh
./run_streamlit.sh
```

#### Windows:
双击 `run_streamlit.bat`

然后在浏览器打开 `http://localhost:8501`

**功能**:
- 🔧 快速参数计算工具
- 📈 查看原始 Excel 数据
- 🔀 参数方案对比
- 📉 敏感性分析

📖 详细指南：[快速开始_Streamlit.md](快速开始_Streamlit.md) 和 [Streamlit前端使用指南.md](Streamlit前端使用指南.md)

---

### 方案 B：Python 编程使用

用于集成到其他应用或自动化脚本。

#### 安装依赖

```bash
pip install -r requirements.txt
```

#### 基础使用

##### 方法 1：Python 代码调用

```python
from wastewater_treatment_calc import WastewaterCalculator

# 初始化
calc = WastewaterCalculator(area=1.0)

# 计算 SLR
slr = calc.calculate_slr(mlss=3500, equivalent_flow=100)
print(f"SLR = {slr:.2f} kg/h/m²")

# 检查安全性
check = calc.check_operating_point(3500, 100)
print(f"安全: {check['overall_safe']}")
```

##### 方法 2：生成 Excel 报告

```python
from excel_handler import ExcelDataHandler

# 初始化（会自动查找 data 目录）
handler = ExcelDataHandler()

# 生成对比分析
variations = {
    '方案A': {'mlss': 3500, 'flow': 100},
    '方案B': {'mlss': 3800, 'flow': 110},
}
handler.create_comparison_excel('output/对比.xlsx', variations)
```

##### 方法 3：运行脚本演示

从工程根目录运行：

```bash
python use_wastewater_tool.py
```

## 📚 核心概念

### 三个关键参数

| 参数 | 单位 | 含义 | 安全范围 | 最优范围 |
|------|------|------|---------|---------|
| MLSS | mg/L | 混合液悬浮固体浓度 | 2000-5400 | 3000-4500 |
| EQ | L/s | 等效流量 | 60-170 | 90-130 |
| SLR | kg/h/m² | 固体负荷率 | 3-24 | 8-16 |

### 计算公式

```
SLR = (MLSS / 1000) × (EQ × 3.6) / 面积
```

其中：
- 3.6：秒/小时的换算系数
- 1000：mg 到 kg 的换算系数
- 面积（m²）：默认为 1

## 📖 文档

### 推荐阅读顺序

1. **🌐 [快速开始_Streamlit.md](快速开始_Streamlit.md)** ⭐ 从这里开始
   - 5 分钟快速启动 Web 应用
   - 最简单的使用方式

2. **🌐 [Streamlit前端使用指南.md](Streamlit前端使用指南.md)**
   - 完整的功能介绍
   - 常见问题解答
   - 高级配置

3. **📚 [使用指南.md](使用指南.md)**
   - 详细的概念解释
   - Python 编程示例
   - 多种使用场景
   - 常见问题解答
   - 扩展和集成示例

4. **🔧 [工程架构描述.md](工程架构描述.md)**
   - 项目文件结构
   - 模块功能说明

## 🔧 模块说明

### wastewater_treatment_calc.py

**核心计算模块**

主要类：`WastewaterCalculator`

主要方法：
- `calculate_slr(mlss, equivalent_flow)` - 计算 SLR
- `calculate_mlss(slr, equivalent_flow)` - 反推 MLSS
- `calculate_equivalent_flow(mlss, slr)` - 反推流量
- `check_operating_point(mlss, equivalent_flow)` - 检查安全性
- `validate_parameter(param_name, value)` - 验证单个参数

### excel_handler.py

**Excel 数据处理模块**

主要类：`ExcelDataHandler`

主要方法：
- `load_excel(excel_path)` - 加载 Excel 文件
- `parse_mlss_table()` - 解析 MLSS 表格
- `create_comparison_excel(output_file, variations)` - 生成对比分析
- `create_sensitivity_analysis(output_file)` - 生成敏感性分析

### xlwings_integration.py

**Excel 集成模块**（可选，需要 xlwings）

提供在 Excel 中直接调用的函数。

## 💡 使用示例

### 示例 1：参数验证

```python
calc = WastewaterCalculator()
check = calc.check_operating_point(3600, 105)

if check['overall_safe']:
    print("✓ 系统运行安全")
else:
    print("✗ 系统需要调整：")
    for rec in check['recommendations']:
        print(f"  {rec}")
```

### 示例 2：参数设计

```python
# 目标：SLR=12 kg/h/m²，流量最多 100 L/s
calc = WastewaterCalculator()
required_mlss = calc.calculate_mlss(slr=12, equivalent_flow=100)
print(f"需要 MLSS: {required_mlss:.0f} mg/L")

# 验证是否在安全范围内
check = calc.check_operating_point(required_mlss, 100)
print(f"可行: {check['overall_safe']}")
```

### 示例 3：多场景对比

```python
handler = ExcelDataHandler()

# 定义不同的运行场景
scenarios = {
    '保守模式': {'mlss': 2800, 'flow': 80},
    '平衡模式': {'mlss': 3500, 'flow': 100},
    '高效模式': {'mlss': 4200, 'flow': 130},
}

# 生成对比报告
handler.create_comparison_excel('output/运行模式对比.xlsx', scenarios)
```

## ⚠️ 安全范围定义

工具内置的安全范围基于行业实践经验：

- **MLSS**
  - 最小值：2000 mg/L（浓度过低则处理效率不足）
  - 最大值：5400 mg/L（浓度过高会导致缺氧）
  - 最优值：3000-4500 mg/L

- **流量**
  - 最小值：60 L/s
  - 最大值：170 L/s
  - 最优值：90-130 L/s

- **SLR**
  - 最小值：3.0 kg/h/m²（过低则浪费能耗）
  - 最大值：24.0 kg/h/m²（过高则处理不彻底）
  - 最优值：8.0-16.0 kg/h/m²

## 🔍 故障排除

### 问题：找不到数据文件

**解决**：确保 `data/MLSS浓度表.xlsx` 存在

```bash
ls -la data/
```

### 问题：计算结果不符合预期

**检查点**：
1. MLSS 单位是否为 mg/L
2. 流量单位是否为 L/s
3. 处理面积设置是否正确

### 问题：Excel 文件打不开

**解决**：
```bash
pip install --upgrade openpyxl
```

## 🌐 Web 应用 (Streamlit)

本工程现在提供了一个完整的 Web 应用，通过友好的图形界面快速使用所有功能。

**启动方式**:

macOS/Linux:
```bash
./run_streamlit.sh
```

Windows:
```
双击 run_streamlit.bat
```

**Web 应用功能**:
| 页面 | 功能 |
|------|------|
| 📊 首页 | 功能介绍和参数说明 |
| 🔧 计算工具 | 快速参数计算和验证 |
| 📈 数据查看 | Excel 数据查看和导出 |
| 🔀 参数对比 | 多方案对比分析 |
| 📉 敏感性分析 | 参数变化影响分析 |

详见：[Streamlit前端使用指南.md](Streamlit前端使用指南.md)

## 📦 依赖项

### 必需依赖
- Python 3.7+
- openpyxl 3.0+ （用于 Excel 处理）
- xlwings （可选，用于 Excel 集成）
- streamlit 1.28+ （用于 Web 应用）
- pandas 1.5+ （用于数据处理）

## 🔐 项目特点

1. **相对路径设计** - 工具不依赖绝对路径，可在任意位置运行
2. **模块化结构** - 各功能模块独立，易于扩展
3. **完整的验证体系** - 自动检查参数安全性
4. **易于集成** - 可导入到其他 Python 项目中
5. **详细文档** - 提供完整的使用指南和示例

## 📝 许可

本工具为开源项目，欢迎自由使用和修改。

## 🤝 贡献

如有建议或发现问题，欢迎提交反馈！

---

**更多信息**：查看 [doc/使用指南.md](doc/使用指南.md)

