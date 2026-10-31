# Fusion 与 Git 提交规范

## 最小目录

每个模型项目直接放在根目录 `<model-id>/`，与 `assets/`、`tools/` 平级；不再套一层 models。共享板卡参考放 assets，不计为独立项目。

项目只需：

- `model.f3d`：一个 Fusion 文档，包含全部零件和装配。外部引用需完整打包时改用唯一的 `model.f3z`。
- `README.md`：简介、版本/tag、状态、尺寸/单位/原点、来源、必要装配说明及倒序更新日志。
- `images/three-view.png`：同版正交正视、俯视、右视合成一张，标清方向；毫米制，避免透视畸变。
- `images/exploded.png`：同版分体展示，零件清楚可辨；单件模型写明无需拆分。
- 可选 `images/assembly.png`：整体外观。
- `print/`：当前版打印导出与摆盘，按下文规范组织。
- 按需增加 `WIRING.md`、`ASSEMBLY.md`，分别记录接线和装配；较多说明放 `docs/`，由项目 README 链接。不要生成空模板。接线需列实际板卡版本、固件引脚、供电和丝印；未核对就明确待确认。

共享资源使用 `assets/<asset-id>/model.*` 和 README，保留一个主文件及来源/尺寸/限制，不强制 Fusion 格式或项目三视图。各项目 README 链接其所用资源，避免复制。发布 tag 冻结整个仓库，包括该版依赖的共享资源。

根 README 作为展示页，只保留总体简介、各项目简介/当前版本及最新三视图。新项目也必须添加展示入口；图片使用相对路径 `<model-id>/images/three-view.png`，不复制图片。缺图时写待补，不放无效图片链接。

三视图和分体图可在 Fusion 临时改变视图/零件位置后截图，截图后恢复装配；不为截图另存一份权威主模型。不得用透视外观图改名冒充三视图。

## 版本

每个模型独立编号，tag 为 `<model-id>/vX.Y.Z`。X 用于重大结构/配合变化，Y 用于兼容的功能或结构改进，Z 用于小修正；未发布改动记在“未发布”节。模型版本写在 README，文件名不带版本号。

旧外壳 L6、L7 保留，下一版可从 `fc-enclosure/v8.0.0` 开始；新模型项目从 v1.0.0 开始，assets 参考资源随提交追踪。单纯仓库整理不提高设计版本。不要把 Fusion 云端 V 数字当作 Git 发布版本；可在 README 附记 Fusion 文档链接/版本用于追溯。

标签是整个仓库提交的快照，模型前缀只是发布范围。一次改多个模型时分别检查、分别打 tag；永远不移动已发布标签。

## 本机流程

1. `git status` 确认工作区；有自己的未提交改动先妥善提交/保存，不覆盖。干净时执行 `git pull --ff-only` 和 `git fetch --tags`。
2. 打开目标目录唯一主模型，确认 mm 和当前组件。保存 Fusion 文档后，导出到 generated 临时位置，再替换目标同名文件。重新导入导出文件，确认文档可打开、引用完整、零件齐全。
3. 检查尺寸、干涉、装配路径和修改相关约束；打印用途另检网格及切片。记录实际完成项，实物未验证必须明说。
4. 导出本版三视图与分体图到固定图片路径，更新项目 README 和根展示页；若接线或装配变化，同步对应说明。新发布的项目 README 必须含下列独立行（以外壳下一版为例）：

   `Version: v8.0.0`
   
   `Tag: fc-enclosure/v8.0.0`

5. 执行 `python tools/check_models.py --release fc-enclosure`。人工检查图像与模型一致，README 图片链接有效。
6. 明确暂存目标文件并检查差异：
   ```sh
   git add fc-enclosure README.md
   git diff --cached --stat
   git commit -m "model(fc-enclosure): describe the design change"
   git tag -a fc-enclosure/v8.0.0 -m "FC enclosure v8.0.0: describe change and validation"
   git push origin main
   git push origin refs/tags/fc-enclosure/v8.0.0
   ```
   示例版本号需换成实际新版本；若在工作分支，先合并进入 main，再对正确发布提交打标签。不要使用 --force 或批量推送未知标签。
7. 可选创建同名 GitHub Release，粘贴本版简介/变更/验证状态，附按需导出的打印包。多色 3MF 必须说明是通用模型还是带机型/材料映射的切片工程。

## 旧版本查看与恢复

`git fetch --tags` 后，可用 `git worktree add --detach ../fc-models-L6 L6` 单独查看旧版，不影响当前工作区。新规范版本同理使用其完整 tag。回退某个模型时只取回该目录，作为新提交记录，不重置其他模型、不移动旧标签。

历史入口：[L6](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L6)、[L7](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L7)、[整理前全部导出与脚本](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1)。已删除的脚本引用旧路径，应在历史 worktree 内使用；不要复制回当前目录而不修路径。

## 当前迁移例外

现有外壳 F3D 和预览图字节未变；缺 three-view.png。默认检查允许外壳历史三视图缺项，发布检查不豁免，并要求根 README 引用该项目三视图。C3 校准 STL 与 BH1750 STEP 是 assets 共享参考的正常格式，不适用项目发布检查。

## 打印输出与摆盘

每个模型项目增加 print/，assets 参考板不需要打印目录：

| 路径 | 内容 |
|---|---|
| print/README.md | 源模型版本、文件清单、格式选择与验证状态 |
| print/stl/ | 单色网格，单位 mm |
| print/step/ | 实体交换；按需保留单色合并或分色实体 |
| print/3mf/ | 通用零件模型包；不冒充含打印机设置的工程 |
| print/plates/validation/ | 验证试打方案、实际 project.3mf、摆盘截图 |
| print/plates/production/ | 批量生产方案、实际 project.3mf、摆盘截图 |

每类摆盘用 README.md 说明；未制作工程时标记待制作，不放空文件。只有说明的目录是方案，不是可直接打印的摆盘。一个工程可包含多个打印盘；确有多机型需求时用稳定机型子目录，不按版本另建目录。

验证盘优先一套完整零件，先确认尺寸、光孔、USB、插盖、转轴及紧固件配合；可先单色检查，再按最终材料组合验证。生产盘根据合格试打结果，选择整套排布或同零件/同材料分盘，记录每盘数量及配套数量，避免某零件缺件。不要事先承诺固定每盘套数。

必须记录目标机型、有效区域及禁区、喷嘴、耗材/材料槽、层高、支撑、裙边/擦料塔、打印顺序、切片器版本及预估耗时耗材。检查超界、零件间距、支撑和擦料塔占位；逐件打印还要验证打印头避让。批量实打结果单独记录。

几何改变时，同步重新导出受影响格式、更新两类摆盘并检查；未更新的输出必须移除或明确标记不可用于当前模型，不把旧工程继续标成可用。所有正式输出与主模型在同一提交/tag 内，固定文件名；Release 可附同一套文件供下载，不替代仓库 print/。G-code 属机型/材料专用产物，默认不提交。
