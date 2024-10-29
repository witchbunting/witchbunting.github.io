from PIL import Image

def change_opacity(image_path, output_path, opacity=0.5):
    # 打开图片并转换为 RGBA 模式（支持透明度）
    image = Image.open(image_path).convert("RGBA")
    
    # 获取图片的像素数据
    pixels = image.getdata()
    
    # 修改每个像素的透明度
    new_pixels = [
        (r, g, b, int(a * opacity)) for r, g, b, a in pixels
    ]
    
    # 更新图片的像素数据
    image.putdata(new_pixels)
    
    # 保存修改后的图片
    image.save(output_path)

# 示例调用
change_opacity("background.png", "background1.png", opacity=0.3)