# 2026年全国大学生嵌入式芯片与系统设计竞赛 - 芯片应用赛道总结报告

## 概述
本报告总结了2026年全国大学生嵌入式芯片与系统设计竞赛（芯片应用赛道）13家芯片厂商的硬件平台和规格。旨在帮助产品和项目经理快速评估各选项的能力。

## 1. 功能对比表

| 厂商 | 平台 | 处理器 / 核心 | AI / NPU 性能 | 内存 / 存储 | 多媒体 / 视频 | 关键特性 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **乐鑫 (Espressif)** | **ESP32-P4** | 双核 RISC-V @ 400MHz | AI指令扩展 (FPU) | 768KB SRAM + PSRAM | H.264, MIPI-CSI/DSI | 高性能MCU, 安全 |
| | **ESP32-S3** | 双核 Xtensa LX7 @ 240MHz | 向量指令 | 512KB SRAM + Octal SPI | LCD, 摄像头接口 | 集成 Wi-Fi/BT |
| **地瓜机器人 (Horizon)** | **RDK S100** | S100 SoC | **80 - 128 TOPS** | 外置 | 高性能 | 具身智能 |
| | **RDK X5** | 旭日 5 (Sunrise 5) | 10 TOPS | 外置 | - | 机器人 VSLAM, 深度 |
| | **RDK X3** | 旭日 3 (Sunrise 3) | 5 TOPS | 外置 | 4K@60 H.264/265 | 高性价比机器人套件 |
| **广和通 (Fibocom)** | **SC171** | 8核 ARM v8 Cortex @ 2.7GHz | 13 TOPS (综合) | 外置 | MIPI, HDMI | 5G, Android/Ubuntu |
| | **L610** | LTE Cat 1 模组 | - | - | - | 低速物联网 |
| **意法半导体 (STMicro)** | **STM32N6** | Cortex-M 系列 | **集成 NPU** | - | 摄像头/显示 | 首款带NPU的STM32 |
| | **Stellar** | ARM Cortex-R52 | - | - | - | 车规级网关 |
| | **STM32H7** | Cortex-M7 (+M4) | - | 内部 SRAM/Flash | - | 高性能 MCU |
| **沁恒 (WCH)** | **CH32H417** | 双核 RISC-V (青稞) | - | - | - | USB 3.0, 千兆以太网 |
| | **CH585** | RISC-V | - | - | - | BLE 5.4, NFC, USB |
| **海思 (HiSilicon)** | **SS928** | 四核 Cortex-A55 @ 1.4GHz | 10 TOPS INT8 | 外置 | 8K 编解码 | 智能摄像机/IPC |
| | **WS63** | 32位 RISC-V | - | - | - | 星闪 (SLE), Wi-Fi 6 |
| **瑞芯微 (Rockchip)** | **RK3588** | 4xA76 + 4xA55 (8nm) | 6 TOPS | 外置 | **8K 视频** | 旗舰性能 |
| | **RV1126B** | 四核 Cortex-A53 @ 1.6GHz | 3 TOPS | 外置 | MIPI CSI/DSI | 视觉 AI |
| **瑞萨 (Renesas)** | **RZ/V2H** | A55 + R8 + M33 | 8 TOPS (DRP-AI3) | 外置 | - | 异构, 低功耗 |
| | **RA8D1** | Cortex-M85 @ 480MHz | Helium 向量扩展 | 1MB SRAM | LCD | 最高性能 Cortex-M |
| **睿赛德 (RT-Thread)** | **K230 套件** | 双核 RISC-V (C908) | KPU (AI) | - | - | 实时AI, 混合OS |
| **移远 (Quectel)** | **QSM368ZP** | Rockchip RK3568 (四核 A55) | 1 TOPS | 外置 | 4K 解码 | 智能模组 |
| **英飞凌 (Infineon)** | **PSoC Edge** | Cortex-M55 + M33 | Ethos-U55 (0.1T) | SRAM + RAM | - | Helium DSP, 低功耗AI |
| | **XMC7000** | Cortex-M7 | - | - | - | 工业控制 |
| **龙芯 (Loongson)** | **LS2K3000** | **8核** LA364E | GPGPU (AI) | 外置 | - | 自主架构 |
| | **LS2K0300** | 单核 LA264 @ 1GHz | - | 16位 DDR4 | - | 低功耗 (<3W) |

## 2. 厂商详细规格

### 乐鑫科技 (Espressif) - ESP32-P4 / S3
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 嵌入式边缘 AI 应用 (本地数据采集/推理)
*   **选题二**: 高性能图形人机交互系统 (HMI, 多媒体)
*   **选题三**: 电机驱动与运动控制 (机械臂, 无人机)
*   **选题四**: 无线协议与网络应用 (Mesh, 网关, 感知)
*   **选题五**: 智能交互驱动的 AIoT 应用系统 (多模态)
*   **选题六**: 自主命题 (基于 P4/S3)

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: AIoT, 边缘AI, HMI, 智能家居
*   **详细规格**:
    *   **处理能力**:
        *   **ESP32-P4**: 高性能双核 RISC-V (400MHz)，带AI指令扩展和FPU。
        *   **ESP32-S3**: 双核 Xtensa LX7 (240MHz)，带AI向量指令。
    *   **内存**:
        *   **P4**: 768KB HP SRAM, 8KB TCM, 支持外置 PSRAM/Flash。
        *   **S3**: 512KB 内部 SRAM, Octal SPI 接口支持 Flash/PSRAM。
    *   **视频/显示**:
        *   **P4**: 支持 H.264 编码, MIPI-CSI (摄像头) / MIPI-DSI (显示), LCD 接口。
        *   **S3**: LCD 接口 (RGB/8080/6800), 摄像头接口。
    *   **连接性**:
        *   **P4**: 需要外接 Wi-Fi/BT 模组 (如 C6)。集成 USB 2.0 高速, 以太网 MAC (通常)。
        *   **S3**: 集成 2.4GHz Wi-Fi (802.11 b/g/n) 和 蓝牙 5 (LE)。
    *   **电气特性**:
        *   P4/S3: TSMC 低功耗工艺 (通常为 40nm 或 22nm，视世代而定)。
*   **独特特性**:
    *   **P4**: 强安全性, 丰富 HMI (触摸, LCD), AI 指令。
    *   **S3**: 经典 AIoT 选择, 集成 Wi-Fi/BT, Arduino/ESP-IDF 广泛支持。
*   **备注**: 竞赛允许使用 P4 或 S3。P4 推荐用于高性能 HMI/AI；S3 用于连接型低功耗 IoT。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 免费一套 (需先购买，完赛后报销). 淘宝“乐鑫科技”或“启明云端”.
*   **资源**: ESP-IDF, 百度/火山引擎 AI 额度支持.

---

### 地瓜机器人 (Horizon Robotics) - RDK系列
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 智能机器人系统 (RDK X3/X5, 闭环控制)
*   **选题二**: 具身智能与高算力机器人 (RDK S100, 大模型)
*   **选题三**: 自主选题

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 机器人, 具身智能, 自主系统。
*   **详细规格**:
    *   **RDK S100**:
        *   **处理器**: S100 智能计算芯片。
        *   **AI**: 80 - 128 TOPS BPU。
        *   **应用**: 复杂机器人, 大模型, 多模态交互。
    *   **RDK X5**:
        *   **处理器**: 旭日 5 (Sunrise 5)。
        *   **AI**: 10 TOPS。
        *   **特性**: 机器人最佳性价比, 支持深度/VSLAM。
    *   **RDK X3**:
        *   **处理器**: 旭日 3 (Sunrise 3)。
        *   **AI**: 5 TOPS。
        *   **视频**: 4K@60fps H.264/H.265。
*   **独特特性**: 强大的 BPU (大脑处理单元), TROS (机器人操作系统) 支持, NodeHub 算法中心。
*   **备注**: 专注于机器人开发套件 (RDK)。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 淘宝“精锋机器人”, 凭报名信息享受折扣.
*   **资源**: RDK OS, NodeHub 算法中心, RDK Studio.

---

### 广和通 (Fibocom) - SC171 / L610
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: AIoT (SC171 智能模组, Android/Linux)
*   **选题二**: 4G IoT 特色应用 (L610 + 协办单位处理器)

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: AIoT, 智慧零售, 工业手持设备, 机器人。
*   **详细规格**:
    *   **SC171 (智能模组)**:
        *   **处理能力**: 8核 ARM v8 Cortex @ 2.7GHz (可能基于高端高通芯片)。
        *   **AI**: 13 TOPS (CPU+GPU+DSP+NPU)。
        *   **连接性**: 5G, Wi-Fi, BT, GNSS。
        *   **I/O**: MIPI DSI/CSI, HDMI, USB, UART, CAN。
        *   **OS**: Android, Linux (Ubuntu), OpenHarmony。
    *   **L610 (CAT1 模组)**:
        *   **连接性**: LTE Cat 1 (10Mbps 下行 / 5Mbps 上行)。
        *   **应用**: 低速物联网, "万物互联"。
*   **独特特性**: SC171 是集成了 5G/AI 的强力“智能模组”。
*   **备注**: SC171 推荐用于高端 AIoT；L610 用于基础连接。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 授权淘宝店优惠购买.
*   **资源**: Fibo AI Stack, 视频课程.

---

### 意法半导体 (STMicroelectronics) - STM32 / Stellar
#### 1. 赛题要求 (Competition Tasks)
*   **选题**: 嵌入式 AI, 数字电源, 飞行汽车(车规), 工业/机器人, 可穿戴, IoT, 自主选题.
*   **核心**: 覆盖 STM32H7/N6/MP2/U5/WLE5 等多系列.

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 通用, 汽车, 工业, AI。
*   **详细规格**:
    *   **STM32N6**:
        *   **处理能力**: Cortex-M 系列，带专用 NPU。
        *   **特性**: 首款集成 Neural Art Accelerator 用于边缘 AI 的 STM32。
    *   **Stellar E1/P3**:
        *   **处理能力**: ARM Cortex-R52 (车规级)。
        *   **应用**: 网关, 域控制器, 电动车控制。
    *   **STM32H7**: 高性能双核 MCU。
    *   **STM32U5**: 超低功耗，带 LPBAM。
*   **独特特性**: 庞大的生态系统 (CubeMX, Cube.AI), 汽车安全 (ASIL), 广泛的产品组合。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 学生支付押金申请 (完赛退押金), 或购买合作伙伴板卡.
*   **工具**: STM32CubeMX, NanoEdge AI Studio, TouchGFX.

---

### 沁恒微电子 (WCH) - CH32系列
#### 1. 赛题要求 (Competition Tasks)
*   **选题**: 无人机 (V203+H415), 边缘 AI (H417), AIoT, USB PD, 计算机周边, 自主选题.

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 连接性, USB, 工业控制。
*   **详细规格**:
    *   **CH32H417/5**:
        *   **处理能力**: 双核 RISC-V (青稞)。
        *   **连接性**: 超高速 USB 3.0, 千兆以太网。
        *   **应用**: 高速数据桥接, 工业网关。
    *   **CH585**:
        *   **处理能力**: RISC-V。
        *   **连接性**: 蓝牙 5, NFC, USB。
*   **独特特性**: 自研 IP (USB/Eth/BT/RISC-V), 专注于“连接与控制”。
*   **备注**: 在 USB 3.0 和接口桥接方面表现强劲。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 淘宝 (官方/VeriMake/金葫芦). 鼓励自制 PCB.
*   **支持**: MounRiver Studio (MRS), 官方 EVT 例程.

---

### 海思 (HiSilicon)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 星闪物联网应用 (WS63/BS21, SLE/BLE/WiFi)
*   **选题二**: AI 端侧智能应用 (SS928, 视觉必选)

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 智能家居, 监控, 工业。
*   **详细规格**:
    *   **SS928**:
        *   **处理能力**: 四核 Cortex-A55 @ 1.4GHz。
        *   **AI**: 神经网络引擎, 10 TOPS INT8。
        *   **视频**: 8K 编解码, 4路传感器输入。
    *   **WS63**:
        *   **处理能力**: 高性能 32位 RISC-V。
        *   **连接性**: Wi-Fi 6, 星闪 (NearLink/SLE), BLE 5.0。
        *   **应用**: 智能家居, 可穿戴。
*   **独特特性**: 星闪 (NearLink) 技术，低延迟无线连接。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 自选购买 (享优惠). AI方向赛后无损可退.
*   **资源**: HiSpark 代码仓, 海思开发者网站.

---

### 瑞芯微 (Rockchip)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 边缘 AI (RK3588, 交互机器人)
*   **选题二**: 端侧 AI 视觉 (RV1126B, 缺陷检测)
*   **选题三**: 智慧工业 (RK3506, 仪表/采集)
*   **选题四**: 自主选题

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 边缘 AI, 平板, 商显。
*   **详细规格**:
    *   **RK3588**:
        *   **处理能力**: 八核 (4xA76 + 4xA55)。8nm 工艺。
        *   **AI**: 6 TOPS NPU, 混合精度。
        *   **多媒体**: 8K 视频, 多路 MIPI CSI/DSI。
    *   **RV1126B**:
        *   **处理能力**: 四核 Cortex-A53 @ 1.6GHz。
        *   **AI**: 3 TOPS。
*   **独特特性**: 高性能 NPU 和媒体能力。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 淘宝“飞凌精灵 ElfBoard”.
*   **资源**: 专属 AI 教程 (Qt/Python).

---

### 瑞萨电子 (Renesas)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 大工业方向 (伺服/变频/机器人/新能源)
*   **选题二**: 物联网 (环境/医疗/家居)
*   **选题三**: 嵌入式 AI (端侧推理/预测性维护)
*   **自主选题**

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 工业, 汽车, 电机控制。
*   **详细规格**:
    *   **RZ/V2H**:
        *   **处理能力**: 异构 (A55 + R8 + M33)。
        *   **AI**: DRP-AI3 加速器 (高效率, 低功耗)。
    *   **RA8系列 (RA8D1)**:
        *   **处理能力**: Cortex-M85 全球首发。480MHz。
        *   **AI**: Helium 向量扩展用于 DSP/AI。
*   **独特特性**: DRP-AI (动态可重构处理器), Helium 技术。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 淘宝“南京娅妮电子”, 赛区三等奖以上退款.
*   **支持**: e2studio IDE, FSP 库.

---

### 睿赛德 (RT-Thread / Canaan)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 虚拟化混合部署 (RK3588, Linux AI + RTT 实时)
*   **选题二**: RT-Smart (K230, 多进程 AI)
*   **自主选题**

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 实时操作系统, RISC-V AI。
*   **详细规格**:
    *   **K230 (RT-Smart AI Kit)**:
        *   **处理能力**: 双核 RISC-V (可能为玄铁 C908)。
        *   **AI**: KPU (知识处理单元)。
*   **备注**: RT-Thread 平台支持在 RK3588 上进行混合部署 (Linux + RT-Thread)。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 淘宝“上海睿赛德”指定店铺.
*   **资源**: RT-Thread Studio, 社区视频/文档.

---

### 移远通信 (Quectel)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 智能骑行头盔 (STM32+4G)
*   **选题二**: 智能零售终端 (RK3568, 识别/计价)
*   **选题三**: 视觉导航机器人 (双目/雷达)
*   **选题四/五**: 声音/LLM应用 (EC800M)

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 智慧零售, 工业网关, 视觉导航。
*   **详细规格**:
    *   **QSM368ZP-WF**:
        *   **处理能力**: Rockchip RK3568 (四核 A55)。
        *   **AI**: 1 TOPS NPU。
        *   **应用**: 智能 POS, NVR, 工业平板。
    *   **UniKnect Kit GEN-1 Pro**:
        *   **处理能力**: STM32 + 4G 模组。
        *   **应用**: 低功耗 IoT。
*   **独特特性**: 蜂窝/通信与计算的强力集成。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 微信小程序/淘宝优惠购买 (三等奖退款).
*   **资源**: QuecPython, 开发者论坛.

---

### 英飞凌 (Infineon)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: Edge AI (PSoC Edge, 语音/视觉/医疗)
*   **选题二**: IoT (PSoC 6, 穿戴/家居)
*   **选题三**: 工业应用 (XMC7000, 电机/电源)

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 边缘 AI, 工业, IoT, 汽车。
*   **详细规格**:
    *   **PSoC Edge E84**:
        *   **处理能力**: Cortex-M55 (400MHz) + M33 (200MHz)。
        *   **AI**: Ethos-U55 NPU + Helium DSP。0.1 TOPS。
        *   **应用**: 语音 UI, 可穿戴, 智能家居。
    *   **PSoC 6**:
        *   **处理能力**: 双核 M4 + M0+。
        *   **应用**: 低功耗 IoT。
    *   **XMC7000**:
        *   **处理能力**: 工业级 Cortex-M7。
        *   **应用**: 电机控制, 电源转换。
*   **独特特性**: PSoC Edge 是带 NPU 的前沿微控制器。广泛的连接性 (AIROC)。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 押金借用 (完赛退) 或购买.
*   **工具**: ModusToolbox, DEEPCRAFT Studio.

---

### 龙芯中科 (Loongson)
#### 1. 赛题要求 (Competition Tasks)
*   **选题一**: 智能智造工业生产线 (2K1000LA/1500/3000)
*   **选题二**: 基于 LLM 的工业仪器 (2K1000LA/1500)
*   **选题三**: 无人智能产品 (2K0300/01, 无人车/机/船)
*   **自主选题**

#### 2. 硬件可选 & 规格 (Hardware Options)
*   **目标应用**: 工业控制, IoT, 网关。
*   **详细规格**:
    *   **LS2K3000**:
        *   **处理能力**: 8核 LA364E (高性能)。10+ 分/GHz。
        *   **AI**: 集成 GPGPU LG200 用于 AI 加速。
        *   **应用**: 工业控制, 边缘计算。
    *   **LS2K0300/0301**:
        *   **处理能力**: 单核/双核 LA264 龙架构核心。
        *   **连接性**: 集成 Wi-Fi (0301)。
        *   **功耗**: 低功耗 (<3W)。
*   **独特特性**: 完全自主的 LoongArch 指令集。高独立性。

#### 3. 资料获取 (Resource Acquisition)
*   **开发板**: 线上渠道 (云晓科技, ICeasy, 中科云等) 自购.
*   **资源**: 龙芯官网, 交流论坛.

---
