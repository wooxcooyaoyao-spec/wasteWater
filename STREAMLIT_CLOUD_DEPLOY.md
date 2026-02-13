# Streamlit Cloud 部署指南

## 问题解决

### 错误：`showStderrMessageOnSuccess` 不是有效的配置选项

**原因**：该配置选项已在较新版本的 Streamlit 中被移除。

**解决**：已在 `.streamlit/config.toml` 中移除此选项。

### 错误：`connection refused` 或应用启动失败

**原因**：通常是由于以下几个原因：
1. `xlwings` 依赖在云环境中无法安装（需要 Windows/Mac/Linux 的特殊系统库）
2. 其他系统级别的依赖缺失

**解决**：
1. 已将 `xlwings` 从 `requirements.txt` 中移除
2. `xlwings` 现在是可选依赖，仅在本地开发中需要

## 部署步骤

### 方法 1：通过 GitHub 部署（推荐）

1. 将代码推送到 GitHub
2. 访问 [share.streamlit.io](https://share.streamlit.io)
3. 点击 "New App" 并选择你的 GitHub 仓库
4. 选择分支和 `app.py` 文件
5. 点击 "Deploy"

### 方法 2：本地部署测试

```bash
# 在项目根目录
streamlit run app.py
```

## 配置文件说明

### `.streamlit/config.toml`

当前配置已针对 Streamlit Cloud 环境优化：

- `headless = true` - 在服务器环境中运行
- `enableXsrfProtection = true` - 启用 CSRF 保护
- `showErrorDetails = true` - 显示详细错误信息

### `requirements.txt`

已移除 `xlwings` 依赖。本地开发若需要 Excel 集成功能，请手动安装：

```bash
pip install xlwings>=0.27.0
```

### `packages.txt`

此文件为 Streamlit Cloud 的系统包依赖配置，目前为空（无额外系统依赖）。

## 常见问题

### 为什么 `xlwings` 被移除了？

`xlwings` 在 Streamlit Cloud 等云环境中容易导致部署失败，因为：
1. 需要特定的系统库支持
2. Streamlit Cloud 沙箱环境的限制
3. Streamlit 前端不需要 `xlwings` 功能

本地使用 Excel 集成功能时，可以单独安装。

### 如何在本地使用 Excel 集成功能？

```bash
# 安装可选依赖
pip install xlwings>=0.27.0

# 或使用 pyproject.toml 的可选依赖
pip install -e ".[excel]"
```

### 部署后应用还是无法启动？

1. 检查 Streamlit Cloud 的部署日志
2. 确保 `app.py` 在仓库的根目录或指定的正确路径
3. 尝试在本地运行 `streamlit run app.py` 验证代码正确性

## 环境变量

如需在 Streamlit Cloud 上设置环境变量：

1. 在项目设置中点击 "Advanced settings"
2. 添加环境变量
3. 重新部署应用

## 支持

如遇到问题，请检查：
- Streamlit 官方文档：https://docs.streamlit.io
- GitHub Issues
- Streamlit Cloud 部署日志

