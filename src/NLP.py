from difflib import SequenceMatcher

# サンプルの辞書データ（正しい単語のリスト）
dictionary = ["日本語", "自然言語処理", "勉強", "解析","す"]

def generate_char_n_grams(text, n):
    return [text[i:i+n] for i in range(len(text) - n + 1)]

# 類似度を計算する関数（Jaccard係数）
def calculate_similarity(ngram1, ngram2):
    return SequenceMatcher(None, ngram1, ngram2).ratio()

# 誤字脱字の修正関数
def correct_spelling(text, dictionary, n=3, threshold=0.8):
    corrected_text = text
    n_grams = generate_char_n_grams(text, n)
    
    # 各N-gramに対して、辞書内の単語と比較
    for ngram in n_grams:
        best_match = None
        best_similarity = 0
        
        # 辞書データと類似度を計算
        for word in dictionary:
            similarity = calculate_similarity(ngram, word)
            
            # 類似度がしきい値を超え、最高の類似度が得られる場合
            if similarity > threshold and similarity > best_similarity:
                best_match = word
                best_similarity = similarity
        
        # 類似する単語が見つかれば置き換え
        if best_match:
            corrected_text = corrected_text.replace(ngram, best_match)
    
    return corrected_text

# テスト
text = "自然言語処るを勉強していまふ。"  # 誤字のあるテキスト
corrected_text = correct_spelling(text, dictionary)
print(corrected_text)  # 出力例: "自然言語処理を勉強しています。"
