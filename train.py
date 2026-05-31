from ultralytics import YOLO


def main():
    model = YOLO('yolov8s-cls.pt')

    # 启动训练
    results = model.train(
        data='./data',  # 数据集根目录路径
        epochs=200,  # 训练轮数。如果后续觉得准确率没达到预期，可以调高到 100
        imgsz=64,  # 4kb 的图片尺寸很小，64x64 足以提取面部特征且训练极快
        batch=32,  # 批次大小
        amp=False,
        workers=4,  # 数据加载线程数
        project='Emotion_Sys',  # 结果保存的文件夹名称
        name='v1_model'  # 本次训练的子文件夹名称
    )

    print("训练完成！最优模型已保存在 Emotion_Sys/v1_model/weights/best.pt")


if __name__ == '__main__':
    main()

'''
D:\pythonProject\venv\Scripts\python.exe D:\Desktop\Yolo-FaceEmotion\train.py 
Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8s-cls.pt to 'yolov8s-cls.pt': 100% ━━━━━━━━━━━━ 12.3MB 1.4MB/s 8.8s
New https://pypi.org/project/ultralytics/8.4.57 available  Update with 'pip install -U ultralytics'
Ultralytics 8.4.56  Python-3.11.5 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
engine\trainer: agnostic_nms=False, amp=False, angle=1.0, augment=False, auto_augment=randaugment, batch=32, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=./data, degrees=0.0, deterministic=True, device=None, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, end2end=None, epochs=200, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=64, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8s-cls.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=v1_model, nbs=64, nms=False, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=Emotion_Sys, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=classify, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=4, workspace=None
train: D:\Desktop\Yolo-FaceEmotion\data\train... found 28709 images in 7 classes  
val: D:\Desktop\Yolo-FaceEmotion\data\valid... found 3589 images in 7 classes  
test: D:\Desktop\Yolo-FaceEmotion\data\test... found 3589 images in 7 classes  
Overriding model.yaml nc=1000 with nc=7

                   from  n    params  module                                       arguments                     
  0                  -1  1       928  ultralytics.nn.modules.conv.Conv             [3, 32, 3, 2]                 
  1                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  2                  -1  1     29056  ultralytics.nn.modules.block.C2f             [64, 64, 1, True]             
  3                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  4                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  5                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  6                  -1  2    788480  ultralytics.nn.modules.block.C2f             [256, 256, 2, True]           
  7                  -1  1   1180672  ultralytics.nn.modules.conv.Conv             [256, 512, 3, 2]              
  8                  -1  1   1838080  ultralytics.nn.modules.block.C2f             [512, 512, 1, True]           
  9                  -1  1    666887  ultralytics.nn.modules.head.Classify         [512, 7]                      
YOLOv8s-cls summary: 56 layers, 5,089,703 parameters, 5,089,703 gradients, 12.6 GFLOPs
Transferred 156/158 items from pretrained weights
train: Fast image access  (ping: 0.10.1 ms, read: 19.75.7 MB/s, size: 1.8 KB)
train: Scanning D:\Desktop\Yolo-FaceEmotion\data\train... 28709 images, 0 corrupt: 100% ━━━━━━━━━━━━ 28709/28709 9.8Kit/s 2.9s
train: New cache created: D:\Desktop\Yolo-FaceEmotion\data\train.cache
val: Fast image access  (ping: 0.10.0 ms, read: 19.85.8 MB/s, size: 1.8 KB)
val: Scanning D:\Desktop\Yolo-FaceEmotion\data\valid... 3589 images, 0 corrupt: 100% ━━━━━━━━━━━━ 3589/3589 8.3Kit/s 0.4s
val: New cache created: D:\Desktop\Yolo-FaceEmotion\data\valid.cache
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: MuSGD(lr=0.01, momentum=0.9) with parameter groups 26 weight(decay=0.0), 27 weight(decay=0.0005), 27 bias(decay=0.0)
Image sizes 64 train, 64 val
Using 4 dataloader workers
Logging results to D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model
Starting training for 200 epochs...

      Epoch    GPU_mem       loss  Instances       Size
      1/200     0.291G       1.76          5         64: 100% ━━━━━━━━━━━━ 898/898 19.0it/s 47.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 102.5it/s 0.6s
                   all      0.407      0.932

      Epoch    GPU_mem       loss  Instances       Size
      2/200     0.354G      1.578          5         64: 100% ━━━━━━━━━━━━ 898/898 22.8it/s 39.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 110.8it/s 0.5s
                   all      0.495      0.966

      Epoch    GPU_mem       loss  Instances       Size
      3/200     0.365G      1.409          5         64: 100% ━━━━━━━━━━━━ 898/898 29.5it/s 30.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 111.3it/s 0.5s
                   all       0.51      0.976

      Epoch    GPU_mem       loss  Instances       Size
      4/200     0.377G      1.321          5         64: 100% ━━━━━━━━━━━━ 898/898 29.1it/s 30.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 108.6it/s 0.5s
                   all      0.561      0.974

      Epoch    GPU_mem       loss  Instances       Size
      5/200     0.436G      1.248          5         64: 100% ━━━━━━━━━━━━ 898/898 26.2it/s 34.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.3it/s 0.6s
                   all       0.57      0.982

      Epoch    GPU_mem       loss  Instances       Size
      6/200     0.449G      1.202          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.2it/s 0.6s
                   all      0.601      0.985

      Epoch    GPU_mem       loss  Instances       Size
      7/200     0.459G      1.172          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 98.3it/s 0.6s
                   all      0.606      0.985

      Epoch    GPU_mem       loss  Instances       Size
      8/200     0.518G      1.152          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.5it/s 0.6s
                   all      0.611      0.987

      Epoch    GPU_mem       loss  Instances       Size
      9/200     0.529G      1.133          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 100.1it/s 0.6s
                   all      0.615      0.986

      Epoch    GPU_mem       loss  Instances       Size
     10/200     0.588G       1.12          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.8it/s 0.6s
                   all      0.625      0.985

      Epoch    GPU_mem       loss  Instances       Size
     11/200       0.6G      1.102          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.0it/s 0.6s
                   all      0.623      0.984

      Epoch    GPU_mem       loss  Instances       Size
     12/200     0.611G      1.093          5         64: 100% ━━━━━━━━━━━━ 898/898 23.8it/s 37.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 98.5it/s 0.6s
                   all      0.631      0.984

      Epoch    GPU_mem       loss  Instances       Size
     13/200      0.67G      1.085          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.635      0.989

      Epoch    GPU_mem       loss  Instances       Size
     14/200     0.682G      1.076          5         64: 100% ━━━━━━━━━━━━ 898/898 23.7it/s 38.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.1it/s 0.7s
                   all       0.63      0.987

      Epoch    GPU_mem       loss  Instances       Size
     15/200     0.693G      1.072          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.3it/s 0.6s
                   all      0.649      0.987

      Epoch    GPU_mem       loss  Instances       Size
     16/200     0.752G      1.067          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.6it/s 0.6s
                   all       0.64      0.989

      Epoch    GPU_mem       loss  Instances       Size
     17/200     0.764G      1.059          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.4it/s 0.6s
                   all      0.639      0.988

      Epoch    GPU_mem       loss  Instances       Size
     18/200     0.822G      1.051          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.9it/s 0.6s
                   all      0.648      0.989

      Epoch    GPU_mem       loss  Instances       Size
     19/200     0.834G      1.042          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.7it/s 0.6s
                   all      0.639      0.988

      Epoch    GPU_mem       loss  Instances       Size
     20/200     0.844G      1.037          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.9it/s 0.7s
                   all      0.642       0.99

      Epoch    GPU_mem       loss  Instances       Size
     21/200     0.904G      1.031          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.7it/s 0.7s
                   all      0.652      0.989

      Epoch    GPU_mem       loss  Instances       Size
     22/200     0.916G      1.029          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.6it/s 0.6s
                   all      0.653      0.988

      Epoch    GPU_mem       loss  Instances       Size
     23/200     0.973G      1.025          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.4it/s 0.6s
                   all       0.65      0.988

      Epoch    GPU_mem       loss  Instances       Size
     24/200     0.984G      1.024          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.649      0.989

      Epoch    GPU_mem       loss  Instances       Size
     25/200     0.996G      1.017          5         64: 100% ━━━━━━━━━━━━ 898/898 25.0it/s 36.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.5it/s 0.6s
                   all      0.655      0.988

      Epoch    GPU_mem       loss  Instances       Size
     26/200      1.05G      1.008          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.3it/s 0.6s
                   all      0.663      0.989

      Epoch    GPU_mem       loss  Instances       Size
     27/200      1.07G      1.014          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.3it/s 0.6s
                   all      0.662       0.99

      Epoch    GPU_mem       loss  Instances       Size
     28/200      1.08G      1.001          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.2it/s 0.6s
                   all      0.671      0.989

      Epoch    GPU_mem       loss  Instances       Size
     29/200      1.14G      1.002          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.0it/s 0.6s
                   all      0.668       0.99

      Epoch    GPU_mem       loss  Instances       Size
     30/200      1.15G     0.9927          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.8it/s 0.6s
                   all      0.666      0.991

      Epoch    GPU_mem       loss  Instances       Size
     31/200      1.21G     0.9919          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.5it/s 0.6s
                   all      0.667       0.99

      Epoch    GPU_mem       loss  Instances       Size
     32/200      1.22G     0.9915          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.6it/s 0.6s
                   all      0.668      0.991

      Epoch    GPU_mem       loss  Instances       Size
     33/200      1.23G     0.9844          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.9it/s 0.6s
                   all       0.67      0.991

      Epoch    GPU_mem       loss  Instances       Size
     34/200      1.29G     0.9862          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.2it/s 0.6s
                   all      0.672      0.991

      Epoch    GPU_mem       loss  Instances       Size
     35/200       1.3G     0.9832          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.9it/s 0.6s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     36/200      1.31G     0.9764          5         64: 100% ━━━━━━━━━━━━ 898/898 22.4it/s 40.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 72.9it/s 0.8s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     37/200      1.37G     0.9775          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.4it/s 0.6s
                   all      0.675      0.992

      Epoch    GPU_mem       loss  Instances       Size
     38/200      1.38G     0.9683          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.5it/s 0.6s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     39/200      1.44G     0.9673          5         64: 100% ━━━━━━━━━━━━ 898/898 24.9it/s 36.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.8it/s 0.6s
                   all      0.673      0.993

      Epoch    GPU_mem       loss  Instances       Size
     40/200      1.45G     0.9712          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 85.4it/s 0.7s
                   all      0.672      0.993

      Epoch    GPU_mem       loss  Instances       Size
     41/200      1.46G      0.964          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.7it/s 0.6s
                   all      0.673      0.992

      Epoch    GPU_mem       loss  Instances       Size
     42/200      1.52G     0.9635          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.9it/s 0.6s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     43/200      1.54G       0.96          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.5it/s 0.7s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     44/200      1.55G     0.9541          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.5it/s 0.6s
                   all      0.673      0.992

      Epoch    GPU_mem       loss  Instances       Size
     45/200      1.61G     0.9535          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.7it/s 0.7s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     46/200      1.62G     0.9506          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.2it/s 0.6s
                   all      0.671      0.991

      Epoch    GPU_mem       loss  Instances       Size
     47/200      1.68G     0.9518          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.9it/s 0.6s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     48/200      1.69G      0.948          5         64: 100% ━━━━━━━━━━━━ 898/898 25.0it/s 36.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.2it/s 0.6s
                   all      0.671      0.992

      Epoch    GPU_mem       loss  Instances       Size
     49/200       1.7G     0.9443          5         64: 100% ━━━━━━━━━━━━ 898/898 25.0it/s 36.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.2it/s 0.6s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     50/200      1.76G     0.9462          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.9it/s 0.6s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     51/200      1.77G     0.9369          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.4it/s 0.6s
                   all      0.673      0.992

      Epoch    GPU_mem       loss  Instances       Size
     52/200      1.78G       0.93          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.3it/s 0.6s
                   all      0.672      0.992

      Epoch    GPU_mem       loss  Instances       Size
     53/200      1.84G     0.9292          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.9it/s 0.6s
                   all      0.673      0.992

      Epoch    GPU_mem       loss  Instances       Size
     54/200      1.85G     0.9277          5         64: 100% ━━━━━━━━━━━━ 898/898 24.9it/s 36.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.5it/s 0.6s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     55/200      1.91G      0.925          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.4it/s 0.7s
                   all      0.673      0.992

      Epoch    GPU_mem       loss  Instances       Size
     56/200      1.92G     0.9259          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.0it/s 0.6s
                   all      0.674      0.992

      Epoch    GPU_mem       loss  Instances       Size
     57/200      1.93G     0.9132          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.5it/s 0.6s
                   all      0.675      0.993

      Epoch    GPU_mem       loss  Instances       Size
     58/200      1.99G      0.915          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.1it/s 0.6s
                   all      0.674      0.993

      Epoch    GPU_mem       loss  Instances       Size
     59/200         2G     0.9133          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 75.1it/s 0.8s
                   all      0.675      0.993

      Epoch    GPU_mem       loss  Instances       Size
     60/200     0.428G     0.9084          5         64: 100% ━━━━━━━━━━━━ 898/898 23.6it/s 38.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.5it/s 0.6s
                   all      0.676      0.993

      Epoch    GPU_mem       loss  Instances       Size
     61/200     0.428G     0.9107          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.1it/s 0.6s
                   all      0.678      0.993

      Epoch    GPU_mem       loss  Instances       Size
     62/200     0.428G     0.9062          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.5it/s 0.7s
                   all      0.677      0.993

      Epoch    GPU_mem       loss  Instances       Size
     63/200     0.438G      0.905          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 85.7it/s 0.7s
                   all      0.677      0.993

      Epoch    GPU_mem       loss  Instances       Size
     64/200     0.447G     0.8958          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.7it/s 0.6s
                   all      0.677      0.993

      Epoch    GPU_mem       loss  Instances       Size
     65/200     0.459G     0.9055          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.3it/s 0.6s
                   all      0.678      0.993

      Epoch    GPU_mem       loss  Instances       Size
     66/200     0.518G       0.89          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.7it/s 0.6s
                   all      0.677      0.993

      Epoch    GPU_mem       loss  Instances       Size
     67/200     0.529G     0.8927          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.5it/s 0.6s
                   all      0.679      0.993

      Epoch    GPU_mem       loss  Instances       Size
     68/200     0.588G     0.8976          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.8it/s 0.6s
                   all       0.68      0.993

      Epoch    GPU_mem       loss  Instances       Size
     69/200       0.6G     0.8867          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.6it/s 0.6s
                   all       0.68      0.993

      Epoch    GPU_mem       loss  Instances       Size
     70/200     0.611G     0.8819          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all       0.68      0.992

      Epoch    GPU_mem       loss  Instances       Size
     71/200      0.67G     0.8917          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.1it/s 0.6s
                   all      0.679      0.992

      Epoch    GPU_mem       loss  Instances       Size
     72/200     0.682G      0.882          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.1it/s 0.6s
                   all       0.68      0.992

      Epoch    GPU_mem       loss  Instances       Size
     73/200     0.693G      0.876          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.4it/s 0.6s
                   all      0.681      0.992

      Epoch    GPU_mem       loss  Instances       Size
     74/200     0.752G     0.8739          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.0it/s 0.6s
                   all      0.679      0.992

      Epoch    GPU_mem       loss  Instances       Size
     75/200     0.764G     0.8682          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.679      0.992

      Epoch    GPU_mem       loss  Instances       Size
     76/200     0.822G     0.8721          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.0it/s 0.6s
                   all      0.678      0.992

      Epoch    GPU_mem       loss  Instances       Size
     77/200     0.834G     0.8689          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.0it/s 0.6s
                   all       0.68      0.992

      Epoch    GPU_mem       loss  Instances       Size
     78/200     0.846G     0.8622          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.9it/s 0.6s
                   all      0.682      0.992

      Epoch    GPU_mem       loss  Instances       Size
     79/200     0.904G     0.8624          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.0it/s 0.6s
                   all      0.681      0.992

      Epoch    GPU_mem       loss  Instances       Size
     80/200     0.914G     0.8589          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.1it/s 0.6s
                   all      0.683      0.992

      Epoch    GPU_mem       loss  Instances       Size
     81/200     0.928G     0.8626          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 83.9it/s 0.7s
                   all      0.683      0.992

      Epoch    GPU_mem       loss  Instances       Size
     82/200     0.984G     0.8503          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.9it/s 0.6s
                   all      0.683      0.993

      Epoch    GPU_mem       loss  Instances       Size
     83/200     0.996G     0.8476          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.7it/s 0.6s
                   all      0.683      0.993

      Epoch    GPU_mem       loss  Instances       Size
     84/200      1.05G     0.8455          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.6it/s 0.6s
                   all      0.684      0.993

      Epoch    GPU_mem       loss  Instances       Size
     85/200      1.07G     0.8369          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.0it/s 0.6s
                   all      0.684      0.993

      Epoch    GPU_mem       loss  Instances       Size
     86/200      1.08G     0.8379          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.6it/s 0.6s
                   all      0.685      0.993

      Epoch    GPU_mem       loss  Instances       Size
     87/200      1.14G     0.8398          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.1it/s 0.6s
                   all      0.684      0.993

      Epoch    GPU_mem       loss  Instances       Size
     88/200      1.15G     0.8365          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.4it/s 0.6s
                   all      0.685      0.993

      Epoch    GPU_mem       loss  Instances       Size
     89/200      1.16G     0.8269          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.2it/s 0.6s
                   all      0.685      0.993

      Epoch    GPU_mem       loss  Instances       Size
     90/200      1.22G     0.8284          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.3it/s 0.6s
                   all      0.686      0.993

      Epoch    GPU_mem       loss  Instances       Size
     91/200      1.23G     0.8235          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.9it/s 0.6s
                   all      0.687      0.993

      Epoch    GPU_mem       loss  Instances       Size
     92/200      1.29G     0.8168          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.2it/s 0.6s
                   all      0.688      0.993

      Epoch    GPU_mem       loss  Instances       Size
     93/200       1.3G     0.8193          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.8it/s 0.6s
                   all      0.688      0.992

      Epoch    GPU_mem       loss  Instances       Size
     94/200      1.31G     0.8133          5         64: 100% ━━━━━━━━━━━━ 898/898 23.8it/s 37.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.2it/s 0.6s
                   all      0.687      0.992

      Epoch    GPU_mem       loss  Instances       Size
     95/200      1.37G     0.8106          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.9it/s 0.6s
                   all      0.689      0.993

      Epoch    GPU_mem       loss  Instances       Size
     96/200      1.38G     0.8049          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.9it/s 0.6s
                   all      0.689      0.992

      Epoch    GPU_mem       loss  Instances       Size
     97/200      1.39G      0.808          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.0it/s 0.6s
                   all      0.688      0.992

      Epoch    GPU_mem       loss  Instances       Size
     98/200      1.45G     0.8015          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.8it/s 0.6s
                   all      0.688      0.992

      Epoch    GPU_mem       loss  Instances       Size
     99/200      1.46G     0.8001          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.6it/s 0.6s
                   all      0.688      0.992

      Epoch    GPU_mem       loss  Instances       Size
    100/200      1.52G     0.7992          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.9it/s 0.6s
                   all      0.689      0.992

      Epoch    GPU_mem       loss  Instances       Size
    101/200      1.54G     0.7886          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.6it/s 0.6s
                   all      0.689      0.992

      Epoch    GPU_mem       loss  Instances       Size
    102/200      1.55G     0.7859          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.2it/s 0.6s
                   all       0.69      0.993

      Epoch    GPU_mem       loss  Instances       Size
    103/200      1.61G     0.7913          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.9it/s 0.6s
                   all       0.69      0.992

      Epoch    GPU_mem       loss  Instances       Size
    104/200      1.62G     0.7867          5         64: 100% ━━━━━━━━━━━━ 898/898 23.8it/s 37.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.3it/s 0.6s
                   all      0.693      0.992

      Epoch    GPU_mem       loss  Instances       Size
    105/200      1.63G     0.7816          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.2it/s 0.6s
                   all      0.694      0.992

      Epoch    GPU_mem       loss  Instances       Size
    106/200      1.69G     0.7813          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.3it/s 0.6s
                   all      0.694      0.992

      Epoch    GPU_mem       loss  Instances       Size
    107/200       1.7G     0.7779          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.6it/s 0.6s
                   all      0.695      0.992

      Epoch    GPU_mem       loss  Instances       Size
    108/200      1.76G     0.7693          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.4it/s 0.6s
                   all      0.697      0.992

      Epoch    GPU_mem       loss  Instances       Size
    109/200      1.77G     0.7667          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 85.9it/s 0.7s
                   all      0.698      0.992

      Epoch    GPU_mem       loss  Instances       Size
    110/200      1.78G     0.7729          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.9it/s 0.7s
                   all      0.699      0.992

      Epoch    GPU_mem       loss  Instances       Size
    111/200      1.84G     0.7557          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.6it/s 0.6s
                   all      0.698      0.991

      Epoch    GPU_mem       loss  Instances       Size
    112/200      1.85G     0.7601          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.1it/s 0.6s
                   all        0.7      0.991

      Epoch    GPU_mem       loss  Instances       Size
    113/200      1.86G     0.7521          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.6it/s 0.6s
                   all      0.701      0.991

      Epoch    GPU_mem       loss  Instances       Size
    114/200      1.92G      0.745          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.4it/s 0.6s
                   all      0.701      0.991

      Epoch    GPU_mem       loss  Instances       Size
    115/200      1.93G     0.7445          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.2it/s 0.6s
                   all      0.701      0.991

      Epoch    GPU_mem       loss  Instances       Size
    116/200      1.99G     0.7373          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.3it/s 0.6s
                   all      0.702      0.992

      Epoch    GPU_mem       loss  Instances       Size
    117/200         2G      0.737          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 79.3it/s 0.7s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    118/200     0.418G     0.7376          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.8it/s 0.6s
                   all      0.703      0.991

      Epoch    GPU_mem       loss  Instances       Size
    119/200     0.418G     0.7317          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.1it/s 0.6s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    120/200     0.426G     0.7276          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.9it/s 0.6s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    121/200     0.438G     0.7243          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.8it/s 0.6s
                   all      0.701      0.991

      Epoch    GPU_mem       loss  Instances       Size
    122/200     0.449G     0.7161          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.0it/s 0.6s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    123/200     0.506G     0.7156          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.3it/s 0.6s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    124/200      0.52G     0.7115          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.3it/s 0.6s
                   all      0.701      0.991

      Epoch    GPU_mem       loss  Instances       Size
    125/200     0.529G     0.7093          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.7it/s 0.6s
                   all      0.699      0.991

      Epoch    GPU_mem       loss  Instances       Size
    126/200     0.588G     0.7003          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.9it/s 0.6s
                   all      0.702      0.991

      Epoch    GPU_mem       loss  Instances       Size
    127/200       0.6G     0.7003          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 98.1it/s 0.6s
                   all      0.703      0.991

      Epoch    GPU_mem       loss  Instances       Size
    128/200     0.611G     0.7019          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.7it/s 0.6s
                   all      0.704      0.991

      Epoch    GPU_mem       loss  Instances       Size
    129/200      0.67G     0.6823          5         64: 100% ━━━━━━━━━━━━ 898/898 21.8it/s 41.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 71.3it/s 0.8s
                   all      0.705      0.991

      Epoch    GPU_mem       loss  Instances       Size
    130/200     0.682G     0.6942          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 98.3it/s 0.6s
                   all      0.703      0.991

      Epoch    GPU_mem       loss  Instances       Size
    131/200      0.74G     0.6877          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.1it/s 0.7s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    132/200     0.752G     0.6838          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.9it/s 0.6s
                   all      0.699       0.99

      Epoch    GPU_mem       loss  Instances       Size
    133/200     0.764G     0.6791          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.7it/s 0.6s
                   all      0.699       0.99

      Epoch    GPU_mem       loss  Instances       Size
    134/200     0.822G     0.6743          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.2it/s 0.6s
                   all      0.698       0.99

      Epoch    GPU_mem       loss  Instances       Size
    135/200     0.834G     0.6644          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.4it/s 0.6s
                   all      0.697       0.99

      Epoch    GPU_mem       loss  Instances       Size
    136/200     0.846G     0.6694          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.0it/s 0.6s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    137/200     0.904G     0.6625          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.1it/s 0.6s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    138/200     0.916G     0.6543          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.1it/s 0.6s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    139/200     0.975G     0.6533          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.7it/s 0.6s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    140/200     0.986G     0.6493          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.9it/s 0.6s
                   all        0.7       0.99

      Epoch    GPU_mem       loss  Instances       Size
    141/200     0.996G     0.6383          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.3it/s 0.6s
                   all      0.702       0.99

      Epoch    GPU_mem       loss  Instances       Size
    142/200      1.05G     0.6427          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.8it/s 0.6s
                   all      0.704       0.99

      Epoch    GPU_mem       loss  Instances       Size
    143/200      1.07G     0.6387          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.5it/s 0.7s
                   all      0.704       0.99

      Epoch    GPU_mem       loss  Instances       Size
    144/200      1.08G     0.6245          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.9it/s 0.6s
                   all      0.704       0.99

      Epoch    GPU_mem       loss  Instances       Size
    145/200      1.14G     0.6273          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.3it/s 0.6s
                   all      0.705      0.989

      Epoch    GPU_mem       loss  Instances       Size
    146/200      1.15G     0.6257          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.707      0.989

      Epoch    GPU_mem       loss  Instances       Size
    147/200      1.21G      0.613          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.7it/s 0.6s
                   all      0.708      0.989

      Epoch    GPU_mem       loss  Instances       Size
    148/200      1.22G     0.6047          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.2it/s 0.7s
                   all      0.707      0.989

      Epoch    GPU_mem       loss  Instances       Size
    149/200      1.23G     0.6045          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.5it/s 0.6s
                   all      0.707      0.989

      Epoch    GPU_mem       loss  Instances       Size
    150/200      1.29G     0.6037          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.1it/s 0.6s
                   all      0.708      0.989

      Epoch    GPU_mem       loss  Instances       Size
    151/200       1.3G     0.5988          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.9it/s 0.6s
                   all      0.707      0.989

      Epoch    GPU_mem       loss  Instances       Size
    152/200      1.31G     0.5871          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.7it/s 0.6s
                   all      0.706      0.989

      Epoch    GPU_mem       loss  Instances       Size
    153/200      1.37G     0.5842          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.5it/s 0.6s
                   all      0.706       0.99

      Epoch    GPU_mem       loss  Instances       Size
    154/200      1.38G     0.5842          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.1it/s 0.6s
                   all      0.705      0.989

      Epoch    GPU_mem       loss  Instances       Size
    155/200      1.44G     0.5752          5         64: 100% ━━━━━━━━━━━━ 898/898 23.8it/s 37.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.8it/s 0.6s
                   all      0.705      0.989

      Epoch    GPU_mem       loss  Instances       Size
    156/200      1.45G     0.5731          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.5it/s 0.6s
                   all      0.705      0.988

      Epoch    GPU_mem       loss  Instances       Size
    157/200      1.46G     0.5645          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.1it/s 0.6s
                   all      0.704      0.988

      Epoch    GPU_mem       loss  Instances       Size
    158/200      1.52G     0.5601          5         64: 100% ━━━━━━━━━━━━ 898/898 23.8it/s 37.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.2it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    159/200      1.54G     0.5532          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 86.2it/s 0.7s
                   all      0.707      0.987

      Epoch    GPU_mem       loss  Instances       Size
    160/200      1.55G     0.5536          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.5it/s 0.7s
                   all      0.706      0.987

      Epoch    GPU_mem       loss  Instances       Size
    161/200      1.61G     0.5423          5         64: 100% ━━━━━━━━━━━━ 898/898 24.1it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.8it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    162/200      1.62G     0.5442          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.5it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    163/200      1.68G     0.5346          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.6it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    164/200      1.69G     0.5202          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.0it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    165/200       1.7G     0.5209          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.2it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    166/200      1.76G     0.5134          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 80.9it/s 0.7s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    167/200      1.77G     0.5123          5         64: 100% ━━━━━━━━━━━━ 898/898 23.4it/s 38.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.7it/s 0.6s
                   all      0.705      0.988

      Epoch    GPU_mem       loss  Instances       Size
    168/200      1.78G     0.5122          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.8it/s 0.6s
                   all      0.704      0.988

      Epoch    GPU_mem       loss  Instances       Size
    169/200      1.84G     0.5053          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.4it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    170/200      1.85G     0.4912          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 87.3it/s 0.7s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    171/200      1.91G     0.4918          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.6it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    172/200      1.92G     0.4776          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.7it/s 0.6s
                   all      0.705      0.986

      Epoch    GPU_mem       loss  Instances       Size
    173/200      1.93G     0.4755          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.2s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 91.8it/s 0.6s
                   all      0.705      0.986

      Epoch    GPU_mem       loss  Instances       Size
    174/200      1.99G     0.4658          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.5it/s 0.6s
                   all      0.706      0.987

      Epoch    GPU_mem       loss  Instances       Size
    175/200         2G     0.4608          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.5it/s 0.6s
                   all      0.706      0.987

      Epoch    GPU_mem       loss  Instances       Size
    176/200     0.521G     0.4581          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.7it/s 0.6s
                   all      0.706      0.987

      Epoch    GPU_mem       loss  Instances       Size
    177/200     0.521G     0.4589          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.5it/s 0.6s
                   all      0.707      0.987

      Epoch    GPU_mem       loss  Instances       Size
    178/200     0.521G     0.4423          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    179/200     0.529G     0.4429          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.2it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    180/200     0.541G     0.4389          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 96.1it/s 0.6s
                   all      0.703      0.987

      Epoch    GPU_mem       loss  Instances       Size
    181/200     0.553G     0.4312          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.3it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    182/200     0.564G     0.4255          5         64: 100% ━━━━━━━━━━━━ 898/898 24.8it/s 36.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.7it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    183/200     0.576G     0.4124          5         64: 100% ━━━━━━━━━━━━ 898/898 24.0it/s 37.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.1it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    184/200     0.588G     0.4124          5         64: 100% ━━━━━━━━━━━━ 898/898 24.2it/s 37.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.1it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    185/200       0.6G     0.3997          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 97.4it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    186/200     0.611G     0.3925          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 90.3it/s 0.6s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    187/200      0.67G     0.3867          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.0it/s 0.6s
                   all      0.703      0.988

      Epoch    GPU_mem       loss  Instances       Size
    188/200     0.682G     0.3897          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.9it/s 0.6s
                   all      0.702      0.988

      Epoch    GPU_mem       loss  Instances       Size
    189/200     0.693G     0.3776          5         64: 100% ━━━━━━━━━━━━ 898/898 23.9it/s 37.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 85.1it/s 0.7s
                   all      0.703      0.988

      Epoch    GPU_mem       loss  Instances       Size
    190/200     0.752G     0.3726          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 36.9s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 92.0it/s 0.6s
                   all      0.703      0.987

      Epoch    GPU_mem       loss  Instances       Size
    191/200     0.764G     0.3554          5         64: 100% ━━━━━━━━━━━━ 898/898 23.4it/s 38.4s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 73.1it/s 0.8s
                   all      0.704      0.987

      Epoch    GPU_mem       loss  Instances       Size
    192/200     0.822G      0.358          5         64: 100% ━━━━━━━━━━━━ 898/898 24.4it/s 36.8s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.6it/s 0.6s
                   all      0.705      0.987

      Epoch    GPU_mem       loss  Instances       Size
    193/200     0.832G     0.3488          5         64: 100% ━━━━━━━━━━━━ 898/898 24.9it/s 36.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.2it/s 0.6s
                   all      0.705      0.986

      Epoch    GPU_mem       loss  Instances       Size
    194/200     0.846G     0.3464          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.6s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 88.5it/s 0.6s
                   all      0.705      0.986

      Epoch    GPU_mem       loss  Instances       Size
    195/200     0.902G     0.3393          5         64: 100% ━━━━━━━━━━━━ 898/898 24.9it/s 36.1s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.0it/s 0.6s
                   all      0.704      0.986

      Epoch    GPU_mem       loss  Instances       Size
    196/200     0.916G     0.3369          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 94.4it/s 0.6s
                   all      0.703      0.986

      Epoch    GPU_mem       loss  Instances       Size
    197/200     0.928G     0.3366          5         64: 100% ━━━━━━━━━━━━ 898/898 24.6it/s 36.5s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 89.0it/s 0.6s
                   all      0.704      0.986

      Epoch    GPU_mem       loss  Instances       Size
    198/200     0.984G     0.3241          5         64: 100% ━━━━━━━━━━━━ 898/898 24.5it/s 36.7s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 83.9it/s 0.7s
                   all      0.704      0.986

      Epoch    GPU_mem       loss  Instances       Size
    199/200     0.996G     0.3285          5         64: 100% ━━━━━━━━━━━━ 898/898 24.3it/s 37.0s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 95.2it/s 0.6s
                   all      0.703      0.985

      Epoch    GPU_mem       loss  Instances       Size
    200/200      1.05G     0.3143          5         64: 100% ━━━━━━━━━━━━ 898/898 24.7it/s 36.3s
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 93.8it/s 0.6s
                   all      0.702      0.985

200 epochs completed in 2.102 hours.
Optimizer stripped from D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model\weights\last.pt, 10.3MB
Optimizer stripped from D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model\weights\best.pt, 10.3MB

Validating D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model\weights\best.pt...
Ultralytics 8.4.56  Python-3.11.5 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 3050 Laptop GPU, 4096MiB)
YOLOv8s-cls summary (fused): 30 layers, 5,084,167 parameters, 0 gradients, 12.5 GFLOPs
train: D:\Desktop\Yolo-FaceEmotion\data\train... found 28709 images in 7 classes  
val: D:\Desktop\Yolo-FaceEmotion\data\valid... found 3589 images in 7 classes  
test: D:\Desktop\Yolo-FaceEmotion\data\test... found 3589 images in 7 classes  
               classes   top1_acc   top5_acc: 100% ━━━━━━━━━━━━ 57/57 104.4it/s 0.5s
                   all      0.709      0.989
Speed: 0.0ms preprocess, 0.1ms inference, 0.0ms loss, 0.0ms postprocess per image
Results saved to D:\Desktop\Yolo-FaceEmotion\runs\classify\Emotion_Sys\v1_model
D:\pythonProject\venv\Lib\site-packages\ultralytics\utils\plotting.py:912: UserWarning: A NumPy version >=1.22.4 and <2.3.0 is required for this version of SciPy (detected version 2.4.4)
  from scipy.ndimage import gaussian_filter1d
训练完成！最优模型已保存在 Emotion_Sys/v1_model/weights/best.pt

进程已结束，退出代码为 0'''