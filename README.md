# FC Sensor Models

适用于 ESP32-C3 SuperMini 与 BH1750 光照模块的 3D 打印外壳和机械参考模型。

外壳采用可折叠显示器支架、USB-C 开口及对准光敏芯片的采光孔。L7 使用内套口定位和隐藏胶槽，配合一颗 M3×30 螺丝连接折叠脚。

![L7 外壳](03_FC传感器外壳/当前版本_L7_加宽套口藏胶/L7-closed.png)

## 功能

- 背靠背安装 C3 与 BH1750，四角支撑和盖内压条固定电路板。
- 折叠脚支持 0–90° 调节，预留走线开口和双面胶凹槽。
- 黑色主体、绿色装饰及齐平的透明 FC 字母与光波图案。
- 提供 Fusion 原生模型、STEP、STL 和通用 3MF。

## 快速开始

1. 编辑模型：在 Autodesk Fusion 打开 [L7 装配](03_FC传感器外壳/当前版本_L7_加宽套口藏胶/FCS-L7-hidden-glue-assembly.f3d)。
2. 准备打印：使用 [L7 print-files](03_FC传感器外壳/当前版本_L7_加宽套口藏胶/print-files)，每个零件选择单色或分色版本之一，导入单位为 mm。
3. 按 [L7 打印与装配说明](03_FC传感器外壳/当前版本_L7_加宽套口藏胶/README.md) 检查摆放、桥接和材料映射，先干装再胶接。

## 目录

| 内容 | 入口 |
|---|---|
| C3 模块参考 | [ESP32-C3 SuperMini](01_ESP32-C3-SuperMini/README.md) |
| 光照模块参考 | [BH1750 / GY-302](02_BH1750-GY302光照模块/README.md) |
| L6 原型版 | [L6](03_FC传感器外壳/当前版本_L6_单件平底/README.md) |
| L7 套口胶接版 | [L7](03_FC传感器外壳/当前版本_L7_加宽套口藏胶/README.md) |
| 结构设计 | [设计说明](docs/DESIGN.md) |
| 文件格式与用途 | [文件导航](docs/FILE_MAP.md) |
| 修改与验证 | [开发指南](CONTRIBUTING.md) |

## 状态

L6 已制作原型。L7 已完成 CAD 干涉检查和网格检查，套口配合、胶接效果及打印工艺仍待实物验证。模块上的部分小元件和孔位采用近似模型，不能替代装配测量。

本外壳面向成品模块组合；[FC PCB Designs](https://github.com/chuanjianghe1024-cmd/fc-pcb-designs) 中的定制 RevC 板具有不同尺寸和接口布局。
