# 多语言支持 - Multilingual Support

## 🌐 功能说明 / Feature Description

应用现在支持中英文切换！The app now supports Chinese-English switching!

## 使用方式 / How to Use

### 1. 启动应用 / Start the app

```bash
streamlit run app.py
```

### 2. 点击语言按钮 / Click language buttons

在侧边栏顶部（Navigation Menu 上方）你会看到两个按钮：

**In the sidebar top (above Navigation Menu), you'll see two buttons:**

- 🇨🇳 **中文** - Switch to Chinese
- 🇬🇧 **English** - Switch to English

### 3. 页面会自动切换 / Page automatically switches

点击按钮后，整个应用界面会切换到对应的语言。

After clicking the button, the entire application interface will switch to the corresponding language.

## 当前支持的翻译 / Currently Supported Translations

- ✅ 侧边栏导航菜单 / Sidebar navigation menu
- ✅ 页面标题 / Page titles
- ✅ 核心功能标签 / Core function labels
- ✅ 100+ 个翻译字符串 / 100+ translation strings

## 翻译字典 / Translation Dictionary

翻译字典位于 `app.py` 顶部的 `TRANSLATIONS` 对象中。

The translation dictionary is located in the `TRANSLATIONS` object at the top of `app.py`.

### 结构 / Structure

```python
TRANSLATIONS = {
    "zh": {
        "key_name": "中文文本",
        ...
    },
    "en": {
        "key_name": "English text",
        ...
    }
}
```

### 获取翻译 / Get Translation

```python
get_text("key_name")  # 返回当前语言的文本 / Returns text in current language
```

## 如何添加更多翻译 / How to Add More Translations

### 步骤 1：添加翻译字符串 / Step 1: Add translation string

在 `TRANSLATIONS` 字典中添加新的键值对：

```python
TRANSLATIONS = {
    "zh": {
        "new_feature": "新功能",
        ...
    },
    "en": {
        "new_feature": "New Feature",
        ...
    }
}
```

### 步骤 2：在代码中使用 / Step 2: Use in code

```python
st.write(get_text("new_feature"))
```

## 代码示例 / Code Examples

### 显示标题 / Display title

```python
# 中文: 污泥处理计算工具
# 英文: Wastewater Treatment Calculator
st.title(get_text("app_title"))
```

### 显示按钮 / Display button

```python
# 中文: 🔄 计算
# 英文: 🔄 Calculate
if st.button(get_text("calculate_btn")):
    # 执行计算 / Execute calculation
    pass
```

### 显示指标卡 / Display metric

```python
st.metric(get_text("result"), f"{slr:.2f} kg/h/m²")
```

## Session State 管理 / Session State Management

应用使用 Streamlit 的 `session_state` 来存储当前语言选择：

```python
st.session_state.language  # "zh" 或 "en"
```

语言选择在用户会话中持久化。用户切换语言后，刷新页面会保持所选语言。

Language selection is persisted in the user session. After switching languages, refreshing the page will maintain the selected language.

##  当前缺失的翻译 / Currently Missing Translations

为了完整的多语言支持，以下内容仍然需要翻译：

- 计算页面中所有硬编码的中文字符串
- 数据查看页面的所有文本
- 参数对比和敏感性分析页面的所有文本
- 帮助侧边栏中的详细指导文本

To complete full multilingual support, the following still needs to be translated:

- All hardcoded Chinese strings in the calculator page
- All text in the data view page
- All text in comparison and sensitivity analysis pages
- Detailed guidance text in the help sidebar

## 扩展计划 / Expansion Plan

### 第 1 阶段 / Phase 1 (✅ 完成 / Completed)
- ✅ 建立翻译框架 / Establish translation framework
- ✅ 翻译导航菜单 / Translate navigation menu
- ✅ 添加语言切换按钮 / Add language switch button

### 第 2 阶段 / Phase 2 (进行中 / In Progress)
- ⏳ 翻译所有页面标题 / Translate all page titles
- ⏳ 翻译所有用户界面文本 / Translate all UI text
- ⏳ 翻译所有帮助文本 / Translate all help text

### 第 3 阶段 / Phase 3 (计划中 / Planned)
- 📋 添加更多语言支持 / Add more language support (日本語, 韓国語, 等)
- 📋 右到左语言支持 / RTL language support
- 📋 本地化日期和数字格式 / Localize date and number formats

## 测试 / Testing

### 测试语言切换 / Test language switching

1. 点击 "🇨🇳 中文" 按钮
2. 验证侧边栏菜单变为中文
3. 点击 "🇬🇧 English" 按钮
4. 验证侧边栏菜单变为英文

### 测试持久化 / Test persistence

1. 切换到英文
2. 刷新浏览器
3. 验证仍然是英文

## 技术细节 / Technical Details

### 语言检测 / Language Detection

```python
lang = st.session_state.get("language", "zh")  # 默认中文 / Default: Chinese
```

### 翻译获取函数 / Translation retrieval function

```python
def get_text(key: str) -> str:
    """获取当前语言的翻译文本"""
    lang = st.session_state.get("language", "zh")
    return TRANSLATIONS.get(lang, TRANSLATIONS["zh"]).get(key, key)
```

### 缺省行为 / Fallback behavior

如果翻译不存在，系统会返回键名本身（作为备选）。

If a translation doesn't exist, the system returns the key name itself (as fallback).

## 故障排除 / Troubleshooting

### 问题：页面切换不工作 / Issue: Language switch not working

**解决：**
1. 清除浏览器缓存
2. 刷新页面
3. 再次点击语言按钮

**Solution:**
1. Clear browser cache
2. Refresh the page
3. Click the language button again

### 问题：部分文本仍为中文 / Issue: Some text still in Chinese

**原因：** 这些文本还没有被翻译

**解决：** 查看"当前缺失的翻译"部分

**Reason:** Those texts haven't been translated yet

**Solution:** Refer to "Currently Missing Translations" section

## 贡献翻译 / Contribute Translations

欢迎提交翻译改进！

To contribute translations, please:

1. 在 `TRANSLATIONS` 字典中添加翻译
2. 在代码中用 `get_text()` 函数替换硬编码文本
3. 测试新的翻译
4. 提交更改

1. Add translations to the `TRANSLATIONS` dictionary
2. Replace hardcoded text with `get_text()` function in code
3. Test the new translations
4. Submit changes

---

**版本**: 1.0.0 | **Version**: 1.0.0
**最后更新**: 2026-02-13 | **Last Updated**: 2026-02-13

