# 示例展示

## LLM

### DeepSeek-R1-Distill-Qwen-7B

```
# 下载仓库
cd /root/
 
hf download AXERA-TECH/DeepSeek-R1-Distill-Qwen-7B --local-dir DeepSeek-R1-Distill-Qwen-7B
 
cd DeepSeek-R1-Distill-Qwen-7B/
chmod 755 main_ax650 run_deepseek-r1_7b_ax650.sh
 
# 运行
cd /root/DeepSeek-R1-Distill-Qwen-7B/
python3 deepseek-r1_tokenizer.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/DeepSeek-R1-Distill-Qwen-7B/
./run_deepseek-r1_7b_ax650.sh
```

### DeepSeek-R1-Distill-Qwen-1.5B

```
# 下载仓库
cd /root/
 
hf download AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B --local-dir DeepSeek-R1-Distill-Qwen-1.5B
 
cd DeepSeek-R1-Distill-Qwen-1.5B/
chmod 755 main_ax650 run_deepseek-r1_1.5b_ax650.sh
 
# 运行
cd /root/DeepSeek-R1-Distill-Qwen-1.5B/
python3 deepseek-r1_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/DeepSeek-R1-Distill-Qwen-1.5B/
./run_deepseek-r1_1.5b_ax650.sh
```

### Qwen3-4B

```
# 下载仓库
cd /root/ 
hf download AXERA-TECH/Qwen3-4B --local-dir Qwen3-4B
 
cd Qwen3-4B/
chmod 755 main_ax650 run_qwen3_4b_int8_ctx_ax650.sh
 
# 运行
cd /root/Qwen3-4B/
python3 qwen3_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen3-4B/
./run_qwen3_4b_int8_ctx_ax650.sh
```

### Qwen3-1.7B

```
# 下载仓库
cd /root/ 
hf download AXERA-TECH/Qwen3-1.7B --local-dir Qwen3-1.7B
 
cd Qwen3-1.7B/
chmod 755 main_ax650 run_qwen3_1.7b_int8_ctx_ax650.sh
 
# 运行
cd /root/Qwen3-1.7B/
python3 qwen3_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen3-1.7B/
./run_qwen3_1.7b_int8_ctx_ax650.sh
```

### Qwen2.5-7B-Instruct

```
# 下载仓库
cd /root/
hf download AXERA-TECH/Qwen2.5-7B-Instruct --local-dir Qwen2.5-7B-Instruct
 
cd Qwen2.5-7B-Instruct/
chmod 777 main_ax650 run_qwen2.5_7b_ctx_int4_ax650.sh
 
# 运行
cd /root/Qwen2.5-7B-Instruct/
python3 qwen2.5_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen2.5-7B-Instruct/
./run_qwen2.5_7b_ctx_int4_ax650.sh
```

### Qwen2.5-1.5B-Instruct

```
# 下载仓库
cd /root/
hf download AXERA-TECH/Qwen2.5-1.5B-Instruct --local-dir Qwen2.5-1.5B-Instruct
 
cd Qwen2.5-1.5B-Instruct/
chmod 777 main_ax650 run_qwen2.5_1.5b_ctx_ax650.sh

# 运行
cd /root/Qwen2.5-1.5B-Instruct/
python3 qwen2.5_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen2.5-1.5B-Instruct/
./run_qwen2.5_1.5b_ctx_ax650.sh
```

## Multimodal Models

### 第三方依赖

```
cd /root/
hf download AXERA-TECH/awesome-files --local-dir awesome-files
cp awesome-files/FFmpeg-n4.4.6-ax650.tar.gz ./
cp awesome-files/decord-ax650.tar.gz ./
```

### InternVL3-2B.axera(图片&视频理解)

```
# 用户使用提供的包：FFmpeg-n4.4.6-ax650.tar.gz
tar xzvf FFmpeg-n4.4.6-ax650.tar.gz
cd FFmpeg-n4.4.6/
make install
 
# 安装decord
cd /root/

# 用户使用提供的包：decord-ax650.tar.gz
tar xzvf decord-ax650.tar.gz
cd decord/python/
export PYTHONPATH=$PYTHONPATH:$PWD
python3 setup.py install --user
 
# 下载仓库
cd /root/
hf download AXERA-TECH/InternVL3-2B --local-dir InternVL3-2B
 
# 运行
cd InternVL3-2B
 
# sample1
python3 infer.py --hf_model internvl3_2b_tokenizer/ --axmodel_path internvl3_2b_axmodel/ --question "请计算函数[y=2x^2+2]的导数, 并提供 markdown 格式的推理过程"
 
# sample2
python3 infer.py --hf_model internvl3_2b_tokenizer/ --axmodel_path internvl3_2b_axmodel/ -q "请分别描述这几幅图像的内容, 并找出它们的异同点" -i examples/image_0.jpg examples/image_1.jpg examples/image_2.png examples/image_3.png --vit_model vit_axmodel/internvl3_2b_vit_slim.axmodel

# sample3
python3 infer_video.py --hf_model internvl3_2b_tokenizer/ --axmodel_path internvl3_2b_axmodel/ --vit_model vit_axmodel/internvl3_2b_vit_slim.axmodel -q "请描述这个视频" -i examples/red-panda.mp4

# sample4， web页面
# 需要安装依赖 gradio，“安装 python 依赖” 小节已包含
python3 gradio_demo_python_api.py --hf_model internvl3_2b_tokenizer/ \
                                 --axmodel_path internvl3_2b_axmodel/ \
                                 --vit_model vit_axmodel/internvl3_2b_vit_slim.axmodel

# 运行后，查看最后log里打印的web地址，例如：“HTTP 服务地址: http://10.126.20.94:7860”。需要用浏览器打开页面来进行交互。
#可以直接使用板子自身桌面系统上的浏览器打开，也可以使用同一局域网内的电脑或手机或其他设备的浏览器打开。
```

### Qwen2.5-VL-3B-Instruct(图片&视频理解)

```
# 下载仓库
cd /root/
hf download AXERA-TECH/Qwen2.5-VL-3B-Instruct --local-dir Qwen2.5-VL-3B-Instruct

cd Qwen2.5-VL-3B-Instruct/
chmod 755 run_qwen2_5_vl_image.sh run_qwen2_5_vl_video.sh main_ax650
 
# 运行
cd /root/Qwen2.5-VL-3B-Instruct/
 
# image sample
cd /root/Qwen2.5-VL-3B-Instruct/
python3 qwen2_tokenizer_image.py --host 127.0.0.1 --port 12345
 
# 再开一个终端执行
cd /root/Qwen2.5-VL-3B-Instruct/
./run_qwen2_5_vl_image.sh
 
# video sample
cd /root/Qwen2.5-VL-3B-Instruct/
python3 qwen2_tokenizer_video_308.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen2.5-VL-3B-Instruct/
./run_qwen2_5_vl_video.sh
```

### lcm-lora-sdv1-5(文生图)

```
# 下载仓库
cd /root/
hf download AXERA-TECH/lcm-lora-sdv1-5 --local-dir lcm-lora-sdv1-5
 
# 运行
cd /root/lcm-lora-sdv1-5/
python3 run_txt2img_axe_infer.py
```

### LibCLIP(文搜大模型)

```
# 下载仓库
cd /root/
hf download AXERA-TECH/LibCLIP --local-dir LibCLIP
 
# 运行
cd /root/LibCLIP
tar -xf coco_1000.tar
cp install/lib/host_650/libclip.so ./pyclip/

# 650 host 运行命令
python3 pyclip/gradio_example.py --ienc cnclip/cnclip_vit_l14_336px_vision_u16u8.axmodel --tenc cnclip/cnclip_vit_l14_336px_text_u16.axmodel --vocab cnclip/cn_vocab.txt --isCN 1 --db_path clip_feat_db_coco --image_folder coco_1000/ --dev_type host

#运行后，如板端ip地址为 192.168.1.100，则使用浏览器打开 http://192.168.1.100:7860 页面来进行交互。
#相关使用方法请参考：https://hf-mirror.com/AXERA-TECH/LibCLIP Model card说明
```

## Vision Models

### Depth-Anything-V2

```
# 下载仓库
cd /root/
hf download AXERA-TECH/Depth-Anything-V2 --local-dir Depth-Anything-V2

cd Depth-Anything-V2/python/
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
 
# 运行
cd /root/Depth-Anything-V2/python/
python3 infer.py --img ../examples/demo01.jpg --model ../depth_anything_v2_vits_ax650.axmodel
```

### YOLO-World-V2(万物检测)

```
# 下载仓库
cd /root/
hf download AXERA-TECH/YOLO-World-V2 --local-dir YOLO-World-V2
cd YOLO-World-V2
 
# 运行
cp install/lib/host_650/libyoloworld.so ./pyyoloworld/
cd pyyoloworld/
python3 gradio_example.py --yoloworld ../models/yolo_u16_ax650.axmodel --tenc ../models/clip_b1_u16_ax650.axmodel --vocab ../vocab.txt --dev_type host

# 运行后，查看最后 log 里打印的 web 地址，例如：“HTTP 服务地址: http://x.x.x.x:7860”，x.x.x.x 替换为板端 ip 地址，使用浏览器打开页面来进行交互。
# 可以直接使用板子自身桌面系统上的浏览器打开，也可以使用同一局域网内的电脑或手机或其他设备的浏览器打开。

#相关使用方法请参考：https://hf-mirror.com/AXERA-TECH/YOLO-World-V2 Model card说明
```

### YOLO11

```
# 下载仓库
cd /root/
hf download AXERA-TECH/YOLO11 --local-dir YOLO11

cd YOLO11/

# 使用提供的ax_yolo11
chmod 755 ./ax_aarch64/ax_yolo11
 
# 运行
cd /root/YOLO11/
./ax_aarch64/ax_yolo11 -m ax650/yolo11s.axmodel -i ssd_horse.jpg
```

## HuggingFaceTB

针对性适配 Huggingface 的 AI LAB 开源的 SLM(Small Large Language Model)

### SmolLM2-360M-Instruct

```
# 下载仓库
cd /root/
hf download AXERA-TECH/SmolLM2-360M-Instruct --local-dir SmolLM2-360M-Instruct

cd SmolLM2-360M-Instruct/
chmod 755 main_prefill run_smollm2_360m_ax650.sh
 
# 运行
cd /root/SmolLM2-360M-Instruct/
python3 smollm2_tokenizer.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/SmolLM2-360M-Instruct/
./run_smollm2_360m_ax650.sh
```

### SmolVLM-256M-Instruct

```
# 下载仓库
cd /root/
hf download AXERA-TECH/SmolVLM-256M-Instruct --local-dir SmolVLM-256M-Instruct

cd SmolVLM-256M-Instruct/
chmod 755 main run_smolvlm_ax650.sh
 
# 运行
cd /root/SmolVLM-256M-Instruct/
python3 smolvlm_tokenizer_512.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/SmolVLM-256M-Instruct/
./run_smolvlm_ax650.sh
```

## Audio Models

### SenseVoice

```
# 下载仓库
cd /root/
hf download AXERA-TECH/SenseVoice --local-dir SenseVoice
 
# 运行
cd /root/SenseVoice/
python3 main.py -i demo.wav
```

### Whisper

```
# 下载仓库
cd /root/
hf download AXERA-TECH/Whisper --local-dir Whisper
 
# 运行
cd /root/Whisper/cpp/
chmod 755 whisper_aarch64
./whisper_aarch64  -w ../demo.wav  -p ../models-ax650/small
```

### MeloTTS

```
# 下载仓库
cd /root/
hf download AXERA-TECH/MeloTTS --local-dir MeloTTS

cd MeloTTS
mkdir models
cp *.bin models/
 
# 运行
cd /root/MeloTTS/python/
export NLTK_DATA="/root/MeloTTS/nltk_data"
python3 melotts.py -s 爱芯元智半导体股份有限公司，致力于打造世界领先的人工智能感知与边缘计算芯片。服务智慧城市、智能驾驶、机器人的海量普惠的应用 -e ../encoder-onnx/encoder-zh.onnx -d ../decoder-ax650/decoder-zh.axmodel
```
