import easyocr
import cv2
# from google.colab.patches import cv2_imshow
reader = easyocr.Reader(['ja','en']) # 文字の選択一回だけでいい
path = r"C:\Users\salmi\Downloads\test.png"
#path = r"C:\Users\salmi\git-kun\src\text\kinkakuji.png"
result2 = reader.readtext(path, detail=0) # 文章のみ
print(result2)