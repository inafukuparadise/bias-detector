# bias_detector.py
BAD_WORDS = ["バカ", "キモい", "死ね", "差別", "部落", 
             "キチガイ", "自殺しろ", "殺す"]  # ← あなたが追加！

def check_bias(text):
    found = []
    for word in BAD_WORDS:
        if word in text:
            found.append(word)
    if found:
        return f"NG: 検出 → {', '.join(found)}"
    return "OK: 問題なし"

# テスト
print(check_bias("この人はキチガイだ"))  # → NG
print(check_bias("こんにちは"))          # → OK
