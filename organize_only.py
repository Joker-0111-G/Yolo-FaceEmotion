"""
将 FER2013 图片按表情分类整理到子文件夹
用法: python organize_only.py
"""

import os, shutil

BASE = r"D:\Desktop\Yolo-FaceEmotion\data"

for subset in ["train", "valid", "test"]:
    src = os.path.join(BASE, subset, "images")
    if not os.path.exists(src):
        print(f"跳过 {subset}（不存在）")
        continue

    # 获取所有 png 文件
    files = [f for f in os.listdir(src) if f.endswith(".png")]
    print(f"\n{subset}: {len(files)} 张")

    for fname in files:
        # 文件名格式: Anger_0.png → 提取 Anger
        emotion = fname.split("_")[0]

        # 创建对应分类文件夹
        dst_dir = os.path.join(BASE, subset, emotion)
        os.makedirs(dst_dir, exist_ok=True)

        # 移动文件
        shutil.move(os.path.join(src, fname), os.path.join(dst_dir, fname))

    # 删除空了的 images 目录
    try:
        os.rmdir(src)
    except:
        pass

    # 统计
    for emo in sorted(os.listdir(os.path.join(BASE, subset))):
        d = os.path.join(BASE, subset, emo)
        if os.path.isdir(d):
            print(f"   {emo}: {len(os.listdir(d))} 张")

print("\n完成！目录结构：")
print(r"train/Anger/  train/Happy/  train/Neutral/  ...")
print(r"valid/Anger/  valid/Happy/  valid/Neutral/  ...")
print(r"test/Anger/   test/Happy/   test/Neutral/   ...")
