from pathlib import Path


print("你好，Python！")

# 變數可以保存不同種類的資料
name = "小安"
age = 18
score = 92.5

print(f"我是{name}，今年{age}歲。")
print(f"我的練習分數是 {score} 分。")

# 簡單運算
apples = 3
oranges = 2
print(f"水果總數：{apples + oranges}")

# 根據條件選擇要執行的程式
if score >= 60:
    print("練習結果：及格")
else:
    print("練習結果：再試一次")

# 清單和迴圈
fruits = ["蘋果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜歡吃{fruit}")

# 定義函式並使用它
def add(number_a, number_b):
    return number_a + number_b


total = add(4, 5)
print(f"4 + 5 = {total}")

# 讀取與本程式放在一起的 notes.txt
notes_path = Path(__file__).with_name("notes.txt")
notes = notes_path.read_text(encoding="utf-8")
print("從 notes.txt 讀到的內容：")
print(notes)
