# Configuration file for the Sphinx documentation builder.
#
# Full option list:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------

project = 'Edge Computing Docs'
copyright = '2026, AXERA Semiconductor Co., Ltd.'
author = 'AXERA & Community'

# The full version, including alpha/beta/rc tags
release = 'v1.0.0'

# -- Internationalization ----------------------------------------------------
# 语言由环境变量驱动，便于同一份配置服务中文 / 英文两个 Read the Docs 项目。
# Read the Docs 在翻译项目构建时会注入 READTHEDOCS_LANGUAGE。
language = os.environ.get('READTHEDOCS_LANGUAGE', 'zh_CN')

# gettext 翻译文件目录（sphinx-intl 生成的 .po/.mo 存放处）
locale_dirs = ['../locale/']
gettext_compact = False
gettext_uuid = True

# -- General configuration ---------------------------------------------------

# myst_parser 支持 Markdown，sphinxcontrib.mermaid 支持流程图/雷达图，
# sphinx_copybutton 提供代码块一键复制。
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']

# 忽略以 _ 开头的迁移过渡文件（_legacy_*），避免进入 toctree 时产生告警。
exclude_patterns = ['examples/*[!.zip]']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = 'AXERA Edge Computing Docs'

# 所有构建环境都使用独立部署的 docs-assistant API。RTD 和本地 Sphinx
# 只生成静态页面；如需切换服务地址，请通过 DOCS_ASSISTANT_API_URL 覆盖。
docs_assistant_api_url = os.environ.get(
    'DOCS_ASSISTANT_API_URL',
    'https://chatbot.hlleng.xx.kg/api/docs-assistant',
).strip()
html_css_files = ['assistant/assistant.css']
html_js_files = [
    (
        'assistant/assistant.js',
        {
            'defer': 'defer',
            'data-api-url': docs_assistant_api_url,
            'data-language': language,
        },
    ),
]

html_theme_options = {
    'repository_url': 'https://github.com/AXERA-TECH/awesome-docs',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'repository_branch': 'dev',
    'path_to_docs': 'source',
}

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# -- mermaid -----------------------------------------------------------------
mermaid_output_format = 'raw'
# 同源加载本仓库内置的 mermaid（source/_static/mermaid/），不依赖 cdn.jsdelivr.net
# （该 CDN 在中国大陆常不可达，会导致流程图无法渲染）。
mermaid_version = '11.12.1'
mermaid_use_local = 'mermaid/mermaid.esm.min.mjs'
# raw 模式下扩展会额外加载 d3（全屏/缩放用），同样改为同源本地文件。
d3_version = '7.9.0'
d3_use_local = 'mermaid/d3.min.js'

# -- myst_parser -------------------------------------------------------------
myst_enable_extensions = ['colon_fence', 'deflist', 'linkify', 'tasklist']
myst_heading_anchors = 3
# 让 ```mermaid 围栏同时在 GitHub 预览与 Sphinx 构建中渲染为流程图。
myst_fence_as_directive = ['mermaid']
