"""
翻译管理器 - 负责加载和管理多语言文本

此模块提供了一个统一的翻译管理接口，支持：
- 多语言文本加载
- 动态语言切换
- 降级处理（如果翻译不存在）
- 缓存机制
"""

import json
from pathlib import Path

import streamlit as st


class TranslationManager:
    """多语言翻译管理器"""

    def __init__(self):
        """初始化翻译管理器，加载所有翻译文件"""
        self.base_dir = Path(__file__).parent
        self.translations = {}
        self._load_translations()

    def _load_translations(self):
        """从 JSON 文件加载所有翻译"""
        for lang in ["zh", "en", "hi", "es", "de", "sv"]:
            json_file = self.base_dir / f"{lang}.json"
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    self.translations[lang] = json.load(f)
            except FileNotFoundError:
                print(f"⚠️ 翻译文件未找到: {json_file}")
                self.translations[lang] = {}
            except json.JSONDecodeError as e:
                print(f"❌ 翻译文件格式错误 ({json_file}): {e}")
                self.translations[lang] = {}

    def get(self, key, lang=None):
        """
        获取翻译文本

        Args:
            key: 翻译键
            lang: 语言代码（默认使用当前语言）

        Returns:
            翻译文本，如果未找到则返回原始 key

        优先级：
            1. 指定语言的翻译
            2. 中文翻译（降级）
            3. 原始 key（最后降级）
        """
        if lang is None:
            lang = st.session_state.get("language", "zh")

        # 从指定语言的翻译字典中获取
        if lang in self.translations and key in self.translations[lang]:
            return self.translations[lang][key]

        # 降级：尝试中文
        if lang != "zh" and "zh" in self.translations and key in self.translations["zh"]:
            return self.translations["zh"][key]

        # 最后降级：返回原始 key
        return key

    def reload(self):
        """
        重新加载翻译文件

        用于开发调试，不需要重启应用就能更新翻译
        """
        self.translations = {}
        self._load_translations()

    def get_all_keys(self, lang="zh"):
        """
        获取指定语言的所有翻译键

        用于调试和文档生成
        """
        return list(self.translations.get(lang, {}).keys())

    def get_missing_keys(self):
        """
        获取缺失的翻译键（中文有但英文没有的）

        用于质量控制和翻译完整性检查
        """
        zh_keys = set(self.translations.get("zh", {}).keys())
        en_keys = set(self.translations.get("en", {}).keys())
        return zh_keys - en_keys


# 全局翻译管理器实例
translation_manager = TranslationManager()


def t(key):
    """
    快速翻译函数

    在 Streamlit 应用中使用此函数获取翻译文本

    使用示例：
        st.write(t("title"))
        st.button(t("btn_calculate"))
    """
    return translation_manager.get(key)

