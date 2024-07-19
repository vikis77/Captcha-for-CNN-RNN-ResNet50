# 基于ResNet50，CNN，RNN的四位验证码识别

![alt text](Snipaste_2024-07-19_17-09-08.png)
![alt text](Snipaste_2024-07-19_17-09-43.png)
![alt text](Snipaste_2024-07-19_17-10-30.png)

RNN预测模型训练准确率约为：92.0%，预测500张图用时：00:03:35，实际预测正确率：94.2%

CNN预测模型训练准确率约为：90.3%，预测500张图用时：00:05:56，实际预测正确率：63.8%

ResNet50预测模型训练准确率约为：94.5%，预测500张图用时：00:06:28，实际预测正确率：94.0%

由于CNN/model_1004-1.6.pth模型权重文件体积较大，如需请联系作者。

CNN模型的预测准确率较低，若不需要使用该模型，可将与该模型相关的代码删除或修改即可。

通过运行对应语句安装环境

`pip install -r requriements.txt`

确定相关路径没有问题后运行启动命令即可

`streamlit run .\App\App.py`

感谢

[**[Resnet50-for-captche](https://github.com/kevinzhao080/Resnet50-for-captche)**]作者: kevinzhao

[**[RNN-for-captche](https://gitee.com/oceanwang12138/captcha_identify)**]作者: Ocean

不知名作者 999感冒灵颗粒
