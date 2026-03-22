# 示例展示

## 安装AX-LLM

LLM和Multimodal Models的示例需要依赖AX-LLM工具来运行，用户可以通过以下任一方式安装AX-LLM：

方式一：克隆仓库后执行安装脚本：

```shell
git clone -b axllm https://github.com/AXERA-TECH/ax-llm.git
cd ax-llm
./install.sh
```

方式二：一行命令安装（默认分支 `axllm`）：

```shell
curl -fsSL https://raw.githubusercontent.com/AXERA-TECH/ax-llm/axllm/install.sh | bash
```

方式三：下载Github Actions CI 导出的可执行程序（适合没有编译环境的用户）：

如果没有编译环境，请到：
`https://github.com/AXERA-TECH/ax-llm/actions?query=branch%3Aaxllm`
下载 **最新 CI 导出的可执行程序**（`axllm`），然后：

```shell
chmod +x axllm
sudo mv axllm /usr/bin/axllm
```

## LLM

### Qwen3-4B

```
# 下载仓库
cd /root/
mkdir -p AXERA-TECH/Qwen3-4B
cd AXERA-TECH/Qwen3-4B

# 使用 huggingface 下载命令
hf download AXERA-TECH/Qwen3-4B --local-dir .
# 使用 modelscope 下载命令
modelscope download AXERA-TECH/Qwen3-4B --local_dir .
 
cd /root
# 运行 CLI
axllm run AXERA-TECH/Qwen3-4B/

# 运行 API 服务
axllm serve AXERA-TECH/Qwen3-4B/

# 详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Qwen3-4B 或https://modelscope.cn/models/AXERA-TECH/Qwen3-4B Model card说明
```

### Qwen3-1.7B

```
# 下载仓库
cd /root/
mkdir -p AXERA-TECH/Qwen3-1.7B
cd AXERA-TECH/Qwen3-1.7B

# 使用 huggingface 下载命令
hf download AXERA-TECH/Qwen3-1.7B --local-dir .
# 使用 modelscope 下载命令
modelscope download AXERA-TECH/Qwen3-1.7B --local_dir .
 
cd /root
# 运行 CLI
axllm run AXERA-TECH/Qwen3-1.7B/

# 运行 API 服务
axllm serve AXERA-TECH/Qwen3-1.7B/

# 详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Qwen3-1.7B 或 https://modelscope.cn/models/AXERA-TECH/Qwen3-1.7B Model card说明
```

### Qwen3-0.6B

```
# 下载仓库
cd /root/
mkdir -p AXERA-TECH/Qwen3-0.6B
cd AXERA-TECH/Qwen3-0.6B

# 使用 huggingface 下载命令
hf download AXERA-TECH/Qwen3-0.6B --local-dir .
# 使用 modelscope 下载命令
modelscope download AXERA-TECH/Qwen3-0.6B --local_dir .

cd /root
# 运行 CLI
axllm run AXERA-TECH/Qwen3-0.6B/
# 运行 API 服务
axllm serve AXERA-TECH/Qwen3-0.6B/

# 详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Qwen3-0.6B 或 https://modelscope.cn/models/AXERA-TECH/Qwen3-0.6B Model card说明
```

## Multimodal Models

### Qwen3-VL-2B-Instruct-GPTQ-Int4(图片&视频理解)

```
# 下载仓库
cd /root/
mkdir -p AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4
cd AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4

# huggingface 下载命令
hf download AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4 --local-dir .
# modelscope 下载命令
modelscope download AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4 --local_dir .

cd /root
# 运行 CLI
axllm run AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4/
# 运行 API 服务
axllm serve AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4/

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4 或 https://modelscope.cn/models/AXERA-TECH/Qwen3-VL-2B-Instruct-GPTQ-Int4 Model card说明
```

### FastVLM-1.5B(图片理解)

```
# 下载仓库
cd /root/
mkdir -p AXERA-TECH/FastVLM-1.5B
cd AXERA-TECH/FastVLM-1.5B

# huggingface 下载命令
hf download AXERA-TECH/FastVLM-1.5B --local-dir .
# modelscope 下载命令
modelscope download AXERA-TECH/FastVLM-1.5B --local_dir .

# 运行
cd /root/
# 运行 CLI
axllm run AXERA-TECH/FastVLM-1.5B/
# 运行 API 服务
axllm serve AXERA-TECH/FastVLM-1.5B/

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/FastVLM-1.5B 或 https://modelscope.cn/models/AXERA-TECH/FastVLM-1.5B Model card说明
```

## Vision Models

### Depth-Anything-V2

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/Depth-Anything-V2 --local-dir Depth-Anything-V2
# modelscope 下载命令
modelscope download AXERA-TECH/Depth-Anything-V2 --local_dir Depth-Anything-V2

cd Depth-Anything-V2/python/
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
 
# 运行
cd /root/Depth-Anything-V2/python/
python3 infer.py --img ../examples/demo01.jpg --model ../depth_anything_v2_vits_ax650.axmodel

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Depth-Anything-V2 或 https://modelscope.cn/models/AXERA-TECH/Depth-Anything-V2 Model card说明
```

### YOLO-World-V2(万物检测)

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/YOLO-World-V2 --local-dir YOLO-World-V2
# modelscope 下载命令
modelscope download AXERA-TECH/YOLO-World-V2 --local_dir YOLO-World-V2

cd YOLO-World-V2

# 运行
cp install/lib/host_650/libyoloworld.so ./pyyoloworld/
cd pyyoloworld/
python3 gradio_example.py --yoloworld ../models/yolo_u16_ax650.axmodel --tenc ../models/clip_b1_u16_ax650.axmodel --vocab ../vocab.txt

# 运行后，查看最后 log 里打印的 web 地址，例如：“HTTP 服务地址: http://x.x.x.x:7860”，x.x.x.x 替换为板端 ip 地址，使用浏览器打开页面来进行交互。
# 可以直接使用板子自身桌面系统上的浏览器打开，也可以使用同一局域网内的电脑或手机或其他设备的浏览器打开。

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/YOLO-World-V2 或 https://modelscope.cn/models/AXERA-TECH/YOLO-World-V2 Model card说明
```

### YOLO11

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/YOLO11 --local-dir YOLO11
# modelscope 下载命令
modelscope download AXERA-TECH/YOLO11 --local_dir YOLO11

cd YOLO11/

# 使用提供的ax_yolo11
chmod 755 ./ax_aarch64/ax_yolo11
 
# 运行
cd /root/YOLO11/
./ax_aarch64/ax_yolo11 -m ax650/yolo11s.axmodel -i ssd_horse.jpg

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/YOLO11 或 https://modelscope.cn/models/AXERA-TECH/YOLO11 Model card说明
```

## HuggingFaceTB

针对性适配 Huggingface 的 AI LAB 开源的 SmolLM2-360M-Instruct 和 SmolVLM2-500M-Video-Instruct_Ax650 模型，提供了在 Ax650 Demo 板上运行的示例，用户可以参考上述示例快速上手运行 Huggingface 的模型。

### SmolLM2-360M-Instruct

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/SmolLM2-360M-Instruct --local-dir SmolLM2-360M-Instruct
# modelscope 下载命令
modelscope download AXERA-TECH/SmolLM2-360M-Instruct --local_dir SmolLM2-360M-Instruct

cd SmolLM2-360M-Instruct/
chmod 755 main_* run_smollm2_360m_*.sh
 
# 运行
cd /root/SmolLM2-360M-Instruct/
python3 smollm2_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/SmolLM2-360M-Instruct/
./run_smollm2_360m_ax650.sh

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/SmolLM2-360M-Instruct 或 https://modelscope.cn/models/AXERA-TECH/SmolLM2-360M-Instruct Model card说明
```

### SmolVLM2-500M-Video-Instruct

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/SmolVLM2-500M-Video-Instruct --local-dir SmolVLM2-500M-Video-Instruct
# modelscope 下载命令
modelscope download AXERA-TECH/SmolVLM2-500M-Video-Instruct --local_dir SmolVLM2-500M-Video-Instruct

# 运行
cd /root/
# 运行 CLI
axllm run AXERA-TECH/SmolVLM2-500M-Video-Instruct/
# 运行 API 服务
axllm serve AXERA-TECH/SmolVLM2-500M-Video-Instruct/

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/SmolVLM2-500M-Video-Instruct 或 https://modelscope.cn/models/AXERA-TECH/SmolVLM2-500M-Video-Instruct Model card说明
```

## Audio Models

### 3D-Speaker-MT.axera（会议音频转录）
```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/3D-Speaker-MT.axera --local-dir 3D-Speaker-MT.axera
# modelscope 下载命令
modelscope download AXERA-TECH/3D-Speaker-MT.axera --local_dir 3D-Speaker-MT.axera

# 安装相关依赖
cd /root/3D-Speaker-MT.axera/
pip3 install -r requirements.txt
pip3 install ax_meeting-0.1.0-py3-none-any.whl

# 运行
python3 -m ax_meeting.server
# 点击终端里打印的链接（例如：http://x.x.x.x:8000）进入会议转录界面，上传会议音频文件（例如：vad_example.wav）即可查看转录结果。

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/3D-Speaker-MT.axera 或 https://modelscope.cn/models/AXERA-TECH/3D-Speaker-MT.axera Model card说明
```

### SenseVoice

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/SenseVoice --local-dir SenseVoice
# modelscope 下载命令
modelscope download AXERA-TECH/SenseVoice --local_dir SenseVoice
 
# 运行
cd /root/SenseVoice/
pip3 install -r requirements.txt
python3 main.py -i ./example/zh.mp3

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/SenseVoice 或 https://modelscope.cn/models/AXERA-TECH/SenseVoice Model card说明
```

### Whisper

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/Whisper --local-dir Whisper
# modelscope 下载命令
modelscope download AXERA-TECH/Whisper --local_dir Whisper
 
# 运行
cd /root/Whisper
pip3 install -r requirements.txt
cd ./python
python3 main.py --model_type small --model_path ../models-ax650 --wav ../demo.wav --language zh

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/Whisper 或 https://modelscope.cn/models/AXERA-TECH/Whisper Model card说明
```

### Kokoro

```
# 下载仓库
cd /root/
# huggingface 下载命令
hf download AXERA-TECH/kokoro.axera --local-dir kokoro.axera
# modelscope 下载命令
modelscope download AXERA-TECH/kokoro.axera --local_dir kokoro.axera

cd kokoro.axera
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm
 
# 运行
# 中文：
python kokoro_ax.py --text "致力于打造世界领先的人工智能感知与边缘计算芯片。" --lang zh --voice checkpoints/voices/zf_xiaoyi.pt --output output_zh.wav -d models -f 0.3
# 英文：
python kokoro_ax.py --text "The sky above the port was the color of television, tuned to a dead channel." --lang en --voice checkpoints/voices/af_heart.pt --output output_en.wav -d models -f 0.3
# 日文：
python kokoro_ax.py --text "「もしおれがただ偶然、そしてこうしようというつもりでなくここに立っているのなら、ちょっとばかり絶望するところだな」と、そんなことが彼の頭に思い浮かんだ。" --lang ja --voice checkpoints/voices/jm_kumo.pt --output output_jp.wav -d models -f 0.3

#详细使用方法请参考：https://hf-mirror.com/AXERA-TECH/MeloTTS 或 https://modelscope.cn/models/AXERA-TECH/MeloTTS Model card说明
```