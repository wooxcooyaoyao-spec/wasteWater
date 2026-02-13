#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WasteWaterTool 安装配置文件

污泥处理系统参数计算工具
"""

from pathlib import Path

from setuptools import setup, find_packages

# 读取 README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# 项目基本信息
setup(
    name="WasteWaterTool",
    version="1.0.0",

    # 项目描述
    description="污泥处理系统参数计算工具 - 专为自来水处理污泥处理环节设计",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # 作者信息
    author="WasteWaterTool Developer",
    author_email="",
    url="https://github.com/yourusername/WasteWaterTool",

    # 项目信息
    project_urls={
        "Documentation": "https://github.com/yourusername/WasteWaterTool#readme",
        "Source Code": "https://github.com/yourusername/WasteWaterTool",
        "Issue Tracker": "https://github.com/yourusername/WasteWaterTool/issues",
    },

    # 许可证
    license="MIT",

    # 分类
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],

    # Python 版本要求
    python_requires=">=3.7",

    # 包查找
    packages=find_packages(exclude=["tests", "docs", "examples"]),

    # 必需依赖
    install_requires=[
        "openpyxl>=3.0.0",
        "xlwings>=0.27.0",
        "streamlit>=1.28.0",
        "pandas>=1.5.0",
    ],

    # 可选依赖
    extras_require={},

    # 数据文件
    package_data={
        "": ["data/*.xlsx", "data/*.jpg", "doc/*.md", "output/*.xlsx"],
    },

    # 包含所有数据文件
    include_package_data=True,

    # 关键字
    keywords=[
        "wastewater",
        "treatment",
        "parameters",
        "calculation",
        "excel",
        "analysis",
        "slr",
        "mlss",
        "污泥处理",
        "参数计算",
        "Excel分析",
    ],

    # 入口点 (可选)
    entry_points={
        "console_scripts": [
            # 可在命令行中运行: wastewater-tool
            # "wastewater-tool=wastewater_tool.cli:main",
        ],
    },

    # 项目URL
    zip_safe=False,  # 不以 zip 形式安装
)

