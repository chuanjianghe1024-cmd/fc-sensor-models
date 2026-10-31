# Fusion 与 Git 提交规范

## 最小目录

每个主题目录为 `models/<model-id>/`，只需：

- `model.f3d`：一个 Fusion 文档，包含全部零件和装配。外部引用需完整打包时改用唯一的 `model.f3z`。
- `README.md`：简介、版本/tag、状态、尺寸/单位/原点、来源、必要装配说明及倒序更新日志。
- `images/three-view.png`：同版正交正视、俯视、右视合成一张，标清方向；毫米制，避免透视畸变。
- `images/exploded.png`：同版分体展示，零件清楚可辨；单件模型写明无需拆分。
- 可选 `images/assembly.png`：整体外观。

三视图和分体图可在 Fusion 临时改变视图/零件位置后截图，截图后恢复装配；不为截图另存一份权威主模型。不得用透视外观图改名冒充三视图。

## 版本

每个模型独立编号，tag 为 `<model-id>/vX.Y.Z`。X 用于重大结构/配合变化，Y 用于兼容的功能或结构改进，Z 用于小修正；未发布改动记在“未发布”节。模型版本写在 README，文件名不带版本号。

旧外壳 L6、L7 保留，下一版可从 `fc-enclosure/v8.0.0` 开始；两个参考模块完成首个规范发布后从 v1.0.0 开始。单纯仓库整理不提高设计版本。不要把 Fusion 云端 V 数字当作 Git 发布版本；可在 README 附记 Fusion 文档链接/版本用于追溯。

标签是整个仓库提交的快照，模型前缀只是发布范围。一次改多个模型时分别检查、分别打 tag；永远不移动已发布标签。

## 本机流程

1. `git status` 确认工作区；有自己的未提交改动先妥善提交/保存，不覆盖。干净时执行 `git pull --ff-only` 和 `git fetch --tags`。
2. 打开目标目录唯一主模型，确认 mm 和当前组件。保存 Fusion 文档后，导出到 generated 临时位置，再替换目标同名文件。重新导入导出文件，确认文档可打开、引用完整、零件齐全。
3. 检查尺寸、干涉、装配路径和修改相关约束；打印用途另检网格及切片。记录实际完成项，实物未验证必须明说。
4. 导出本版三视图与分体图到固定图片路径，更新 README。新发布的 README 必须含下列独立行（以外壳下一版为例）：

   `Version: v8.0.0`
   
   `Tag: fc-enclosure/v8.0.0`

5. 执行 `python tools/check_models.py --release fc-enclosure`。人工检查图像与模型一致，README 图片链接有效。
6. 明确暂存目标文件并检查差异：
   ```sh
   git add models/fc-enclosure
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

L6/L7 的旧目录及全部导出可从根 README 历史链接取回。已删除的脚本引用旧路径，应在历史 worktree 内使用；不要复制回当前目录而不修路径。

## 当前迁移例外

现有外壳 F3D 和预览图字节未变；缺 three-view.png。C3 只有校准 STL，无预览；BH1750 只有 STEP 和外观预览。默认检查允许这三个已知旧资产缺项，但发布检查不豁免。必须在本机 Fusion 补齐真实资产后才能发新规范 tag。
