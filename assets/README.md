# 共享资源 / Shared resources

与各模型项目目录平级，存放可复用的模块/芯片参考模型；项目通过相对链接引用，避免各复制一套。这里的 C3、BH1750 是开发板/模块参考，不是裸芯片封装。

Shared module/chip references live alongside model project directories. Projects link to them rather than copying them. The C3 and BH1750 assets here represent development boards/modules, not bare IC packages.

| 参考资源 / Reference | 主文件 / Master | 用途 / Purpose |
|---|---|---|
| [ESP32-C3 SuperMini](esp32-c3-supermini/) | model.stl | 校准后的板卡装配占位 / Calibrated board fit reference |
| [BH1750 / GY-302](bh1750-gy302/) | model.step | 光照板装配占位 / Light-sensor board fit reference |

每个资源保留一个主文件及 README，记录尺寸、原点、来源、估算限制和变更。允许 STEP/STL 等上游原生参考格式，不必为资源目录强制制作 Fusion 文件或分体图。确需转换时核对尺寸、保留来源，不只改扩展名。

Keep one master file and a README per resource, documenting dimensions, origin, source, estimation limits and changes. Upstream formats such as STEP/STL are allowed; Fusion files and exploded views are not mandatory. If conversion is needed, verify dimensions and retain provenance rather than simply renaming the extension.

资源改动随 Git 提交留存；发布模型的 tag 同时冻结当时 assets 的状态。项目 README 需列出使用的资源和装配方向。参考资源如果改变配合尺寸，逐个检查引用它的项目；不自动替换已有 Fusion 文档的嵌入组件。

Resource changes are tracked in Git; a model release tag also freezes the corresponding assets. Each project README must identify its resources and assembly orientation. If a shared reference changes mating dimensions, check every affected project; do not automatically replace embedded components in existing Fusion documents.

接线、装配说明属于具体项目，放在该项目内；跨项目通用资料确有复用需求时再放 assets 并链接。打印临时导出不放这里。

Wiring and assembly instructions belong in the relevant project. Only genuinely reusable documentation should be placed in assets and linked by projects. Temporary print exports do not belong here.
