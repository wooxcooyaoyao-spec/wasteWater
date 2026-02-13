# 🚀 快速开始 - Streamlit Web 应用

> 5 分钟快速启动污泥处理计算工具 Web 应用

---

## 📋 前置要求

- ✅ Python 3.8+
- ✅ 网络连接
- ✅ 任何现代浏览器

---

## ⚡ 快速启动

### macOS / Linux

#### 1️⃣ 打开终端，进入项目目录

```bash
cd /Users/niupi/worksapce/gitspace/AI-OPEN/WastWaterTool
```

#### 2️⃣ 给启动脚本赋予执行权限

```bash
chmod +x run_streamlit.sh
```

#### 3️⃣ 运行启动脚本

```bash
./run_streamlit.sh
```

#### 4️⃣ 打开浏览器

脚本运行后，会显示：
```
Local URL: http://localhost:8501
```

复制这个 URL 到浏览器中打开即可。

---

### Windows

#### 1️⃣ 打开命令提示符或 PowerShell

进入项目目录：
```cmd
cd C:\path\to\WastWaterTool
```

#### 2️⃣ 双击运行启动脚本

直接双击 `run_streamlit.bat` 文件，或在命令行中运行：

```cmd
run_streamlit.bat
```

#### 3️⃣ 打开浏览器

会自动在浏览器中打开应用，URL 通常是：
```
http://localhost:8501
```

---

## 🎯 基本使用

### 首页

- 查看应用功能概览
- 了解核心参数说明
- 查看计算公式

### 计算工具（推荐开始）

1. 选择计算模式：
   - **计算 SLR**: 输入 MLSS 和 Flow，计算 SLR
   - **计算 MLSS**: 输入 SLR 和 Flow，计算 MLSS
   - **计算 Flow**: 输入 MLSS 和 SLR，计算 Flow

2. 输入数值，点击"🔄 计算"

3. 查看结果和安全建议

### 数据查看

- 查看原始的 MLSS 浓度表
- 下载为 CSV 或 Excel

### 参数对比

- 对比多个运行方案
- 评估每个方案的安全性
- 查看可视化图表

### 敏感性分析

- 分析参数变化的影响
- 理解参数间的关系
- 优化运行条件

---

## 🔧 常见命令

### 启动应用

```bash
# 默认启动
streamlit run app.py

# 指定端口
streamlit run app.py --server.port 8080

# 调试模式
streamlit run app.py --logger.level=debug
```

### 停止应用

在终端中按 `Ctrl+C`

### 清除缓存

```bash
streamlit cache clear
```

---

## 📊 页面功能速查

| 页面 | 功能 | 用途 |
|------|------|------|
| 📊 首页 | 功能介绍 | 了解应用 |
| 🔧 计算工具 | 快速计算 | 计算参数 |
| 📈 数据查看 | 查看表格 | 参考数据 |
| 🔀 参数对比 | 方案对比 | 选择方案 |
| 📉 敏感性 | 趋势分析 | 参数优化 |

---

## 💡 使用技巧

### 💡 技巧 1：快速计算

最常用的是"计算工具"页面，可以快速计算参数值。

### 💡 技巧 2：查看建议

计算结果下方会显示"💡 运行建议"，按建议调整参数。

### 💡 技巧 3：对比优选

使用"参数对比"功能可以对比多个方案，快速选择最优方案。

### 💡 技巧 4：导出数据

在"数据查看"页面可以导出原始数据为 CSV 或 Excel。

---

## ❓ 常见问题

### Q: 应用打不开？

**A**: 确保：
1. Streamlit 已成功安装
2. 应用仍在运行（检查终端）
3. 浏览器打开的是 `http://localhost:8501`
4. 尝试刷新页面 (Ctrl+R)

### Q: 找不到数据文件？

**A**: 确保 `data/MLSS浓度表.xlsx` 文件存在。

### Q: 应用运行很慢？

**A**: 这是正常的。第一次加载会初始化环境，可能需要几秒。

### Q: 如何退出应用？

**A**: 在终端中按 `Ctrl+C`

---

## 📚 更多文档

- 📖 **完整使用指南**: `doc/Streamlit前端使用指南.md`
- 📊 **核心模块文档**: `doc/工程架构描述.md`
- 💻 **Excel 集成指南**: `doc/Excel集成指南.md`
- 🔧 **依赖说明**: `doc/DEPENDENCIES.md`

---

## 🎉 成功启动！

如果看到以下信息，说明应用已成功启动：

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

在浏览器中打开 `http://localhost:8501` 开始使用！

---

**更新时间**: 2026-02-13
**Streamlit 版本**: 1.28+
**Python 版本**: 3.8+

