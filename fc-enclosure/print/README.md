# L7 打印输出 / L7 print outputs

Source-Version: L7

来源：整理前提交 bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1 的 L7 print-files；直接复用原文件，与当前 model.f3d 同属 L7。此次未重新导出、切片或实打。

Source: L7 print-files at pre-reorganization commit bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1. Original files are reused unchanged and correspond to the current L7 model.f3d. No new export, slicing or physical printing was performed.

| 零件 / Part | STL（单色） / STL (single color) | STEP | 通用 3MF / Generic 3MF |
|---|---|---|---|
| 底壳 / Base | [单色 / Single](stl/01_Base_single.stl) | [单色 / Single](step/01_Base_single.step) | [单色 / Single](3mf/01_Base_single.3mf) |
| 前挡板 / Front stop | [单色 / Single](stl/02_Front_hook_single.stl) | [单色 / Single](step/02_Front_hook_single.step) | [单色 / Single](3mf/02_Front_hook_single.3mf) |
| 折叠脚 / Folding leg | [单色 / Single](stl/03_H_leg_single.stl) | [单色 / Single](step/03_H_leg_single.step) / [分色 / Color](step/03_H_leg_color.step) | [单色 / Single](3mf/03_H_leg_single.3mf) / [分色 / Color](3mf/03_H_leg_color.3mf) |
| 上盖 / Lid | [单色 / Single](stl/04_Lid_single.stl) | [单色 / Single](step/04_Lid_single.step) / [分色 / Color](step/04_Lid_color.step) | [单色 / Single](3mf/04_Lid_single.3mf) / [分色 / Color](3mf/04_Lid_color.3mf) |

同一零件只选择一个格式和一种配色版本，不能重复导入。STL 按 mm；分色件作为同一对象的多个部件导入，保持相对位置。通用 3MF 未配置机型、喷嘴和 AMS，不是可直接打印的切片工程。

Choose one format and one color variant per part; do not import duplicates. STL units are mm. Import color-separated geometry as multiple parts of one object, preserving relative positions. Generic 3MF files lack printer, nozzle and AMS configuration and are not ready-to-print slicer projects.

## 摆盘 / Plate plans

- [验证试打](plates/validation/README.md)：一套零件，确认配合与工艺。
- [批量生产](plates/production/README.md)：试打合格后按机型、材料和产量排盘。

[Validation printing](plates/validation/README.md): one complete set to check fit and process. [Batch production](plates/production/README.md): arrange plates for the chosen printer, materials and volume after successful trials.

两类目前均为**方案说明，待制作 project.3mf**。缺少目标打印机、喷嘴和最终材料配置，未给出未经验证的套数或打印参数。历史 L6 拓竹工程不适用于 L7，不能搬来当本版摆盘。

Both are currently **plans only; project.3mf remains to be created**. The target printer, nozzle and final material setup are unknown, so no unverified set counts or settings are specified. Historical L6 Bambu projects must not be reused as L7 plate projects.

历史记录称四件单色 STL 的封闭性、法向及连通性检查通过；此次未复验。装配顺序和打印方向见[装配说明](../ASSEMBLY.md)。

Historical records report successful watertightness, normal and connectivity checks for four single-color STL parts; these were not rerun. See [assembly instructions](../ASSEMBLY.md) for assembly and print orientation.
