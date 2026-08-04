# Configuration file for the Sphinx documentation builder.
#
# Full option list:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------

project = 'Axera Terminal Product Line Docs'
master_doc = 'index'
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
    "sphinx.ext.mathjax",      # 渲染数学公式的引擎，支持Latex风格
    'sphinx_copybutton',       #代码块一键复制功能，匹配requirement.txt安装的sphinx-copybutton
    #'sphinxcontrib.mermaid',   #流程图/时序图支持，匹配sphinxcontrib-mermaid
    #'sphinxcontrib.plantuml',  #plantuml支持，匹配sphinxcontrib-plantuml
    #'breathe'
    #'sphinx_tabs.tabs',
    #'sphinxcontrib.svg2pdfconverter', #apt_packages内需要librsvg2-bin
    #'linkify',                 # 自动将纯文本 URL 转换为可点击的超链接
]

templates_path = ['_templates']

# 忽略以 _ 开头的迁移过渡文件（_legacy_*），避免进入 toctree 时产生告警。
exclude_patterns = ['examples/*[!.zip]']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = 'AXERA Terminal Product Line Docs'

html_theme_options = {
    'repository_url': 'https://github.com/jessenchen/axera-terminal-product-manual',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'repository_branch': 'axera-terminal-product-manual',
    'path_to_docs': 'source',
}

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- mermaid -----------------------------------------------------------------
mermaid_output_format = 'raw'
# 同源加载本仓库内置的 mermaid（source/_static/mermaid/），不依赖 cdn.jsdelivr.net
# （该 CDN 在中国大陆常不可达，会导致流程图无法渲染）。
mermaid_version = '11.12.1'
mermaid_use_local = 'mermaid/mermaid.esm.min.mjs'
# raw 模式下扩展会额外加载 d3（全屏/缩放用），同样改为同源本地文件。
d3_version = '7.9.0'
d3_use_local = 'mermaid/d3.min.js'

# -- plantuml 支持--------------------------------------------------------------
#plantuml = 'plantuml'
#plantuml_output_format = 'svg'

# -- myst_parser支持------------------------------------------------------------
#myst_enable_extensions = [
#    'colon_fence',        # 允许使用 ::: 作为代码围栏的定界符，替代传统的 ```
#    'deflist',            # 启用定义列表语法，类似于 HTML 中的 <dl> 标签
#    'linkify',            # 自动将文档中的裸 URL（如 https://example.com）转换为可点击的超链接
#    'tasklist',           # 支持 GitHub 风格的任务列表语法，如 - [x] 已完成
    # 'dollarmath',         # 启用 LaTeX 风格的美元符号 $ 作为数学公式的定界符,
#]
# 为文档中的标题自动生成 HTML 锚点（ID），方便其他页面或链接直接引用，仅作用前三级标题
myst_heading_anchors = 3
# 让 ```mermaid 围栏同时在 GitHub 预览与 Sphinx 构建中渲染为流程图。
myst_fence_as_directive = ['mermaid']
# 自动更新
myst_update_mathjax = True

# --Breathe 连接 Doxygen 配置 -------------------------------------------------
# breathe_projects = {"X2000": os.path.join(os.path.dirname(__file__), "..", "doxygen", "xml")}
# breathe_default_project = "X2000"
# breathe_default_members = ('members', 'undoc-members')

# ----pdf格式生成
#svg2pdf_converter = 'cairosvg'
# 设置 LaTeX 引擎为 xelatex
#latex_engine = 'xelatex'
#latex_elements = {
#    'preamble': r'''
#        \usepackage[UTF8]{ctex}
#        % 指定系统存在的字体，例如 Noto Sans CJK SC
#        \setCJKmainfont{Noto Sans CJK SC}[
#            BoldFont=Noto Sans CJK SC Bold,
#            ItalicFont=Noto Sans CJK SC,
#        ]
#    ''',
#}

#latex_documents = [(master_doc, f'{project}.tex', project, author, 'manual'),]

# ----eupb格式生成
#epub_title = project
#epub_author = author
#epub_language = 'zh_CN'  # 例如 'zh_CN'
#epub_publisher = author   # 可选
#epub_copyright = '2026, AXERA Semiconductor Co., Ltd.'  # 可选
#epub_description = 'Axera Terminal Product Line Documentation' #可选

