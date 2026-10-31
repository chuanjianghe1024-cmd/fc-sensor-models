# 批量生产摆盘 / Production plate plan

状态：方案已记录；未具备生产放行条件。当前目标版本 L7；验证试打尚未通过，project.3mf 和实际每盘数量待确定。

Status: plan recorded, not released for production. Target version: L7. Validation trials have not passed; project.3mf and actual quantities per plate remain undetermined.

## 计划 / Plan

在[验证试打](../validation/README.md)确认配合与最终材料后，选择：

After [validation trials](../validation/README.md) confirm fit and final materials, choose:

- 整套生产：每套底壳、前挡板、折叠脚、上盖各 1 件，记录每盘 N 套。
- 分件/分材料生产：同类件集中排盘，降低不必要的换色；记录各盘件数、需打印盘数及最终可配齐套数。多材料部件保持坐标关系。

- Complete sets: one base, front stop, folding leg and lid per set; record N sets per plate.
- Separate part/material batches: group similar parts to reduce unnecessary color changes. Record pieces per plate, required plate runs and the number of complete sets they yield. Preserve relative coordinates within multimaterial parts.

优先稳定成品率，不盲目塞满。按目标设备检查有效区域/禁区、零件间距、裙边/支撑/擦料塔占位；逐件打印需验证打印头与已完成零件不碰撞。切片预览和首批实际结果均需记录。

Prioritize repeatable yield rather than maximum packing. Check usable area/exclusion zones, spacing, skirts, supports and purge-tower footprints on the target printer. Sequential printing requires toolhead clearance checks against completed objects. Record slicer previews and actual first-batch results.

## 制作时填写 / Fields to complete

- 打印机、喷嘴、材料/材料槽、层高、支撑、打印顺序：待确认。
- 生产方式、各盘零件数量、配套套数：待确定，不预设固定套数。
- 切片器版本、project.3mf、preview.png：待制作。
- 预计每盘时间/耗材、单套耗材及实际良率：待测。
- 验证试打依据、首批日期/数量/问题、生产是否放行：未放行。

- Printer, nozzle, material/slot mapping, layer height, supports and print order: pending.
- Production strategy, quantities per plate and complete-set count: pending; no fixed capacity assumed.
- Slicer version, project.3mf and preview.png: pending.
- Estimated plate time/material, material per set and measured yield: pending.
- Validation evidence, first-batch date/count/issues and production approval: not approved.

每次改几何或关键工艺重新评估。源零件见[打印输出](../../README.md)，不另存带版本号的副本。

Reassess after geometry or key process changes. Source parts are in [print outputs](../../README.md); do not create version-suffixed copies.
