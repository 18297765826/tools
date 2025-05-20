import os
import pandas as pd

def convert_excel_to_csv(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            file_path = os.path.join(input_dir, filename)
            try:
                # 读取 Excel 文件（默认读取第一个工作表）
                df = pd.read_excel(file_path, sheet_name=0)

                # 生成对应的 CSV 文件名
                csv_filename = os.path.splitext(filename)[0] + ".csv"
                csv_path = os.path.join(output_dir, csv_filename)

                # 保存为 CSV 文件
                df.to_csv(csv_path, index=False, encoding="utf-8")
                print(f"已转换: {filename} -> {csv_filename}")
            except Exception as e:
                print(f"转换失败: {filename}，原因: {e}")


# 使用示例
input_folder = "input_path"      # 输入文件夹路径
output_folder = "output_path"  # 输出文件夹路径
convert_excel_to_csv(input_folder, output_folder)
