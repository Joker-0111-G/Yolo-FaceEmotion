import cv2
from ultralytics import YOLO


def run_realtime_system():
    # 1. 加载情绪分类引擎
    emotion_model = YOLO('runs/classify/Emotion_Sys/v1_model/weights/best.pt')

    # 2. 加载 OpenCV 内置的人脸检测器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 3. 启动本地摄像头 (0 代表默认摄像头)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("警告：无法打开摄像头！")
        return

    print("系统启动成功！对准摄像头做表情吧。按键盘 'q' 键退出。")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 将画面转为灰度图，大幅提升人脸检测速度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测画面中的人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

        for (x, y, w, h) in faces:
            # 适度向外扩展截取框，防止下巴或额头被切掉影响情绪判断
            padding = 15
            y1 = max(0, y - padding)
            y2 = min(frame.shape[0], y + h + padding)
            x1 = max(0, x - padding)
            x2 = min(frame.shape[1], x + w + padding)

            # 抠出人脸区域
            face_crop = frame[y1:y2, x1:x2]

            if face_crop.size == 0:
                continue

            # 送入 YOLO 进行前向推理，关闭 verbose 防止控制台被刷屏
            results = emotion_model(face_crop, verbose=False)

            # 提取置信度最高的结果
            top_idx = results[0].probs.top1
            emotion = results[0].names[top_idx]
            confidence = results[0].probs.top1conf.item()

            # 在画面上绘制绿色的识别框和文字信息
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{emotion} ({confidence * 100:.1f}%)"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # 渲染最终画面
        cv2.imshow('YOLO Emotion Recognition', frame)

        # 监听退出指令
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run_realtime_system()