# FC 传感器外壳 / FC sensor enclosure

Version: L7
Tag: L7

ESP32-C3 SuperMini 与 BH1750 背靠背安装的显示器顶部折叠外壳。当前为 40 mm 加宽、内套圈定位、内部藏胶槽方案，黑绿主体配透明图案。

A folding monitor-top enclosure for back-to-back ESP32-C3 SuperMini and BH1750 modules. The current 40 mm-wide design uses an internal locating skirt and concealed glue grooves, with a black/green body and transparent graphics.

主模型：[model.f3d](model.f3d)。当前原生装配包含隐藏历史/参考组件，保留建模依赖；导出打印件时仅选本版底壳、上盖、折叠脚与前挡板。部分前挡板/图案组件沿用旧名称，不代表应打印所有隐藏旧件。

Master: [model.f3d](model.f3d). Hidden historical/reference components are retained to preserve modeling dependencies. Export only the current base, lid, folding leg and front stop for printing. Some reused stop/graphic components retain older names; this does not mean all hidden historical parts should be printed.

## 预览 / Previews

![装配外观 / Assembly](images/assembly.png)

![分体视图 / Exploded view](images/exploded.png)

**三视图待补**：现有图是透视装配/分体图，尚无正交三视图。下一次正式发布前在 Fusion 导出 images/three-view.png。

**Orthographic views are missing.** Existing images are perspective assembly/exploded views. Export images/three-view.png from Fusion before the next formal release.

## 参考资源与说明 / References and guides

- [ESP32-C3 SuperMini](../assets/esp32-c3-supermini/)：C3 板卡参考。
- [BH1750 / GY-302](../assets/bh1750-gy302/)：光照模块参考。
- [打印输出与摆盘](print/README.md)：当前 L7 的 STL、STEP、通用 3MF，以及验证/生产摆盘方案。
- [装配说明](ASSEMBLY.md)：尺寸、定位、转轴、胶接及打印摆放。
- 接线说明：尚未整理；需要时增加本目录 WIRING.md，并以实际固件引脚和模块丝印核对，不从几何模型推断线序。

References: [C3 board](../assets/esp32-c3-supermini/) and [BH1750 module](../assets/bh1750-gy302/). [Print outputs and plate plans](print/README.md) contain L7 STL, STEP and generic 3MF files. [Assembly instructions](ASSEMBLY.md) cover dimensions, locating features, pivot, bonding and print orientation. Wiring documentation is pending; add WIRING.md when needed after checking actual firmware pins and board markings, never by inferring connections from geometry.

F3D 已嵌入的参考组件保持不变。assets 为共享参考入口，不意味着本次已重新链接或更新 Fusion 内的组件。

Embedded F3D references are unchanged. The shared assets entry points do not imply that Fusion components were relinked or updated during reorganization.

## 验证状态 / Validation status

历史记录：静态与 PCB 干涉、分段插盖、0–90° 每 3° 转动采样、四件单色网格检查通过。不是对所有中间位置的连续验证。**L7 实物打印、套口、胶接、螺纹耐久仍待验证**。本次整理未重新运行 Fusion 或切片。

Historical records report successful static/PCB interference checks, sampled lid insertion, rotation checks at 3° intervals over 0–90°, and checks of four single-color meshes. These are not continuous checks of every intermediate position. **L7 printing, skirt fit, bonding and thread durability still require physical validation.** Fusion and slicing were not rerun during reorganization.

[原始检查、打印导出及脚本](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1/03_FC传感器外壳/当前版本_L7_加宽套口藏胶)。通用 3MF 不等同于已配置拓竹机型/AMS 的工程。

The linked historical directory above contains original checks, print exports and scripts. Generic 3MF files are not Bambu projects configured for a specific printer and AMS mapping.

## 更新日志 / Changelog

### 2026-10-31 — 打印输出归档
恢复同版 L7 零件导出至 print/，按格式归类；增加验证与生产摆盘方案。尚无实际切片摆盘工程，未重新生成或验证几何。

Print-output archiving: restored same-version L7 part exports under print/, grouped by format, and added validation/production plate plans. No actual slicer plate project exists yet; geometry was neither regenerated nor revalidated.

### 2026-10-31 — 项目与资源分离
项目移至根目录 fc-enclosure；参考模块统一移入 assets；装配说明独立到 ASSEMBLY.md。几何不变。

Project/resource separation: moved fc-enclosure to the repository root, references into assets, and assembly instructions into ASSEMBLY.md. Geometry is unchanged.

### 2026-10-31 — 仓库整理（几何不变）
统一 model.f3d 与固定预览路径，移除工作树中的版本副本和重复导出。保留 L6/L7 原 tag，不新建几何版号。

Repository cleanup: standardized model.f3d and preview paths; removed version copies and duplicate exports from the working tree. Original L6/L7 tags remain unchanged; no new geometry version was created.

### L7 — 2026-10-26
宽度 36→40；取消卡扣，改内套圈和隐藏胶槽；保留光孔/PCB位置、支撑压条、配色和螺丝有效跨度。实物待验证。[历史 tag](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L7)。

L7: width increased from 36 to 40 mm; clips replaced with an internal skirt and concealed glue grooves. Light-hole/PCB positions, supports, lid pressure rib, colors and effective screw span were preserved. Physical validation remains pending; see the historical tag linked above.

### L6 — 原型基线
单件平底、已有第一台实物原型反馈；[历史 tag](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L6)。历史图片和打印工程保留在该快照。

L6 prototype baseline: individual parts with flat bottoms and feedback from the first physical prototype. Images and print projects remain in the historical tag linked above.
