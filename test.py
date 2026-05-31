from ultralytics import YOLO


def evaluate():
    # 加载刚刚训练好的最优权重
    model = YOLO('runs/classify/Emotion_Sys/v1_model/weights/best.pt')

    # 强制在独立的 test 集上进行验证
    metrics = model.val(data='./data', split='test')

    # 打印 Top-1 准确率
    print(f"\n======================================")
    print(f"测试集真实准确率 (Top-1): {metrics.top1 * 100:.2f}%")
    print(f"======================================")


if __name__ == '__main__':
    evaluate()


'''
D:\pythonProject\venv\Scripts\python.exe D:\Desktop\Yolo-FaceEmotion\test.py 
Ultralytics 8.4.56  Python-3.11.5 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
YOLOv8s-cls summary (fused): 30 layers, 5,084,167 parameters, 0 gradients, 12.5 GFLOPs
train: D:\Desktop\Yolo-FaceEmotion\data\train... found 28709 images in 7 classes  
val: D:\Desktop\Yolo-FaceEmotion\data\valid... found 3589 images in 7 classes  
test: D:\Desktop\Yolo-FaceEmotion\data\test... found 3589 images in 7 classes  
test: Fast image access  (ping: 0.10.0 ms, read: 4.01.1 MB/s, size: 1.8 KB)
test: Scanning D:\Desktop\Yolo-FaceEmotion\data\test... 3589 images, 0 corrupt: 100% ━━━━━━━━━━━━ 3589/3589 8.1Kit/s 0.4s
test: New cache created: D:\Desktop\Yolo-FaceEmotion\data\test.cache
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 225/225 175.6it/s 1.3s
                   all      0.716      0.992
Speed: 0.0ms preprocess, 0.3ms inference, 0.0ms loss, 0.0ms postprocess per image
Results saved to D:\Desktop\Yolo-FaceEmotion\runs\classify\val

======================================
测试集真实准确率 (Top-1): 71.61%
======================================

进程已结束，退出代码为 0
'''