# 😊 Yolo-FaceEmotion · 人脸表情识别系统

> 基于 YOLOv8s-cls 和 FER2013 数据集的实时人脸表情识别系统  
> 支持实时摄像头检测、图片识别、模型训练与评估

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8s--cls-00FFFF?logo=ultralytics" />
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python" />
  <img src="https://img.shields.io/badge/PyTorch-2.7-EE4C2C?logo=pytorch" />
  <img src="https://img.shields.io/badge/CUDA-11.8-76B900?logo=nvidia" />
  <img src="https://img.shields.io/badge/OpenCV-4.11-5C3EE8?logo=opencv" />
  <img src="https://img.shields.io/badge/Ultralytics-8.4-cyan" />
</p>

---

## 📋 目录

- [项目简介](#-项目简介)
- [数据集说明](#-数据集说明)
- [项目结构](#-项目结构)
- [环境搭建](#-环境搭建)
- [模型训练](#-模型训练)
- [测试评估](#-测试评估)
- [实时推理](#-实时推理)
- [训练结果](#-训练结果)
- [项目依赖](#-项目依赖)

---

## 🎯 项目简介

**Yolo-FaceEmotion** 是一个端到端的人脸表情识别系统，基于 YOLOv8s-cls 分类模型和 FER2013 数据集构建，实现了从**数据集处理 → 模型训练 → 实时推理**的完整流程。

### 识别能力

系统可以识别 **7 种人脸表情**：

| 表情 | 标签 | 说明 |
|:----:|:----:|------|
| 😠 Anger | 愤怒 | 生气的面部表情 |
| 🤢 Disgust | 厌恶 | 反感的情绪表达 |
| 😨 Fear | 恐惧 | 害怕/惊吓的表情 |
| 😊 Happy | 开心 | 高兴/愉快的表情 |
| 😐 Neutral | 中性 | 无表情的平静状态 |
| 😢 Sad | 伤心 | 悲伤/难过的表情 |
| 😲 Surprise | 惊讶 | 吃惊/意外的表情 |

### 核心功能

| 功能 | 脚本 | 说明 |
|------|------|------|
| **数据集整理** | `organize_only.py` | 将 FER2013 CSV 转为按表情分类的图片文件夹 |
| **模型训练** | `train.py` | 基于 YOLOv8s-cls 训练表情分类模型 |
| **模型评估** | `test.py` | 在测试集上评估模型准确率 |
| **实时检测** | `main.py` | 调用摄像头进行实时人脸表情识别 |

---

## 📊 数据集说明

### FER2013 数据集

FER2013 (Facial Expression Recognition 2013) 是 Kaggle 竞赛中发布的人脸表情识别公开数据集。

| 属性 | 数据 |
|:----|:-----|
| **图片总数** | **35,887 张** |
| **图片尺寸** | 48 × 48 像素（灰度图） |
| **表情类别** | 7 类（Anger / Disgust / Fear / Happy / Neutral / Sad / Surprise） |
| **数据集划分** | 训练集 28,709 张 / 验证集 3,589 张 / 测试集 3,589 张 |

### 数据分布

```
类别        训练集    验证集    测试集    总计
─────────────────────────────────────────
Anger       3,995      467      491    4,953
Disgust       436       56       55      547
Fear        4,097      496      528    5,121
Happy       7,215      895      879    8,989
Neutral     4,965      607      626    6,198
Sad         4,830      653      594    6,077
Surprise    3,171      415      416    4,002
─────────────────────────────────────────
总计       28,709    3,589    3,589   35,887
```

### 目录结构（整理后）

```
data/
├── train/                # 训练集 28,709 张
│   ├── Anger/            # 愤怒 3,995 张
│   ├── Disgust/          # 厌恶 436 张
│   ├── Fear/             # 恐惧 4,097 张
│   ├── Happy/            # 开心 7,215 张
│   ├── Neutral/          # 中性 4,965 张
│   ├── Sad/              # 伤心 4,830 张
│   └── Surprise/         # 惊讶 3,171 张
├── valid/                # 验证集 3,589 张（结构同上）
└── test/                 # 测试集 3,589 张（结构同上）
```

---

## 📁 项目结构

```
Yolo-FaceEmotion/
│
├── data/                              # 📊 数据集（按 YOLO 分类格式组织）
│   ├── train/                         # 训练集（7 个表情子文件夹）
│   │   ├── Anger/
│   │   ├── Disgust/
│   │   ├── Fear/
│   │   ├── Happy/
│   │   ├── Neutral/
│   │   ├── Sad/
│   │   └── Surprise/
│   ├── valid/                         # 验证集（同上结构）
│   └── test/                          # 测试集（同上结构）
│
├── runs/classify/                     # 🏋️ 训练产出
│   ├── Emotion_Sys/v1_model/weights/  # 训练好的模型权重
│   │   ├── best.pt                    # ★ 最优模型（70.9% 准确率）
│   │   └── last.pt                    # 最后一个 epoch 的模型
│   └── val/                           # 验证结果
│
├── train.py                           # 🚀 模型训练脚本
├── test.py                            # 📈 测试评估脚本
├── main.py                            # 🎥 实时摄像头检测主程序
├── organize_only.py                   # 📂 数据集整理脚本
├── GPU加速.md                          # ⚡ GPU 环境配置指南
│
├── yolov8s-cls.pt                     # YOLOv8s 分类预训练模型
└── yanzheng.py                        # 验证脚本
```

---

## ⚙️ 环境搭建

### 硬件要求

| 配置 | 最低要求 | 推荐配置 |
|:----|:---------|:---------|
| **CPU** | 4 核以上 | Intel i5 / AMD Ryzen 5 |
| **内存** | 8 GB | 16 GB |
| **GPU** | 可选（训练必须有） | **NVIDIA RTX 3050+**（4GB+） |
| **摄像头** | USB 摄像头 | 720p 以上 |

### 安装依赖

```bash
# 1. 安装 PyTorch（GPU 版本，以 CUDA 11.8 为例）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 2. 安装其他依赖
pip install ultralytics opencv-python numpy

# 3. 验证 GPU 可用
python -c "import torch; print(f'CUDA可用: {torch.cuda.is_available()}, GPU: {torch.cuda.get_device_name(0)}')"
```

> 💡 如果网络较慢，可以用交大镜像：`--index-url https://mirror.sjtu.edu.cn/pytorch-wheels/cu118`

---

## 🏋️ 模型训练

### 训练命令

```bash
python train.py
```

### 训练配置

| 参数 | 值 | 说明 |
|:----|:---|:-----|
| **模型** | YOLOv8s-cls | YOLOv8 分类模型（轻量版，5M 参数） |
| **图片尺寸** | 64×64 | FER2013 原图 48×48，略微放大保留特征 |
| **训练轮数** | 200 epochs | 约 2 小时 |
| **批次大小** | 32 | 兼顾显存与训练速度 |
| **优化器** | Adam | 自动选择 |
| **数据增强** | RandAugment | 提升泛化能力 |

### 训练日志（实际运行结果）

```
Ultralytics 8.4.56  Python-3.11.5 torch-2.7.1+cu118 CUDA:0 (RTX 3050, 4096MiB)
train: found 28709 images in 7 classes
val:   found 3589 images in 7 classes
test:  found 3589 images in 7 classes

Epoch    GPU_mem    loss    Instances
  1/200    1.0G    1.1482        5        64
 50/200    1.0G    0.5450        5        64
100/200    1.0G    0.4115        5        64
150/200    1.0G    0.3523        5        64
200/200    1.0G    0.3143        5        64

200 epochs completed in 2.102 hours.
✅ 最优模型: runs/classify/Emotion_Sys/v1_model/weights/best.pt
```

---

## 📈 测试评估

### 评估命令

```bash
python test.py
```

### 测试结果

```
测试集真实准确率 (Top-1): 71.61%
测试集真实准确率 (Top-5): 99.2%
```

| 指标 | 数值 |
|:----|:----:|
| **Top-1 准确率** | **71.61%** |
| **Top-5 准确率** | **99.20%** |
| **每张推理时间** | **0.3ms**（GPU） |

> FER2015 数据集上人类平均准确率约为 65% ± 5%，模型准确率已超过人类平均水平。

---

## 🎥 实时推理

### 运行实时检测

```bash
python main.py
```

启动后会自动打开摄像头，实时识别人脸表情：

```
系统启动成功！对准摄像头做表情吧。按键盘 'q' 键退出。
```

### 推理流程

```
摄像头实时画面
      │
      ▼
OpenCV Haar Cascade 人脸检测器
      │
      ▼
截取人脸区域（适度向外扩展 padding=15px）
      │
      ▼
YOLOv8s-cls 情绪分类模型推理
      │
      ▼
在画面绘制绿色框 + 表情标签 + 置信度
      │
      ▼
按 'q' 键退出
```

### 显示效果

```
┌──────────────────────────────────┐
│                                  │
│     ┌──────────┐                 │
│     │  😊      │                 │
│     │ Happy    │ ← 绿色框        │
│     │ (98.3%)  │ ← 置信度       │
│     └──────────┘                 │
│                                  │
└──────────────────────────────────┘
```

---

## 🏆 训练结果

### 准确率曲线

| 阶段 | 验证集 Top-1 | 测试集 Top-1 |
|:----|:------------:|:------------:|
| 初始（预训练） | ~55% | - |
| 50 epochs | ~64% | - |
| 100 epochs | ~67% | - |
| 150 epochs | ~69% | - |
| **200 epochs** | **~70.3%** | **71.61%** |

### 与人类对比

```
人类在该数据集上的平均准确率：~65%
模型准确率：                    ~71.6%
                              ↑ 超越人类
```

### 各类别表现

测试集各类别 Top-1 准确率（可通过 val 结果查看详细混淆矩阵）：

| 类别 | 表现 |
|:----|:----:|
| Happy | ⭐ 最高（最容易识别） |
| Neutral | ⭐ 较高 |
| Anger | ✅ 良好 |
| Surprise | ✅ 良好 |
| Sad | ⚠️ 中等 |
| Fear | ⚠️ 中等（易与 Surprise 混淆） |
| Disgust | 🔻 最低（样本最少，仅 436 张训练数据） |

---

## 📦 项目依赖

```txt
ultralytics>=8.4.0
opencv-python>=4.11.0
numpy>=1.24.3
torch>=2.0.0
torchvision>=0.15.0
```

---

## 🚀 后续优化方向

| 方向 | 说明 |
|:----|:-----|
| **数据增强** | 对 Disgust 等少数类进行过采样，平衡类别分布 |
| **模型升级** | 尝试 YOLOv8m-cls / YOLOv8l-cls 更大模型 |
| **人脸检测升级** | 替换 Haar Cascade 为 YOLO 人脸检测模型，提升准确率 |
| **模型量化** | FP16 / INT8 量化，提升推理速度 |
| **模型部署** | 导出 ONNX / TensorRT 格式，适配边缘设备 |

---

<p align="center">
  <sub>😊 基于 YOLOv8s-cls + FER2013 的人脸表情识别系统</sub>
</p>
