# 模型仓库协作规则

适用于本仓库内所有目录；本机 Codex 与 Fusion 建模流程必须遵守。

1. 先读根 README、CONTRIBUTING 和目标模型 README，执行 git status，保留用户未提交工作。
2. 一个主题一个稳定目录 `models/<model-id>/`。同主题改版覆盖同名文件，不新建版本目录、final、backup、copy 或按日期命名的副本。
3. 每个目录只保留一个权威主模型：通常 model.f3d；含外部引用时使用自包含 model.f3z。组装、零件、装饰和视图留在这一个文档中，不额外另存“分体版 F3D”。
4. 旧模块 C3 的 model.stl、BH1750 的 model.step 是明确的迁移例外。未在 Fusion 打开并实际导出前不得伪称已有 F3D，不得只改扩展名。正式发布前完成转换，确认尺寸、实体/网格属性与引用后移除被替代的主文件。
5. README 记录简介、版本/tag、主文件、单位/原点/尺寸、来源和估算限制、实测状态、更新日志。避免再生成 HANDOFF、FILE_MAP、按版本说明等重复文档。
6. 每个新发布 tag 必须包含同版 images/three-view.png（正交正/俯/右三视图）及 images/exploded.png（装配分体图；单件允许部件展示并说明无可拆分件）。assembly.png 为可选外观图。图片来自真实 CAD，不能用 AI 概念图充当工程截图。
7. 先保存/导出本版主文件，再截同版图，更新 README、完成检查、commit，最后创建不可变 annotated tag：<model-id>/vX.Y.Z。不要移动、删除或覆盖已发布 tag。
8. 无真实 Fusion 环境或截图时如实标注缺项，可提交整理/草稿，但不能声称 CAD 复验或发布完成。旧 L6/L7 保持原样，不伪补历史截图。
9. 临时文件、截图草稿、STL/STEP/3MF 导出及日志放被忽略的 generated/，选定的发布附件上传对应 Release。禁止把完整旧版本搬进 archive 继续堆积。
10. 不删除 F3D 内隐藏参考/历史组件以追求文件精简；先验证建模依赖。不要重写仓库历史，不强推；一次提交聚焦一个模型，仓库整理可跨目录。
11. 外壳修改后复核采光孔、USB、PCB/焊线空间、支撑压条、插盖路径、转轴及螺丝。CAD、网格、切片、实物检查分别记录，未做就写未做。
12. 提交前运行 python tools/check_models.py；发布前运行 python tools/check_models.py --release <model-id>。此检查只验证文件组织和元数据，不代替 Fusion 几何检查或图像真实性审查。
