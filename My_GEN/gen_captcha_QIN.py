import os
import shutil
import string
import random
from PIL import Image, ImageDraw, ImageFont

# 定义颜色和字体列表
colors1 = ['red', 'blue', 'green', 'purple', 'brown', 'orange', 'black']
colors2 = ['black']
font1 = "arial.ttf"
font2 = r'font_room\Arial Black.ttf'
font3 = r'font_room\DFPShaoNvW5-GB.ttf'
font4 = r'font_room\huawennishu.TTF'
font5 = r'font_room\PingFang SC Regular.ttf'
fontlist1 = [font1, font2, font3, font4, font5]
fontlist2 = [font1, font3, font5]
fontlist3 = [font2, font4]
fontlist4 = [font1]
fontlist5 = [font2]
fontlist6 = [font3]
fontlist7 = [font4]
fontlist8 = [font5]

# 验证码生成函数
def generate_captcha_image(captcha_text):
    # 随机生成背景颜色
    if random.random() < 0.3:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        color = 'white'
    
    # 创建新图像，大小为320x120
    image = Image.new('RGB', (320, 120), color)
    draw = ImageDraw.Draw(image)

    # 随机选择验证码文本颜色
    if random.random() < 0.7:
        color = random.choice(colors1)
    else:
        color = random.choice(colors2)

    # 绘制验证码文本，每个字符随机选择字体
    for i in range(len(captcha_text)):
        randomnum2 = random.random()
        if randomnum2 <= 0.2:
            font = random.choice(fontlist1)
        elif 0.2 < randomnum2 <= 0.3:
            font = random.choice(fontlist2)
        elif 0.3 < randomnum2 <= 0.4:
            font = random.choice(fontlist3)
        elif 0.4 < randomnum2 <= 0.5:
            font = random.choice(fontlist4)
        elif 0.5 < randomnum2 <= 0.6:
            font = random.choice(fontlist5)
        elif 0.6 < randomnum2 <= 0.7:
            font = random.choice(fontlist6)
        elif 0.7 < randomnum2 <= 0.8:
            font = random.choice(fontlist7)
        else:
            font = random.choice(fontlist8)
        font = ImageFont.truetype(font, random.randint(20, 30))
        draw.text((i * random.randint(15, 25) + 120, random.randint(29, 39)), captcha_text[i], font=font, fill=color)

    # 随机添加干扰线
    if random.random() < 0.3:
        for _ in range(random.randint(0, 7)):
            x1 = random.randint(0, 320)
            y1 = random.randint(0, 120)
            x2 = random.randint(0, 320)
            y2 = random.randint(0, 120)
            draw.line(((x1, y1), (x2, y2)), fill=random.choice(colors1), width=random.randint(1, 3))

    # 随机扭曲图像
    if random.random() < 0.3:
        image = image.transform((320, 120), Image.AFFINE, (1, random.uniform(-0.2, 0.2), 0, -0.1, 1, 0))

    # 随机添加背景噪声点
    if random.random() < 0.3:
        for _ in range(random.randint(0, 3000)):
            x = random.randint(0, 320)
            y = random.randint(0, 120)
            draw.point((x, y), fill='black')

    # 随机生成裁剪区域的坐标
    if random.random() < 0.2:
        left = 320 / random.uniform(2.9, 5)
        top = 120 / random.uniform(2.9, 5)
        right = 320 / 3 * random.uniform(1.9, 3.2)
        bottom = 120 / 3 * random.uniform(1.9, 3.3)
    else:
        left = 320 / 3
        top = 120 / 3
        right = 320 / 3 * 2
        bottom = 120 / 3 * 2

    # 裁剪图片
    image = image.crop((left, top, right, bottom))

    # 随机选择目标大小并调整图像大小
    if random.random() < 0.5:
        num = random.uniform(0.8, 3.0)
        w, h = image.size
        target_width = w * num
        target_height = h * num
    else:
        target_width = 160
        target_height = 60
    
    image = image.resize((int(target_width), int(target_height)))
    return image

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
    path = './gen_pic'
    if not os.path.exists(path):
        os.makedirs(path)
    
    clear_folder(path)  # 清空文件夹

    length = 4  # 验证码长度
    num = 300  # 生成验证码数量
    characters = string.ascii_uppercase + string.digits  # 验证码字符集
    
    # 生成验证码图片并保存
    for i in range(num):
        captcha_text = ''.join(random.choices(characters, k=length))  # 生成随机验证码文本
        image = generate_captcha_image(captcha_text)  # 生成验证码图片
        image.save(f"./gen_pic/{captcha_text}.png")  # 保存图片
        print(f"Generated {i+1}: {captcha_text}")  # 打印生成信息
