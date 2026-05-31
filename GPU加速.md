pip uninstall torch torchvision torchaudio 
删除默认pytorch 安装有GPU加速的
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --force-reinstall

使用交大镜像 
pip install torch torchvision torchaudio --index-url https://mirror.sjtu.edu.cn/pytorch-wheels/cu118 --force-reinstall

