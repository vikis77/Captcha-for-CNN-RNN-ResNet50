import os
import shutil
import string
import random
from PIL import Image, ImageDraw, ImageFont

folder_path = r'Captcha_GEN\gen_pic'
# 定义颜色和字体列表
colors1 = ['red', 'blue', 'green', 'purple', 'brown', 'orange', 'black']
colors2 = ['black']
font1 = "arial.ttf"
font2 = r'Captcha_GEN\font_room\Arial Black.ttf'
font3 = r'Captcha_GEN\font_room\DFPShaoNvW5-GB.ttf'
font4 = r'Captcha_GEN\font_room\Y-B008YeZiGongChangDanDanHei-2.ttf'
font5 = r'Captcha_GEN\font_room\PingFang SC Regular.ttf'
font6 = r'Captcha_GEN\font_room\SanJiLuoLiHei-2.ttf'
font7 = r'Captcha_GEN\font_room\Franklin Gothic Medium_0.ttf'
fontlist4 = [font1]
fontlist5 = [font2]
fontlist6 = [font3] #弯弯字体
fontlist7 = [font4]
fontlist8 = [font5]
fontlist9 = [font6]
fontlist10 = [font7]

# 验证码生成函数
def generate_captcha_image(user_input=''):

    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    # 检查文件数量是否超过限制
    if len(files) > 500:
        # 清空文件夹
        for file in files:
            file_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # 删除文件或链接
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # 删除文件夹及其内容
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    if user_input!='':
        captcha_text = user_input
    else:
        length = 4  # 验证码长度
        characters = (string.ascii_uppercase + string.digits).replace('I','').replace('O','')  # 验证码字符集
        captcha_text = ''.join(random.choices(characters, k=length))  # 生成随机验证码文本

    # 随机生成背景颜色
    if random.random() < 0.3:
        color_bg = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    else:
        color_bg = 'white'
    
    # 创建新图像，大小为320x120
    image = Image.new('RGB', (320, 120), color_bg)
    draw = ImageDraw.Draw(image)

    # 随机选择验证码文本颜色
    if random.random() < 0.7:
        color = random.choice(colors1)
    else:
        color = random.choice(colors2)

    # 绘制验证码文本，每个字符随机选择字体
    randomnum2 = random.random()
    if randomnum2 <= 0.1:
        font = random.choice(fontlist4)
    elif 0.1 < randomnum2 <= 0.2:
        font = random.choice(fontlist5)
    elif 0.2 < randomnum2 <= 0.3:
        font = random.choice(fontlist6)
    elif 0.3 < randomnum2 <= 0.4:
        font = random.choice(fontlist7)
    elif 0.4 < randomnum2 <= 0.5:
        font = random.choice(fontlist8)
    elif 0.5 < randomnum2 <= 0.6:
        font = random.choice(fontlist9)
    else:
        font = random.choice(fontlist10)

    # 字体大小根据随机数的大小来确定
    if randomnum2 <=0.2:
        font = ImageFont.truetype(font, random.randint(30, 46))
    elif 0.2< randomnum2 <=0.6:
        font = ImageFont.truetype(font, 35)
    else:
        font = ImageFont.truetype(font, 40)
    # 50%的概率下将验证码文本旋转
    if random.random()<0.5:
        for i in range(len(captcha_text)):
            # 创建一个新的透明图像
            char_image = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
            # 在新的图像上绘制验证码文本
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((1, 1), captcha_text[i], font=font, fill=color)
            # 将验证码文本旋转
            angle = random.uniform(-45, 45)
            char_image = char_image.rotate(angle, expand=1)
            # 将旋转的验证码文本粘贴到主图像上
            image.paste(char_image, (i * random.randint(32, 34) + 95, 24), char_image)
    else:
        for i in range(len(captcha_text)):
            # 创建一个新的透明图像
            char_image = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
            # 在新的图像上绘制验证码文本
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((1, 1), captcha_text[i], font=font, fill=color)
            # 将验证码文本旋转
            angle = random.uniform(0, 0)
            char_image = char_image.rotate(angle, expand=1)
            # 将旋转的验证码文本粘贴到主图像上
            image.paste(char_image, (i * random.randint(32, 34) + 95, 24), char_image)

    # 随机添加干扰线
    if random.random() < 0.4:
        for _ in range(random.randint(0, 3)):
            x1 = random.randint(0, 320)
            y1 = random.randint(0, 120)
            x2 = random.randint(0, 320)
            y2 = random.randint(0, 120)
            draw.line(((x1, y1), (x2, y2)), fill=random.choice(colors1), width=random.randint(1, 3))

    # 随机扭曲图像
    if random.random() < 0.3:
        image = image.transform((320, 120), Image.AFFINE, (1, random.uniform(-0.2, 0.2), 0, -0.1, 1, 0))

    # 随机添加背景噪声点
    if random.random() < 0.6:
        for _ in range(random.randint(0, 2700)):
            x = random.randint(0, 320)
            y = random.randint(0, 120)
            draw.point((x, y), fill='black')

    # 随机生成裁剪区域的坐标
    if random.random() < 0.2:
        left = 80+random.uniform(-50, 20)
        top = 30+random.uniform(-15, 0)
        right = 240+random.uniform(-20, 50)
        bottom = 90+random.uniform(5, 15)
    else:
        left = 80
        top = 30
        right = 240
        bottom = 90
    image = image.crop((left, top, right, bottom))

    # 随机选择目标大小并调整图像大小
    w, h = image.size
    if random.random() < 0.5:
        num = random.uniform(0.8, 3.0)
        w = w * num
        h = h * num
    
    image = image.resize((int(w), int(h)))

    image.save(f"./Captcha_GEN/gen_pic/{captcha_text}.png")  # 保存图片
    
    return captcha_text,image

# 清空文件夹函数
def clear_folder(folder_path):
    # 遍历文件夹中的所有文件和子文件夹并删除
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

if __name__ == '__main__':
    # 定义生成图片的文件夹路径
    path = './Captcha_GEN/gen_pic'
    if not os.path.exists(path):
        os.makedirs(path)
    
    clear_folder(path)  # 清空文件夹

    num = 50  # 生成验证码数量
    
    # 生成验证码图片并保存
    for i in range(num):
        captcha_text,image = generate_captcha_image()  # 生成验证码图片
        print(f"Generated {i+1}: {captcha_text}")  # 打印生成信息
        
