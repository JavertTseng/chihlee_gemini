# ── 1. 基本 print ────────────────────────────────────────────────
print("Hello, World!")
print(123, 3.14, True)               # 同時印多個值，預設用空格隔開
print("a", "b", "c", sep="-")       # 自訂分隔符號
print("第一行", end=" ")             # end 預設是 \n，這裡改成空格
print("接在同一行")

# ── 2. f-string 格式化 ───────────────────────────────────────────
name = "小明"
score = 87.5
print(f"\n姓名：{name}，分數：{score:.1f}")   # 保留一位小數
print(f"{'置中':^20}")                        # 寬度 20 置中對齊
print(f"{'靠右':>20}")                        # 靠右對齊
print(f"{'靠左':<20}|")                       # 靠左對齊

# ── 3. 迴圈 + print 組合 ─────────────────────────────────────────
print("\n九九乘法表（3 的倍數）：")
for i in range(1, 10):
    print(f"3 x {i} = {3*i:2d}")            # :2d 讓數字佔兩格，對齊

# ── 4. 星號三角形 ────────────────────────────────────────────────
print("\n直角三角形：")
for row in range(1, 6):
    print("★" * row)

print("\n等腰三角形：")
height = 5
for row in range(1, height + 1):
    spaces = " " * (height - row)
    stars  = "★" * (2 * row - 1)
    print(spaces + stars)

# ── 5. 清單與字典的漂亮輸出 ─────────────────────────────────────
fruits = ["蘋果", "香蕉", "芒果", "草莓"]
print("\n水果清單：")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

grades = {"國文": 90, "數學": 78, "英文": 85, "自然": 92}
print("\n成績單：")
for subject, grade in grades.items():
    bar = "█" * (grade // 10)               # 每 10 分一格
    print(f"  {subject}：{bar} {grade}")

# ── 6. 分隔線與標題框 ────────────────────────────────────────────
def print_box(title: str) -> None:
    width = len(title) + 4
    print("\n┌" + "─" * width + "┐")
    print(f"│  {title}  │")
    print("└" + "─" * width + "┘")

print_box("期末總結")
print_box("Python 練習")

# ── 7. 數字金字塔 ────────────────────────────────────────────────
print("\n數字金字塔：")
rows = 5
for i in range(1, rows + 1):
    nums = " ".join(str(n) for n in range(1, i + 1))
    print(f"{'':>{rows - i}}{nums}")

# ── 8. 進度條模擬 ────────────────────────────────────────────────
print("\n模擬進度條：")
total = 20
for i in range(total + 1):
    filled = "█" * i
    empty  = "░" * (total - i)
    percent = i / total * 100
    print(f"\r  [{filled}{empty}] {percent:5.1f}%", end="", flush=True)
print("\n完成！")
