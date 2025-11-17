# 示例展示（算力卡 x86 平台，多芯级联）

## Pulsar2
Pulsar2 由 爱芯元智 自主研发 的 all-in-one 新一代神经网络编译器, 即 转换、 量化、 编译、 异构 四合一, 实现深度学习神经网络模型 快速、 高效 的部署需求. 针对新一代 AX6、M7、M5 系列芯片（AX615、AX630C、AX637、AX620Q、AX650A、AX650N、M76H、M57H 等）特性进行了深度定制优化, 充分发挥片上异构计算单元(CPU+NPU)算力, 提升神经网络模型的产品部署效率.

工具链下载地址: [Pulsar2](https://huggingface.co/AXERA-TECH/Pulsar2/tree/main)
相关使用文档：[Pulsar2 Doc](https://pulsar2-docs.readthedocs.io/zh-cn/latest/pulsar2/introduction.html)

Pulsar2提供多芯级联模型编译功能，当前支持Qwen系列LLM编译，以Qwen2.5-7B-Instruct为例
编译命令
```
pulsar2 llm_build --input_path Qwen2.5-7B-Instruct \
                  --output_path Qwen2.5-7B-Instruct-parallel \
                  --hidden_state_type bf16 \
                  --prefill_len 128 --kv_cache_len 2047 \
                  --last_kv_cache_len 128 --last_kv_cache_len 256 \
                  --last_kv_cache_len 384 --last_kv_cache_len 512 \
                  --last_kv_cache_len 640 --last_kv_cache_len 768 \
                  --last_kv_cache_len 896 --last_kv_cache_len 1024 \
                  --chip AX650 -c 1 --parallel 8 --tensor_parallel_size 4
```

## LLM
### Qwen2.5-7B-Instruct-TensorParallel
```
# 下载仓库
cd /root/
hf download AXERA-TECH/Qwen2.5-7B-Instruct-TensorParallel --local-dir Qwen2.5-7B-Instruct-TensorParallel

cd ./Qwen2.5-7B-Instruct-TensorParallel/
chmod 755 main_a* run_qwen2.5_7B_*
 
# 运行
cd /root/Qwen2.5-7B-Instruct-TensorParallel/
python3 qwen2.5_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen2.5-7B-Instruct-TensorParallel/
./run_qwen2.5_7B_axcl_context_tp.sh
```

### 性能对比
以Qwen2.5-7B-Instruct为例，统计对比axcl-x86平台下单卡与多芯级联的相关性能
|模型|TTFT(245token)|TPS(toekns/s)|DDR占用|flash占用|
|--|--|--|--|--|
|Qwen2.5-7B-Instruct-w8a16-parallel|2184.62ms|5.93|11.1GB|9.5GB|
|Qwen2.5-7B-Instruct-w4a16-parallel|2071.71ms|7.82|7.8GB|6.3GB|
|Qwen2.5-7B-Instruct-w4a16|2747.23ms|3.97|5.7GB|5.7GB|