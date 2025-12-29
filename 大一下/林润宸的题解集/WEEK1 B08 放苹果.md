# **B08 放苹果** <span id="sectionB08"></span>

## 题目分析

有 M 个相同的苹果和 N 个相同的盘子，允许有的盘子空着不放。求将苹果全部放入盘子的不同放法总数（5,1,1 和 1,5,1 视为同一种放法）。

## 解题思路


### 1. 递归分治

1. **定义函数 f(a, b)：**将 a 个苹果放入 b 个盘子的放法数。通过分类讨论分解问题：

    - 至少一个空盘：放法数等价于 
	### <math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>f</mi><mo stretchy="false">(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></math>

    - 无空盘：每个盘子至少放 1 个苹果，等价于先放 b 个苹果（每盘 1 个），剩余 a-b 个苹果放 b 个盘子，即 f(a-b, b)

2. **递推关系：**
### <math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>f</mi><mo stretchy="false">(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo stretchy="false">)</mo><mo>=</mo><mi>f</mi><mo stretchy="false">(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>+</mo><mi>f</mi><mo stretchy="false">(</mo><mi>a</mi><mo>−</mo><mi>b</mi><mo>,</mo><mi>b</mi><mo stretchy="false">)</mo></math>
3. **边界处理：**

    - 盘子过多：b > a → 多余盘必空，等价于 f(a, a)

    - 无苹果：a = 0 → 仅 1 种放法（全空盘）

    - 无盘子：b ≤ 0 → 无法放置，返回 0

### 2. 动态规划

**针对递归的重复计算问题，使用 DP 表存储子问题解。相比递归，动态规划可以有效减少重复计算次数。**

## 算法

### 推公式 -> 递归 or 动态规划（dp）###

### **\* 动态规划（Dynamic Programming）**

**动态规划（DP） 是一种解决复杂问题的算法思想，它将问题分解为相互重叠的子问题，通过保存子问题的解避免重复计算，从而高效求解原问题。其核心特征：**

1. **重叠子问题：** 问题可分解为重复出现的子问题

2. **最优子结构：** 问题最优解包含子问题最优解

3. **状态转移：** 子问题之间存在递推关系

### 模板
```cpp
for (int j = 0; j <= n; j++) dp[0][j] = 1 or 0;//预处理，不固定

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
				dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...) //递归关系，因题目而相异
            }
        }
```

## 代码示例 1 递归
```cpp
#include <iostream>
using namespace std;

int f(int a, int b) {
    if (b > a) return f(a, a);  // 盘子过多 → 等价于f(a,a)
    if (a == 0) return 1;       // 无苹果 → 仅1种放法
    if (b <= 0) return 0;       // 无盘子 → 无法放置
    return f(a, b - 1) + f(a - b, b);  // 分类讨论：有空盘 + 无空盘
}

int main() {
    int cnt;
    cin >> cnt;  // 测试用例数
    while (cnt--) {
        int m, n;
        cin >> m >> n;  // 苹果数m, 盘子数n
        cout << f(m, n) << endl;
    }
    return 0;
}
```

## 代码示例 2 dp
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int cnt;
    cin >> cnt;
    while (cnt--) {
        int m, n;
        cin >> m >> n;
        // dp[i][j]: i个苹果放j个盘子的放法数
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // 初始化：无苹果时放法数为1
        for (int j = 0; j <= n; j++) dp[0][j] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (j > i) {
                    dp[i][j] = dp[i][i];  // 盘子过多 → 等价于dp[i][i]
                } else {
                    // 分类讨论：有空盘 + 无空盘
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j];
                }
            }
        }
        cout << dp[m][n] << endl;
    }
    return 0;
}
```