# WasteWaterTool 依赖包说明

## 📋 依赖总览

WasteWaterTool 使用的 Python 依赖包包括：

| 包名 | 版本 | 类型 | 用途 |
|------|------|------|------|
| openpyxl | >=3.0.0 | 必需 | Excel 文件读写 |
| xlwings | >=0.27.0 | 必需 | Excel 集成函数和交互式仪表板 |

## 🔴 必需依赖 (Required)

### openpyxl >=3.0.0

**描述**: 用于操作 Excel 文件的纯 Python 库

**用途**:
- 读取 `data/MLSS浓度表.xlsx` 参考数据表
- 生成参数对比分析 Excel 文件
- 生成敏感性分析 Excel 文件
- 应用格式化和条件格式

**安装**:
```bash
pip install openpyxl>=3.0.0
```

**导入方式**:
```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils import get_column_letter
```

**文档**: https://openpyxl.readthedocs.io/

---

## 🔴 xlwings >=0.27.0

**描述**: Excel 和 Python 的桥接库，支持 Excel 中调用 Python 代码

**用途**:
- 在 Excel 中直接调用污泥处理参数计算函数
- 创建交互式 Excel 仪表板
- 实时计算和自动更新

**安装**:
```bash
pip install xlwings>=0.27.0
```

**平台支持**:
- Windows (推荐使用 Excel 365 或 2019+)
- macOS (需要 Excel 2016+)
- Linux (需要特殊配置)

**系统要求**:
- xlwings 在系统中需要 Microsoft Office 或兼容版本
- Windows: Excel 2010 或更高版本
- macOS: Excel 2011 或更高版本
- Linux: 需要 LibreOffice 或 Calc

**导入方式**:
```python
import xlwings as xw
```

**文档**: https://docs.xlwings.org/

---

## 🟢 标准库依赖 (Built-in)

以下是工具使用的 Python 标准库，无需额外安装：

| 模块 | 用途 |
|------|------|
| `dataclasses` | 定义 WastewaterParams 数据类 |
| `typing` | 类型提示 (Optional, Dict) |
| `pathlib` | 路径处理和相对路径查询 |
| `sys` | 系统路径操作 |

---

## 📦 安装指南

### 方式 1：快速安装 (推荐)

```bash
pip install -r requirements.txt
```

### 方式 2：完整安装

```bash
pip install openpyxl>=3.0.0 xlwings>=0.27.0
```

### 方式 3：从源代码安装

```bash
cd WastWaterTool
pip install -e .
```

---

## ✅ 验证安装

运行以下命令验证依赖是否正确安装：

### 验证必需依赖

```bash
python -c "import openpyxl; print(f'openpyxl 版本: {openpyxl.__version__}')"
python -c "import xlwings; print(f'xlwings 版本: {xlwings.__version__}')"
```

### 验证工具可用性

```bash
cd WastWaterTool
python use_wastewater_tool.py
```

---

## 🔍 依赖关系图

```
WasteWaterTool
│
├── wastewater_treatment_calc.py
│   └── 无外部依赖 (仅使用标准库)
│
├── excel_handler.py
│   ├── openpyxl ✅ (必需)
│   └── wastewater_treatment_calc.py
│
├── xlwings_integration.py
│   ├── xlwings ✅ (必需)
│   └── wastewater_treatment_calc.py
│
└── use_wastewater_tool.py
    ├── wastewater_treatment_calc.py
    └── excel_handler.py
```

---

## 🚀 必需配置

- Python 3.7+
- openpyxl>=3.0.0
- xlwings>=0.27.0

---

## 📊 依赖大小

| 包 | 大小 | 下载时间 |
|----|------|--------|
| openpyxl | ~7.5 MB | ~2-3 秒 |
| xlwings | ~3.2 MB | ~1-2 秒 |

---

## ⚠️ 常见问题

### Q1: openpyxl 和 xlwings 都是必需的吗？

**A**: 是的。两个依赖都是必需的：
- openpyxl: 用于 Excel 文件读写
- xlwings: 用于 Excel 集成和交互式仪表板

### Q2: 支持 Python 版本？

**A**:
- Python 3.7+ 正式支持
- Python 3.11 已充分测试
- 建议使用 Python 3.8+ 以获得最佳性能

### Q3: 如何离线安装？

**A**:
```bash
# 下载所有依赖
pip download -r requirements.txt -d ./packages/

# 离线安装
pip install --no-index --find-links=./packages/ -r requirements.txt
```

### Q4: 依赖能升级吗？

**A**:
- openpyxl 可升级到最新版本
- xlwings 可升级到最新版本
- 建议保持次版本号兼容 (如 3.x, 0.27.x)

### Q5: xlwings 需要 Microsoft Office 吗？

**A**:
- Windows: 需要 Excel 2010 或更高版本
- macOS: 需要 Excel 2011 或更高版本
- Linux: 可使用 LibreOffice 或 Calc

---

## 📝 版本更新记录

### v1.0.0 (2026-02-13)

**依赖冻结版本**:
- openpyxl>=3.0.0, <4.0.0
- xlwings>=0.27.0, <1.0.0 (可选)
- Python>=3.7, <4.0

---

## 🔗 相关资源

- **openpyxl 官方文档**: https://openpyxl.readthedocs.io/
- **xlwings 官方文档**: https://docs.xlwings.org/
- **Python 官方网站**: https://www.python.org/
- **pip 使用指南**: https://pip.pypa.io/

---

**更新时间**: 2026-02-13
**维护者**: WasteWaterTool 项目组

