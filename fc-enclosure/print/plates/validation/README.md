# 验证试打摆盘 / Validation plate plan

状态：方案已记录；project.3mf 与摆盘截图待本机切片制作。当前目标版本 L7，未实打验证。

Status: plan recorded; project.3mf and plate screenshots await local slicer preparation. Target version: L7. No physical validation has been performed.

## 计划 / Plan

一套底壳、前挡板、折叠脚、上盖，各 1 件。初次单色试配合；多色生产前再用最终材料组合验证，不能只凭单色通过就放行多色。

One base, front stop, folding leg and lid. Start with a single-color fit trial, then validate the final material combination before multicolor production; a single-color pass alone does not qualify the multicolor process.

底壳与脚平底朝下，前挡板侧放，上盖外观面朝下套圈向上。具体支撑、桥接、附着和材料参数需在目标切片器确认；详见[装配说明](../../../ASSEMBLY.md)。

Base/leg flat-side down, front stop on its side, lid exterior-face down with skirt upward. Confirm supports, bridging, adhesion and material settings in the target slicer; see [assembly instructions](../../../ASSEMBLY.md).

验收：PCB及焊线空间、USB插拔、感光孔对准、上盖套口、压条、M3×30啮合、0–90°转动；先干配合，随后验证少量胶接。记录实际尺寸、问题及照片；未通过则修模型后重试。

Acceptance checks: PCB/wire clearance, USB insertion, sensor aperture alignment, lid skirt, pressure rib, M3×30 engagement and rotation over 0–90°. Dry-fit first, then test a small amount of adhesive. Record actual dimensions, issues and photos; revise and retest failed fits.

## 制作时填写 / Fields to complete

- 打印机/有效区域/禁区、喷嘴：待确认。
- 材料与颜色/材料槽、层高、支撑、打印顺序：待确认。
- 切片器与版本、工程文件：待制作，固定名称 project.3mf。
- 摆盘截图：待制作，固定名称 preview.png。
- 切片预估时间/耗材、试打日期与结果：未执行。

- Printer, usable area/exclusion zones and nozzle: pending.
- Material/color/slot mapping, layer height, supports and print order: pending.
- Slicer/version and project: pending; use fixed filename project.3mf.
- Plate screenshot: pending; use fixed filename preview.png.
- Estimated time/material usage, trial date and results: not yet recorded.

零件文件统一从[打印输出](../../README.md)导入，不在本目录复制一套 STL/STEP。

Import parts from [print outputs](../../README.md); do not duplicate STL/STEP files in this directory.
