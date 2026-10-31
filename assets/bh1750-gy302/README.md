# BH1750 / GY-302 V322

Version: legacy-reference
Tag: none

用于 FC 外壳装配占位的光照模块参考。唯一主文件 [model.step](model.step)，单位 **mm**。尚无独立 Fusion 原生文件，作为共享实体参考保留 STEP。

An ambient-light module reference for FC enclosure fit studies. The sole master is [model.step](model.step), in **mm**. There is no independent native Fusion file; STEP is retained as the shared solid reference.

![模块外观 / Module appearance](images/assembly.png)

## 尺寸与来源 / Dimensions and provenance

用户实测 PCB 18.5×14.2，厚 1.1，含元件总厚 2.0。元件面照片左下角为原点，X 沿宽度、Y 指向五孔排、Z 指向元件。孔径/孔位/小元件尺寸依据照片估算，不可当作加工级数据；不含排针、焊点和飞线。

User measurements: PCB 18.5×14.2, thickness 1.1, total component-side thickness 2.0 mm. Origin: bottom-left of the component-side photo; X follows width, Y points toward the five-hole row, Z toward components. Hole sizes/positions and small components are photo estimates, not machining-grade data. Headers, solder and wires are excluded.

模型由旧建模脚本按实测包络及照片构建；原参数、脚本、实物照片保留在[整理前目录](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1/02_BH1750-GY302光照模块)。装配时不随意镜像或改变原点。

The original script built this model from measured envelopes and photographs. Original parameters, scripts and photographs remain in the linked pre-reorganization directory above. Do not arbitrarily mirror the model or change its origin during assembly.

## 验证与待补 / Validation and pending items

历史参数记录 STEP 往返校验通过，包络 14.2×18.5×2.0，55 个组件；本次未重跑。当前预览非三视图。作为共享参考资源，不强制转换 F3D 或补齐项目级三视图/分体图；项目使用前仍需核对尺寸与方向。

Historical records report a successful STEP round-trip check, an envelope of 14.2×18.5×2.0 mm and 55 components; these checks were not rerun. The current preview is not an orthographic sheet. Shared references do not require F3D conversion or project-level orthographic/exploded views, but dimensions and orientation must still be checked before use.

## 更新日志 / Changelog

### 2026-10-31 — 共享资源归类
移入根目录 assets，供模型项目链接复用；主模型字节不变。

Shared-resource classification: moved into root-level assets for reuse by model projects. Master file bytes are unchanged.

### 2026-10-31 — 整理
保留一个 STEP 主模型及一张外观图；其余资料从 Git 历史追溯，几何不变。未发布独立 tag。

Cleanup: retain one STEP master and one appearance preview. Other records remain in Git history; geometry is unchanged. No separate tag has been published.
