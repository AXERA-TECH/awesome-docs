# awesome-docs 使用手册

[Web Preview](待补充)

## 1. 项目背景

**awesome-docs** 是为了方便基于 AX650N DEMO Board（16+64GB）客户推广使用时快速评估 NPU 特性使用。

- 指导搭建评估 NPU 示例必要的系统软件环境;
- 指导搭建评估 NPU 示例必要的软件依赖环境;
- 各种 NPU 示例获取及上板运行示例；
- 促进社区开发人员共同维护文档。

## 2. 本地编译指南

### 2.1 git clone

```bash
git clone https://github.com/AXERA-TECH/awesome-docs.git
```

目录如下:

```bash
.
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── res
└── source
    ├── 00_introduction.md
    ├── 01_hardware.md
    ├── 02_software.md
    ├── 03_samples.md
    ├── 04_faq.md
    ├── 05_resource.md
    ├── conf.py
    └── index.rst
```

### 2.2 编译

安装依赖

```bash
pip install -r requirements.txt
```

在项目根目录下执行以下命令

```bash
$ make clean
$ make html
```

### 2.3 本地预览

编译后，使用浏览器查看它 `build/html/index.html`

## 3. 参考设计

这个项目是基于Sphinx，更多关于Sphinx的信息可以在这里找到 https://www.sphinx-doc.org/en/master/

## 4. 在线发布

基于 [ReadtheDocs](https://readthedocs.org/) 平台代理在线 Web 服务。
