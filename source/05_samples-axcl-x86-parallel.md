# 示例展示（算力卡 x86 平台，多芯级联）

## Pulsar2
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
chmod 755 main_a* run_qwen2.5_7B_axcl_context_tp.sh
 
# 运行
cd /root/Qwen2.5-7B-Instruct-TensorParallel/
python3 qwen2.5_tokenizer_uid.py --host 127.0.0.1 --port 12345

# 再开一个终端执行
cd /root/Qwen2.5-7B-Instruct-TensorParallel/
./run_qwen2.5_7B_axcl_context_tp.sh
```