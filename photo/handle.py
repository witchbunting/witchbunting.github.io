import os

def rename_images_in_directory(directory_path):
    # 获取目录下的所有文件，并过滤出 .jpg 文件
    files = [f for f in os.listdir(directory_path) if f.lower().endswith('.jpg')]
    
    # 对文件排序以确保按序号顺序重命名
    files.sort()
    
    # 遍历并重命名每个文件
    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(directory_path, filename)
        new_filename = f"{index}.jpg"  # 按序号生成新的文件名
        new_path = os.path.join(directory_path, new_filename)
        
        # 重命名文件
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

# 示例调用
rename_images_in_directory("观鸟/plant_and_other/")