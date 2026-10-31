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

本项目原创内容采用 [个人非商业使用许可 1.0](LICENSE)，仅供自然人个人非商业自用，可学习、修改和自制；不允许商业项目集成、企业业务或客户用途、收费服务，以及软件、固件、模型或打印成品销售。独立再分发也不获授权；向官方贡献的有限 fork/PR 例外见许可。其他用途须取得相关权利人书面授权。第三方及历史授权保持有效；这是源码/设计公开的受限许可，不是 OSI 开源许可。

Original project material uses the [Personal Noncommercial Use License 1.0](LICENSE), solely for an individual's own noncommercial use, study, modification and DIY fabrication. Commercial integration, business/customer use, paid services and sales of software, firmware, models or printed products are not permitted. Independent redistribution is not granted; see the limited upstream fork/PR contribution exception. Other uses require written permission from the relevant rightsholders. Third-party and earlier grants remain effective. This is a restricted source/design-available license, not an OSI open-source license.

模型许可包含个人自用打印，禁止销售外壳、套件或其他衍生成品。生产摆盘资料不授予商业生产权。assets/esp32-c3-supermini 的上游授权未记录，该参考模型及其嵌入部分不由本许可补授权；使用或再分发前须另行核实。

Personal DIY printing is covered; enclosure, kit and derivative-product sales are prohibited. Production plate documentation does not grant commercial manufacturing rights. Upstream permission for assets/esp32-c3-supermini is unrecorded; this license does not supply permission for that reference or embedded copies. Verify rights separately before use or redistribution.
