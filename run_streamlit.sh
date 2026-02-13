#!/bin/bash
# Streamlit 应用启动脚本

echo "启动污泥处理计算工具 Web 应用..."
echo ""

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "安装依赖..."
python3 -m pip install -r requirements.txt

# 启动 Streamlit 应用
echo "启动 Streamlit 应用..."
echo ""
streamlit run app.py

