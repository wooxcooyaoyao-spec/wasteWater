# Windows 系统快速参考卡

> ⚠️ **重要**: 本工具需要 **Python 3** (推荐 3.8+)
>
> 所有命令中请使用 `python3` 而不是 `python`

## 🚀 一键启动（复制粘贴）

### 初次使用

```cmd
cd D:\Projects\WastWaterTool
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python3 use_wastewater_tool.py
```

### 后续使用

```cmd
cd D:\Projects\WastWaterTool
venv\Scripts\activate
python3 use_wastewater_tool.py
```

## 📋 详细步骤

### 1️⃣ 安装 Python 3

⚠️ **必须使用 Python 3**，不支持 Python 2.x

- 下载：https://www.python.org/downloads/
- 安装时 **勾选 "Add Python to PATH"**
- 验证：`python3 --version` （确保输出为 3.8 或以上版本）

### 2️⃣ 创建虚拟环境（使用 Python 3）

```cmd
python3 -m venv venv
```

### 3️⃣ 激活虚拟环境

**CMD 中：**
```cmd
venv\Scripts\activate
```

**PowerShell 中：**
```powershell
venv\Scripts\Activate.ps1
```

成功后会显示 `(venv)` 前缀。

### 4️⃣ 安装依赖（pip 会自动使用当前环境的 Python 3）

```cmd
pip install -r requirements.txt
```

验证安装（使用 Python 3）：
```cmd
python3 -c "import openpyxl; print('✓ openpyxl 已安装')"
python3 -c "import xlwings; print('✓ xlwings 已安装')"
```

### 5️⃣ 运行工具（使用 Python 3）

**方式 A：运行演示脚本**
```cmd
python3 use_wastewater_tool.py
```

**方式 B：编写自己的脚本**

创建 `my_analysis.py`：
```python
from WasteWaterTool.wastewater_treatment_calc import WastewaterCalculator
from WasteWaterTool.excel_handler import ExcelDataHandler

# 计算示例
calc = WastewaterCalculator()
slr = calc.calculate_slr(mlss=3500, equivalent_flow=100)
print(f"SLR = {slr:.2f} kg/h/m²")

# 生成 Excel 报告
handler = ExcelDataHandler()
scenarios = {
    '方案A': {'mlss': 3500, 'flow': 100},
    '方案B': {'mlss': 4000, 'flow': 110},
}
handler.create_comparison_excel('output/对比.xlsx', scenarios)
```

然后使用 Python 3 运行：
```cmd
python3 my_analysis.py
```

## ❓ 常见问题速查

| 问题 | 解决方案 |
|------|--------|
| `python3: 命令未找到` | 重启 CMD 或重装 Python 3（勾选 "Add Python to PATH"） |
| `python: 命令不是 Python 3` | 使用 `python3` 替代 `python`，确保调用的是 Python 3 |
| `ModuleNotFoundError` | 检查是否激活虚拟环境（看 `(venv)` 提示），确保使用 `python3` 命令 |
| 虚拟环境激活不了 | 在 PowerShell 中尝试：`venv\Scripts\Activate.ps1` |
| 重新开始 | `deactivate` 然后 `rmdir /s venv` 再用 `python3 -m venv venv` 重新创建 |
| 下次不想重新安装 | 虚拟环境已保存，直接激活即可（虚拟环境内已有 Python 3） |
| 如何确认用的是 Python 3 | 激活虚拟环境后，运行 `python3 --version` 检查版本 |

## 🔗 完整文档

详见：`doc/使用指南.md` - 包含详细的 Windows 使用步骤

## 📊 工作目录结构

```
WastWaterTool/
├── venv/                    # 虚拟环境（自动创建）
├── data/                    # 输入数据
│   └── MLSS浓度表.xlsx
├── output/                  # 生成的分析报告
├── doc/                     # 文档
├── requirements.txt         # 依赖列表
├── setup.py                 # 包配置
├── use_wastewater_tool.py   # 演示脚本
└── *.py                     # 源代码文件
```

## 💡 提示

- **⚠️ 必须使用 Python 3**：所有命令中请使用 `python3` 而不是 `python`
- **推荐 Python 版本**：3.8+ （推荐 3.9 或 3.10）
- **推荐编辑器**：VS Code, PyCharm Community
- **Excel 版本**：Excel 2010 或更新
- **所有命令都在项目根目录执行**
- **验证 Python 版本**：运行 `python3 --version` 确保不是 Python 2.x

---

**需要帮助？** 查看 `doc/使用指南.md` 获取完整文档

