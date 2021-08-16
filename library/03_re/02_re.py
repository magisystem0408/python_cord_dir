# /[a-z0-9]/+im

# /デリミタ/
# imは修飾詞

[]
# 文字または数字を一文字分指定する

# ^
# キャロット直後の文字または数字を指定しない

# -
# 範囲を指定する

# ()
# グループ化される

# 繰り返したいパターン

# 最短一致
# .{0,}?



# 日本語をカバーする正規表現

# ・ひらがな
# [ぁ-ん]
# [\u3041-\u3096]
# [\x{3041}-\x{3096}]
#
# ・カタカナ
# [ァ-ヶ]
# [\u30A1-\u30FA]
# [\x{30A1}-\x{30FA}]
#
# ・漢字
# [亜-熙]
# [々〇〻\u3400-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]
# [々〇〻\x{3400}-\x{9FFF}\x{F900}-\x{FAFF}]|[\x{D840}-\x{D87F}][\x{DC00}-\x{DFFF}]

# ・半角文字以外
# [^\x01-\x7E]