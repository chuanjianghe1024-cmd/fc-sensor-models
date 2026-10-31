# FC Sensor Models

一个模型一个目录，只保留当前主模型。历史版本通过 Git tag 查看，不在主分支堆放 L6/L7、备份或导出副本。

| 模型 | 当前版本 | 主文件 | 状态 |
|---|---|---|---|
| [FC 传感器外壳](models/fc-enclosure/) | L7（历史标签） | model.f3d | CAD 检查已有记录，实物待验证 |
| [ESP32-C3 SuperMini](models/esp32-c3-supermini/) | 参考模型，未独立发布 | model.stl | 旧资产迁移；待 Fusion 原生化及三视图 |
| [BH1750 / GY-302](models/bh1750-gy302/) | 参考模型，未独立发布 | model.step | 旧资产迁移；待 Fusion 原生化及三视图 |

![FC 外壳装配](models/fc-enclosure/images/assembly.png)

## 打开与修改

进入模型目录，读 README，打开唯一的主文件。新建/后续正式发布的 Fusion 模型统一为 `model.f3d`，零件、装配和分体视图放在同一 Fusion 文档内。原生存在外部引用时使用完整 `model.f3z` 作为唯一主文件，不能只提交缺少引用的 F3D。

每次覆盖同名主文件，更新 README 的简介、版本、验证状态、更新日志及图片，然后 commit；正式版本打 `<模型目录名>/v<主版本>.<次版本>.<修订号>` 标签。例如下一次外壳设计发布可用 `fc-enclosure/v8.0.0`。

本机 Codex 先读 [AGENTS.md](AGENTS.md)，操作步骤和发布检查见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 历史与迁移

- [L6 原型](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L6)：已保留的历史 tag。
- [L7 设计](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/L7)：已保留的历史 tag。
- [整理前完整目录](https://github.com/chuanjianghe1024-cmd/fc-sensor-models/tree/bd3a33ef6047b93d584d7ea6c29092cb1b13ddc1)：全部导出、照片、校准数据、重建脚本及检查报告。

2026-10-31 仅整理目录与规范，主模型和保留图片直接复用原 Git blob，几何未改，不新增设计版本、不移动旧标签。旧标签仍显示旧目录，这是历史快照的正常行为。Git tag 标记整个提交，名称前缀表示这次发布哪个模型，并不是目录独立拥有 Git 历史。

当前缺少真实三视图，C3 也没有现成预览，均如实记在对应 README。未补齐前不发布符合新规范的新 tag。历史版本不追补伪造截图。

打印时从主模型按需导出到本地 `generated/`；需要分发的 STEP/STL/3MF 放对应 GitHub Release 附件，不在主分支持续堆放。旧打印文件仍可从上述历史入口下载。
