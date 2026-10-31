# ESP32-C3 SuperMini

Version: legacy-reference
Tag: none

用于外壳装配占位的校准模块参考，唯一主文件为 [model.stl](model.stl)，导入单位 **mm**。目前没有独立 Fusion 原生特征模型；作为共享网格参考保留，不要求转换；不能把 STL 改名为 F3D。

A calibrated module reference for enclosure fit studies. The sole master is [model.stl](model.stl); import in **mm**. No independent native Fusion feature model is available. This shared mesh does not require conversion; renaming STL to F3D is not conversion.

PCB 22.5×17.8，含 USB 长 23.5；USB 参考外形 8.8×3.1；总包络约 23.5×17.8×4.1。板厚 1 mm 沿用源模型，非实测；小元件近似，不含焊点、飞线及组合后的绝缘层。保留模型现有坐标，原点定义尚待在 Fusion 核对。

PCB: 22.5×17.8; length including USB: 23.5; USB reference profile: 8.8×3.1; overall envelope: approximately 23.5×17.8×4.1 mm. The 1 mm PCB thickness is inherited, not measured. Small components are approximate; solder, wires and assembly insulation are excluded. Preserve existing coordinates; the origin definition still needs checking in Fusion.

来源：原记录为本机下载的 esp32c3supermini.stl，经尺寸校准。上游作者/授权未记录，不能据此宣称原创或已有再分发许可。源网格、校准脚本和参数可从[整理前目录](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1/01_ESP32-C3-SuperMini)追溯。

Source: a locally downloaded esp32c3supermini.stl, subsequently dimensionally calibrated. The upstream author/license was not recorded, so originality or redistribution permission cannot be assumed. The source mesh, calibration script and parameters remain in the linked pre-reorganization directory above.

## 预览与状态 / Preview and status

无现成截图；作为共享参考资源，不强制提供项目级三视图或分体图。需要时在 Fusion 导入核对并截图。不能声称网格转换后具有原生参数化特征。

No screenshot is currently available. Shared references do not require project-level orthographic or exploded views; import, inspect and capture them in Fusion when needed. Mesh conversion must not be described as restoring native parametric features.

历史校准记录标注网格封闭、3400 面；此次仅移动同一 blob，没有重新验证尺寸或网格。未发布独立 tag。

Historical calibration records report a watertight mesh with 3400 faces. Reorganization reused the same blob without rechecking geometry or dimensions. No separate tag has been published.

## 更新日志 / Changelog

### 2026-10-31 — 共享资源归类
移入根目录 assets，供模型项目链接复用；主模型字节不变。

Shared-resource classification: moved into root-level assets for reuse by model projects. Master file bytes are unchanged.

### 2026-10-31 — 整理
只保留校准后的主模型，原始下载网格/脚本转由 Git 历史追溯。几何不变。

Cleanup: retain only the calibrated master; original downloads and scripts remain accessible through Git history. Geometry is unchanged.
