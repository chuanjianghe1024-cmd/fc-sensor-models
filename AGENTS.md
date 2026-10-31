# 模型仓库协作规则 / Repository collaboration rules

适用于本仓库内所有目录；本机 Codex 与 Fusion 建模流程必须遵守。

Applies throughout this repository; local Codex and Fusion workflows must follow these rules.

1. 先读根 README、CONTRIBUTING 和目标模型 README，执行 git status，保留用户未提交工作。

   Read the root README, CONTRIBUTING and target project README first. Run git status and preserve uncommitted user work.

2. 一个主题一个稳定目录，位于根目录 `<model-id>/`，与 `assets/` 平级。同主题改版覆盖同名文件，不新建版本目录、final、backup、copy 或按日期命名的副本。

   Use one stable root-level <model-id>/ directory per topic, alongside assets/. Update fixed filenames; do not create version directories or final/backup/copy/date-suffixed duplicates.

3. 每个目录只保留一个权威主模型：通常 model.f3d；含外部引用时使用自包含 model.f3z。组装、零件、装饰和视图留在这一个文档中，不额外另存“分体版 F3D”。

   Keep one authoritative master per project: normally model.f3d, or a self-contained model.f3z for external references. Keep assemblies, parts, decoration and views in that document; do not create a separate exploded-view F3D master.

4. 共享参考模型统一放 assets/<asset-id>/，C3 与 BH1750 不再算独立模型项目。参考资源允许一个 STEP/STL/F3D/F3Z 主文件及来源说明；项目链接复用，不复制目录。Fusion 自包含文档中嵌入参考组件可以保留。共享资源变化后检查受影响项目，不擅自更新嵌入组件。

   Shared references belong in assets/<asset-id>/. C3 and BH1750 are resources, not separate projects. Allow one STEP/STL/F3D/F3Z master with provenance; link rather than copy resource directories. Embedded references in self-contained Fusion documents may remain. Check affected projects after resource changes; do not silently replace embedded components.

5. README 记录简介、版本/tag、主文件、单位/原点/尺寸、来源和估算限制、实测状态、更新日志。避免再生成 HANDOFF、FILE_MAP、按版本说明等重复文档。

   The project README records its introduction, version/tag, master, units/origin/dimensions, sources, estimation limits, measured status and changelog. Avoid duplicate HANDOFF, FILE_MAP or per-version documents.

6. 每个新发布 tag 必须包含同版 images/three-view.png（正交正/俯/右三视图）及 images/exploded.png（装配分体图；单件允许部件展示并说明无可拆分件）。assembly.png 为可选外观图。图片来自真实 CAD，不能用 AI 概念图充当工程截图。

   Each new release tag must include same-version images/three-view.png (orthographic front/top/right) and images/exploded.png (exploded assembly; a single part may use a component view with an explanation). assembly.png is optional. Capture real CAD, never AI concepts presented as engineering screenshots.

7. 先保存/导出本版主文件，再截同版图，更新 README、完成检查、commit，最后创建不可变 annotated tag：<model-id>/vX.Y.Z。不要移动、删除或覆盖已发布 tag。

   Save/export the master, capture matching views, update the README, check and commit, then create an immutable annotated tag: <model-id>/vX.Y.Z. Never move, delete or overwrite published tags.

8. 无真实 Fusion 环境或截图时如实标注缺项，可提交整理/草稿，但不能声称 CAD 复验或发布完成。旧 L6/L7 保持原样，不伪补历史截图。

   When Fusion or real screenshots are unavailable, state missing items. Cleanup/draft commits are allowed, but do not claim CAD revalidation or a completed release. Preserve historical L6/L7 tags and do not fabricate historical screenshots.

9. 每个模型项目维护 print/ 打印输出目录：stl/、step/、3mf/ 保存当前版本选定的导出；plates/validation/ 保存验证试打摆盘，plates/production/ 保存批量生产摆盘。文件名不带版本号，与主模型同步覆盖并随 tag 留存；临时导出和日志仍放 generated/。禁止把旧版本搬进 archive 堆积。

   Each project maintains print/: stl/, step/ and 3mf/ contain selected current exports; plates/validation/ contains trial plates and plates/production/ contains production plates. Use fixed filenames, update with the master and preserve versions through tags. Temporary exports/logs remain in generated/. Do not accumulate old versions under archive.

10. 不删除 F3D 内隐藏参考/历史组件以追求文件精简；先验证建模依赖。不要重写仓库历史，不强推；一次提交聚焦一个模型，仓库整理可跨目录。

   Do not delete hidden historical/reference components merely to shrink F3D files; verify dependencies first. Do not rewrite history or force-push. Focus each commit on one model, except repository-wide organization changes.

11. 外壳修改后复核采光孔、USB、PCB/焊线空间、支撑压条、插盖路径、转轴及螺丝。CAD、网格、切片、实物检查分别记录，未做就写未做。

   After enclosure changes, recheck the light aperture, USB, PCB/wire clearances, supports/pressure rib, lid insertion, pivot and screws. Record CAD, mesh, slicing and physical checks separately; explicitly identify checks not performed.

12. 提交前运行 python tools/check_models.py；发布前运行 python tools/check_models.py --release <model-id>。此检查只验证文件组织和元数据，不代替 Fusion 几何检查或图像真实性审查。

   Run python tools/check_models.py before committing and python tools/check_models.py --release <model-id> before releasing. These check organization and metadata only, not Fusion geometry or screenshot authenticity.


13. 每个项目按需增加 WIRING.md（接线）和 ASSEMBLY.md（装配），也可在 docs/ 增加必要说明及配图，并由项目 README 链接。无内容就不创建空模板。接线必须核对固件、板卡版本和丝印，不从 CAD 推断。

   Add WIRING.md and ASSEMBLY.md when needed, or necessary documentation/images under docs/, linked from the project README. Do not create empty templates. Verify wiring against firmware, board revision and silkscreen; never infer it from CAD.

14. 根 README 只作项目展示页：总体简介、每个项目的简介/当前版本和最新真实三视图，链接到项目详情。共享资源只提供入口，不与实际项目混列。补齐或更新项目 three-view.png 时，同一提交同步根 README 图片引用；缺图明确标注，不制造断链或拿透视图替代。

   The root README is a showcase: overall introduction, each project's description/current version and latest real orthographic views, linking to project details. Link shared resources separately. Whenever three-view.png is added/updated, update its root README reference in the same commit. State missing images explicitly; do not use broken links or perspective substitutes.


15. print/README.md 必须说明源模型版本、格式/单色/多色用途和验证状态。两类摆盘各有 README，实际工程使用固定 project.3mf（多机型时用机型子目录），可附 preview.png。记录机型、有效打印区域、喷嘴、材料、层高、零件数量/套数、支撑与打印顺序、切片软件版本、耗时耗材及验证结果。未确定设备和未切片时只保留方案说明，不伪造工程或把通用 3MF 称作切片工程。生产盘必须经过试打确认，不能以最大塞满数量代替工艺验证。

   print/README.md must identify the source model version, formats, single/multicolor use and validation status. Each plate category has its own README; actual projects use project.3mf, with printer-specific subdirectories only when needed, and optional preview.png. Record printer, usable area, nozzle, materials, layer height, part/set counts, supports, print order, slicer version, time/material usage and results. Without equipment selection and slicing, keep plans only; never mislabel generic 3MF as a slicer project. Production plates require trial validation, not merely maximum packing.


16. 主要 Markdown 在同一文件内维护中英双语，中文在前，紧随对应英文段落或小节；简介、操作说明、更新日志和待验证状态同步更新。路径、命令、Version/Tag/Source-Version 字段及数值保持一致，不重复机器读取字段、不另建 .en.md 副本。代码、原始日志和上游原文可保留原语言。

   Maintain major Markdown documents in Chinese and English within the same file, Chinese first with corresponding English paragraphs or sections. Update both languages together, including introductions, instructions, changelogs and pending-validation status. Preserve paths, commands, Version/Tag/Source-Version fields and exact numeric values; do not duplicate machine-readable fields or create parallel .en.md copies. Code, raw logs and upstream documents may retain their original language.

