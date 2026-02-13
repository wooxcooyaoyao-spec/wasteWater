# Streamlit 前端应用使用指南

> 污泥处理系统参数计算工具 - Web 应用详细使用说明

**版本**: 1.0.0
**更新时间**: 2026-02-13

---

## 📑 目录

1. [概述](#概述)
2. [前置要求](#前置要求)
3. [安装步骤](#安装步骤)
4. [运行应用](#运行应用)
5. [功能详解](#功能详解)
6. [常见问题](#常见问题)

---

## 概述

### 什么是 Streamlit？

Streamlit 是一个开源的 Python 库，可以快速构建和部署数据应用。通过 Streamlit，我们为污泥处理计算工具创建了一个友好的 Web 界面。

### 应用功能

| 功能 | 说明 |
|------|------|
| 📊 首页 | 应用介绍和核心参数说明 |
| 🔧 计算工具 | 快速参数计算工具 |
| 📈 数据查看 | 查看和导出原始 Excel 数据 |
| 🔀 参数对比 | 对比多个运行方案 |
| 📉 敏感性分析 | 分析参数变化影响 |

---

## 前置要求

### 系统要求

- **Python**: 3.8+（必需）
- **操作系统**: Windows、macOS 或 Linux
- **浏览器**: Chrome、Firefox、Safari 等现代浏览器

### 软件依赖

```
streamlit>=1.28.0       # Web 应用框架
pandas>=1.5.0           # 数据处理
openpyxl>=3.0.0         # Excel 处理
xlwings>=0.27.0         # Excel 集成
```

---

## 安装步骤

### 步骤 1：创建虚拟环境

#### macOS/Linux

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate
```

#### Windows

```cmd
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
venv\Scripts\activate
```

### 步骤 2：安装依赖

激活虚拟环境后，运行：

```cmd
python3 -m pip install -r requirements.txt
```

或单独安装 Streamlit：

```cmd
python3 -m pip install streamlit>=1.28.0
```

### 步骤 3：验证安装

```cmd
streamlit --version
```

应该看到版本号，如 `Streamlit, version 1.28.x`

---

## 运行应用

### 方法 1：使用启动脚本（推荐）

#### macOS/Linux

```bash
# 给脚本赋予执行权限
chmod +x run_streamlit.sh

# 运行脚本
./run_streamlit.sh
```

#### Windows

双击运行：
```
run_streamlit.bat
```

或在命令行运行：
```cmd
run_streamlit.bat
```

### 方法 2：直接启动

激活虚拟环境后，运行：

```cmd
streamlit run app.py
```

### 方法 3：指定端口运行

```cmd
streamlit run app.py --server.port 8080
```

### 应用启动信息

启动成功后，您会看到：

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

在浏览器中打开显示的 URL（通常是 `http://localhost:8501`）。

---

## 功能详解

### 📊 首页

首页展示应用的功能概览和核心参数说明。

**内容**:
- 🔧 计算工具说明
- 📊 数据查看说明
- 📈 分析工具说明
- 核心参数的范围和最优值
- 计算公式

### 🔧 计算工具

快速参数计算工具，支持三种计算模式。

#### 模式 1：计算 SLR

**输入**:
- MLSS 浓度 (mg/L)
- 等效流量 (L/s)
- 处理面积 (m²)

**输出**:
- 计算的 SLR 值
- 运行状态（✓ 安全 / ✗ 需要调整）
- SLR 状态（最优/正常/过低/过高）
- 详细的参数分析
- 运行建议

**使用步骤**:
1. 选择"计算 SLR"模式
2. 输入 MLSS 和 Flow 值
3. 点击"🔄 计算"按钮
4. 查看计算结果和建议

#### 模式 2：计算 MLSS

**输入**:
- SLR (kg/h/m²)
- 等效流量 (L/s)
- 处理面积 (m²)

**输出**:
- 反推的 MLSS 值
- 运行安全性
- 运行建议

#### 模式 3：计算流量

**输入**:
- MLSS 浓度 (mg/L)
- SLR (kg/h/m²)
- 处理面积 (m²)

**输出**:
- 反推的流量值
- 运行安全性
- 运行建议

### 📈 数据查看

查看和导出原始的 MLSS 浓度表数据。

**功能**:
- ✅ 查看完整的 Excel 表格
- ✅ 查看数据统计信息（行数、列数、数据点数）
- ✅ 下载为 CSV 格式
- ✅ 下载为 Excel 格式

**表格说明**:
- 第一行：MLSS 值（2000, 2200, 2400, ..., 5400）
- 第一列：等效流量值（60, 65, 70, ..., 170）
- 单元格内容：对应的 SLR 值

### 🔀 参数对比

对比多个运行方案，找到最优解决方案。

**使用步骤**:
1. 设置要对比的方案数量（2-10 个）
2. 为每个方案输入：
   - 方案名称
   - MLSS 值
   - Flow 值
3. 点击"📊 生成对比报告"
4. 查看对比结果和可视化图表

**输出内容**:
- 对比数据表格
- 各方案的参数状态
- 安全性评估
- 参数可视化图表（MLSS、Flow）

**应用场景**:
- 比较不同的运行策略
- 评估参数调整的影响
- 选择最优方案

### 📉 敏感性分析

分析参数变化对结果的影响。

**分析类型**:
1. **MLSS 敏感性分析**
   - 固定 Flow，改变 MLSS
   - 观察 SLR 的变化趋势

2. **Flow 敏感性分析**
   - 固定 MLSS，改变 Flow
   - 观察 SLR 的变化趋势

**输出内容**:
- 线性图表（参数 vs SLR）
- 数据表格（详细数值）
- 趋势分析

**应用场景**:
- 理解参数间的关系
- 预测参数变化的影响
- 优化运行条件

---

## 常见问题

### Q1：应用打不开

**症状**: 浏览器显示"无法连接"或"Connection refused"

**解决方案**:
1. 确保 Streamlit 应用仍在运行
2. 确认终端中没有错误消息
3. 尝试刷新浏览器 (Ctrl+R)
4. 检查是否在正确的 URL 上 (通常是 http://localhost:8501)

### Q2：依赖安装失败

**症状**: `pip install` 失败，显示"ModuleNotFoundError"

**解决方案**:
1. 确保虚拟环境已激活
2. 更新 pip：`python3 -m pip install --upgrade pip`
3. 重新运行：`python3 -m pip install -r requirements.txt`
4. 如果仍然失败，尝试单个安装：
   ```cmd
   python3 -m pip install streamlit
   python3 -m pip install pandas
   python3 -m pip install openpyxl
   ```

### Q3：Excel 文件找不到

**症状**: "❌ 找不到数据文件"

**解决方案**:
1. 确认文件在 `data/MLSS浓度表.xlsx`
2. 检查文件名是否完全匹配（包括大小写和中文字符）
3. 文件应该是 .xlsx 格式，不是 .xls

### Q4：应用运行很慢

**症状**: 页面加载缓慢，响应延迟

**原因和解决**:
- 第一次加载需要初始化，可能较慢 - 等待几秒
- 大量数据处理可能需要时间 - 这是正常的
- 如果持续缓慢，尝试：
  1. 关闭其他应用
  2. 检查网络连接
  3. 重启应用

### Q5：在 Windows 上运行脚本出错

**症状**: 双击 .bat 文件后立即关闭

**解决方案**:
1. 在命令行中运行脚本以查看错误信息
2. 检查 Python 是否安装正确
3. 确保 Python 已添加到 PATH
4. 尝试直接运行：
   ```cmd
   python3 -m venv venv
   venv\Scripts\activate
   python3 -m pip install -r requirements.txt
   streamlit run app.py
   ```

### Q6：如何在公网上访问应用？

**不推荐在公网部署**（安全原因），但如果需要：

```bash
# 启用网络访问
streamlit run app.py --server.address 0.0.0.0
```

然后从其他机器使用服务器的 IP 地址访问。

---

## 高级配置

### Streamlit 配置文件

创建 `.streamlit/config.toml` 文件来自定义应用：

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
headless = false
runOnSave = true
```

### 环境变量

设置 Streamlit 特定的环境变量：

```bash
# 禁用分析
export STREAMLIT_LOGGER_LEVEL=info

# 禁用运行前提醒
export STREAMLIT_CLIENT_SHOWSTDERRMESSAGEONSUCCESS=false
```

---

## 性能优化

### 缓存数据

如果数据加载慢，可以使用 Streamlit 的缓存功能：

```python
import streamlit as st

@st.cache_data
def load_data():
    # 加载数据的代码
    return df
```

### 减少重新计算

- 避免在循环中进行复杂计算
- 使用 `@st.cache_data` 装饰符缓存结果
- 合理使用 session state

---

## 故障排除检查清单

如果应用不正常工作，请检查：

- ✅ Python 版本是否 3.8+
- ✅ 虚拟环境是否激活
- ✅ 所有依赖是否安装
- ✅ 数据文件是否存在
- ✅ 文件权限是否正确
- ✅ 端口 8501 是否被占用
- ✅ 防火墙是否允许访问
- ✅ 浏览器是否是最新版本

---

## 部署建议

### 本地开发

适合开发和测试：
```cmd
streamlit run app.py
```

### 生产部署

使用 Streamlit Cloud 或其他平台部署（需要 GitHub 账户）。

详见 [Streamlit Cloud 文档](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

---

## 常见命令

| 命令 | 说明 |
|------|------|
| `streamlit run app.py` | 启动应用 |
| `streamlit run app.py --logger.level=debug` | 启用调试模式 |
| `streamlit config show` | 显示配置 |
| `streamlit cache clear` | 清除缓存 |
| `streamlit hello` | 运行官方示例 |

---

## 获取帮助

### 官方资源

- 📖 [Streamlit 文档](https://docs.streamlit.io/)
- 💬 [Streamlit 社区论坛](https://discuss.streamlit.io/)
- 🐛 [问题报告](https://github.com/streamlit/streamlit/issues)

### 本项目资源

- 📄 查看其他文档：`doc/` 目录
- 💻 查看源代码：`app.py`
- 📊 查看核心模块：`wastewater_treatment_calc.py`

---

## 更新日志

### v1.0.0 (2026-02-13)
- ✅ 初始发布
- ✅ 添加计算工具页面
- ✅ 添加数据查看页面
- ✅ 添加参数对比页面
- ✅ 添加敏感性分析页面
- ✅ 支持 Windows 和 macOS/Linux

---

**Streamlit 版本**: 1.28+
**Python 版本**: 3.8+
**更新时间**: 2026-02-13

