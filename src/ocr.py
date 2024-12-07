import easyocr
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(title="ファイルを選択してください")

reader = easyocr.Reader(['ja','en'])
# path = "text/tegaki.jpg" # git-kun/src/text/
combined_text = ""

result = reader.readtext(path, detail=0) # 文章のみ
result_all = reader.readtext(path, paragraph=True)

for text in result:
    print(text, end="")
    combined_text += text
    combined_text = combined_text.replace('\n', '')

output_dir = 'output_text'
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'result.txt')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(combined_text)