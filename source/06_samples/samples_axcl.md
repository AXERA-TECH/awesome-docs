# NPU 示例展示（算力卡平台）

算力卡（M.2 加速卡）基于 AXCL 开发库进行 NPU 推理。完整的驱动安装、API 说明、示例代码和 Benchmark 请参阅 AXCL 专用文档：

- **中文文档**：[AXCL 使用手册](https://axcl-docs.readthedocs.io/zh-cn/latest/)
- **英文文档**：[AXCL Documentation](https://axcl-docs-en.readthedocs.io/en/latest/)

文档涵盖以下内容：

- 版本信息
- 简介
- Linux 驱动安装
- AXCL-SMI
- 快速上手
- NPU 示例
- NPU Benchmark
- SDK Samples
- SDK API
- SDK 编译
- FFmpeg
- 常见问题
- Windows 驱动安装（Beta）

```{note}
算力卡支持 x86 和 aarch64 两种 Host 平台，具体差异与编译方法见 AXCL 文档的 SDK 编译章节。
```

## M.2 算力卡多核性能提升技巧

在使用 M.2 算力卡进行多路推理或 Benchmark 时，可以通过频率、CPU 亲和性和中断亲和性减少调度及 PCIe 通信开销，提升 Host 与算力卡协同运行时的性能稳定性：

- 将 Host CPU、卡端 DDR 和 NPU 频率设置为平台允许的最高档位；
- 将应用线程绑定到负责该任务的 Host CPU 大核；
- 将算力卡的 NPU 中断绑定到应用所使用的 Host CPU 大核。

这些设置应在运行 Benchmark 或正式业务前完成，并在测试记录中注明 Host CPU/DDR、卡端 DDR/NPU 的实际频率，以及应用线程和 NPU 中断的 CPU 亲和性。频率调整、线程绑核和 IRQ 绑核的节点及命令会随 Host 架构、Linux 内核、AXCL 驱动和算力卡固件版本变化，请按照对应版本的 [AXCL 文档](https://axcl-docs.readthedocs.io/zh-cn/latest/)执行，不能直接套用其他平台的配置。
