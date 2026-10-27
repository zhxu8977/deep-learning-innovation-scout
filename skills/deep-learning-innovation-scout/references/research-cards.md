# 逐项研究卡
这些卡明确区分“机制已归纳”“摘要核对”“仅题名索引”。下列实验路径为条件化研究建议；没有机制摘要的记录不冒充完成精读。

## RES-001 · UCMNet: Uncertainty-Aware Context Memory Network for Under-Display Camera Image Restoration
- 原目录页码：[1]；书目：DLI-001。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用空间不确定性估计指导上下文记忆检索，使不同退化区域获得不同恢复信息。
- 研究问题：围绕“UCMNet: Uncertainty-Aware Context Memory Network for Under-Display Camera Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-168
- 原始来源：https://arxiv.org/pdf/2604.00381

## RES-002 · VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion
- 原目录页码：[1, 35]；书目：DLI-002。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过模态间差分增强交互，突出红外与可见光的互补信息。；在融合视频中聚合前后时刻的上下文，以建模帧间连续性。
- 研究问题：围绕“VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-169,MOD-170
- 原始来源：https://arxiv.org/pdf/2503.23359

## RES-003 · It Takes Two: A Duet of Periodicity and Directionality for Burst Flicker Removal
- 原目录页码：[1]；书目：DLI-003。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过帧间相位相关对齐并融合短曝光连拍中的周期性闪烁信息。；利用帧内自相关强化重复空间结构，补充连拍去闪烁的周期建模。；以小波域高频方向变化引导低频暗区恢复，用于定位具有方向性的闪烁。
- 研究问题：围绕“It Takes Two: A Duet of Periodicity and Directionality for Burst Flicker Removal”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-171,MOD-172,MOD-173
- 原始来源：https://arxiv.org/pdf/2603.22794

## RES-004 · Vision Transformers are Circulant Attention Learners
- 原目录页码：[1]；书目：DLI-004。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将视觉注意力图约束到块循环结构，通过该结构的快速矩阵乘法降低计算负担。
- 研究问题：围绕“Vision Transformers are Circulant Attention Learners”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-174
- 原始来源：https://arxiv.org/pdf/2512.21542

## RES-005 · Decoding with Structured Awareness: Integrating Directional, Frequency-Spatial, and Structural Attention for Medical Image Segmentation
- 原目录页码：[1, 2]；书目：DLI-005。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：组合通道增强与空间注意力，并引入平面、水平和垂直方向的可学习引导。；融合空间、傅里叶和小波域特征，联系局部边缘与全局结构。；使用多尺度上下文和结构显著性筛选跳跃特征，以减少冗余传递。
- 研究问题：围绕“Decoding with Structured Awareness: Integrating Directional, Frequency-Spatial, and Structural Attention for Medical Image Segmentation”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-175,MOD-176,MOD-177
- 原始来源：https://arxiv.org/pdf/2512.05494

## RES-006 · DCMM-Transformer: Degree-Corrected Mixed-Membership Attention for Medical Imaging
- 原目录页码：[2]；书目：DLI-006。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DCMM-Transformer: Degree-Corrected Mixed-Membership Attention for Medical Imaging”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/37317

## RES-007 · AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs
- 原目录页码：[2, 27]；书目：DLI-007。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ABDUCTIVEMLLM: Boosting Visual Abductive Reasoning Within MLLMs”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2601.02771

## RES-008 · MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images
- 原目录页码：[2]；书目：DLI-008。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MODA: The First Challenging Benchmark for Multispectral Object Detection in Aerial Images”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2512.09489

## RES-009 · SAT: Selective Aggregation Transformer for Image Super-Resolution
- 原目录页码：[2]；书目：DLI-009。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：保留完整查询分辨率，依据密度与孤立性将键值聚合为代表token。
- 研究问题：围绕“SAT: Selective Aggregation Transformer for Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-178
- 原始来源：https://arxiv.org/pdf/2604.07994

## RES-010 · Revisiting Network Inertia: Dynamic Inertia Inhibition Coupled Multidimensional Periodicity for Infrared and Visible Image Fusion
- 原目录页码：[2]；书目：DLI-010。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Revisiting Network Inertia: Dynamic Inertia Inhibition Coupled Multidimensional Periodicity for Infrared and Visible Image Fusion”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/11371373

## RES-011 · Freqformer: Image-Demoiréing Transformer via Effective Frequency Decomposition
- 原目录页码：[2]；书目：DLI-011。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：为高频局部摩尔纹与低频颜色畸变分路处理，再以可学习频率组合变换融合。；利用空间感知的通道注意力加强摩尔纹敏感区域和跨通道互补信息。
- 研究问题：围绕“Freqformer: Image-Demoiréing Transformer via Effective Frequency Decomposition”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-179,MOD-180
- 原始来源：https://arxiv.org/pdf/2505.19120

## RES-012 · MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization
- 原目录页码：[2]；书目：DLI-012。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://icml.cc/virtual/2026/poster/64502

## RES-013 · HVI: A New Color Space for Low-light Image Enhancement
- 原目录页码：[2]；书目：DLI-013。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：使用水平垂直色度与可学习强度表示，把低光增强中的颜色和亮度处理解耦。
- 研究问题：围绕“HVI: ANewColor Space for Low-light Image Enhancement”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-181
- 原始来源：https://arxiv.org/pdf/2502.20272

## RES-014 · U-RWKV: Lightweight medical image segmentation with direction-adaptive RWKV
- 原目录页码：[2]；书目：DLI-014。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过双RWKV与多方向扫描聚合上下文，减轻视觉序列化的方向偏置。；随特征提取阶段调整挤压激励设计，以平衡高分辨率细节和深层语义。
- 研究问题：围绕“U-RWKV: Lightweight medical image segmentation with direction-adaptive”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-182,MOD-183
- 原始来源：https://arxiv.org/pdf/2507.11415

## RES-015 · Linear Attention with Global Context: A Multipole Attention Mechanism for Vision and Physics
- 原目录页码：[2, 3]；书目：DLI-015。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：借鉴多极交互，以距离分层的多尺度交互在每个头中保持全局感受范围。
- 研究问题：围绕“Linear Attention with Global Context: A Multipole Attention Mechanism for Vision and Physics”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-184
- 原始来源：https://arxiv.org/pdf/2507.02748

## RES-016 · Probability-Guided Edge Enhancement Network for Remote Sensing Image Semantic Segmentation
- 原目录页码：[3, 7]；书目：DLI-016。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Probability-Guided Edge Enhancement Network for Remote Sensing Image Semantic Segmentation”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11080472

## RES-017 · CTOD: Cross-Attentive Task-Alignment for One-Stage Object Detection | IEEE Journals & Magazine | IEEE Xplore
- 原目录页码：[3]；书目：DLI-017。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CTOD: Cross-Attentive Task-Alignment for One-Stage Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/10583896

## RES-018 · A Universal Scale-Adaptive Deformable Transformer for Image Restoration across Diverse Artifacts
- 原目录页码：[3]；书目：DLI-018。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A Universal Scale-Adaptive Deformable Transformer for Image Restoration across Diverse Artifacts”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/He_A_Universal_Scale-Adaptive_Deformable_Transformer_for_Image_Restoration_across_Diverse_CVPR_2025_paper.pdf

## RES-019 · Wavelet and Adaptive Coordinate Attention Guided Fine-Grained Residual Network for Image Denoising
- 原目录页码：[3]；书目：DLI-019。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：source_only。
- 机制：分解水平与垂直聚合，在通道门控中保留方向位置信息。
- 研究问题：围绕“Wavelet and Adaptive Coordinate Attention Guided Fine-Grained Residual Network for Image Denoising”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-004
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10379168

## RES-020 · Deep Fourier-embedded Network for RGB and Thermal Salient Object Detection
- 原目录页码：[3]；书目：DLI-020。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在傅里叶表示中协调双模态感知、分解低层边缘并执行残差通道交互。
- 研究问题：围绕“Deep Fourier-embedded Network for RGB and Thermal Salient Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-185
- 原始来源：https://arxiv.org/pdf/2411.18409

## RES-021 · VolFormer: Explore More Comprehensive Cube Interaction for Hyperspectral Image Restoration and Beyond
- 原目录页码：[3]；书目：DLI-021。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将平面交互扩展到立体光谱体，并通过注意力分解降低全体交互负担。
- 研究问题：围绕“VolFormer: Explore More Comprehensive Cube Interaction for Hyperspectral Image Restoration and Beyond”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-186
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Yu_VolFormer_Explore_More_Comprehensive_Cube_Interaction_for_Hyperspectral_Image_Restoration_CVPR_2025_paper.pdf

## RES-022 · Rethinking Transformer-Based Blind-Spot Network for Self-Supervised Image Denoising
- 原目录页码：[3, 7, 8]；书目：DLI-022。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：重新设计通道和空间交互，避免多尺度重排把中心像素信息泄漏到盲点预测。
- 研究问题：围绕“Rethinking Transformer-Based Blind-Spot Network for Self-Supervised Image Denoising”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-187
- 原始来源：https://arxiv.org/pdf/2404.07846

## RES-023 · MCA: Multidimensional collaborative attention in deep convolutio
- 原目录页码：[3, 4]；书目：DLI-023。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MCA: Multidimensional collaborative attention in deep convolutio”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S0952197623012630

## RES-024 · MCANet: Medical Image Segmentation with Multi-Scale Cross-Axis Attention
- 原目录页码：[4]；书目：DLI-024。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以不同长度的横纵条带深度卷积组织多尺度跨轴注意力。；在并行轴向路径间进行交叉交互，并用不同长度条形卷积提供尺度信息。
- 研究问题：围绕“MCANet: Medical Image Segmentation withMulti-Scale Cross-Axis Attention”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-188,MOD-152
- 原始来源：https://arxiv.org/pdf/2312.08866v1

## RES-025 · Recursive Generalization Transformer for Image Super-Resolution
- 原目录页码：[4]；书目：DLI-025。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过递归泛化构造较紧凑的全局表示，用于高分辨率超分的长程交互。
- 研究问题：围绕“Recursive Generalization Transformer for Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-189
- 原始来源：https://arxiv.org/abs/2303.06373

## RES-026 · Energy-Based Cross Attention for Bayesian Context Update in Text-to-Image Diffusion Models
- 原目录页码：[4]；书目：DLI-026。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Energy-Based Cross Attention for Bayesian Context Update in Text-to-Image Diffusion Models”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2306.09869

## RES-027 · Fast Vision Transformers with HiLo Attention
- 原目录页码：[4]；书目：DLI-027。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将注意力处理分为高频局部与低频全局路径，围绕实际吞吐设计计算分配。
- 研究问题：围绕“Fast Vision Transformers with HiLo Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-190
- 原始来源：https://arxiv.org/abs/2205.13213

## RES-028 · HCF-Net: Hierarchical Context Fusion Network for Infrared Small Object Detection
- 原目录页码：[4, 10]；书目：DLI-028。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：并行局部卷积与分块感知特征，增强红外微小目标的上下文。；按维度选择并整合不同层级信息，服务小目标多尺度融合。；多膨胀率通道细化补充红外小目标上下文。
- 研究问题：围绕“HCF-Net: Hierarchical Context Fusion Network for Infrared Small Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-077,MOD-078,MOD-079
- 原始来源：https://arxiv.org/abs/2403.10778

## RES-029 · AGCA: An Adaptive Graph Channel Attention Module for Steel Surface Defect Detection
- 原目录页码：[4]；书目：DLI-029。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“AGCA: An Adaptive Graph Channel Attention Module for Steel Surface Defect Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10050536

## RES-030 · Relation-Aware Global Attention for Person Re-identification
- 原目录页码：[4]；书目：DLI-030。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Relation-Aware Global Attention for Person Re-identification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/1904.02998

## RES-031 · Edge-Enhanced GCIFFNet: A Multiclass Semantic Segmentation Network Based on Edge Enhancement and Multiscale Attention Mechanism
- 原目录页码：[4]；书目：DLI-031。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Edge-Enhanced GCIFFNet: A Multiclass Semantic Segmentation Network Based on Edge Enhancement and Multiscale Attention Mechanism”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10412635

## RES-032 · Agent Attention: On the Integration of Softmax and Linear Attention
- 原目录页码：[4, 5]；书目：DLI-032。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Agent Attention: On the Integration of Softmax and Linear Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2312.08874

## RES-033 · Squeeze-and-Excitation Networks
- 原目录页码：[5]；书目：DLI-033。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：全局空间统计压缩为通道描述，再经瓶颈映射生成通道门控；适合检验通道选择是否不足。
- 研究问题：围绕“Squeeze-and-Excitation Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-001
- 原始来源：https://arxiv.org/abs/1709.01507

## RES-034 · ULSAM: Ultra-Lightweight Subspace Attention Module for Compact Convolutional Neural Networks
- 原目录页码：[5]；书目：DLI-034。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：分割特征子空间并分别产生轻量注意力，选择不同子空间的空间响应。
- 研究问题：围绕“Ultra-Lightweight Subspace Attention Module for Compact Convolutional Neural Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-165
- 原始来源：https://arxiv.org/pdf/2006.15102.pdf

## RES-035 · Concurrent Spatial and Channel Squeeze & Excitation in Fully Convolutional Networks
- 原目录页码：[5]；书目：DLI-035。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：并行通道激励与空间激励，再合并两路重标定特征。
- 研究问题：围绕“Concurrent Spatial and Channel Squeeze & Excitation in Fully Convolutional Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-009
- 原始来源：https://arxiv.org/abs/1803.02579

## RES-036 · Gated Channel Transformation for Visual Recognition
- 原目录页码：[5]；书目：DLI-036。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以通道响应嵌入、归一化和可学习门控控制通道竞争与协作。
- 研究问题：围绕“Gated Channel Transformation for Visual Recognition”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-015
- 原始来源：https://arxiv.org/abs/1909.11519

## RES-037 · DICAM promotes T(H)17 lymphocyte trafficking across the blood-brain barrier during autoimmune neuroinflammation
- 原目录页码：[5]；书目：DLI-037。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：quarantine。
- 机制：多分支感受野和通道调制用于水下图像颜色与细节恢复。
- 研究问题：围绕“DICAM promotes T(H)17 lymphocyte trafficking across the blood-brain barrier during autoimmune neuroinflammation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-080
- 原始来源：https://www.science.org/doi/10.1126/scitranslmed.abj0473

## RES-038 · AAU-net: An Adaptive Attention U-net for Breast Lesions Segmentation in Ultrasound Images
- 原目录页码：[5]；书目：DLI-038。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：联合自适应通道与空间路径，适应超声病灶形态和低对比特征。
- 研究问题：围绕“AAU-net: An Adaptive Attention U-net for Breast Lesions Segmentation in Ultrasound Images”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-075
- 原始来源：https://arxiv.org/pdf/2204.12077

## RES-039 · Half Wavelet Attention on M-Net+ for Low-Light Image Enhancement
- 原目录页码：[5]；书目：DLI-039。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“HALF WAVELET ATTENTION ON M-NET+ FOR LOW-LIGHT IMAGE ENHANCEMENT”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2203.01296

## RES-040 · Unsupervised Bidirectional Contrastive Reconstruction and Adaptive Fine-Grained Channel Attention Networks for image dehazing
- 原目录页码：[5, 6, 8]；书目：DLI-040。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Unsupervised Bidirectional Contrastive Reconstruction and Adaptive Fine-Grained Channel Attention Networks for image dehazing”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S0893608024002387；https://doi.org/10.1016/j.neunet.2024.106314

## RES-041 · SCSA: Exploring the Synergistic Effects Between Spatial and Channel Attention
- 原目录页码：[6]；书目：DLI-041。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以共享多语义空间注意力和渐进通道自注意力建立空间与通道协同。
- 研究问题：围绕“SCSA: Exploring the Synergistic Effects Between Spatial and Channel Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-191
- 原始来源：https://arxiv.org/abs/2407.05128

## RES-042 · Perspective+ Unet: Enhancing Segmentation with Bi-Path Fusion and Efficient Non-Local Attention for Superior Receptive Fields
- 原目录页码：[6]；书目：DLI-042。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：显式计算远距离位置关系并聚合上下文。
- 研究问题：围绕“Perspective+ Unet: Enhancing Segmentation with Bi-Path Fusion and Efficient Non-Local Attention for Superior Receptive Fields”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-019
- 原始来源：https://arxiv.org/abs/2406.14052

## RES-043 · Demystify Mamba in Vision: A Linear Attention Perspective
- 原目录页码：[6]；书目：DLI-043。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Demystify Mamba in Vision: A Linear Attention Perspective”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2405.16605

## RES-044 · SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications
- 原目录页码：[6, 16]；书目：DLI-044。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：quarantine。
- 机制：以非规则初始采样点和学习偏移改变采样形状与参数配置。
- 研究问题：围绕“LDConv: Linear deformable convolution for improving convolutional neural networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-051
- 原始来源：https://arxiv.org/abs/2303.15446；https://arxiv.org/abs/2311.11587v3

## RES-045 · A dual encoder crack segmentation network with Haar wavelet-based high-low frequency attention
- 原目录页码：[6, 9]；书目：DLI-045。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A dual encoder crack segmentation network with Haar wavelet-based high-low frequency attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/pii/S0957417424018177；https://doi.org/10.1016/j.eswa.2024.124950

## RES-046 · LGAG-Net: Lesion-Guided Adaptive Graph Network for Bone Abnormality Detection From Musculoskeletal Radiograph | IEEE Journals & Magazine | IEEE Xplore
- 原目录页码：[6]；书目：DLI-046。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“LGAG-Net: Lesion-Guided Adaptive Graph Network for Bone Abnormality Detection from Musculoskeletal Radiograph”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/10371282

## RES-047 · CSAM: A 2.5D Cross-Slice Attention Module for Anisotropic Volumetric Medical Image Segmentation
- 原目录页码：[6]；书目：DLI-047。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以语义、位置和切片注意力联系体数据中的切片信息，用于各向异性2.5D分割。
- 研究问题：围绕“CSAM: A 2.5D Cross-Slice Attention Module for Anisotropic Volumetric Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-266
- 原始来源：https://arxiv.org/abs/2311.04942

## RES-048 · TransNeXt: Robust Foveal Visual Perception for Vision Transformers
- 原目录页码：[6, 7]；书目：DLI-048。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在通道门控中引入邻域图像特征，把局部建模与门控通道变换结合。
- 研究问题：围绕“TransNeXt: Robust Foveal Visual Perception for Vision Transformers”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-192
- 原始来源：https://arxiv.org/abs/2311.17132

## RES-049 · Multi-scale Attention Network for Single Image Super-Resolution
- 原目录页码：[7]；书目：DLI-049。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在大核注意力中加入多尺度和门控，使注意力图覆盖不同粒度。
- 研究问题：围绕“Multi-scale Attention Network for Single Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-193
- 原始来源：https://arxiv.org/abs/2209.14145

## RES-050 · Vision Transformer with Deformable Attention
- 原目录页码：[7]；书目：DLI-050。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：根据输入学习键值采样位置，使自注意力集中在相关区域。
- 研究问题：围绕“Vision Transformer with Deformable Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-194
- 原始来源：https://arxiv.org/abs/2201.00520

## RES-051 · FECAM: Frequency Enhanced Channel Attention Mechanism for Time Series Forecasting
- 原目录页码：[7]；书目：DLI-051。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以DCT频率描述增强时序通道交互。
- 研究问题：围绕“FECAM: Frequency Enhanced Channel Attention Mechanism for Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-094
- 原始来源：https://arxiv.org/abs/2212.01209

## RES-052 · DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting
- 原目录页码：[7]；书目：DLI-052。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DSANet: Dual Self-Attention Network for Multivariate Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://dl.acm.org/doi/10.1145/3357384.3358132

## RES-053 · Interpretable local flow attention for multi-step traffic flow prediction
- 原目录页码：[7]；书目：DLI-053。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Interpretable local flow attention for multi-step traffic flow prediction”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S0893608023000230?via%3Dihub

## RES-054 · DCT-Former: Efficient Self-Attention with Discrete Cosine Transform
- 原目录页码：[7]；书目：DLI-054。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以离散余弦变换构造注意力近似，借鉴有损压缩的频率表示。
- 研究问题：围绕“DCT-Former: Efficient Self-Attention with Discrete Cosine Transform”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-195
- 原始来源：https://arxiv.org/abs/2203.01178

## RES-055 · MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer-GCNFormer Network
- 原目录页码：[7]；书目：DLI-055。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用并行Transformer与图分支分别建模全局关系和相邻关节结构。
- 研究问题：围绕“MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer- GCNFormer Network”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-196
- 原始来源：https://arxiv.org/abs/2310.16288

## RES-056 · RMT: Retentive Networks Meet Vision Transformers
- 原目录页码：[8]；书目：DLI-056。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：把保留网络的衰减思想扩展到空间，用曼哈顿距离构造显式空间先验。
- 研究问题：围绕“RMT: Retentive Networks Meet Vision Transformers”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-197
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Fan_RMT_Retentive_Networks_Meet_Vision_Transformers_CVPR_2024_paper.pdf

## RES-057 · CATANet: Efficient Content-Aware Token Aggregation for Lightweight Image Super-Resolution
- 原目录页码：[8]；书目：DLI-057。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：为超分聚合长距离内容相似token，训练期间更新共享token中心。
- 研究问题：围绕“CATANet: Efficient Content-Aware Token Aggregation for Lightweight Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-198
- 原始来源：https://arxiv.org/pdf/2503.06896

## RES-058 · FSTA-SNN:Frequency-based Spatial-Temporal Attention Module for Spiking Neural Networks
- 原目录页码：[8, 37]；书目：DLI-058。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FSTA-SNN:Frequency-based Spatial-Temporal Attention Module for Spiking Neural Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2501.14744

## RES-059 · High-Similarity-Pass Attention for Single Image Super-Resolution
- 原目录页码：[8]；书目：DLI-059。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过软阈值保留高相似关联，减少超分中低相关token的干扰。
- 研究问题：围绕“High-Similarity-Pass Attention for Single Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-199
- 原始来源：https://arxiv.org/pdf/2305.15768

## RES-060 · PMFSNet: Polarized Multi-scale Feature Self-attention Network For Lightweight Medical Image Segmentation
- 原目录页码：[8]；书目：DLI-060。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以极化多尺度特征自注意力结合全局与局部信息，控制分割的计算冗余。
- 研究问题：围绕“PMFSNet: Polarized Multi-scale Feature Self-attention Network For Lightweight Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-200
- 原始来源：https://arxiv.org/pdf/2401.07579

## RES-061 · Fourier Angle Alignment for Oriented Object Detection in Remote Sensing
- 原目录页码：[8, 9]；书目：DLI-061。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用傅里叶旋转等变性估计主方向，再做方向对齐的融合或检测。
- 研究问题：围绕“Fourier Angle Alignment for Oriented Object Detection in Remote Sensing”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-201
- 原始来源：https://arxiv.org/pdf/2602.23790

## RES-062 · ReflexSplit: Single Image Reflection Separation via Layer Fusion-Separation
- 原目录页码：[8]；书目：DLI-062。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在双流中交替融合共享结构与分离差分信息，减少透射和反射层混淆。
- 研究问题：围绕“ReflexSplit: Single Image Reflection Separation via Layer Fusion-Separation”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-202
- 原始来源：https://arxiv.org/pdf/2601.17468

## RES-063 · MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention
- 原目录页码：[9]；书目：DLI-063。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过方向引导的边缘门控卷积强化不规则裂纹边缘。
- 研究问题：围绕“MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-203
- 原始来源：https://arxiv.org/pdf/2603.01361

## RES-064 · Wavelet and Prototype Augmented Query-based Transformer for Pixel-level Surface Defect Detection
- 原目录页码：[9, 10, 11]；书目：DLI-064。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在小波域聚合高低频图像特征来细化掩码预测查询。
- 研究问题：围绕“Wavelet and Prototype Augmented Query-based Transformer for Pixel-level Surface Defect Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-204
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Yan_Wavelet_and_Prototype_Augmented_Query-based_Transformer_for_Pixel-level_Surface_Defect_CVPR_2025_paper.pdf

## RES-065 · Dual-Stage Cross-Modal Network with Dynamic Feature Fusion for Emotional Mimicry Intensity Estimation
- 原目录页码：[9]；书目：DLI-065。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Dual-Stage Cross-Modal Network with Dynamic Feature Fusion for Emotional Mimicry Intensity Estimation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025W/ABAW/papers/Yu_Dual-Stage_Cross-Modal_Network_with_Dynamic_Feature_Fusion_for_Emotional_Mimicry_CVPRW_2025_paper.pdf

## RES-066 · ConDSeg: A General Medical Image Segmentation Framework via Contrast-Driven Feature Enhancement
- 原目录页码：[9, 10, 24]；书目：DLI-066。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过对比驱动的训练一致性增强编码器对照明和对比度变化的稳健性。
- 研究问题：围绕“ConDSeg: A General Medical Image Segmentation Framework via Contrast-Driven Feature Enhancement”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-205
- 原始来源：https://arxiv.org/pdf/2412.08345；https://arxiv.org/pdf/2412.08345**官方github

## RES-067 · Dynamic Feature Fusion for Semantic Edge Detection
- 原目录页码：[9]；书目：DLI-067。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Dynamic Feature Fusion for Semantic Edge Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/1902.09104.pdf

## RES-068 · PnPNet: Pull-and-Push Networks for Volumetric Segmentation with Boundary Confusion
- 原目录页码：[10]；书目：DLI-068。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“PnPNet: Unified Network for Precise Boundary Segmentation of Volumetric Images”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/html/2312.08323v1

## RES-069 · DS-TransUNet:Dual Swin Transformer U-Net for Medical Image Segmentation
- 原目录页码：[10]；书目：DLI-069。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用跨分支交互融合局部卷积与全局Transformer特征。
- 研究问题：围绕“DS-TransUNet: Dual Swin Transformer U-Net for Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-109
- 原始来源：https://arxiv.org/abs/2106.06716

## RES-070 · Image fusion in the loop of high-level vision tasks: A semantic-aware real-time infrared and visible image fusion network
- 原目录页码：[10]；书目：DLI-070。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Image fusion in the loop of high-level vision tasks: A semantic-aware real-time infrared and visible image fusion network”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S1566253521002542?via%3Dihub

## RES-071 · DEA-Net: Single image dehazing based on detail-enhanced convolution and content-guided attention
- 原目录页码：[10, 14]；书目：DLI-071。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：结合通道、空间和像素条件生成融合权重。
- 研究问题：围绕“DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content- Guided Attention”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-067
- 原始来源：https://ieeexplore.ieee.org/document/10411857；https://arxiv.org/abs/2301.04805

## RES-072 · DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation
- 原目录页码：[10]；书目：DLI-072。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：全局到局部空间聚合与选择性边界聚合共同联系高层语义和低层边界。
- 研究问题：围绕“DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-206
- 原始来源：https://arxiv.org/abs/2212.11677

## RES-073 · MARSS: Radar Semantic Segmentation via Modular Attention and State Space Models
- 原目录页码：[11]；书目：DLI-073。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MARSS: Radar Semantic Segmentation via Modular Attention and State Space Models”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_MARSS_Radar_Semantic_

## RES-074 · Hilbert Curve-Based Attention Enabling Topology-Preserving Image Tensor Representation for Semantic Segmentation Network
- 原目录页码：[11]；书目：DLI-074。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Hilbert Curve-Based Attention Enabling Topology-Preserving Image Tensor Representation for Semantic Segmentation Network”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Hilbert_Curve-Based_Attention_Enabling_Topology-Preserving_Image_Tensor_Representation_for_Semantic_CVPR_2026_paper.pdf

## RES-075 · FreDFT: Frequency Domain Fusion Transformer for Visible-Infrared Object Detection
- 原目录页码：[11]；书目：DLI-075。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FreDFT: Frequency Domain Fusion Transformer for Visible-Infrared Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2511.10046

## RES-076 · BCN: Batch Channel Normalization for Image Classification
- 原目录页码：[11, 12]；书目：DLI-076。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“BCN: Batch Channel Normalization for Image Classification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2312.00596

## RES-077 · Lipschitz Normalization for Self-Attention Layers with Application to Graph Neural Networks
- 原目录页码：[11]；书目：DLI-077。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：依据注意力的Lipschitz连续性约束构造无额外参数的归一化。
- 研究问题：围绕“Lipschitz Normalization for Self-Attention Layers with Application to Graph Neural Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-207
- 原始来源：https://arxiv.org/pdf/2103.04886

## RES-078 · CrossNorm and SelfNorm for Generalization under Distribution Shifts
- 原目录页码：[11]；书目：DLI-078。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SelfNorm and CrossNorm for Out-of-Distribution Robustness”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2102.02811v1

## RES-079 · ContraNorm: A Contrastive Learning Perspective on Oversmoothing and Beyond
- 原目录页码：[11]；书目：DLI-079。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：从对比学习防止维度塌缩的角度设计归一化，以缓解表示过平滑。
- 研究问题：围绕“CONTRANORM: A CONTRASTIVE LEARNING PERSPECTIVE ON OVERSMOOTHING AND BEYOND”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-208
- 原始来源：https://arxiv.org/pdf/2303.06562

## RES-080 · CrossNorm and SelfNorm for Generalization under Distribution Shifts
- 原目录页码：[11, 12]；书目：DLI-080。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过跨样本统计扰动与自适应统计处理研究分布变化下的泛化。
- 研究问题：围绕“CrossNorm and SelfNorm for Generalization under Distribution Shifts”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-209
- 原始来源：https://arxiv.org/pdf/2102.02811

## RES-081 · Transformers without Normalization
- 原目录页码：[12]；书目：DLI-081。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以带可学习尺度的逐元素tanh运算替代Transformer中的归一化操作。
- 研究问题：围绕“Transformers without Normalization”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-210
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Zhu_Transformers_without_Normalization_CVPR_2025_paper.pdf

## RES-082 · Alleviating Distortion in Image Generation via Multi-Resolution Diffusion Models and Time-Dependent Layer Normalization
- 原目录页码：[12]；书目：DLI-082。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Alleviating Distortion in Image Generation via Multi-Resolution Diffusion Models and Time-Dependent Layer Normalization”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://proceedings.neurips.cc/paper_files/paper/2024/file/f1aa53cac69ef6980ca4a911ffcf278b-https://github.com/qihao067/DiMR

## RES-083 · Towards Real-World Test-Time Adaptation: Tri-Net Self-Training with Balanced Normalization
- 原目录页码：[12]；书目：DLI-083。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在持续测试时域偏移中平衡批归一化，并以锚定约束稳定自训练更新。
- 研究问题：围绕“Towards Real-World Test-Time Adaptation: Tri-net Self-Training with Balanced Normalization”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-211
- 原始来源：https://arxiv.org/pdf/2309.14949

## RES-084 · Test-Time Domain Adaptation by Learning Domain-Aware Batch Normalization
- 原目录页码：[12]；书目：DLI-084。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Test-Time Domain Adaptation by Learning Domain-Aware Batch Normalization”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2312.10165

## RES-085 · Spectral Normalization and Dual Contrastive Regularization for Image-to-Image Translation
- 原目录页码：[12]；书目：DLI-085。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Spectral Normalization and Dual Contrastive Regularization for Image-to-Image Translation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2304.11319

## RES-086 · Hyperspherical Normalization for Scalable Deep Reinforcement Learning
- 原目录页码：[12]；书目：DLI-086。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Hyperspherical Normalization for Scalable Deep Reinforcement Learning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2502.15280

## RES-087 · A Novel Perspective on Low-Light Image Enhancement: Leveraging Artifact Regularization and Walsh- Hadamard Transform
- 原目录页码：[12, 13]；书目：DLI-087。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A Novel Perspective on Low-Light Image Enhancement: Leveraging Artifact Regularization and Walsh- Hadamard Transform”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://doi.org/10.1145/3746027.3758142

## RES-088 · Partial Channel Network: Compute Fewer, Perform Better
- 原目录页码：[13]；书目：DLI-088。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将通道分组分配给卷积、注意力、池化或恒等操作以减少冗余处理。
- 研究问题：围绕“Partial Channel Network: Compute Fewer, Perform Better”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-212
- 原始来源：https://arxiv.org/pdf/2502.01303?

## RES-089 · Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection
- 原目录页码：[13]；书目：DLI-089。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用顺序正交的大条形卷积捕捉遥感目标的方向与长距离空间信息。
- 研究问题：围绕“Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-213
- 原始来源：https://arxiv.org/pdf/2501.03775

## RES-090 · TM-BSN: Triangular-Masked Blind-Spot Network for Real-World Self-Supervised Image Denoising
- 原目录页码：[13]；书目：DLI-090。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：限制卷积核到三角区域，以在原分辨率形成排除相关噪声的盲区。
- 研究问题：围绕“TM-BSN: Triangular-Masked Blind-Spot Network for Real-World Self-Supervised Image Denoising”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-214
- 原始来源：https://arxiv.org/pdf/2604.04484

## RES-091 · Remote Sensing Forestry Similarity Convolution
- 原目录页码：[13, 17]；书目：DLI-091。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过特征关系选择动态卷积核尺寸，以适应遥感林业目标的结构变化。
- 研究问题：围绕“Remote Sensing Forestry Similarity Convolution”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-215
- 原始来源：https://openaccess.thecvf.com/content/WACV2026/papers/Wang_Remote_Sensing_Forestry_Similarity_Convolution_WACV_2026_paper.pdf

## RES-092 · A synergistic CNN-transformer network with pooling attention fusion for hyperspectral image classification
- 原目录页码：[14, 18, 19]；书目：DLI-092。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A synergistic CNN-transformer network with pooling attention fusion for hyperspectral image classification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/pii/S1051200425000922

## RES-093 · Hyperspectral Image Classification via Dynamic Adaptive Graph Convolutional Network
- 原目录页码：[14]；书目：DLI-093。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Hyperspectral Image Classification via Dynamic Adaptive Graph Convolutional Network”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/11422015

## RES-094 · MobileIE: An Extremely Lightweight and Effective ConvNet for Real-Time Image Enhancement on Mobile Devices
- 原目录页码：[14]；书目：DLI-094。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MobileIE: An Extremely Lightweight and Effective ConvNet for Real-Time Image Enhancement on Mobile Devices”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.arxiv.org/pdf/2507.01838

## RES-095 · Adaptive Rectangular Convolution for Remote Sensing Pansharpening
- 原目录页码：[14, 16]；书目：DLI-095。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Adaptive Rectangular Convolution for Remote Sensing Pansharpening”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2503.00467

## RES-096 · Reverse Convolution and Its Applications to Image Restoration
- 原目录页码：[14]；书目：DLI-096。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将反转深度卷积写为正则化最小二乘问题，并与通道变换构成恢复块。
- 研究问题：围绕“Reverse Convolution and Its Applications to Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-216
- 原始来源：https://arxiv.org/pdf/2508.09824v1

## RES-097 · Pinwheel-shaped Convolution and Scale-based Dynamic Loss for Infrared Small Target Detection
- 原目录页码：[14, 16]；书目：DLI-097。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用风车形空间采样适配暗弱小目标的局部像素分布。
- 研究问题：围绕“Pinwheel-shaped Convolution and Scale-based Dynamic Loss for Infrared Small Target Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-217
- 原始来源：https://arxiv.org/pdf/2412.16986

## RES-098 · Channel-wise Topology Refinement Graph Convolution for Skeleton-Based Action Recognition
- 原目录页码：[14]；书目：DLI-098。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用共享拓扑先验加通道特定关系细化，为不同通道学习不同关节交互。
- 研究问题：围绕“Channel-wise Topology Refinement Graph Convolution for Skeleton-Based Action Recognition”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-218
- 原始来源：https://arxiv.org/pdf/2107.12213

## RES-099 · Wavelet Convolutions for Large Receptive Fields
- 原目录页码：[14, 15]；书目：DLI-099。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用多层小波分解扩大卷积有效感受野，以多频表示避免单纯扩张大核的参数增长。
- 研究问题：围绕“Wavelet Convolutions for Large Receptive Fields”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-265
- 原始来源：https://arxiv.org/abs/2407.05848

## RES-100 · TVConv: Efficient Translation Variant Convolution for Layout-aware Visual Processing
- 原目录页码：[15]；书目：DLI-100。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用任务相关的空间布局先验构造位置相关卷积。
- 研究问题：围绕“TVConv: Efficient Translation Variant Convolution for Layout-aware Visual Processing”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-058
- 原始来源：https://arxiv.org/abs/2203.10489

## RES-101 · Dynamic Convolution: Attention over Convolution Kernels
- 原目录页码：[15, 16]；书目：DLI-101。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：从多组卷积核生成输入相关的核组合。
- 研究问题：围绕“Dynamic Convolution: Attention over Convolution Kernels”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-053
- 原始来源：https://arxiv.org/abs/1912.03458

## RES-102 · Pyramidal Convolution: Rethinking Convolutional Neural Networks for Visual Recognition
- 原目录页码：[15]；书目：DLI-102。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：不同核尺度与不同分组深度的金字塔卷积并行提取特征。
- 研究问题：围绕“Pyramidal Convolution: Rethinking Convolutional Neural Networks for Visual Recognition”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-056
- 原始来源：https://arxiv.org/abs/2006.11538

## RES-103 · MDCR: A Dataset for Multi-Document Conditional Reasoning
- 原目录页码：[15]；书目：DLI-103。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MDCR: A Dataset for Multi-Document Conditional Reasoning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2406.11784

## RES-104 · CondConv: Conditionally Parameterized Convolutions for Efficient Inference
- 原目录页码：[15]；书目：DLI-104。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：为每个样本生成专家卷积核的组合系数。
- 研究问题：围绕“CondConv: Conditionally Parameterized Convolutions for Efficient Inference”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-052
- 原始来源：https://arxiv.org/pdf/1904.04971v2

## RES-105 · DO-Conv: Depthwise Over-parameterized Convolutional Layer
- 原目录页码：[15]；书目：DLI-105。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：训练时引入额外深度卷积参数化，线性组成在适用条件下可折叠。
- 研究问题：围绕“DO-Conv: Depthwise Over-parameterized Convolutional Layer”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-054
- 原始来源：https://arxiv.org/abs/2006.12030

## RES-106 · Run, Don't Walk: Chasing Higher FLOPS for Faster Neural Networks
- 原目录页码：[15]；书目：DLI-106。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：仅对部分通道做空间卷积，再通过通道混合利用保留分支。
- 研究问题：围绕“Run, Don’t Walk: Chasing Higher FLOPS for Faster Neural Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-044
- 原始来源：https://arxiv.org/abs/2303.03667

## RES-107 · Complex matrix inversion via real matrix inversions
- 原目录页码：[15]；书目：DLI-107。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Complex Matrix Inversion via Real Matrix Inversions”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2208.01239

## RES-108 · LDConv: Linear deformable convolution for improving convolutional neural networks
- 原目录页码：[16]；书目：DLI-108。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以非规则初始采样点和学习偏移改变采样形状与参数配置。
- 研究问题：围绕“AKConv: Convolutional Kernel with Arbitrary Sampled Shapes and Arbitrary Number of Parameters”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-051
- 原始来源：https://arxiv.org/pdf/2311.11587

## RES-109 · BHViT: Binarized Hybrid Vision Transformer
- 原目录页码：[16, 24]；书目：DLI-109。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“BHViT: Binarized Hybrid Vision Transformer”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2503.02394

## RES-110 · Efficient Frequency-Domain Image Deraining with Contrastive Regularization
- 原目录页码：[16]；书目：DLI-110。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Efficient Frequency-Domain Image Deraining with Contrastive Regularization”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05751.pdf

## RES-111 · A Cross-Modality Feature Adaptive Interaction Approach for RGB-Infrared Object Detection in Aerial Imagery
- 原目录页码：[16]；书目：DLI-111。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A Cross-Modality Feature Adaptive Interaction Approach for RGB-Infrared Object Detection in Aerial Imagery”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11363305

## RES-112 · SFS-DETR: Spatial-Frequency Selection for UAV Object Detection
- 原目录页码：[16, 17]；书目：DLI-112。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在多尺度融合中校准语义错位，减少小目标信息被高层语义稀释。
- 研究问题：围绕“SFS-DETR: Spatial-Frequency Selection for UAV Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-219
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026F/papers/Jia_SFS-DETR_Spatial-Frequency_Selection_for_UAV_Object_Detection_CVPRF_2026_paper.pdf

## RES-113 · Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization
- 原目录页码：[17]；书目：DLI-113。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Mesoscopic Insights: Orchestrating Multi-scale & Hybrid Architecture for Image Manipulation Localization”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2412.13753

## RES-114 · Flora-NET: Integrating dual coordinate attention with adaptive kernel based convolution networkformedicinalfloweridentification
- 原目录页码：[17]；书目：DLI-114。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：source_only。
- 机制：分解水平与垂直聚合，在通道门控中保留方向位置信息。
- 研究问题：围绕“Flora-NET: Integrating dual coordinate attention with adaptive kernel based convolution networkformedicinalfloweridentification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-004
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S0168169924012250

## RES-115 · Real-World Remote Sensing Image Dehazing: Benchmark and Baseline
- 原目录页码：[17]；书目：DLI-115。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Real-World Remote Sensing Image Dehazing: Benchmark and Baseline”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2503.17966；https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11058953

## RES-116 · I2U-Net: A dual-path U-Net with rich information interaction for medical image segmentation
- 原目录页码：[17]；书目：DLI-116。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“I2U-Net: A dual-path U-Net with rich information interaction for medical image segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S136184152400166X

## RES-117 · MixDehazeNet : Mix Structure Block For Image Dehazing Network
- 原目录页码：[17]；书目：DLI-117。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用逐元素乘法构成非线性特征交互，并结合卷积空间混合。
- 研究问题：围绕“MixDehazeNet : Mix Structure Block For Image Dehazing Network”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-106
- 原始来源：https://arxiv.org/abs/2305.17654

## RES-118 · SCConv: Spatial and Channel Reconstruction Convolution for Feature Redundancy
- 原目录页码：[17, 18]；书目：DLI-118。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：先进行空间冗余重构，再用通道分割转换融合减少冗余。
- 研究问题：围绕“SCConv: Spatial and Channel Reconstruction Convolution for Feature Redundancy”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-043
- 原始来源：https://openaccess.thecvf.com/content/CVPR2023/papers/Li_SCConv_Spatial_and_Channel_Reconstruction_Convolution_for_Feature_Redundancy_CVPR_2023_paper.pdf

## RES-119 · SCSegamba: Lightweight Structure-Aware Vision Mamba for Crack Segmentation in Structures
- 原目录页码：[18, 29]；书目：DLI-119。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将轻量门控瓶颈卷积和结构感知扫描结合，用于裂纹的形态与纹理建模。
- 研究问题：围绕“SCSegamba: Lightweight Structure-Aware Vision Mamba for Crack Segmentation in Structures”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-220
- 原始来源：https://arxiv.org/pdf/2503.01113

## RES-120 · Depth Information Assisted Collaborative Mutual Promotion Network for Single Image Dehazing
- 原目录页码：[18]；书目：DLI-120。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Depth Information Assisted Collaborative Mutual Promotion Network for Single Image Dehazing”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Depth_Information_Assisted_Collaborative_Mutual_Promotion_Network_for_Single_Image_CVPR_2024_paper.pdf

## RES-121 · OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction
- 原目录页码：[18]；书目：DLI-121。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“OTTER:A Vision-Language-Action Model with Text-Aware Visual Feature Extraction”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2503.03734?

## RES-122 · LogicAD: Explainable Anomaly Detection via VLM-based Text Feature Extraction
- 原目录页码：[18]；书目：DLI-122。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“LogicAD: Explainable Anomaly Detection via VLM-based Text Feature Extraction”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/32433

## RES-123 · Deconstructing Denoising Diffusion Models for Self-Supervised Learning
- 原目录页码：[19]；书目：DLI-123。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Deconstructing Denoising Diffusion Models for Self-Supervised Learning”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openreview.net/pdf?id=9oMB6wnFYM

## RES-124 · Text-to-Image Diffusion Models are Great Sketch-Photo Matchmakers
- 原目录页码：[19]；书目：DLI-124。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Text-to-Image Diffusion Models are Great Sketch-Photo Matchmakers”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Koley_Text-to-Image_Diffusion_Models_are_Great_Sketch-Photo_Matchmakers_CVPR_2024_paper.pdf

## RES-125 · Latent Feature-Guided Diffusion Models for Shadow Removal
- 原目录页码：[19]；书目：DLI-125。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Latent Feature-Guided Diffusion Models for Shadow Removal”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/WACV2024/papers/Mei_Latent_Feature-Guided_Diffusion_Models_for_Shadow_Removal_WACV_2024_paper.pdf

## RES-126 · Weak-Mamba-UNet: Visual Mamba Makes CNN and ViT Work Better for Scribble-based Medical Image Segmentation
- 原目录页码：[19]；书目：DLI-126。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Weak-Mamba-UNet: Visual Mamba Makes CNN and ViT Work Better for Scribble-based Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2402.10887

## RES-127 · BEFUnet: A Hybrid CNN-Transformer Architecture for Precise Medical Image Segmentation
- 原目录页码：[20, 41]；书目：DLI-127。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“BEFUnet: A Hybrid CNN-Transformer Architecture for Precise Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2402.08793

## RES-128 · Multimodal Deep Learning for Remote Stress Estimation Using CCT-LSTM
- 原目录页码：[20]；书目：DLI-128。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Multimodal Deep Learning for Remote Stress Estimation Using CCT-LSTM”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/WACV2024/papers/Ziaratnia_Multimodal_Deep_Learning_for_Remote_Stress_Estimation_Using_CCT-LSTM_WACV_2024_paper.pdf

## RES-129 · T-FREX: A Transformer-based Feature Extraction Method from Mobile App Reviews
- 原目录页码：[20]；书目：DLI-129。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“T-FREX: A Transformer-based Feature Extraction Method from Mobile App Reviews”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2401.03833

## RES-130 · TR-DETR: Task-Reciprocal Transformer for Joint Moment Retrieval and Highlight Detection
- 原目录页码：[20]；书目：DLI-130。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TR-DETR: Task-Reciprocal Transformer for Joint Moment Retrieval and Highlight Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/28304

## RES-131 · MambaVision: A Hybrid Mamba-Transformer Vision Backbone
- 原目录页码：[20]；书目：DLI-131。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MambaVision: A Hybrid Mamba-Transformer Vision Backbone”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2407.08083

## RES-132 · Transformer-Based No-Reference Image Quality Assessment via Supervised Contrastive Learning
- 原目录页码：[20, 21]；书目：DLI-132。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Transformer-Based No-Reference Image Quality Assessment via Supervised Contrastive Learning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/28285

## RES-133 · Tri-VAE: Triplet Variational Autoencoder for Unsupervised Anomaly Detection in Brain Tumor MRI
- 原目录页码：[21]；书目：DLI-133。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用健康样本学习的深层语义门控跳跃信息，兼顾细节恢复与异常抑制。
- 研究问题：围绕“Tri-VAE: Triplet Variational Autoencoder for Unsupervised Anomaly Detection in Brain Tumor MRI”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-221
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024W/VAND/papers/Wijanarko_Tri-VAE_Triplet_Variational_Autoencoder_for_Unsupervised_Anomaly_Detection_in_Brain_CVPRW_2024_paper.pdf

## RES-134 · TSLANet: Rethinking Transformers for Time Series Representation Learning
- 原目录页码：[21, 37]；书目：DLI-134。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：自适应频谱处理与交互卷积块分别处理长短依赖和噪声。
- 研究问题：围绕“TSLANet: Rethinking Transformers for Time Series Representation Learning”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-095
- 原始来源：https://arxiv.org/pdf/2404.08472

## RES-135 · GraphKAN: Enhancing Feature Extraction with Graph Kolmogorov Arnold Networks
- 原目录页码：[21]；书目：DLI-135。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以KAN代替图特征变换中的MLP与固定激活，探索函数学习对表示的影响。
- 研究问题：围绕“GraphKAN: Enhancing Feature Extraction with Graph Kolmogorov Arnold Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-222
- 原始来源：https://arxiv.org/pdf/2406.13597

## RES-136 · Accurate Leukocyte Detection Based on Deformable-DETR and Multi-Level Feature Fusion for Aiding Diagnosis of Blood Diseases
- 原目录页码：[21]；书目：DLI-136。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用高层通道信息筛选低层特征，再进行多级特征融合以处理目标尺度差异。
- 研究问题：围绕“Accurate Leukocyte Detection Based on Deformable-DETR and Multi-Level Feature Fusion for Aiding Diagnosis of Blood Diseases”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-223
- 原始来源：https://arxiv.org/pdf/2401.00926

## RES-137 · Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed
- 原目录页码：[22]；书目：DLI-137。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Efficient_LoFTR_Semi-Dense_Local_Feature_Matching_with_Sparse-Like_Speed_CVPR_2024_paper.pdf

## RES-138 · XFeat: Accelerated Features for Lightweight Image Matching
- 原目录页码：[22]；书目：DLI-138。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“XFeat: Accelerated Features for Lightweight Image Matching”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Potje_XFeat_Accelerated_Features_for_Lightweight_Image_Matching_CVPR_2024_paper.pdf

## RES-139 · Enhancing Graph Collaborative Filtering with FourierKAN Feature Transformation
- 原目录页码：[22]；书目：DLI-139。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FourierKAN-GCF: Fourier Kolmogorov-Arnold Network- An Effective and Efficient Feature Transformation for Graph Collaborative Filtering”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2406.01034

## RES-140 · Infrared Image Super-Resolution via Lightweight Information Split Network
- 原目录页码：[22]；书目：DLI-140。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Infrared Image Super-Resolution via Lightweight Information Split Network”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2405.10561

## RES-141 · WaveNet-SF: A Hybrid Network for Retinal Disease Detection Based on Wavelet Transform in Spatial-Frequency Domain
- 原目录页码：[22]；书目：DLI-141。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“WaveNet-SF: A Hybrid Network for Retinal Disease Detection Based on Wavelet Transform in the Spatial-Frequency Domain”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2501.11854

## RES-142 · MLP-KAN: Unifying Deep Representation and Function Learning
- 原目录页码：[23]；书目：DLI-142。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MLP-KAN: UNIFYING DEEP REPRESENTATION AND FUNCTION LEARNING”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2410.03027

## RES-143 · Exploring State Space Model in Wavelet Domain: An Infrared and Visible Image Fusion Network via Wavelet Transform and State Space Model
- 原目录页码：[23]；书目：DLI-143。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在小波表示中组合多频局部信息与SSM全局建模，并进行跨模态调制。
- 研究问题：围绕“Exploring State Space Model in Wavelet Domain: An Infrared and Visible Image Fusion Network via Wavelet Transform and State Space Model”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-224
- 原始来源：https://arxiv.org/pdf/2503.18378

## RES-144 · DCCS-Det: Directional Context andCross-Scale-Aware Detector forInfrared Small Target
- 原目录页码：[23]；书目：DLI-144。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DCCS-Det: Directional Context andCross-Scale-Aware Detector forInfrared Small Target”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11305185

## RES-145 · Dual-Path Learning based on Frequency Structural Decoupling and Regional-Aware Fusion for Low-Light Image Super-Resolution
- 原目录页码：[23]；书目：DLI-145。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Dual-Path Learning based on Frequency StructuralDecoupling and Regional-Aware Fusion forLow- Light Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2603.27301

## RES-146 · FBRT-YOLO: Faster and Better for Real-Time Aerial Image Detection
- 原目录页码：[23]；书目：DLI-146。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FBRT-YOLO: Faster and Better for Real-Time Aerial Image Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2504.20670

## RES-147 · Lightweight Multiscale Feature Fusion and Multireceptive Field Feature Enhancement for Small Object Detection in the Aerial Images
- 原目录页码：[23]；书目：DLI-147。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Lightweight Multiscale Feature Fusion and Multireceptive Field Feature Enhancement for Small Object Detection in the Aerial Images”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/11141438；https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11014226

## RES-148 · SHISRCNet: Super-resolution And Classification Network For Low-resolution Breast Cancer Histopathology Image
- 原目录页码：[24]；书目：DLI-148。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“HISRCNet: Super-resolution And Classification Network For Low-resolution Breast Cancer Histopathology Image”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2306.14119

## RES-149 · CEDNet: A Cascade Encoder-Decoder Network for Dense Prediction
- 原目录页码：[24]；书目：DLI-149。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CEDNET: A CASCADE ENCODER-DECODER NET WORK FOR DENSE PREDICTION”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2302.06052

## RES-150 · Adaptive Multi-Scale Decomposition Framework for Time Series Forecasting
- 原目录页码：[24, 37]；书目：DLI-150。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以残差多尺度分解混合、时序与通道依赖交互及自适应预测综合处理不同时间模式。
- 研究问题：围绕“Adaptive Multi-Scale Decomposition Framework for Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-225
- 原始来源：https://arxiv.org/abs/2406.03751；https://arxiv.org/pdf/2406.03751

## RES-151 · MF-Mamba: Multiscale Convolution and MambaFusion Model for Semantic Segmentation ofRemote Sensing Imagery
- 原目录页码：[24]；书目：DLI-151。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MF-Mamba: Multiscale Convolution and MambaFusion Model for Semantic Segmentation ofRemote Sensing Imagery”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11098811

## RES-152 · MDFM: Multi-Decision Fusing Model for Few-Shot Learning
- 原目录页码：[24]；书目：DLI-152。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MDFM: Multi-Decision Fusing Model for Few-Shot Learning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2112.00690

## RES-153 · D-Net: Dynamic Large Kernel with Dynamic Feature Fusion for Volumetric Medical Image Segmentation
- 原目录页码：[24]；书目：DLI-153。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“D-Net: Dynamic Large Kernel with Dynamic Feature Fusion for Volumetric Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2403.10674

## RES-154 · DETRs Beat YOLOs on Real-time Object Detection
- 原目录页码：[24]；书目：DLI-154。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DETRs Beat YOLOs on Real-time Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2304.08069

## RES-155 · Spatial Frequency Modulation for Semantic Segmentation
- 原目录页码：[25, 31, 32]；书目：DLI-155。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在下采样前把高频信息调制到较低频率，再于上采样阶段解调以减轻混叠。
- 研究问题：围绕“Spatial Frequency Modulation for Semantic Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-226
- 原始来源：https://arxiv.org/abs/2507.11893；https://ieeexplore.ieee.org/abstract/document/11095993

## RES-156 · FSDETR: Frequency-Spatial Feature Enhancement for Small Object Detection
- 原目录页码：[25]；书目：DLI-156。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FSDETR: Frequency-Spatial Feature Enhancement for Small Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2604.14884

## RES-157 · Spectral Dynamic Attention Network for Hyperspectral Image Super-Resolution
- 原目录页码：[25]；书目：DLI-157。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：按数据动态稀疏化光谱通道相关性，抑制冗余光谱交互。
- 研究问题：围绕“Spectral Dynamic Attention Network for Hyperspectral Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-227
- 原始来源：https://arxiv.org/pdf/2604.27326

## RES-158 · DF2Net: A Differential-Feature Dynamic-Fusion Network for Building Change Detection in Remote Sensing Images
- 原目录页码：[25]；书目：DLI-158。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DF2Net: A Differential-Feature Dynamic-Fusion Network for Building Change Detection in Remote Sensing Images”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/11352975

## RES-159 · CPUBone: Efficient Vision Backbone Design for Devices with Low Parallelization Capabilities
- 原目录页码：[25, 36]；书目：DLI-159。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CPUBone: Efficient Vision Backbone Design for Devices with Low Parallelization Capabilities”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2603.26425；https://arxiv.org/abs/2603.26425

## RES-160 · Rewrite the Stars
- 原目录页码：[25]；书目：DLI-160。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用逐元素乘法构成非线性特征交互，并结合卷积空间混合。
- 研究问题：围绕“Rewrite the Stars”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-106
- 原始来源：https://arxiv.org/abs/2403.19967

## RES-161 · GhostNetV2: Enhance Cheap Operation with Long-Range Attention
- 原目录页码：[25]；书目：DLI-161。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：先生成较少本征特征，再用便宜变换扩展特征；V2增加长程建模设计。；以硬件友好的长距离交互补充廉价Ghost特征生成的全局信息不足。
- 研究问题：围绕“GhostNetV2: Enhance Cheap Operation with Long-Range Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-228,MOD-055
- 原始来源：https://arxiv.org/abs/2211.12905v1

## RES-162 · Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding
- 原目录页码：[25, 26]；书目：DLI-162。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：并行组织部分变换路径，探索网络深度与宽度的替代关系。；以分块近似KV缓存和置信度感知并行解码加速双向扩散语言模型。
- 研究问题：围绕“Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-229,MOD-105
- 原始来源：http://arxiv.org/abs/2505.22618

## RES-163 · Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM
- 原目录页码：[26]；书目：DLI-163。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：并行组织部分变换路径，探索网络深度与宽度的替代关系。；按层间token动态分配缓存更新预算，并自适应校准并行解码阈值。
- 研究问题：围绕“DYNAMIC-DLLM: DYNAMIC CACHE-BUDGET AND ADAPTIVE PARALLEL DECODING FOR TRAINING FREE ACCELERATION OF DIFFUSION LLM”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-230,MOD-105
- 原始来源：https://arxiv.org/pdf/2606.26120

## RES-164 · Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models
- 原目录页码：[26]；书目：DLI-164。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Video Compression Commander: Plug-and-PlayInference Acceleration for Video Large LanguageModels”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2505.14454

## RES-165 · Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models
- 原目录页码：[26, 27]；书目：DLI-165。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过额外预训练记忆组件进行领域适配，同时保持原语言模型参数。
- 研究问题：围绕“Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-231
- 原始来源：https://www.arxiv.org/abs/2508.09874；https://www.arxiv.org/pdf/2508.09874

## RES-166 · VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer
- 原目录页码：[26]；书目：DLI-166。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“VLSA: Vision-Language-Action Models withPlug-and-Play Safety Constraint Layer”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2512.11891

## RES-167 · UniComp: Rethinking Video Compression Through Informational Uniqueness
- 原目录页码：[26]；书目：DLI-167。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：依据token信息独特性进行帧分组、预算分配和空间压缩，控制视频表示冗余。
- 研究问题：围绕“UniComp: Rethinking Video Compression Through Informational Uniqueness”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-232
- 原始来源：https://arxiv.org/pdf/2512.03575

## RES-168 · SLOT: Sample-specific Language Model Optimization at Test-time
- 原目录页码：[26]；书目：DLI-168。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SLOT: Sample-specific Language Model Optimization at Test-time”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2505.12392

## RES-169 · RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding
- 原目录页码：[26]；书目：DLI-169。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“RACER:Retrieval-Augmented Contextual Rapid Speculative Decoding”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2604.14885

## RES-170 · Policy Contrastive Decoding for Robotic Foundation Models
- 原目录页码：[26]；书目：DLI-170。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Policy Contrastive Decoding for Robotic Foundation Models”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：

## RES-171 · LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation
- 原目录页码：[27]；书目：DLI-171。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2411.04997v

## RES-172 · In-Place Test-Time Training
- 原目录页码：[27]；书目：DLI-172。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：把MLP最终投影作为可适配快权重，并以分块更新进行测试时学习。
- 研究问题：围绕“In-Place Test-Time Training”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-233
- 原始来源：https://arxiv.org/pdf/2604.06169

## RES-173 · All-in-One Slider for Attribute Manipulation in Diffusion Models
- 原目录页码：[27]；书目：DLI-173。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“All-in-One Slider for Attribute Manipulation in Diffusion Models”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.alphaxiv.org/abs/2508.19195

## RES-174 · BEVDiffuser: Plug-and-Play Diffusion Model for BEV Denoising with Ground-Truth Guidance
- 原目录页码：[27]；书目：DLI-174。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“BEVDiffuser: Plug-and-Play Diffusion Model for BEV Denoising with Ground-Truth Guidanc”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2502.19694

## RES-175 · FreeU: Free Lunch in Diffusion U-Net
- 原目录页码：[27]；书目：DLI-175。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：调整扩散U-Net骨干与跳跃特征的相对贡献，以平衡语义去噪与高频细节。
- 研究问题：围绕“FreeU: Free Lunch in Diffusion U-Net”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-234
- 原始来源：https://arxiv.org/abs/2309.11497

## RES-176 · One step further with Monte-Carlo sampler to guide diffusion better
- 原目录页码：[27]；书目：DLI-176。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ONE STEP FURTHER WITH MONTE-CARLO SAMPLER TO GUIDE DIFFUSION BETTER”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2603.06685；https://openreview.net/forum?id=cpdHmRtx7d

## RES-177 · Plug-and-play Diffusion Models for Image Compressive Sensing with Data Consistency Projection
- 原目录页码：[27]；书目：DLI-177。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将去噪先验、测量一致性与采样步骤分开，并组合多种保真项处理压缩感知重建。
- 研究问题：围绕“PLUG-AND-PLAY DIFFUSION MODELS FOR IMAGE COMPRESSIVE SENSING WITH DATA CONSISTENCY PROJECTION”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-235
- 原始来源：http://arxiv.org/pdf/2509.09365v1

## RES-178 · Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation
- 原目录页码：[27]；书目：DLI-178。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2605.05960

## RES-179 · Super-Resolution and Denoising of Corneal B-Scan OCT Imaging Using Diffusion Model Plug-and-Play Priors
- 原目录页码：[28]；书目：DLI-179。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Super-Resolution and Denoising of Corneal B-Scan OCT Imaging Using Diffusion Model Plug-and-Play Priors”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2602.02795v1.pdf；https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Align_Images_Before_You_Generate_CVPR_2026_paper.html；https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Align_Images_Before_You_Generate_CVPR_2026_paper.pdf；https://openaccess.thecvf.com/content/CVPR2026/supplemental/Zhang_Align_Images_Before_CVPR_2026_supplemental.pdf

## RES-180 · Golden Noise for Diffusion Models: A Learning Framework
- 原目录页码：[28]；书目：DLI-180。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Golden Noise for Diffusion Models: A Learning Framework”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_Golden_Noise_for_Diffusion_Models_A_Learning_Framework_ICCV_2025_paper.pdf

## RES-181 · Spectral Progressive Diffusion for Efficient Image and Video Generation
- 原目录页码：[28]；书目：DLI-181。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：沿去噪轨迹逐步增加分辨率，并依据功率谱设计噪声扩展和分辨率调度。
- 研究问题：围绕“Spectral Progressive Diffusion for Efficient Image and Video Generation”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-236
- 原始来源：https://arxiv.org/pdf/2605.18736

## RES-182 · Elucidating the SNR-t Bias of Diffusion Probabilistic Models
- 原目录页码：[28]；书目：DLI-182。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Elucidating the SNR-t Bias of Diffusion Probabilistic Models”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_Elucidating_the_SNR-t_Bias_of_Diffusion_Probabilistic_Models_CVPR_2026_paper.pdf

## RES-183 · InteractDiffusion: Interaction Control in Text-to-Image Diffusion Models
- 原目录页码：[28]；书目：DLI-183。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“InteractDiffusion: Interaction Control in Text-to-Image Diffusion Models”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2312.05849

## RES-184 · Beyond Illumination: Fine-Grained Detail Preservation in Extreme Dark Image Restoration
- 原目录页码：[28, 29]；书目：DLI-184。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：先通过傅里叶引导恢复照明，再用不降采样局部片段与高梯度区域SSM细化纹理。
- 研究问题：围绕“Beyond Illumination: Fine-Grained Detail Preservation in Extreme Dark Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-237
- 原始来源：https://arxiv.org/pdf/2508.03336

## RES-185 · Scan Clusters, Not Pixels: A Cluster-Centric Paradigm for Efficient Ultra-high-definition Image Restoration
- 原目录页码：[29]；书目：DLI-185。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以少量聚类中心进行序列扫描，再通过相似性把全局信息扩散回像素。
- 研究问题：围绕“Scan Clusters, Not Pixels: A Cluster-Centric Paradigm for EfficientUltra-high-definition Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-238
- 原始来源：https://arxiv.org/pdf/2602.21917

## RES-186 · AKCMamba-YOLO: Selective State Space Models For Real-Time Object Detection
- 原目录页码：[29]；书目：DLI-186。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“AKCMamba-YOLO: Selective State Space Models For Real-Time Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_AKCMamba-YOLO_Selective_State_Space_Models_For_Real-Time_Object_Detection_CVPR_2026_paper.pdf

## RES-187 · MaIR: ALocality- and Continuity-Preserving Mamba for Image Restoration
- 原目录页码：[29]；书目：DLI-187。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MaIR: ALocality- and Continuity-Preserving Mamba for Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2412.2006

## RES-188 · MobileMamba: Lightweight Multi-Receptive Visual Mamba Network
- 原目录页码：[29, 31]；书目：DLI-188。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MobileMamba: Lightweight Multi-Receptive Visual Mamba Network”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/html/2411.15941v1；https://arxiv.org/pdf/2411.15941；https://arxiv.org/abs/2411.15941

## RES-189 · MambaHSI: Spatial-Spectral Mamba for Hyperspectral Image Classification
- 原目录页码：[29]；书目：DLI-189。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MambaHSI:Spatial-Spectral Mamba for Hyperspectral Image Classification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2501.04944

## RES-190 · EfficientViM: Efficient Vision Mamba with Hidden State Mixer based State Space Duality
- 原目录页码：[29, 31]；书目：DLI-190。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将通道混合移入压缩隐状态空间，并结合多阶段隐状态融合减轻内存瓶颈。
- 研究问题：围绕“EfficientViM: Efficient Vision Mamba with Hidden State Mixer based State Space Duality”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-239
- 原始来源：https://arxiv.org/pdf/2411.15241

## RES-191 · GLVMamba: A Global–Local Visual State-Space Model for Remote Sensing Image Segmentation
- 原目录页码：[29]；书目：DLI-191。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“GLVMamba: A Global–Local Visual State-Space Model for Remote Sensing Image Segmentation”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11014226

## RES-192 · Convolutional State Space Models for Long-Range Spatiotemporal Modeling
- 原目录页码：[29, 30]；书目：DLI-192。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Convolutional State Space Models for Long-Range Spatiotemporal Modeling”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2310.19694

## RES-193 · nnMamba: 3D Biomedical Image Segmentation, Classification and Landmark Detection with State Space Model
- 原目录页码：[30]；书目：DLI-193。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：把Mamba与卷积结合，通过通道空间孪生学习建模体素长距离关系。
- 研究问题：围绕“nnMamba: 3D Biomedical Image Segmentation, Classification and Landmark Detection with State Space Model”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-240
- 原始来源：https://arxiv.org/pdf/2402.03526

## RES-194 · TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting
- 原目录页码：[30]；书目：DLI-194。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2403.09898

## RES-195 · MambaIR: A Simple Baseline for Image Restoration with State-Space Model
- 原目录页码：[30]；书目：DLI-195。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MambaIR: A Simple Baseline for Image Restoration with State-Space Model”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2402.15648；https://arxiv.org/abs/2402.15648

## RES-196 · RSCaMa: Remote Sensing Image Change Captioning with State Space Model
- 原目录页码：[30]；书目：DLI-196。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：结合空间差分感知SSM与双时相交错扫描，对变化描述任务进行联合时空建模。
- 研究问题：围绕“RSCaMa: Remote Sensing Image Change Captioning with State Space Model”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-241
- 原始来源：https://arxiv.org/abs/2404.18895

## RES-197 · Jamba: A Hybrid Transformer-Mamba Language Model
- 原目录页码：[30]；书目：DLI-197。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Jamba: A Hybrid Transformer-Mamba Language Model”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2403.19887

## RES-198 · VMamba: Visual State Space Model
- 原目录页码：[30]；书目：DLI-198。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以二维选择性扫描在视觉状态空间块中建立多方向长距离交互。
- 研究问题：围绕“VMamba: Visual State Space Model”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-242
- 原始来源：https://arxiv.org/abs/2401.10166

## RES-199 · CM-UNet: Hybrid CNN-Mamba UNet for Remote Sensing Image Semantic Segmentation
- 原目录页码：[30, 31]；书目：DLI-199。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CM-UNet: Hybrid CNN-Mamba UNet for Remote Sensing Image Semantic Segmentation”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2405.10530

## RES-200 · SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation
- 原目录页码：[31]；书目：DLI-200。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：局部卷积路径辅助体分割全局序列建模。
- 研究问题：围绕“SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-107
- 原始来源：https://arxiv.org/html/2401.13560v3

## RES-201 · Wavelet-based Mamba with Fourier Adjustment for Low-light Image Enhancement
- 原目录页码：[31]；书目：DLI-201。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：使用小波域Mamba处理照明，再借傅里叶调整细化局部细节。
- 研究问题：围绕“Wavelet-based Mamba with Fourier Adjustment for Low-light Image Enhancement”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-243
- 原始来源：https://arxiv.org/pdf/2410.20314

## RES-202 · MambaOut: Do We Really Need Mamba for Vision?
- 原目录页码：[31]；书目：DLI-202。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MambaOut: Do We Really Need Mamba for Vision?”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2405.07992

## RES-203 · KAN: Kolmogorov-Arnold Networks
- 原目录页码：[31]；书目：DLI-203。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“KAN: Kolmogorov–Arnold Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/html/2404.19756v1

## RES-204 · SCKansformer: Fine-Grained Classification of Bone Marrow Cells via Kansformer Backbone and Hierarchical Attention Mechanisms
- 原目录页码：[31]；书目：DLI-204。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SCKansformer: Fine-Grained Classification of Bone Marrow Cells via Kansformer Backbone and Hierarchical Attention Mechanisms”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2406.09931

## RES-205 · MobileNetV4 -- Universal Models for the Mobile Ecosystem
- 原目录页码：[32]；书目：DLI-205。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：统一组织倒瓶颈与可选深度卷积位置，适应移动算子设计。
- 研究问题：围绕“MobileNetV4 - Universal Models for the Mobile Ecosystem”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-108
- 原始来源：https://arxiv.org/abs/2404.10518

## RES-206 · FMViT: A multiple-frequency mixing Vision Transformer
- 原目录页码：[32]；书目：DLI-206。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FMViT:Amultiple-frequencymixingVisionTransformer”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2311.05707.pdf

## RES-207 · Rethinking Attention: Exploring Shallow Feed-Forward Neural Networks as an Alternative to Attention Layers in Transformers
- 原目录页码：[32]；书目：DLI-207。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Rethinking Attention: Exploring Shallow Feed-Forward Neural Networks as an Alternative to Attention Layers in Transformers”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2311.10642

## RES-208 · Learning an Inference-accelerated Network from a Pre-trainedLearning an Inference-accelModel with Frequencyenhanced Feature Distillation
- 原目录页码：[32]；书目：DLI-208。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Learning an Inference-accelerated Network from a Pre-trainedLearning an Inference-accelModel with Frequencyenhanced Feature Distillation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://dl.acm.org/doi/10.1145/3503161.3547983

## RES-209 · MobileDenseNet: A new approach to object detection onmobile devices
- 原目录页码：[32]；书目：DLI-209。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MobileDenseNet: A new approach to object detection onmobile devices”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/ftp/arxiv/papers/2207/2207.11031.pdf

## RES-210 · Skip-Attention: Improving Vision Transformers by Paying Less Attention
- 原目录页码：[32]；书目：DLI-210。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Skip-Attention: Improving Vision Transformers by Paying Less Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2301.02240v2.pdf

## RES-211 · SHViT: Single-Head Vision Transformer with Memory Efficient Macro Design
- 原目录页码：[32]；书目：DLI-211。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SHViT: Single-Head Vision Transformer with Memory Efficient Macro Design”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2401.16456v1.pdf

## RES-212 · To Perceive or Not to Perceive: Lightweight Stacked Hourglass Network
- 原目录页码：[32]；书目：DLI-212。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“To Perceive or Not to Perceive: Lightweight Stacked Hourglass Network”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2302.04815v1.pdf

## RES-213 · EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention
- 原目录页码：[33]；书目：DLI-213。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2305.07027.pdf

## RES-214 · Less is More: Focus Attention for Efficient DETR
- 原目录页码：[33]；书目：DLI-214。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Less is More: Focus Attention for Efficient DETR”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2307.12612

## RES-215 · FalconNet: Factorization for the Light-weight ConvNets
- 原目录页码：[33]；书目：DLI-215。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FalconNet: Factorization for the Light-weight ConvNets”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2306.06365v1.pdf

## RES-216 · MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer
- 原目录页码：[33]；书目：DLI-216。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：局部卷积特征变换为序列进行较长程交互，再融合回空间表示。
- 研究问题：围绕“MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-155
- 原始来源：https://arxiv.org/pdf/2110.02178v2.pdf

## RES-217 · EdgeNeXt: Efficiently Amalgamated CNN-Transformer Architecture for Mobile Vision Applications
- 原目录页码：[33]；书目：DLI-217。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“EdgeNeXt: EfcientlyAmalgamated CNN-Transformer Architecture forMobile Vision Applications”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2206.10589

## RES-218 · EfficientFormer: Vision Transformers at MobileNet Speed
- 原目录页码：[33]；书目：DLI-218。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：围绕设备友好的算子与特征表示组织高效视觉骨干。
- 研究问题：围绕“EfficientFormer: Vision Transformers at MobileNet Speed”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-156
- 原始来源：https://arxiv.org/abs/2206.01191

## RES-219 · TinyViT: Fast Pretraining Distillation for Small Vision Transformers
- 原目录页码：[33]；书目：DLI-219。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TinyViT: Fast Pretraining Distillation for Small Vision Transformers”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2207.10666.pdf

## RES-220 · MobileOne: An Improved One millisecond Mobile Backbone
- 原目录页码：[33]；书目：DLI-220。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“An Improved One millisecond Mobile Backbone”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2206.04040.pdf

## RES-221 · Learning to Upsample by Learning to Sample
- 原目录页码：[34]；书目：DLI-221。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：预测采样偏移，通过grid_sample等操作生成更高分辨率特征。
- 研究问题：围绕“Learning to Upsample by Learning to Sample”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-062
- 原始来源：https://arxiv.org/pdf/2308.15085

## RES-222 · ASCNet: Asymmetric Sampling Correction Network for Infrared Image Destriping
- 原目录页码：[34]；书目：DLI-222。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ASCNet: Asymmetric Sampling Correction Network for Infrared Image Destriping”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10855453

## RES-223 · DBCFS-Net: Dynamic Blocks and Cross-Domain Feature Synergy for Remote Sensing Object Detection | IEEE Journals & Magazine | IEEE Xplore
- 原目录页码：[34]；书目：DLI-223。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DBCFS-Net: Dynamic Blocks and Cross-Domain Feature Synergy for Remote Sensing Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/11303973/

## RES-224 · Not All Rollouts are Useful: Down-Sampling Rollouts in LLM Reinforcement Learning
- 原目录页码：[34]；书目：DLI-224。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：依据奖励差异选择部分rollout用于策略更新，将生成和更新的预算分开。
- 研究问题：围绕“NOT ALL ROLLOUTS ARE USEFUL: DOWN-SAMPLING ROLLOUTS IN LLM REINFORCEMENT LEARNING”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-244
- 原始来源：https://arxiv.org/pdf/2504.13818

## RES-225 · DABI: Evaluation of Data Augmentation Methods Using Downsampling in Bilateral Control-Based Imitation Learning with Images
- 原目录页码：[34]；书目：DLI-225。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DABI: Evaluation of Data Augmentation Methods Using Downsampling in Bilateral Control-Based Imitation Learning with Images”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2410.04370

## RES-226 · Group Downsampling with Equivariant Anti-aliasing
- 原目录页码：[34]；书目：DLI-226。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“GROUP DOWNSAMPLING WITH EQUIVARIANT ANTI ALIASING”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2504.17258

## RES-227 · DS-Pnet: FM-Based Positioning via Downsampling
- 原目录页码：[34]；书目：DLI-227。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DS-Pnet: FM-Based Positioning via Downsampling”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2504.07429

## RES-228 · ADAPTOR: Adaptive Token Reduction for Video Diffusion Transformers
- 原目录页码：[34]；书目：DLI-228。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ADAPTOR: Adaptive Token Reduction for Video Diffusion Transformers”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025W/EDGE/papers/Peruzzo_ADAPTOR_Adaptive_Token_Reduction_for_Video_Diffusion_Transformers_CVPRW_2025_paper.pdf

## RES-229 · Dynamic U-Net: Adaptively Calibrate Features for Abdominal Multi-organ Segmentation
- 原目录页码：[34]；书目：DLI-229。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Dynamic U-Net: Adaptively Calibrate Features for Abdominal Multi-organ Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2403.07303

## RES-230 · UAV-DETR: Efficient End-to-End Object Detection for Unmanned Aerial Vehicle Imagery
- 原目录页码：[34]；书目：DLI-230。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“UAV-DETR: Efficient End-to-End Object Detection for Unmanned Aerial Vehicle Imagery”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2501.01855

## RES-231 · Leveraging Multispectral Sensors for Color Correction in Mobile Cameras
- 原目录页码：[35]；书目：DLI-231。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Leveraging Multispectral Sensors for Color Correction in Mobile Cameras”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2512.08441

## RES-232 · Reliable Thinking with Images
- 原目录页码：[35]；书目：DLI-232。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：估计视觉线索与文字推理的可靠性，再通过过滤和投票减少错误线索传播。
- 研究问题：围绕“Reliable Thinking with Images”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-245
- 原始来源：https://arxiv.org/pdf/2602.12916https://github.com/XLearning-SCU/Reliable_TWI

## RES-233 · DashFusion: Dual-stream Alignment with Hierarchical Bottleneck Fusion for Multimodal Sentiment Analysis
- 原目录页码：[35]；书目：DLI-233。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过残差路径组织较深卷积网络并改善优化。；先做时间和语义对齐，再通过层级瓶颈融合多模态情感信息。
- 研究问题：围绕“DashFusion: Dual-stream Alignment with Hierarchical Bottleneck Fusion for Multimodal Sentiment Analysis”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-246,MOD-158
- 原始来源：https://arxiv.org/pdf/2512.05515

## RES-234 · ZUMA: Training-free Zero-shot Unified Multimodal Anomaly Detection
- 原目录页码：[35]；书目：DLI-234。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ZUMA: Training-free Zero-shot Unified Multimodal Anomaly Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/11367454

## RES-235 · Boosting Medical Visual Understanding From Multi-Granular Language Learning
- 原目录页码：[35]；书目：DLI-235。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Boosting Medical Visual Understanding From Multi-Granular Language Learning”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openreview.net/forum?id=ccjukmExrB

## RES-236 · FusionRegister: Every Infrared and Visible Image Fusion Deserves Registration
- 原目录页码：[35]；书目：DLI-236。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FusionRegister: Every Infrared and Visible Image Fusion Deserves Registration”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2603.07667v1

## RES-237 · Accelerating Streaming Video Large Language Models via Hierarchical Token Compression
- 原目录页码：[35, 36]；书目：DLI-237。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：缓存相似帧视觉特征，并在进入语言模型前筛除冗余时空token。
- 研究问题：围绕“Accelerating Streaming Video Large Language Models via Hierarchical Token Compression”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-247
- 原始来源：https://arxiv.org/abs/2512.00891

## RES-238 · An efficient, scalable, and adaptable plug-and-play temporal attention module for motion-guided cardiac segmentation with sparse temporal labels
- 原目录页码：[36]；书目：DLI-238。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“An efficient, scalable, and adaptable plug-and-play temporal attention module for motion-guided cardiac segmentation with sparse temporal labels”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/pii/S1361841526000502

## RES-239 · TimeBase: The Power of Minimalism in Efficient Long-term Time Series Forecasting
- 原目录页码：[36]；书目：DLI-239。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TimeBase: The Power of Minimalism in Efficient Long-term Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openreview.net/forum?id=GhTdNOMfOD

## RES-240 · Temporal Restoration and Spatial Rewiring for Source-Free Multivariate Time Series Domain Adaptation
- 原目录页码：[36]；书目：DLI-240。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Temporal Restoration and Spatial Rewiring for Source-Free Multivariate Time Series Domain Adaptation”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://dl.acm.org/doi/10.1145/3711896.3737150

## RES-241 · MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting
- 原目录页码：[36]；书目：DLI-241。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2603.18432

## RES-242 · FreqEvo: Enhancing Time Series Forecasting With Multi-Level Frequency Domain Feature Extraction
- 原目录页码：[36]；书目：DLI-242。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FreqEvo: Enhancing Time Series Forecasting With Multi-Level Frequency Domain Feature Extraction”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://doi.org/10.1109/tkde.2025.3632365

## RES-243 · CoRA: Covariate-Aware Adaptation of Time Series Foundation Models
- 原目录页码：[36, 37]；书目：DLI-243。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CORA: COVARIATE-AWARE ADAPTATION OF TIME SERIES FOUNDATION MODELS”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2510.12681

## RES-244 · FITS: Modeling Time Series with $10k$ Parameters
- 原目录页码：[37]；书目：DLI-244。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FITS: MODELING TIME SERIES WITH 10k PARAME TERS”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2307.03756；https://arxiv.org/abs/2307.03756

## RES-245 · SST: Multi-Scale Hybrid Mamba-Transformer Experts for Time Series Forecasting
- 原目录页码：[37]；书目：DLI-245。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SST: Multi-Scale Hybrid Mamba-Transformer Experts for Long-Short Range Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2404.14757

## RES-246 · CrossLinear: Plug-and-Play Cross-Correlation Embedding for Time Series Forecasting with Exogenous Variables
- 原目录页码：[37]；书目：DLI-246。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以轻量交叉相关嵌入捕捉外生变量的直接且时间相对稳定的依赖。
- 研究问题：围绕“CrossLinear: Plug-and-Play Cross-Correlation Embedding for Time Series Forecasting with Exogenous Variables”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-248
- 原始来源：https://arxiv.org/pdf/2505.23116

## RES-247 · MSGNet: Learning Multi-Scale Inter-Series Correlations for Multivariate Time Series Forecasting
- 原目录页码：[37]；书目：DLI-247。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过频域拆分时间尺度，在各尺度学习变量间关系并建模序列内依赖。
- 研究问题：围绕“MSGNet: Learning Multi-Scale Inter-Series Correlations for Multivariate Time Series Forecasting”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-249
- 原始来源：https://arxiv.org/abs/2401.00423

## RES-248 · A Time Series is Worth 64 Words: Long-term Forecasting with Transformers
- 原目录页码：[37, 38]；书目：DLI-248。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：把时间序列切成子序列patch作为token，并以共享模型处理各单变量通道。
- 研究问题：围绕“A Time Series is Worth 64 Words: Long-term Forecasting with Transformers”在时序预测中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：历史窗口、预测步长、时间划分与未来协变量可用性
- 简单对照：简单线性/季节基线、固定相关结构及候选机制
- 最小验证：按预测步长、漂移时段与变量分组报告误差，不读取未来统计
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-267
- 原始来源：https://arxiv.org/pdf/2211.14730.pdf

## RES-249 · UACANet: Uncertainty Augmented Context Attention for Polyp Segmentation
- 原目录页码：[38]；书目：DLI-249。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用前一预测划分前景、背景和不确定区域，再聚合对应上下文细化分割。
- 研究问题：围绕“UACANet: Uncertainty Augmented Context Attention for Polyp Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-250
- 原始来源：https://arxiv.org/abs/2107.02368

## RES-250 · SFFNet: A Wavelet-Based Spatial and Frequency Domain Fusion Network for Remote Sensing Segmentation
- 原目录页码：[38]；书目：DLI-250。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以Haar小波分离高低频特征，并与空间路径联合用于遥感分割。
- 研究问题：围绕“SFFNet: A Wavelet-Based Spatial and Frequency Domain Fusion Network for Remote Sensing Segmentation”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-251
- 原始来源：https://arxiv.org/abs/2405.01992

## RES-251 · SAM2-LOVE: Segment Anything Model 2 in Language-aided Audio-Visual Scenes
- 原目录页码：[38]；书目：DLI-251。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SAM2-LOVE: Segment Anything Model 2 in Language-aided Audio-Visual Scenes”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_SAM2-LOVE_Segment_Anything_Model_2_in_Language-aided_Audio-Visual_Scenes_CVPR_2025_paper.pdf

## RES-252 · CRISP-SAM2: SAM2 with Cross-Modal Interaction and Semantic Prompting for Multi-Organ Segmentation
- 原目录页码：[38]；书目：DLI-252。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CRISP-SAM2 : SAM2 with Cross-Modal Interaction and Semantic Prompting for Multi- Organ Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2506.23121https://github.com/YU-deep/CRISP_SAM2

## RES-253 · SAM2-SGP: Enhancing SAM2 for Medical Image Segmentation via Support-Set Guided Prompting
- 原目录页码：[38]；书目：DLI-253。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用支持集图像掩码对生成伪掩码，再据此形成框提示与局部注意力。
- 研究问题：围绕“SAM2-SGP: Enhancing SAM2 for Medical Image Segmentation via Support-Set Guided Prompting”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-252
- 原始来源：https://arxiv.org/pdf/2506.19658?https://github.com/astlian9/SAM_Support

## RES-254 · SAMba-UNet: SAM2-Mamba UNet for Cardiac MRI in Medical Robotic Perception
- 原目录页码：[39]；书目：DLI-254。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SAMba-UNet: Synergizing SAM2 and Mamba in UNet with Heterogeneous Aggregation for Cardiac MRI Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2505.16304

## RES-255 · SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation
- 原目录页码：[39]；书目：DLI-255。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SAM2-UNet: Segment Anything 2 Makes Strong Encoder for Natural and Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2408.08870

## RES-256 · SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to Downstream Segmentation Tasks
- 原目录页码：[39]；书目：DLI-256。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SAM2-UNeXT: An Improved High-Resolution Baseline for Adapting Foundation Models to DownstreamSegmentationTasks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2508.03566?

## RES-257 · MedSAM2: Segment Anything in 3D Medical Images and Videos
- 原目录页码：[39]；书目：DLI-257。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MedSAM2: Segment Anything in 3D Medical Images and Videos”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2504.03600

## RES-258 · DyCON: Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi-supervised Medical Image Segmentation
- 原目录页码：[40]；书目：DLI-258。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：按不确定性动态加权一致性，并以熵相关对比学习增强半监督分割。
- 研究问题：围绕“DyCON:Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi- supervised Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-253
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Assefa_DyCON_Dynamic_Uncertainty-aware_Consistency_and_Contrastive_Learning_for_Semi-supervised_Medical_CVPR_2025_paper.pdf

## RES-259 · Show and Segment: Universal Medical Image Segmentation via In-Context Learning
- 原目录页码：[40]；书目：DLI-259。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Show and Segment: Universal Medical Image Segmentation via In-Context Learning”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Gao_Show_and_Segment_Universal_Medical_Image_Segmentation_via_In-Context_Learning_CVPR_2025_paper.pdf

## RES-260 · ConText: Driving In-context Learning for Text Removal and Segmentation
- 原目录页码：[40]；书目：DLI-260。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ConText: Driving In-context Learning for Text Removal and Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2506.03799?

## RES-261 · Explore In-Context Segmentation via Latent Diffusion Models
- 原目录页码：[40]；书目：DLI-261。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Explore In-Context Segmentation via Latent Diffusion Models”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/32812

## RES-262 · Hybrid Global-Local Representation with Augmented Spatial Guidance for Zero-Shot Referring Image Segmentation
- 原目录页码：[40]；书目：DLI-262。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Hybrid Global-Local Representation with Augmented Spatial Guidance for Zero-Shot Referring Image Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Hybrid_Global-Local_Representation_with_Augmented_Spatial_Guidance_for_Zero-Shot_Referring_CVPR_2025_paper.pdf

## RES-263 · TBConvL-Net: A Hybrid Deep Learning Architecture for Robust Medical Image Segmentation
- 原目录页码：[41]；书目：DLI-263。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TBConvL-Net: A Hybrid Deep Learning Architecture for Robust Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2409.03367

## RES-264 · HResFormer: Hybrid Residual Transformer for Volumetric Medical Image Segmentation
- 原目录页码：[41]；书目：DLI-264。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：融合切片内二维细节与体积三维上下文，并以残差学习形成体数据表征。
- 研究问题：围绕“HResFormer: Hybrid Residual Transformer for Volumetric Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-254
- 原始来源：https://arxiv.org/pdf/2412.11458

## RES-265 · ScribFormer: Transformer Makes CNN Work Better for Scribble-based Medical Image Segmentation
- 原目录页码：[41]；书目：DLI-265。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“ScribFormer: Transformer Makes CNN Work Better for Scribble-based Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2402.02029

## RES-266 · Efficient Vision Foundation Models for High-Resolution Generation and Perception
- 原目录页码：[41]；书目：DLI-266。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Efficient Vision Foundation Models for High-Resolution Generation and Perception”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10677874

## RES-267 · RepViT-SAM: Towards Real-Time Segmenting Anything
- 原目录页码：[41]；书目：DLI-267。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“RepViT-SAM: Towards Real-Time Segmenting Anything”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2312.05760

## RES-268 · TinySAM: Pushing the Envelope for Efficient Segment Anything Model
- 原目录页码：[41]；书目：DLI-268。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“TinySAM: Pushing the Envelope for Efficient Segment Anything Model”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ojs.aaai.org/index.php/AAAI/article/view/34255

## RES-269 · FFCA-YOLO for Small Object Detection in Remote Sensing Images | IEEE Journals & Magazine | IEEE Xplore
- 原目录页码：[41]；书目：DLI-269。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FFCA-YOLO for Small Object Detection in Remote Sensing Images”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/10423050

## RES-270 · MAGNet: Multi-scale Awareness and Global fusion Network for RGB-D salient object detection
- 原目录页码：[41]；书目：DLI-270。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MAGNet: Multi-scale Awareness and Global fusion Network for RGB-D salient object detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://www.sciencedirect.com/science/article/abs/pii/S0950705124007603

## RES-271 · RemoteDet-Mamba: A Hybrid Mamba-CNN Network for Multi-modal Object Detection in Remote Sensing Images
- 原目录页码：[42]；书目：DLI-271。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“RemoteDet-Mamba: A Hybrid Mamba-CNN Network for Multi-modal Object Detection in Remote Sensing Images”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2410.13532v1

## RES-272 · U-DECN: End-to-End Underwater Object Detection ConvNet with Improved DeNoising Training
- 原目录页码：[42]；书目：DLI-272。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“U-DECN: End-to-End Underwater Object Detection ConvNet with Improved DeNoising Training”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2408.05780v2

## RES-273 · Low-light Object Detection
- 原目录页码：[42]；书目：DLI-273。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Low-light Object Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2405.03519

## RES-274 · DRPCA-Net: Make Robust PCA Great Again for Infrared Small Target Detection
- 原目录页码：[42]；书目：DLI-274。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将低秩稀疏分解展开为可学习网络，并用输入条件化的超网络生成迭代参数。
- 研究问题：围绕“DRPCA-Net: Make Robust PCA Great Again for Infrared Small Target Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-255
- 原始来源：https://arxiv.org/pdf/2507.09541

## RES-275 · Rethinking Generalizable Infrared Small Target Detection: A Real-scene Benchmark and Cross-view Representation Learning
- 原目录页码：[42]；书目：DLI-275。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Rethinking Generalizable Infrared Small Target Detection: A Real-scene Benchmark and Cross-view Representation Learning”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2504.16487v1

## RES-276 · CROWn: A Unified Framework for Anti-Aliased Downsampling and Phase-Calibrated Fusion in 3D Medical Segmentation
- 原目录页码：[42]；书目：DLI-276。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CROWn: A Unified Framework for Anti-Aliased Downsampling and Phase-Calibrated Fusion in 3D Medical Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.pdf

## RES-277 · CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction
- 原目录页码：[42]；书目：DLI-277。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：卷积重建用于脑电伪迹去除，关注跨受试者迁移。
- 研究问题：围绕“CLEEGN: A Convolutional Neural Network for Plug-and-Play Automatic EEG Reconstruction”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-091
- 原始来源：https://arxiv.org/html/2210.05988v2

## RES-278 · GLSANet: Global-Local Self-Attention Network for Remote Sensing Image Semantic Segmentation
- 原目录页码：[42]；书目：DLI-278。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“GLSANet: Global-Local Self-Attention Network for Remote Sensing Image Semantic Segmentation”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10011428

## RES-279 · Exploiting Scale-Variant Attention for Segmenting Small Medical Objects
- 原目录页码：[42]；书目：DLI-279。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SvANet: A Scale-variant Attention-based Network for Small Medical Object Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/html/2407.07720v1

## RES-280 · EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation
- 原目录页码：[42]；书目：DLI-280。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation”在语言/多模态推理中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、提示、上下文长度、缓存状态与生成预算
- 简单对照：原始推理、固定压缩或缓存及候选策略
- 最小验证：同时报告答案质量、真实延迟、显存与额外适配成本
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2405.06880

## RES-281 · DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional Indistinct-Boundary Object Segmentation
- 原目录页码：[43]；书目：DLI-281。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional Indistinct-Boundary Object Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2311.00483

## RES-282 · MSA$^2$Net: Multi-scale Adaptive Attention-guided Network for Medical Image Segmentation
- 原目录页码：[43]；书目：DLI-282。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MSA2Net: Multi-scale Adaptive Attention-guided Network for Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2407.21640

## RES-283 · Vision-LSTM: xLSTM as Generic Vision Backbone
- 原目录页码：[43]；书目：DLI-283。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：将xLSTM块用于图像patch序列，交替按相反方向处理以聚合视觉上下文。
- 研究问题：围绕“Vision-LSTM: xLSTM as Generic Vision Backbone”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-256
- 原始来源：https://arxiv.org/pdf/2406.04303

## RES-284 · Generative Information-guided Heterogeneous Cross-fusion Network with Contrastive Learning for Multimodal Remote Sensing Image Classification
- 原目录页码：[43]；书目：DLI-284。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Generative Information-guided Heterogeneous Cross-fusion Network with Contrastive Learning for Multimodal Remote Sensing Image Classification”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/11177538

## RES-285 · RFAConv: Receptive-Field Attention Convolution for Improving Convolutional Neural Networks
- 原目录页码：[43]；书目：DLI-285。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“RFAConv: Innovating Spatial Attention and Standard Convolutional Operation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2304.03198

## RES-286 · Salient Positions based Attention Network for Image Classification
- 原目录页码：[43]；书目：DLI-286。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Salient Positions based Attention Network for Image Classification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2106.04996

## RES-287 · SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications
- 原目录页码：[43]；书目：DLI-287。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2303.15446

## RES-288 · CoordGate: Efficiently Computing Spatially-Varying Convolutions in Convolutional Neural Networks
- 原目录页码：[44]；书目：DLI-288。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：使用坐标编码网络生成乘性门控，使卷积能表达空间位置相关的变化。
- 研究问题：围绕“CoordGate: Efficiently Computing Spatially-Varying Convolutions in Convolutional Neural Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-268
- 原始来源：https://arxiv.org/abs/2401.04680

## RES-289 · Efficient Multi-Scale Attention Module with Cross-Spatial Learning
- 原目录页码：[44]；书目：DLI-289。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：分组特征经方向聚合与局部分支交互，形成多尺度空间权重。
- 研究问题：围绕“Efficient Multi-Scale Attention Module with Cross-Spatial Learning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-151
- 原始来源：https://arxiv.org/pdf/2305.13563v2

## RES-290 · Context-Aware Crowd Counting
- 原目录页码：[44]；书目：DLI-290。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Context-Aware Crowd Counting”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/1811.10452

## RES-291 · Self-Supervised Predictive Convolutional Attentive Block for Anomaly Detection
- 原目录页码：[44]；书目：DLI-291。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：利用逐元素乘法构成非线性特征交互，并结合卷积空间混合。
- 研究问题：围绕“Self-Supervised Predictive Convolutional Attentive Block for Anomaly Detection”在检测/遥感中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：原图或地区独立划分、像素预算、检测头与训练轮数
- 简单对照：原检测器、提高分辨率或简单融合与候选机制
- 最小验证：按目标大小、朝向和复杂背景报告召回、误检及真实延迟
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-106
- 原始来源：https://arxiv.org/abs/2111.09099

## RES-292 · Dynamic Filter Networks
- 原目录页码：[44]；书目：DLI-292。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Dynamic Filter Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/1605.09673

## RES-293 · FMB: a Functional Manipulation Benchmark for Generalizable Robotic Learning
- 原目录页码：[44]；书目：DLI-293。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“FMB: a Functional Manipulation Benchmark for Generalizable Robotic Learning”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2401.08553

## RES-294 · Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution
- 原目录页码：[44]；书目：DLI-294。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在多个空间尺度提取和聚合特征，再生成空间调制。
- 研究问题：围绕“Spatially-Adaptive Feature Modulation for Efficient Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-037
- 原始来源：https://arxiv.org/abs/2302.13800

## RES-295 · Efficient Long-Range Attention Network for Image Super-resolution
- 原目录页码：[44, 45]；书目：DLI-295。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Efficient Long-Range Attention Network for Image Super-resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2203.06697

## RES-296 · Dual Aggregation Transformer for Image Super-Resolution
- 原目录页码：[45]；书目：DLI-296。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以学习采样位置减少注意力对固定窗口的依赖。
- 研究问题：围绕“Dual Aggregation Transformer for Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-112
- 原始来源：https://arxiv.org/abs/2308.03364

## RES-297 · Adaptive Graph Convolution for Point Cloud Analysis
- 原目录页码：[45]；书目：DLI-297。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Adaptive Graph Convolution for Point Cloud Analysis”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2108.08035

## RES-298 · GeoConv: Geodesic Guided Convolution for Facial Action Unit Recognition
- 原目录页码：[45]；书目：DLI-298。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用粗重建三维人脸的测地距离给二维卷积核加权，以利用脸部流形结构。
- 研究问题：围绕“GeoConv: Geodesic Guided Convolution for Facial Action Unit Recognition”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-257
- 原始来源：https://arxiv.org/abs/2003.03055

## RES-299 · PnP-3D: A Plug-and-Play for 3D Point Clouds
- 原目录页码：[45]；书目：DLI-299。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：融合点坐标局部上下文与全局特征响应，细化点云表征。
- 研究问题：围绕“PnP-3D: A Plug-and-Play for 3D Point Clouds”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-090
- 原始来源：https://arxiv.org/abs/2108.07378

## RES-300 · Parameter is Not All You Need: Starting from Non-Parametric Networks for 3D Point Cloud Analysis
- 原目录页码：[45]；书目：DLI-300。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Parameter is Not All You Need, Starting from Non-parametric Networks for 3D Point Cloud Analysis”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2303.08134

## RES-301 · PF-Net: Point Fractal Network for 3D Point Cloud Completion
- 原目录页码：[45]；书目：DLI-301。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“PF-Net: Point Fractal Network for 3D Point Cloud Completion”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2003.00410

## RES-302 · PRA-Net: Point Relation-Aware Network for 3D Point Cloud Analysis
- 原目录页码：[45]；书目：DLI-302。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“PRA-Net: Point Relation-Aware Network for 3D Point Cloud Analysis”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2112.04903

## RES-303 · KPConv: Flexible and Deformable Convolution for Point Clouds
- 原目录页码：[45]；书目：DLI-303。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：在连续点云中通过核点定义卷积，不需先转换成体素或图像网格。
- 研究问题：围绕“KPConv: Flexible and Deformable Convolution for Point Clouds”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-258
- 原始来源：https://arxiv.org/pdf/1904.08889

## RES-304 · SimVP: Simpler Yet Better Video Prediction
- 原目录页码：[46]；书目：DLI-304。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SimVP: Simpler yet Better Video Prediction”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2022/papers/Gao_SimVP_Simpler_Yet_Better_Video_Prediction_CVPR_2022_paper.pdf

## RES-305 · PoseBERT: A Generic Transformer Module for Temporal 3D Human Modeling
- 原目录页码：[46]；书目：DLI-305。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“PoseBERT: A Generic Transformer Module for Temporal 3D Human Modeling”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2208.10211

## RES-306 · A Geometric Knowledge Oriented Single-Frame 2D-to-3D Human Absolute Pose Estimation Method
- 原目录页码：[46]；书目：DLI-306。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“A Geometric Knowledge Oriented Single-Frame 2D-to-3D Human Absolute Pose Estimation Method”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/10131895

## RES-307 · Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image Segmentation
- 原目录页码：[46]；书目：DLI-307。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Beyond Self-Attention: Deformable Large Kernel Attention for Medical Image Segmentation”在医学图像研究中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：患者独立划分、体素间距、分辨率、标注与支持集隔离
- 简单对照：原基线、同容量简单卷积或融合与候选机制
- 最小验证：按边界、细小结构和域差异分桶，不据研究指标声称临床有效
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2309.00121

## RES-308 · MoE3D: A Mixture-of-Experts Module for 3D Reconstruction
- 原目录页码：[46]；书目：DLI-308。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用多个平滑深度专家及其混合表示处理深度边界的不确定性。
- 研究问题：围绕“MoE3D: AMixture-of-Experts Module for 3D Reconstruction”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-259
- 原始来源：https://arxiv.org/pdf/2601.05208

## RES-309 · CorNET Deep Learning Framework for Heart Rate Estimation and Biometric Identification
- 原目录页码：[46]；书目：DLI-309。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“CorNET Deep Learning Framework for Heart Rate Estimation and Biometric Identification”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/document/8607019

## RES-310 · FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information
- 原目录页码：[46]；书目：DLI-310。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：从对角经验Fisher与自然梯度视角修正动量、偏差、epsilon、裁剪和衰减。
- 研究问题：围绕“FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-260
- 原始来源：https://arxiv.org/pdf/2405.12807

## RES-311 · SmoothNet: A Plug-and-Play Network for Refining Human Poses in Videos
- 原目录页码：[47]；书目：DLI-311。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：对姿态轨迹进行时序平滑，抑制持续或偶发抖动。
- 研究问题：围绕“SmoothNet: A Plug-and-Play Network for Refining Human Poses in Videos”在点云/几何中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：点采样、邻域定义、几何对应、密度与传感器划分
- 简单对照：固定几何聚合、同邻点预算及候选关系建模
- 最小验证：按密度、遮挡及几何扰动评估；图和网格的轴语义不可混用
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-092
- 原始来源：https://arxiv.org/abs/2112.13715

## RES-312 · Dual Attention Network for Scene Segmentation
- 原目录页码：[47]；书目：DLI-312。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：并行位置与通道关系建模，服务场景分割。
- 研究问题：围绕“Dual Attention Network for Scene Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-101
- 原始来源：https://arxiv.org/abs/1809.02983

## RES-313 · Simple Baselines for Image Restoration
- 原目录页码：[47]；书目：DLI-313。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以简单门控和残差组织恢复特征，检验复杂激活是否必要。
- 研究问题：围绕“Simple Baselines for Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-083
- 原始来源：https://arxiv.org/pdf/2204.04676

## RES-314 · DSAM: A Deep Learning Framework for Analyzing Temporal and Spatial Dynamics in Brain Networks
- 原目录页码：[47]；书目：DLI-314。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：quarantine。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“DSAM: A Deep Learning Framework for Analyzing Temporal and Spatial Dynamics in Brain Networks”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/html/2405.15805v1

## RES-315 · Restoring Images in Adverse Weather Conditions via Histogram Transformer
- 原目录页码：[47]；书目：DLI-315。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：按强度排序并分桶空间特征，用相近亮度的关联聚合天气退化信息。
- 研究问题：围绕“Restoring Images in Adverse Weather Conditions via Histogram Transformer”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-261
- 原始来源：https://arxiv.org/abs/2407.10172

## RES-316 · Adapt or Perish: Adaptive Sparse Transformer with Attentive Feature Refinement for Image Restoration
- 原目录页码：[47]；书目：DLI-316。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：通过自适应稀疏自注意力减少无关区域交互，再以前馈细化减少特征冗余。
- 研究问题：围绕“Adapt or Perish: Adaptive Sparse Transformer with Attentive Feature Refinement for Image Restoration”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-262
- 原始来源：https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_Adapt_or_Perish_Adaptive_Sparse_Transformer_with_Attentive_Feature_Refinement_CVPR_2024_paper.pdf

## RES-317 · Context-Guided Spatial Feature Reconstruction for Efficient Semantic Segmentation
- 原目录页码：[47, 48]；书目：DLI-317。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：用矩形上下文与形状自校准重建空间特征，使关键区域贴近前景。
- 研究问题：围绕“Context-Guided Spatial Feature Reconstruction for Efficient Semantic Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-263
- 原始来源：https://arxiv.org/abs/2405.06228

## RES-318 · SCTNet: Single-Branch CNN with Transformer Semantic Information for Real-Time Segmentation
- 原目录页码：[48]；书目：DLI-318。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“SCTNet: Single-Branch CNN with Transformer Semantic Information for Real-Time Segmentation”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/pdf/2312.17071

## RES-319 · Burstormer: Burst Image Restoration and Enhancement Transformer
- 原目录页码：[48]；书目：DLI-319。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Burstormer: Burst Image Restoration and Enhancement Transformer”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://arxiv.org/abs/2304.01194

## RES-320 · SeD: Semantic-Aware Discriminator for Image Super-Resolution
- 原目录页码：[48]；书目：DLI-320。
- 完成程度：有关联机制卡（摘要级/既有资料级），不代表整篇已精读；证据：verified_metadata。
- 机制：以预训练视觉语义作为判别器条件，结合空间交叉注意力学习细粒度分布。
- 研究问题：围绕“SeD: Semantic-Aware Discriminator for Image Super-Resolution”在图像恢复中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：退化生成、配对划分、输入动态范围与训练预算
- 简单对照：普通卷积、固定频率滤波或简单融合与候选机制
- 最小验证：分别评价细节、色偏和噪声，使用独立真实退化验证
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：MOD-264
- 原始来源：https://arxiv.org/abs/2402.19387

## RES-321 · MCDB-Net: Multiview Collaborative Dual-Branch Unmixing Network for Hyperspectral Images | IEEE Journals & Magazine | IEEE Xplore
- 原目录页码：[48]；书目：DLI-321。
- 完成程度：官方题名与摘要已核对；机制细读待完成；证据：verified_metadata。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“MCDB-Net: Multiview Collaborative Dual-Branch Unmixing Network for Hyperspectral Images”在表征与结构中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：输入输出语义、数据划分、模型容量与训练预算
- 简单对照：原结构、同参数简单替代与候选结构
- 最小验证：先隔离一个机制，记录失败条件、代价及最近邻差异
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://ieeexplore.ieee.org/abstract/document/11427018

## RES-322 · Align Images Before You Generate
- 原目录页码：[28]；书目：DLI-322。
- 完成程度：仅来源题名/链接；原文机制待核实；证据：source_only。
- 机制：当前未写出经核对的具体机制，不从题名臆造结构、公式或通用接入方式。
- 研究问题：围绕“Align Images Before You Generate”在生成与逆问题中的原始问题，明确一个能观察的失败现象；以下是研究者拟议的验证路径，不是论文已完成的实验。
- 控制条件：模型检查点、采样器、种子、步数、测量算子及条件信息
- 简单对照：原始采样、简单固定校正与候选控制
- 最小验证：区分保真、感知与条件一致性，检查额外计算和不稳定样例
- 后续阅读：先核对原始问题、核心算子、假设及最近邻，再抽取输入输出轴、代价和失败边界。不得把完整框架或数据基准都叫即插即用层。
- 机制卡：尚未制卡
- 原始来源：https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Align_Images_Before_You_Generate_CVPR_2026_paper.html
