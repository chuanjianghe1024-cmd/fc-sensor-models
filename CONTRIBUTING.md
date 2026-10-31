# Fusion 与 Git 提交规范 / Fusion and Git contribution guide

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

### English

Each model project is a root-level <model-id>/ directory alongside assets/ and tools/; there is no models wrapper. Shared board references live in assets and are not standalone projects.

Required or supported project files:

- model.f3d: one document containing all parts and assemblies; use a single self-contained model.f3z when external references must be packaged.
- README.md: introduction, version/tag, status, dimensions/units/origin, source, required assembly notes and reverse-chronological changelog.
- images/three-view.png: same-version orthographic front/top/right views in one labeled sheet, in mm without perspective distortion.
- images/exploded.png: same-version exploded parts; explain when a single-part model requires no disassembly.
- Optional images/assembly.png for overall appearance.
- print/ for current print exports and plate projects.
- WIRING.md and ASSEMBLY.md as needed; additional documentation goes in docs/ and is linked from the project README. Do not create empty templates. Wiring must identify board revision, firmware pins, supply and markings; unverified items remain pending.

Shared assets use assets/<asset-id>/model.* and a README with source, dimensions and limitations. Fusion conversion and project-level orthographic views are not mandatory. Projects link to references instead of copying them; release tags freeze the whole repository, including dependencies.

The root README shows the overall introduction, each project's description/current version and latest orthographic views. Add a showcase entry for every new project. Reference <model-id>/images/three-view.png directly; state missing images instead of linking nonexistent files.

Temporary Fusion view/component-position changes may be used for screenshots; restore assembly positions afterward. Do not create a second master for screenshots or rename perspective images as orthographic views.

## 版本

每个模型独立编号，tag 为 `<model-id>/vX.Y.Z`。X 用于重大结构/配合变化，Y 用于兼容的功能或结构改进，Z 用于小修正；未发布改动记在“未发布”节。模型版本写在 README，文件名不带版本号。

旧外壳 L6、L7 保留，下一版可从 `fc-enclosure/v8.0.0` 开始；新模型项目从 v1.0.0 开始，assets 参考资源随提交追踪。单纯仓库整理不提高设计版本。不要把 Fusion 云端 V 数字当作 Git 发布版本；可在 README 附记 Fusion 文档链接/版本用于追溯。

标签是整个仓库提交的快照，模型前缀只是发布范围。一次改多个模型时分别检查、分别打 tag；永远不移动已发布标签。

### English

Each project has independent versions and tags named <model-id>/vX.Y.Z: X for major structural/mating changes, Y for compatible functionality or structural improvements, Z for small fixes. Keep unreleased changes under an Unreleased section. Put versions in README, not filenames.

Preserve L6/L7; the next enclosure release may start at fc-enclosure/v8.0.0. New projects begin at v1.0.0; assets follow Git commits. Repository-only cleanup does not bump geometry versions. Fusion cloud revision numbers are not Git release versions; a Fusion link/revision may be recorded for traceability.

Tags snapshot the entire repository; the prefix identifies release scope. Check and tag each project separately when several change. Never move published tags.

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

### English

1. Check git status and preserve existing work. When clean, run git pull --ff-only and git fetch --tags.
2. Open the sole master, confirm mm and the active component, save in Fusion, export temporarily under generated, then replace the fixed master file. Reimport it to verify that it opens with complete references and parts.
3. Check dimensions, interference, assembly paths and affected constraints. Printing additionally requires mesh/slicer checks. Record what was actually checked and explicitly state missing physical validation.
4. Capture same-version orthographic/exploded views at fixed paths. Update the project README, root showcase and affected wiring/assembly instructions. Use the exact Version and Tag fields shown above once, without translating or duplicating them.
5. Run python tools/check_models.py --release fc-enclosure. Manually check image/model consistency and README image links.
6. Stage the intended project files and root README, inspect staged changes, commit, create an annotated tag and push main and that specific tag using the commands above. Replace example versions with the actual new version. On a work branch, merge into main first and tag the correct release commit. Do not force-push or push unknown tags in bulk.
7. Optionally create a matching GitHub Release with the introduction, changes, validation status and print outputs. Specify whether multicolor 3MF is a generic model package or a configured printer/material project.

## 旧版本查看与恢复

`git fetch --tags` 后，可用 `git worktree add --detach ../fc-models-L6 L6` 单独查看旧版，不影响当前工作区。新规范版本同理使用其完整 tag。回退某个模型时只取回该目录，作为新提交记录，不重置其他模型、不移动旧标签。

历史入口：[L6](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L6)、[L7](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L7)、[整理前全部导出与脚本](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1)。已删除的脚本引用旧路径，应在历史 worktree 内使用；不要复制回当前目录而不修路径。

### English

After git fetch --tags, use git worktree add --detach ../fc-models-L6 L6 to inspect an old version independently. Use the full tag for newer releases. To restore one project, bring back only that directory as a new commit; do not reset other projects or move old tags.

Use the L6, L7 and pre-reorganization links above for original exports and scripts. Removed scripts refer to historical paths and should run inside a historical worktree; do not copy them into the current tree without fixing paths.

## 当前迁移例外

现有外壳 F3D 和预览图字节未变；缺 three-view.png。默认检查允许外壳历史三视图缺项，发布检查不豁免，并要求根 README 引用该项目三视图。C3 校准 STL 与 BH1750 STEP 是 assets 共享参考的正常格式，不适用项目发布检查。

### English

Existing enclosure F3D and previews are byte-identical to their earlier versions; three-view.png is missing. Default checks allow this historical exception. Release checks do not: the image must exist and the root README must reference it. C3 STL and BH1750 STEP are valid shared-reference formats under assets, outside project release checks.

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

### English

Every model project includes print/; shared reference boards under assets do not require it. The table above maps the paths to output descriptions, single-color STL in mm, STEP solids, generic 3MF, validation plate projects and production plate projects.

Each plate category has a README. If its project is not prepared, mark it pending and do not create empty files. A directory containing only notes is a plan, not a ready-to-print plate. One project may contain multiple plates; use stable printer subdirectories only when multiple printer variants are genuinely needed, never version directories.

Validation starts with a complete set to check dimensions, light aperture, USB, lid insertion, pivot and fasteners. Single-color trials may precede validation with final materials. After successful trials, production may use complete-set plates or separate part/material batches. Record pieces per plate and complete-set yields; do not promise a fixed capacity in advance.

Record target printer, usable/excluded areas, nozzle, materials/slots, layer height, supports, skirts/purge towers, print order, slicer version and estimated time/materials. Check boundaries, spacing and support/tower footprints; sequential printing requires toolhead-clearance checks. Record actual batch results separately.

When geometry changes, regenerate affected exports, update both plate categories and recheck. Remove stale outputs or explicitly mark them unusable for the current model; do not leave obsolete projects labeled usable. Formal outputs and the master share a commit/tag with fixed filenames. Release attachments may mirror these files but do not replace repository print/. Machine/material-specific G-code is not committed by default.

## 文档语言 / Documentation languages

主要 Markdown 默认中英双语，在同一文件内中文在前、英文紧随对应段落或小节。根展示页保持简洁；表格可使用双语单元格，图片无需重复。后续新增接线、装配和摆盘说明及更新日志，也同时维护两种语言。路径、命令、版本字段和尺寸只保留准确原值；不重复机器读取字段，不另存一套英文文件。原始日志、代码和上游原文可维持原语言。提交前检查中英文状态、数量和限制一致。

Major Markdown documents are bilingual by default, with Chinese followed by matching English paragraphs or sections in the same file. Keep the root showcase concise; use bilingual table cells and avoid repeating images. Maintain both languages for new wiring, assembly, plate instructions and changelogs. Preserve exact paths, commands, version fields and dimensions; do not duplicate machine-readable fields or create separate English copies. Raw logs, code and upstream documents may retain their original language. Check that status, quantities and limitations agree across languages before committing.
