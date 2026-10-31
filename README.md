# FluentControl Companion Hardware Models

[FluentControl（FC）](https://github.com/chuanjianghe1024-cmd/FluentControl) 的官方配套硬件模型项目：提供环境光传感器外壳、安装结构、3D 打印文件和装配指南。FC 负责桌面控制，FCS 负责设备接入与固件，本仓库负责机械结构。每个项目保留一个当前主模型，历史版本通过 Git tag 查看。

Official companion hardware models for [FluentControl (FC)](https://github.com/chuanjianghe1024-cmd/FluentControl): ambient-light sensor enclosures, mounting structures, 3D print files and assembly guides. FC handles desktop controls, FCS handles device integration and firmware, and this repository handles mechanical designs. Each project keeps one current master; previous versions are available through Git tags.

[FC 桌面端 / Desktop app](https://github.com/chuanjianghe1024-cmd/FluentControl) · [公开设备接入说明 / Public device guide](https://github.com/chuanjianghe1024-cmd/FluentControl/blob/main/docs/device-signals.md) · [FCS 固件与设备协议 / Firmware and device protocols](https://github.com/chuanjianghe1024-cmd/FluentControl-Sensors)（私有，需授权 / private, access required）

## [FC 传感器外壳 / FC sensor enclosure · L7](fc-enclosure/)

适配 ESP32-C3 SuperMini 与 BH1750 的显示器顶部折叠外壳。40 mm 宽，内套圈定位与隐藏胶槽，保留黑绿配色、透明图案和单颗 M3×30 转轴。

A folding monitor-top enclosure for ESP32-C3 SuperMini and BH1750 modules. The 40 mm-wide design uses an internal locating skirt and concealed glue grooves, with black/green styling, transparent graphics and a single M3×30 pivot screw.

**最新三视图：待从 Fusion 导出。** 当前已有装配与分体预览，见[项目说明](fc-enclosure/)。CAD 检查已有记录，实物配合仍待验证。

**Latest orthographic views: awaiting export from Fusion.** Assembly and exploded previews are available in the [project documentation](fc-enclosure/). CAD checks have been recorded; physical fit still needs validation.

---

[共享参考资源](assets/) · [提交规范](CONTRIBUTING.md)

[Shared references](assets/) · [Contribution guide](CONTRIBUTING.md)

## 使用许可 / Usage license

当前采用 [PolyForm Noncommercial 1.0.0](LICENSE)，允许许可定义范围内的非商业使用、修改和分发，包括条款列明的教育、科研、慈善等机构用途；不限于个人自用。不授予一般商业用途，其他用途需相关权利人另行授权。分发须遵守许可及声明保留要求。第三方内容和此前合法取得的授权保持有效。这是源码/设计可见的非商业许可，不是 OSI 开源许可；摘要不增加或替代 LICENSE 的条款。

The current license is [PolyForm Noncommercial 1.0.0](LICENSE). It permits noncommercial use, modification and distribution as defined by the license, including the listed educational, research and charitable organization uses; it is not limited to personal use. General commercial use is not granted; other uses require separate permission from the relevant rightsholders. Follow the license and notice requirements when distributing. Third-party terms and previously lawfully obtained grants remain effective. This is a source/design-available noncommercial license, not an OSI open-source license; this summary does not add to or replace LICENSE.

本许可用于本项目有权授权的原创设计文件、脚本和文档。模型下载包应附同版 LICENSE 及第三方声明。PolyForm 面向软件起草，此采用不承诺覆盖所有实体制造、外观设计或专利权；生产摆盘不是另行商业生产授权。assets/esp32-c3-supermini 的上游授权未记录，该参考及其嵌入部分不由本许可补授权，使用或分发前须另行核实。历史标签保持原样。

These terms apply to original design files, scripts and documentation the project is entitled to license. Include the matching LICENSE and third-party notices in model bundles. PolyForm was drafted for software; adoption does not claim to cover all physical manufacturing, design or patent rights. Production plates are not separate commercial manufacturing permission. Upstream permission for assets/esp32-c3-supermini is unrecorded; this license does not supply permission for that reference or embedded copies. Verify rights separately before use or distribution. Historical tags remain unchanged.
