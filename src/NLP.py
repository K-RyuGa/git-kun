from googletrans import Translator

translator = Translator()
quit_list = ["q","Q","ｑ","Ｑ"]

while(1):
    text_ja = input("英語翻訳したい日本語(exit:q)：")
    if text_ja in quit_list:
        exit()
    text_en = translator.translate(text_ja, src='ja', dest='en').text
    print(text_en)
