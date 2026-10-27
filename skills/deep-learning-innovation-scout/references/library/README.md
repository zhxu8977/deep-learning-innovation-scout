# 分层知识库

v2.1.0：268张已整理机制卡（36类）、322条研究卡、363行来源对应记录（361次方法/论文出现，含重复；2行栏目/别名），以及208份文档索引、1708个静态代码单元、95条数据集、20个实验配方。

这些数量的单位不同，不能相加成算法总数。原目录各栏目标称合计366，逐项计数差异见 [覆盖表](../source-coverage-map.md)。仍未完成机制细读的研究卡明确标记，不能称全量精读版。

- modules.json：机制、接入、风险、最小实验与证据范围。
- research-cards.json：逐条题名、完成程度、关联机制、控制条件和后续研究路径。
- source-items.json：每次出现的页码、原栏目与书目对应；保留重复及非方法行。
- papers.json：本机文档索引，不含原PDF。
- code-interfaces.json：静态类、函数、依赖与风险，不是已验证实现。
- datasets.json / recipes.json：数据与验证路径。
- [书目目录](../catalog.md)：322条，保留质量问题与隔离标记。

运行 `python scripts/search_catalog.py 任务词 --kind research --json`。默认检索不把source重复行计作方法。用 `--kind source` 或 `--inspect SRC-001` 审计来源，用 `--inspect RES-001` 查看研究卡。只有本机增强归档持有原始全文与代码。
