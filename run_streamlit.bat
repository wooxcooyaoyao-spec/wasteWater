@echo off
REM Streamlit 应用启动脚本 (Windows)

echo 启动污泥处理计算工具 Web 应用...
echo.

REM 检查虚拟环境
if not exist "venv" (
    echo 创建虚拟环境...
    python3 -m venv venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call venv\Scripts\activate

REM 安装依赖
echo 安装依赖...
python3 -m pip install -r requirements.txt

REM 启动 Streamlit 应用
echo 启动 Streamlit 应用...
echo.
streamlit run app.py

pause

