# 环境准备

## 主控开发板

### 固件版本

固件版本，是指烧写的 AXP 版本，确保手上的开发板已经升级到对应的版本，目前验证的是 `v3.6.2`。板子正常通电进入系统之后，使用 `cat /proc/ax_proc/version` 可以查询

```
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.73 aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Mon Sep  8 16:59:51 2025 from 10.126.33.50
root@ax650:~#
root@ax650:~# cat /proc/ax_proc/version
Ax_Version V3.6.2_20250731140456
root@ax650:~#

```

| 名称                | AXP 版本                                                     | OS:CMM |
| ------------------- | ------------------------------------------------------------ | ------ |
| AX650N DEMO Board   | AX650_emmc_ubuntu_rootfs_desktop_V3.6.2_20250731140456_NO26076_sdk | 6 : 10 |
| M4N-Dock(爱芯派Pro) | AX650_pipro_box_ubuntu_rootfs_desktop_V3.6.2_20250603154858_NO4873_sdk.axp | 4 : 4  |

对应的 axp 版本可以通过以下方式获取

- 签约客户请联系对应的 FAE 获取；
- 社区用户请从 [BoardImages](https://hf-mirror.com/AXERA-TECH/BoardImages) 获取。

### 网络确认

首先确保开发板能正常访问互联网。

```
root@ax650:~# ping www.baidu.com
PING www.a.shifen.com (180.101.49.44): 56 data bytes
64 bytes from 180.101.49.44: icmp_seq=0 ttl=49 time=33.924 ms
64 bytes from 180.101.49.44: icmp_seq=1 ttl=49 time=33.714 ms
64 bytes from 180.101.49.44: icmp_seq=2 ttl=49 time=33.718 ms
64 bytes from 180.101.49.44: icmp_seq=3 ttl=49 time=33.731 ms
^C--- www.a.shifen.com ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max/stddev = 33.714/33.772/33.924/0.088 ms
root@ax650:~#
```

### 环境依赖安装

#### 安装基础依赖

```
apt-get update
yes | apt-get install rsync python3-dev python3-setuptools unzip python3-pip
yes | apt-get install libsndfile1-dev libmecab-dev
yes | apt-get install libass-dev libfdk-aac-dev libmp3lame-dev libopus-dev libvpx-dev libx264-dev libx265-dev libssl-dev libgl1-mesa-glx
```

#### 安装 Python 依赖

```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy opencv-python transformers ml_dtypes tqdm jinja2 torch torchvision onnxruntime
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple ultralytics diffusers peft protobuf librosa kaldi_native_fbank sentencepiece
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple zhconv cn2an pypinyin jieba g2p_en nltk
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple gradio
```

#### 安装 huggingface_hub

```
cd /root/
# 外网下载安装
pip3 install huggingface_hub -i https://pypi.tuna.tsinghua.edu.cn/simple
# 配置国内镜像
export HF_ENDPOINT=https://hf-mirror.com
```

从 huggingface 上下载 repo，建议使用 huggingface_hub 下载。

#### 安装 PyAXEngine

PyAXEngine 是 NPU Python API，其 API 尽可能的兼容了算法工程师熟悉的 ONNXRuntime Python API，方便用户上板快速验证结果。源码仓库请见 [pyaxengine
](https://github.com/AXERA-TECH/pyaxengine)


直接从 Github 上下载安装（有概率失败😖）

```
wget https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc1/axengine-0.1.3-py3-none-any.whl
```

或者从 huggingface 镜像站上下载

```
hf download AXERA-TECH/PyAXEngine --local-dir PyAXEngine
cp PyAXEngine/axengine-0.1.3-py3-none-any.whl ./
```

安装 pyaxengine

```
pip3 install axengine-0.1.3-py3-none-any.whl
```

**基于 AX650N 主控开发板的依赖环境安装完成！🚀**

## 算力卡
### AXCL驱动安装

算力卡需要提前配置AXCL驱动，详细安装流程请参考：[AXCL文档](https://axcl-docs.readthedocs.io/zh-cn/latest/)

### 网络确认
首先确保开发板能正常访问互联网。

```
(base) axera@raspberrypi:~ $ ping www.baidu.com -c 5
PING www.a.shifen.com (180.101.49.44) 56(84) bytes of data.
64 bytes from 180.101.49.44: icmp_seq=1 ttl=49 time=34.1 ms
64 bytes from 180.101.49.44: icmp_seq=2 ttl=49 time=33.8 ms
64 bytes from 180.101.49.44: icmp_seq=3 ttl=49 time=33.9 ms
64 bytes from 180.101.49.44: icmp_seq=4 ttl=49 time=33.9 ms
64 bytes from 180.101.49.44: icmp_seq=5 ttl=49 time=33.9 ms

--- www.a.shifen.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4004ms
rtt min/avg/max/mdev = 33.831/33.924/34.122/0.103 ms
```

### 环境依赖安装
#### 安装基础依赖

```
apt-get update
yes | apt-get install rsync python3-dev python3-setuptools unzip python3-pip
yes | apt-get install libsndfile1-dev libmecab-dev
yes | apt-get install libass-dev libfdk-aac-dev libmp3lame-dev libopus-dev libvpx-dev libx264-dev libx265-dev libssl-dev libgl1-mesa-glx
```

#### 安装 Python 依赖

```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy opencv-python transformers ml_dtypes tqdm jinja2 torch torchvision onnxruntime
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple ultralytics diffusers peft protobuf librosa kaldi_native_fbank sentencepiece
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple zhconv cn2an pypinyin jieba g2p_en nltk
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple gradio
```

#### 安装 huggingface_hub

```
cd /root/
# 外网下载安装
pip3 install huggingface_hub -i https://pypi.tuna.tsinghua.edu.cn/simple
# 配置国内镜像
export HF_ENDPOINT=https://hf-mirror.com
```

从 huggingface 上下载 repo，建议使用 huggingface_hub 下载。

#### 安装 PyAXEngine

PyAXEngine 是 NPU Python API，其 API 尽可能的兼容了算法工程师熟悉的 ONNXRuntime Python API，方便用户上板快速验证结果。源码仓库请见 [pyaxengine
](https://github.com/AXERA-TECH/pyaxengine)


直接从 Github 上下载安装（有概率失败😖）

```
wget https://github.com/AXERA-TECH/pyaxengine/releases/download/0.1.3.rc1/axengine-0.1.3-py3-none-any.whl
```

或者从 huggingface 镜像站上下载

```
hf download AXERA-TECH/PyAXEngine --local-dir PyAXEngine
cp PyAXEngine/axengine-0.1.3-py3-none-any.whl ./
```

安装 pyaxengine

```
pip3 install axengine-0.1.3-py3-none-any.whl
```