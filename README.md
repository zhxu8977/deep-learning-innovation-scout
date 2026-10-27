# 深度学习创新思路助手

当模型效果上不去、论文创新点卡住，先诊断失败机制，再查模块、论文、代码接口与数据，最后用最小实验决定方向。

技能名：`deep-learning-innovation-scout` · 版本 **2.1.0**。

[下载安装包](https://github.com/zhxu8977/deep-learning-innovation-scout/releases/latest/download/deep-learning-innovation-scout-v2.1.0.zip) · [下载 HTML 内容展示页](https://github.com/zhxu8977/deep-learning-innovation-scout/releases/latest/download/deep-learning-innovation-scout-overview.html) · [全部版本](https://github.com/zhxu8977/deep-learning-innovation-scout/releases)

HTML 展示页包含完整分类清单，下载后用浏览器打开即可离线搜索、筛选和查看详情。它是独立展示附件，无需安装技能。

## 数量与完成范围更正

旧版167张机制卡来自人工选择，**不是“366个”逐项去重后的全部模块**。本版新增101张有官方摘要依据的卡，并建立原目录逐项对应：各栏目标称合计366，实际方法/论文出现361次（含重复），另保留2条栏目/别名行。不能按标题数字硬凑模块。

新增322条逐项研究卡，明确区分“有关联机制”“摘要核对”“仅来源线索”。尚未完成机制分析的条目直接标出，不称全量精读版。核对272条官方题名/摘要，接受身份匹配269条；题名错链和领域误配保留隔离。

先看[每项对应表](skills/deep-learning-innovation-scout/references/source-coverage-map.md)、[研究卡](skills/deep-learning-innovation-scout/references/research-cards.md)、[数量JSON](skills/deep-learning-innovation-scout/references/count-reconciliation.json)。

## 内容

- **268张已整理机制卡**：机制、接入位置、兼容风险、最小区分实验。
- **208个PDF文档索引、3165页本机文字归档**：公开版保留事实索引，本机持有者可回读完整来源。
- **1708个代码单元的静态接口**：类、构造器、forward、依赖、形状示例与风险；包含支持代码，不代表1708个独立模块。
- **95条数据集线索**：任务、标注与划分注意事项。
- **20个实验配方、分任务指南、七阶段科研工作流与案例**。
- 322条书目线索保留，误配隔离；所有层次有重叠，数量不相加。

机制覆盖通道/空间注意力、长程关系、窗口交互、多尺度、频域、动态卷积、结构重参数化、上/下采样、跨层融合、恢复、三维、点云、时序、归一化、长尾、少样本及骨干/训练策略。资料对大语言模型本身的专用方法覆盖有限，应结合原始文献补充。

阅读入口：[整合报告](docs/reading-report.zh-CN.md)、[模块手册](skills/deep-learning-innovation-scout/references/module-handbook.md)、[逐篇研究线索](skills/deep-learning-innovation-scout/references/paper-notes.md)、[科研工作流](skills/deep-learning-innovation-scout/references/innovation-workflow.md)、[质量审计](skills/deep-learning-innovation-scout/references/source-audit.md)。

## 安装

需要Python 3.10+。下载本仓库或Release ZIP并解压，在包含 `install.py` 的目录运行：

```powershell
python install.py --target both
```

也可以通过 Git 下载后安装：

```powershell
git clone https://github.com/zhxu8977/deep-learning-innovation-scout.git
cd deep-learning-innovation-scout
python install.py --target both
```

如果使用支持 GitHub 技能安装的 Codex 助手，也可以直接告诉它：

> 请从 https://github.com/zhxu8977/deep-learning-innovation-scout 安装技能，技能路径是 skills/deep-learning-innovation-scout。

单独装Codex或DSH可分别用 `--target codex`、`--target dsh`。已有旧版时：

```powershell
python install.py --target both --upgrade
```

安装器先校验随包SHA-256清单。相同内容跳过，不同版本只有加 `--upgrade` 才替换；旧版保存在对应home的 `skill-backups/`，已有本机全文归档会保留。普通安装与检索只用Python标准库，无需安装PyTorch或训练环境。

Codex默认装到 `~/.codex/skills`，设置CODEX_HOME时使用其目录；`~/.agents/skills`建立发现链接。DSH默认装到 `~/.dsh/skills`，支持DSH_HOME。也可通过 `--codex-home`、`--dsh-home`、`--agents-home` 指定位置。

保持自动选择开启。刷新技能或开始新对话后即可使用；客户端未发现时再重启。无需在每个项目重复安装。自动触发仍取决于客户端发现与任务匹配，不承诺每句模糊表达都调用。

## 触发

不用记名字，可以说：

> 我做深度学习，模型效果上不去了，帮我看看有什么思路。

> 我做医学分割，细小结构总断，结合模块资料帮我找原因和实验方向。

> 论文创新点卡住了，按研究工作流帮我分析，不要只列模块名。

> 时序预测跨时间段误差很大，先查内置资料，再给最省预算的验证实验。

> 小目标检测漏检多，帮我比较尺度、采样和融合的改进思路。

明确调用：

```text
$deep-learning-innovation-scout
我的任务是……，基线是……，主要失败是……，已有数据和算力是……。
请检索内置知识库，诊断瓶颈，给出有来源、可验证的优先方向。
```

DSH中也可以直接说“使用 deep-learning-innovation-scout 帮我分析”。新对话可用；带上研究任务与失败现象最容易匹配。普通报错或仅润色文字不由这个技能接管。

## 检索

在技能文件夹运行：

```powershell
python scripts/search_catalog.py 医学分割 边界 --limit 5
python scripts/search_catalog.py RevIN --kind module --json
python scripts/search_catalog.py 缓存 扩散 --kind research --limit 5
python scripts/search_catalog.py --inspect SRC-001 --json
python scripts/search_catalog.py 小目标 --kind dataset --limit 5
python scripts/search_catalog.py GRN --kind code --json
python scripts/search_catalog.py --family sampling --kind module
python scripts/search_catalog.py --inspect MOD-001 --json
python scripts/search_catalog.py --stats
```

类型：`module`已整理机制卡、`research`逐项研究卡、`source`原目录出现记录（审计）、`paper`论文、`guide`研究辅助文档、`code`静态接口、`dataset`数据线索、`lead`旧书目、`recipe`实验配方。默认优先机制卡并排除误配/语法失败；审计用 `--include-quarantined`。分数只表示检索相关性，不是质量、创新或涨点概率。

本机增强归档可按检索得到的DOC/CODE/NOTE/DATA编号读取：

```powershell
python scripts/read_source.py --id DOC-实际编号 --pages 2 3
python scripts/read_source.py --id CODE-实际编号 --search forward
```

公开包不包含这些完整原文和第三方代码。自行持有资料时，可安装可选的 `pypdf` 并运行：

```powershell
python tools/archive_materials.py --source-dir "本机资料目录" --skill-dir "已安装技能目录"
```

归档保存在 `references/local-only/`，不参与Git或发布包。公开机制卡和接口索引可独立使用。

## 发布到GitHub

可直接以本目录作为仓库；`.gitignore`排除本机全文、PDF、构建缓存和Release ZIP。生成的公共Release ZIP使用明确文件范围打包，适合上传到GitHub Release：

```powershell
python tools/package_release.py
python -m unittest discover -s tests -v
```

产物为 `dist/deep-learning-innovation-scout-v2.1.0.zip` 及SHA-256文件。修改技能后先重新打包更新清单，再测试。也可让支持技能安装的助手从真实GitHub仓库的 `skills/deep-learning-innovation-scout` 路径安装。

说明按模块与机制归纳，不介绍资料收集者。原始论文和必要许可仍应准确引用；公开包没有原PDF、第三方实现、模型权重或私有路径。原创部分采用MIT许可，范围见 [NOTICE.md](NOTICE.md)。
