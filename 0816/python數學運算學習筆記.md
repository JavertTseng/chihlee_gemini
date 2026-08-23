# Python 數學運算學習筆記

本筆記用於學習 Python 在數學上的應用，涵蓋**中學、高中、大學**三個階段的數學運算範例，並附上詳細說明。

---

## 一、Python 基本數學運算子

在開始之前，先認識 Python 最基本的數學運算子：

| 運算子 | 說明 | 範例 | 結果 |
|:------:|------|------|:----:|
| `+` | 加法 | `7 + 3` | `10` |
| `-` | 減法 | `7 - 3` | `4` |
| `*` | 乘法 | `7 * 3` | `21` |
| `/` | 除法（回傳小數） | `7 / 3` | `2.333...` |
| `//` | 整數除法（無條件捨去小數） | `7 // 3` | `2` |
| `%` | 取餘數 | `7 % 3` | `1` |
| `**` | 次方 | `2 ** 10` | `1024` |
| `abs()` | 絕對值 | `abs(-5)` | `5` |
| `round()` | 四捨五入 | `round(3.14159, 2)` | `3.14` |

### 運算子優先順序（先算誰？）

Python 遵循數學上的「先乘除、後加減」，與括號優先：
1. **括號 `()`** 最優先
2. **次方 `**`**
3. **乘、除、取餘數 `* / // %`**
4. **加、減 `+ -`**

```python
# 範例：判斷括號的重要性
print(2 + 3 * 4)      # 3*4 先算 → 2 + 12 = 14
print((2 + 3) * 4)    # 括號先算 → 5 * 4 = 20
print(2 ** 3 ** 2)    # 次方由右往左 → 2 ** (3**2) = 2**9 = 512
```

---

## 二、國中數學範例（七年級～九年級）

### 範例 1：四則運算與質數判斷

**題目**：判斷一個數是不是質數（只能被 1 和自己整除）。

```python
def is_prime(n):
    """判斷 n 是否為質數"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需檢查到 √n 即可
        if n % i == 0:                      # 能被整除 → 不是質數
            return False
    return True

print(is_prime(17))   # True，17 是質數
print(is_prime(21))   # False，21 = 3 × 7
```

**詳細說明**：
- `range(2, int(n ** 0.5) + 1)`：從 2 檢查到 `√n`（n 的平方根）。因為若 `n = a × b`，則 `a` 或 `b` 至少一個小於等於 `√n`，所以檢查到平方根就夠了，可以大幅減少運算量。
- `%` 取餘數：若 `n % i == 0`，代表 `n` 可以被 `i` 整除。

### 範例 2：公因數與公倍數（輾轉相除法）

**題目**：求兩數的最大公因數（GCD）與最小公倍數（LCM）。

```python
def gcd(a, b):
    """輾轉相除法求最大公因數"""
    while b != 0:
        a, b = b, a % b    # 用 a % b 取代 a，直到餘數為 0
    return a

def lcm(a, b):
    """最小公倍數 = 兩數相乘 ÷ 最大公因數"""
    return a * b // gcd(a, b)

print(gcd(48, 36))   # 12
print(lcm(48, 36))   # 144
```

**詳細說明**：
- **輾轉相除法**（歐幾里得演算法）：重複執行「較大數 ÷ 較小數取餘數」，直到餘數為 0，最後的除數就是最大公因數。
  - 48 % 36 = 12 → 36 % 12 = 0 → 最大公因數 = 12
- Python 的 `a, b = b, a % b` 會同時交換兩數，不需要暫存變數。
- 而 `math` 模組其實已經內建 `math.gcd()`，之後會介紹。

### 範例 3：一元一次方程式求解

**題目**：解 `ax + b = c`，求 `x = (c - b) / a`。

```python
def solve_linear(a, b, c):
    """解 ax + b = c"""
    if a == 0:
        if b == c:
            return "無限多解"
        return "無解"
    return (c - b) / a

print(solve_linear(2, 3, 11))   # x = 4.0 → 2*4+3 = 11 ✓
print(solve_linear(0, 5, 5))    # 無限多解
print(solve_linear(0, 5, 6))    # 無解
```

**詳細說明**：
- 把 `b` 移到等號右邊：`ax = c - b`
- 再除以 `a`：`x = (c - b) / a`
- 當 `a = 0` 時要特別處理：若 `b = c` 則任何 x 都成立（無限多解）；否則無解。

### 範例 4：三角形面積（海龍公式）

**題目**：已知三角形三邊長 `a、b、c`，用海龍公式求面積。

```python
def triangle_area(a, b, c):
    """海龍公式：面積 = √(s(s-a)(s-b)(s-c))，s = 半周長"""
    s = (a + b + c) / 2                    # 半周長
    area_squared = s * (s - a) * (s - b) * (s - c)
    return area_squared ** 0.5             # 開根號

print(triangle_area(3, 4, 5))   # 6.0（直角三角形 3-4-5）
print(triangle_area(6, 8, 10))  # 24.0
```

**詳細說明**：
- **海龍公式（Heron's formula）**：`面積 = √[s(s−a)(s−b)(s−c)]`，其中 `s = (a+b+c)/2`。
- 開根號可以用 `** 0.5` 或 `math.sqrt()`。

---

## 三、高中數學範例

### 範例 5：等差數列與等比數列

**題目**：求等差數列第 n 項與前 n 項總和。

```python
def arithmetic_nth(a1, d, n):
    """等差數列第 n 項：a_n = a1 + (n-1)*d"""
    return a1 + (n - 1) * d

def arithmetic_sum(a1, d, n):
    """等差數列前 n 項和：S_n = n/2 * (2*a1 + (n-1)*d)"""
    return n * (2 * a1 + (n - 1) * d) // 2

# 範例：首項 3，公差 5，求第 10 項和前 10 項總和
print(arithmetic_nth(3, 5, 10))   # 3 + 9*5 = 48
print(arithmetic_sum(3, 5, 10))   # 10/2 * (2*3 + 9*5) = 255
```

**詳細說明**：
- 等差數列：每項相差固定的**公差 d**。
  - 第 n 項：`a_n = a1 + (n-1)d`
  - 前 n 項和：`S_n = n/2 × [2a1 + (n-1)d]`（也可用 `n × (首項+末項)/2`）
- 等比數列同理：`a_n = a1 × r^(n-1)`。

### 範例 6：多項式因式分解與根

**題目**：求一元二次方程式 `ax² + bx + c = 0` 的根（公式解）。

```python
import math

def quadratic_roots(a, b, c):
    """一元二次方程式公式解"""
    delta = b ** 2 - 4 * a * c        # 判別式 Δ = b² - 4ac
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"兩相異實根：x = {x1}, {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"重根：x = {x}"
    else:
        return "無實數根（有虛根）"

print(quadratic_roots(1, -5, 6))   # Δ=1 → x = 3.0, 2.0
print(quadratic_roots(1, 2, 1))    # Δ=0 → x = -1.0（重根）
print(quadratic_roots(1, 0, 1))    # Δ<0 → 無實數根
```

**詳細說明**：
- **判別式** `Δ = b² - 4ac` 決定根的情況：
  - `Δ > 0`：兩個相異實根
  - `Δ = 0`：一個重根
  - `Δ < 0`：無實數根（虛根，使用複數可解）
- **公式解**：`x = (−b ± √Δ) / (2a)`
- `math.sqrt()` 只能開「非負數」，若 Δ < 0 要開虛數需改用 `cmath.sqrt()`。

### 範例 7：三角函數與解三角形（正弦、餘弦定理）

**題目**：已知兩邊與夾角，求第三邊（餘弦定理）。

```python
import math

def law_of_cosines(a, b, angle_deg):
    """
    餘弦定理：c² = a² + b² - 2ab·cos(C)
    angle_deg：夾角 C（度）
    """
    C = math.radians(angle_deg)                  # 度 → 弧度
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
    return c

print(law_of_cosines(3, 4, 90))    # 5.0（90度夾角即畢氏定理）
print(law_of_cosines(5, 6, 60))    # ≈ 5.568
```

**詳細說明**：
- **弧度（radian）與度（degree）**：Python 的三角函數 `math.sin/cos/tan` 都要求**弧度**輸入，所以要先用 `math.radians(角度)` 轉換。
- **餘弦定理**：`c² = a² + b² − 2ab·cos(C)`，當 `C = 90°` 時 `cos(90°) = 0`，就退化為畢氏定理 `c² = a² + b²`。
- 常見轉換：`角度 → 弧度` 用 `math.radians()`，`弧度 → 角度` 用 `math.degrees()`。

### 範例 8：排列組合

**題目**：計算排列數 `P(n, k)` 與組合數 `C(n, k)`。

```python
import math

def perm(n, k):
    """排列數 P(n,k) = n! / (n-k)!"""
    return math.factorial(n) // math.factorial(n - k)

def comb(n, k):
    """組合數 C(n,k) = n! / (k! (n-k)!)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# 從 5 個人中選 3 人排隊（排列）vs 選 3 人參加比賽（組合）
print(perm(5, 3))   # 60
print(comb(5, 3))   # 10
```

**詳細說明**：
- **排列（有順序）**：`P(n,k) = n!/(n−k)!`，例：5 人選 3 人排隊有 60 種排法。
- **組合（無順序）**：`C(n,k) = n!/[k!(n−k)!]`，例：5 人選 3 人出賽有 10 種選法。
- Python 內建的 `math.comb(n, k)` 與 `math.perm(n, k)` 可以直接使用，更方便。

### 範例 9：指數與對數

**題目**：利用指數與對數解題（例如求 2 的幾次方 = 1024）。

```python
import math

# 對數：log₂(1024) = ?
print(math.log(1024, 2))    # 10.0，因為 2**10 = 1024

# 指數：e 的 3 次方
print(math.exp(3))          # ≈ 20.0855

# 自然對數：ln(e³) = 3
print(math.log(math.exp(3)))  # 3.0（math.log 預設是自然對數）

# 常用對數：log₁₀(1000) = ?
print(math.log10(1000))     # 3.0
```

**詳細說明**：
- **對數定義**：`log_a(b) = x ⟺ a^x = b`。`math.log(x, base)` 可指定底數。
- `math.exp(x)` = `e^x`，`math.log(x)` 預設為**自然對數** `ln(x)`（底數為 e ≈ 2.718）。
- 記憶口訣：對數是「次方的反向操作」。

---

## 四、大學數學範例

### 範例 10：微積分——導數與極限

**題目**：用數值方法計算函數 `f(x) = x²` 在 `x = 3` 的導數，以及逼近極限值。

```python
def derivative(f, x, h=1e-6):
    """
    數值微分：使用「對稱差分」公式
    f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def f(x):
    return x ** 2

print(derivative(f, 3))    # ≈ 6.0（數學上 f'(3) = 2*3 = 6）
print(derivative(lambda x: x**3, 2))   # ≈ 12.0（f'(x)=3x²，f'(2)=12）
```

**詳細說明**：
- **導數定義**：`f'(x) = lim[h→0] [f(x+h) − f(x)] / h`
- 但直接用這個公式誤差較大，改用**對稱差分** `[f(x+h) − f(x−h)] / (2h)` 更精確。
- `lambda` 是 Python 的匿名函數，適合一次性使用的小函數。
- `h` 取太小會因為浮點數精度出問題，通常取 `10⁻⁶` 左右。

### 範例 11：微積分——定積分（數值積分）

**題目**：用「黎曼和」與「辛普森法」數值計算 `∫₀¹ x² dx`。

```python
def riemann_sum(f, a, b, n=1000):
    """右端點黎曼和近似定積分"""
    h = (b - a) / n          # 每個子區間寬度
    total = 0
    for i in range(1, n + 1):
        total += f(a + i * h) * h   # 長方形面積：高 × 寬
    return total

def simpson(f, a, b, n=1000):
    """辛普森積分法（需 n 為偶數）"""
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2    # 奇數點係數 4，偶數點係數 2
        total += coef * f(a + i * h)
    return total * h / 3

f = lambda x: x ** 2
print(riemann_sum(f, 0, 1))   # ≈ 0.333（正確值 = 1/3）
print(simpson(f, 0, 1))       # ≈ 0.3333333333333333，更精確
```

**詳細說明**：
- **黎曼和**：把積分區間切成 n 等分，用長方形面積近似曲線下面積，n 越大越精確。
- **辛普森法**：用拋物線近似曲線，收斂速度快很多，誤差更小。
- 數學上 `∫₀¹ x² dx = 1/3`，辛普森法幾乎精確得到答案。
- 若不想自己寫，`scipy.integrate.quad()` 是專業的數值積分工具。

### 範例 12：線性代數——矩陣運算

**題目**：矩陣加法、乘法與行列式。

```python
def matrix_mult(A, B):
    """矩陣乘法：A(m×n) × B(n×p) = C(m×p)"""
    m, n = len(A), len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_det2(A):
    """2×2 矩陣行列式：det = ad - bc"""
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(matrix_mult(A, B))
# [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19, 22], [43, 50]]
print(matrix_det2(A))   # 1*4 - 2*3 = -2
```

**詳細說明**：
- **矩陣乘法**：`C[i][j]` 是 A 的第 i 列與 B 的第 j 行對應相乘再相加，前提是 A 的行數 = B 的列數。
- **行列式（2×2）**：`det = ad − bc`，若行列式為 0 代表矩陣不可逆。
- 實務上直接使用 `numpy`：`import numpy as np`、`np.dot(A, B)`、`np.linalg.det(A)`，速度快又方便。

### 範例 13：線性代數——解聯立方程組

**題目**：用高斯消去法解聯立方程組。

```
x +  y + z = 6
2x -  y + z = 3
x + 2y - z = 2
```

```python
def gauss_solve(A, b):
    """高斯消去法解 Ax = b（方陣）"""
    n = len(A)
    # 擴展增廣矩陣
    M = [row[:] + [b[i]] for i, row in enumerate(A)]

    # 前向消去（化為上三角）
    for col in range(n):
        pivot = M[col][col]
        if pivot == 0:
            for r in range(col + 1, n):
                if M[r][col] != 0:
                    M[col], M[r] = M[r], M[col]   # 交換列
                    pivot = M[col][col]
                    break
        for r in range(col + 1, n):
            factor = M[r][col] / pivot
            for c in range(col, n + 1):
                M[r][c] -= factor * M[col][c]

    # 後向代入（解上三角）
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = s / M[i][i]
    return x

A = [[1, 1, 1],
     [2, -1, 1],
     [1, 2, -1]]
b = [6, 3, 2]

print(gauss_solve(A, b))   # [1.0, 2.0, 3.0] → x=1, y=2, z=3
```

**詳細說明**：
- **高斯消去法**分兩階段：
  1. **前向消去**：透過列運算把係數矩陣化成上三角（主對角線以下全為 0）。
  2. **後向代入**：從最後一列開始逐一解出未知數。
- 主對角線元素（pivot）若為 0，需先交換列，否則會除零錯誤。
- 實務上直接使用 `numpy.linalg.solve(A, b)` 一行搞定。

### 範例 14：機率與統計——期望值與變異數

**題目**：計算一組資料的平均數、變異數、標準差。

```python
def mean(data):
    """平均數（期望值）"""
    return sum(data) / len(data)

def variance(data):
    """母體變異數：σ² = Σ(x - μ)² / n"""
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)

def std(data):
    """標準差：√σ²"""
    return variance(data) ** 0.5

scores = [85, 90, 78, 92, 88, 70, 95, 82]
print(f"平均數: {mean(scores):.2f}")        # 85.00
print(f"變異數: {variance(scores):.2f}")    # 61.50
print(f"標準差: {std(scores):.2f}")         # 7.84
```

**詳細說明**：
- **平均數（期望值）** `μ = Σxᵢ / n`：資料的集中趨勢。
- **母體變異數** `σ² = Σ(xᵢ − μ)² / n`：資料的離散程度。
- **標準差** `σ = √σ²`：與平均數相同單位的離散指標。標準差越大，代表資料越分散。
- 實務上可使用 `statistics.mean()`、`statistics.stdev()` 或 `numpy`。

---

## 五、實用的 `math` 模組總整理

```python
import math

# 常數
math.pi        # 圓周率 ≈ 3.14159
math.e         # 自然對數底 ≈ 2.71828
math.inf       # 無窮大
math.nan       # 不是數字

# 基本運算
math.sqrt(16)       # 平方根 → 4.0
math.factorial(5)   # 階乘 → 120
math.comb(5, 2)     # 組合 → 10
math.perm(5, 2)     # 排列 → 20
math.gcd(48, 36)    # 最大公因數 → 12
math.ceil(3.1)      # 無條件進位 → 4
math.floor(3.9)     # 無條件捨去 → 3
math.trunc(3.7)     # 取整數部分 → 3

# 指數與對數
math.pow(2, 10)     # 2 的 10 次方 → 1024.0
math.exp(1)         # e¹ → 2.718...
math.log(8, 2)      # log₂(8) → 3.0
math.log10(100)     # log₁₀(100) → 2.0

# 三角函數（注意：輸入需為弧度）
math.sin(math.pi / 2)   # sin(90°) → 1.0
math.cos(0)             # → 1.0
math.tan(math.pi / 4)   # tan(45°) → 1.0
math.asin(1)            # arcsin(1) → π/2
math.degrees(math.pi)   # 弧度轉角度 → 180.0
math.radians(180)       # 角度轉弧度 → π
```

---

## 六、練習題（自我測試）

1. **國中**：寫一個程式，找出 100 以內的所有質數。
2. **國中**：輸入年月日，計算該日是西元第幾天（提示：判斷閏年）。
3. **高中**：求等比數列 2, 6, 18, 54... 的第 8 項與前 8 項總和。
4. **高中**：使用餘弦定理，已知三邊長求三角形其中一個夾角。
5. **大學**：用數值方法估算 `∫₀ᵖⁱ sin(x) dx`（正確答案為 2）。
6. **大學**：用高斯消去法解 4 個未知數的聯立方程組，並與 `numpy` 結果比較。

---

> **小提醒**：當運算變複雜或資料量很大時，建議使用 `numpy`、`scipy`、`sympy`（符號運算）等專業套件，它們經過最佳化且內建大量數學函式。
