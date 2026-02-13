# WasteWaterTool 安装指南

## 📋 系统要求

- **Python**: 3.7 或更高版本
- **操作系统**: Windows, macOS, Linux
- **依赖**: openpyxl (必需), xlwings (可选)

---

## 🚀 快速安装

### 方式 1：使用 pip 安装（推荐）

#### 1.1 仅安装核心功能

```bash
cd /path/to/WastWaterTool
pip install -r requirements.txt
```

或

```bash
pip install openpyxl>=3.0.0
```

#### 1.2 安装完整功能（包括 Excel 集成）

```bash
pip install openpyxl xlwings
```

或使用可选依赖：

```bash
cd /path/to/WastWaterTool
pip install -e .[excel]
```

#### 1.3 安装开发版本（包含测试工具）

```bash
cd /path/to/WastWaterTool
pip install -e .[dev]
```

#### 1.4 安装所有功能

```bash
cd /path/to/WastWaterTool
pip install -e .[all]
```

### 方式 2：本地开发模式

在项目目录中进行可编辑安装：

```bash
cd /path/to/WastWaterTool
pip install -e .
```

这样可以直接修改代码，无需重新安装即可生效。

### 方式 3：从 setup.py 安装

```bash
cd /path/to/WastWaterTool
python setup.py install
```

---

## 📦 依赖说明

### 必需依赖

| 包 | 版本 | 说明 |
|---|------|------|
| openpyxl | >=3.0.0 | Excel 文件处理库 |
| Python | >=3.7 | Python 运行时 |

### 可选依赖

| 包 | 版本 | 说明 | 何时需要 |
|---|------|------|--------|
| xlwings | >=0.27.0 | Excel 集成库 | 需要 Excel 交互功能 |

### 开发依赖

| 包 | 用途 |
|---|------|
| black | 代码格式化 |
| flake8 | 代码检查 |
| pytest | 测试框架 |
| pytest-cov | 测试覆盖率 |

---

## ✅ 验证安装

### 1. 检查 Python 版本

```bash
python --version
# 输出: Python 3.7.x 或更高
```

### 2. 验证必需依赖

```bash
python -c "import openpyxl; print(f'openpyxl {openpyxl.__version__} 已安装')"
```

**预期输出**:
```
openpyxl 3.0.x 已安装
```

### 3. 验证可选依赖（如已安装）

```bash
python -c "import xlwings; print(f'xlwings {xlwings.__version__} 已安装')" 2>/dev/null || echo "xlwings 未安装（可选）"
```

### 4. 验证工具可用性

```bash
cd WastWaterTool
python use_wastewater_tool.py
```

**预期输出**: 完整的演示脚本运行结果

### 5. 验证工具导入

```python
# test_import.py
from wastewater_treatment_calc import WastewaterCalculator
from excel_handler import ExcelDataHandler

print("✅ 所有模块导入成功！")

# 测试基础功能
calc = WastewaterCalculator()
slr = calc.calculate_slr(3500, 100)
print(f"✅ 计算测试通过: SLR = {slr:.2f} kg/h/m²")
```

运行：
```bash
python test_import.py
```

---

## 🔧 常见安装问题解决

### 问题 1：ModuleNotFoundError: No module named 'openpyxl'

**原因**: openpyxl 未安装

**解决**:
```bash
pip install openpyxl
```

### 问题 2：pip 命令找不到

**原因**: pip 未在 PATH 中

**解决**:
```bash
# 使用 Python 模块形式运行 pip
python -m pip install openpyxl
```

### 问题 3：权限被拒绝 (Permission denied)

**原因**: 需要管理员权限

**解决方案 A**: 使用 --user 标志
```bash
pip install --user openpyxl
```

**解决方案 B**: 使用虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
pip install openpyxl
```

### 问题 4：版本冲突

**原因**: 依赖版本不兼容

**解决**:
```bash
# 升级 pip
pip install --upgrade pip

# 清除缓存重新安装
pip install --no-cache-dir --force-reinstall openpyxl
```

### 问题 5：xlwings 在 Linux 上无法工作

**原因**: Linux 默认不支持 Excel

**解决**: 在 Linux 上使用 LibreOffice 或跳过 xlwings 安装

---

## 🌐 虚拟环境设置（推荐）

### 使用 venv

```bash
# 创建虚拟环境
python -m venv ww_env

# 激活虚拟环境
# Linux/macOS:
source ww_env/bin/activate

# Windows:
ww_env\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 使用完毕后停用虚拟环境
deactivate
```

### 使用 Conda

```bash
# 创建 Conda 环境
conda create -n wastewatertools python=3.11

# 激活环境
conda activate wastewatertools

# 安装依赖
pip install -r requirements.txt

# 停用环境
conda deactivate
```

---

## 📥 离线安装

### 步骤 1: 在有网络的机器上下载包

```bash
pip download -r requirements.txt -d ./offline_packages/
```

### 步骤 2: 将 `offline_packages/` 复制到离线机器

### 步骤 3: 在离线机器上安装

```bash
pip install --no-index --find-links=./offline_packages/ -r requirements.txt
```

---

## 🐍 Python 版本兼容性

| Python 版本 | 兼容性 | 测试状态 |
|-----------|--------|--------|
| 3.7 | ✅ 支持 | 已测试 |
| 3.8 | ✅ 支持 | 已测试 |
| 3.9 | ✅ 支持 | 已测试 |
| 3.10 | ✅ 支持 | 已测试 |
| 3.11 | ✅ 支持 | 已测试 |
| 3.12 | ⚠️ 预期支持 | 未测试 |

---

## 🖥️ 平台特定说明

### Windows

```bash
# 使用命令行
py -m pip install openpyxl

# 或使用 PowerShell
python -m pip install openpyxl
```

### macOS

```bash
# 使用 Homebrew（如果安装了 Python）
pip3 install openpyxl
```

### Linux

```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3-pip
pip3 install openpyxl

# 或使用虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate
pip install openpyxl
```

---

## 📚 后续步骤

安装完成后，您可以：

1. **查看快速开始**: 阅读 `QUICK_START.md`
2. **运行演示**: 执行 `python use_wastewater_tool.py`
3. **详细文档**: 查看 `doc/使用指南.md`
4. **集成项目**: 在自己的项目中导入使用

---

## 🆘 获取帮助

如遇问题，请检查：

1. **Python 版本**: `python --version` 需要 >= 3.7
2. **pip 版本**: `pip --version` 建议 >= 20.0
3. **依赖版本**: `pip list` 查看已安装包
4. **文档**: 查看 `DEPENDENCIES.md` 了解更多

---

**最后更新**: 2026-02-13
**作者**: WasteWaterTool 项目组

