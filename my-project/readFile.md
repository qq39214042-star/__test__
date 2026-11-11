# Python 初學者一步一步練習

這份練習從最基本的輸出開始，接著認識變數、判斷、迴圈、函式，最後練習讀取文字檔。建議照順序操作，每次只改一小段，再執行看看結果。

## 開始之前

請先安裝 Python 3，並在 VS Code 開啟這個專案資料夾。開啟終端機（選單：**終端機 → 新增終端機**），輸入以下指令確認 Python 可以使用：

```powershell
py --version
```

如果看到類似 `Python 3.12.x` 的版本資訊，就可以繼續。若 `py` 無法使用，也可以試試：

```powershell
python --version
```

本練習的範例檔是 [`examples/python_basics.py`](examples/python_basics.py)。在專案根目錄的終端機執行：

```powershell
py examples\python_basics.py
```

如果使用 `python` 指令，則執行：

```powershell
python examples\python_basics.py
```

## 練習 1：讓 Python 顯示文字

開啟 `examples/python_basics.py`，找到第一個 `print(...)`。`print` 會把括號中的內容顯示在終端機：

```python
print("你好，Python！")
```

試著把文字改成自己的問候語，儲存後重新執行範例檔。

**小練習：** 再加一行 `print("我正在學 Python。")`，看看它會顯示在哪裡。

## 練習 2：認識註解與變數

以 `#` 開頭的是註解，Python 會忽略它，常用來寫給人看的說明：

```python
# 這是註解，不會被當成程式執行
```

變數可以用來保存資料：

```python
name = "小安"
age = 18
print(name)
print(age)
```

文字要用引號包起來；數字不用引號。`=` 在這裡表示把右邊的值存進左邊的變數。

**小練習：** 把 `name` 改成自己的名字，並新增 `favorite_food = "壽司"`，用 `print` 顯示它。

## 練習 3：文字、數字與簡單運算

範例檔中的 `score` 是整數，`price` 是小數，`message` 是文字。你可以用 `+`、`-`、`*`、`/` 做基本運算：

```python
apples = 3
oranges = 2
print(apples + oranges)
```

用 f-string 可以把變數放進文字中，注意字串前面有 `f`，變數放在 `{}` 裡：

```python
name = "小安"
print(f"你好，{name}！")
```

**小練習：** 在範例中新增兩個數字變數，印出它們相加的結果。

## 練習 4：用 `if` 做判斷

程式可以根據條件選擇要執行的內容：

```python
temperature = 28

if temperature >= 30:
    print("今天很熱")
else:
    print("今天還可以")
```

條件成立時執行 `if` 下方縮排的程式，否則執行 `else` 下方縮排的程式。Python 使用縮排表示程式區塊，請保留範例中的四個空格。

**小練習：** 改變範例中的 `score`，觀察程式輸出的結果如何改變。

## 練習 5：清單與 `for` 迴圈

清單可以保存多筆資料，資料放在方括號 `[]` 裡：

```python
fruits = ["蘋果", "香蕉", "橘子"]
```

`for` 可以逐一取出清單中的項目：

```python
for fruit in fruits:
    print(fruit)
```

**小練習：** 在 `fruits` 清單中加一種水果，再執行程式，確認它也會被印出來。

## 練習 6：建立自己的函式

函式是可以重複使用的一段程式。用 `def` 定義函式，呼叫它才會執行：

```python
def greet(name):
    print(f"你好，{name}！")

greet("小安")
```

範例檔中的 `add` 函式會收到兩個數字，並用 `return` 傳回相加的結果。

**小練習：** 呼叫 `add` 時換成不同的數字，看看結果有什麼變化。

## 練習 7：讀取文字檔

範例檔會讀取同一個資料夾中的 [`examples/notes.txt`](examples/notes.txt)。它使用 `pathlib` 找到文字檔，再用 UTF-8 編碼讀取，讓中文內容也能正確顯示：

```python
from pathlib import Path

notes_path = Path(__file__).with_name("notes.txt")
text = notes_path.read_text(encoding="utf-8")
print(text)
```

`notes.txt` 必須和 `python_basics.py` 放在同一個資料夾。你可以開啟 `notes.txt` 加上一行自己的文字，再重新執行範例檔。

## 建議的練習方式

1. 先執行一次範例檔，確認終端機有顯示內容。
2. 每次只做一個「小練習」，儲存後再執行。
3. 如果看到錯誤，先檢查引號、括號和縮排是否完整。
4. 可以試著改變範例中的值，預測結果，再執行確認。

## 完成後挑戰

- 將 `fruits` 改成你喜歡的三種食物。
- 用 `if` 判斷一個數字是大於、等於或小於 10。
- 寫一個函式，接收姓名並回傳一段問候文字。
- 在 `notes.txt` 寫入自己的學習目標，讓範例程式讀出來。
