# Python 3 强制使用说明

## 📌 重要声明

**本工具需要 Python 3，不支持 Python 2.x**

所有 Windows 系统使用指南中的命令都已更新为使用 `python3` 命令。

---

## ✅ 更新内容

### 1. Windows 快速参考卡 (`doc/Windows使用指南.md`)

#### 新增的强制声明
```
⚠️ **重要**: 本工具需要 **Python 3** (推荐 3.8+)

所有命令中请使用 `python3` 而不是 `python`
```

#### 更新的命令示例

| 步骤 | 原命令 | 新命令 |
|------|--------|--------|
| 创建虚拟环境 | `python -m venv venv` | `python3 -m venv venv` |
| 验证版本 | `python --version` | `python3 --version` |
| 验证依赖 | `python -c "import openpyxl..."` | `python3 -c "import openpyxl..."` |
| 运行演示 | `python use_wastewater_tool.py` | `python3 use_wastewater_tool.py` |
| 运行脚本 | `python my_script.py` | `python3 my_script.py` |

#### 新增常见问题

- `python3: 命令未找到` → 重新安装 Python 3（勾选 "Add Python to PATH"）
- `python: 命令不是 Python 3` → 使用 `python3` 替代 `python`
- 如何确认用的是 Python 3 → 运行 `python3 --version` 检查版本

### 2. 主使用指南 (`doc/使用指南.md`)

#### 新增的 Python 3 强调

**第一步：准备环境**
- 新增：⚠️ **重要提示** 强调需要 Python 3
- 更新：安装步骤明确指出 "Python 3.8+"
- 更新：验证命令改为 `python3 --version`

**第二步：创建虚拟环境**
- 更新：命令改为 `python3 -m venv venv`
- 新增：说明虚拟环境包含 Python 3

**第三步：安装依赖**
- 更新：验证命令改为 `python3 -c "..."`

**第四步：使用工具**
- 更新：所有运行命令改为 `python3 use_wastewater_tool.py` 等
- 新增：明确说明 "使用 Python 3 运行"

**第五步：常见问题**
- 更新：Q4 新增 "确保使用 `python3` 而不是 `python`"
- 新增：Q5 重新创建虚拟环境时使用 `python3 -m venv venv`
- 新增：Q6 "如何确认我使用的是 Python 3？"

**第六步：快速参考**
- 更新：所有命令示例改为 `python3`
- 新增："（使用 Python 3）" 标签说明

---

## 📊 更新统计

### Windows 使用指南
- `python3` 出现次数：**15+** 次
- 新增强调和警告：**5+** 处
- 新增常见问题：**2** 个

### 主使用指南
- `python3` 出现次数：**20+** 次
- 新增强调和警告：**8+** 处
- 新增常见问题：**1** 个

### 总计
- **35+** 次 `python3` 命令示例
- **13+** 处 Python 3 强调和警告
- **3** 个新增 Python 3 相关问题解答

---

## 🚀 关键命令汇总

### 必须使用 python3 的命令

```cmd
# 验证 Python 版本
python3 --version

# 创建虚拟环境
python3 -m venv venv

# 验证依赖安装
python3 -c "import openpyxl; print('✓ openpyxl 已安装')"
python3 -c "import xlwings; print('✓ xlwings 已安装')"

# 运行工具
python3 use_wastewater_tool.py

# 运行自定义脚本
python3 my_script.py

# 使用 pip 重新安装（虚拟环境激活后）
python3 -m pip install -e .
```

---

## ⚠️ 不要使用的命令

❌ **以下命令已过时，请勿使用：**

```cmd
python -m venv venv          # ❌ 改为 python3 -m venv venv
python --version             # ❌ 改为 python3 --version
python -c "import ..."       # ❌ 改为 python3 -c "import ..."
python use_wastewater_tool.py   # ❌ 改为 python3 use_wastewater_tool.py
python my_script.py          # ❌ 改为 python3 my_script.py
```

---

## 🔍 如何验证正确性

### 1. 检查 Python 版本
```cmd
python3 --version
```
✅ 正确：`Python 3.8.x`, `Python 3.9.x`, `Python 3.10.x` 等
❌ 错误：`Python 2.7.x` 或 "命令未找到"

### 2. 检查虚拟环境
```cmd
# 激活虚拟环境
venv\Scripts\activate

# 验证虚拟环境中的 Python 版本
python3 --version
```

### 3. 检查依赖
```cmd
python3 -c "import openpyxl; import xlwings; print('✓ 所有依赖都已安装')"
```

---

## 📝 文档更新清单

- ✅ `doc/Windows使用指南.md` - 更新所有 python 命令为 python3
- ✅ `doc/使用指南.md` - 更新 Windows 部分的所有命令为 python3
- ✅ 新增 Python 3 强调和警告
- ✅ 新增 Python 3 相关常见问题
- ✅ 本文档 - Python 3 强制使用说明

---

## 🎯 使用建议

1. **初学者** - 严格按照文档中的 `python3` 命令执行
2. **开发者** - 务必使用 Python 3.8+ 进行开发和测试
3. **维护者** - 未来的文档更新中继续强调 Python 3 的必要性

---

**最后更新**: 2026-02-13
**状态**: ✅ 完成

