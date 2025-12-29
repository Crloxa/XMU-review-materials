# **<span id="section2A05"></span>WEEK2 A05 击杀黄金蛋糕人马**

## 题目分析

给定一个宽度w，高度h的蛋糕，要求把它分成m块时，（即切m-1刀时）这m块中最大蛋糕面积的最小值。（注意，蛋糕边长都是整数）

## 解题思路

### 记忆化搜索 + DFS

1. **状态定义：** 

-   way[w][h][k] 表示当前蛋糕尺寸为 w × h，还需切 k 刀（即分成 k+1 块）时，最大蛋糕块面积的最小值。

<br>

2. **状态转移：** 

-   **竖切：** 在宽度 x 处切一刀（1 ≤ x < w），将蛋糕分为左右两部分（x × h 和 (w − x) × h）。分配 j 刀给左边，k − 1 − j 刀给右边，更新最小值。

-   **横切：** 在高度 y 处切一刀（1 ≤ y < h），将蛋糕分为上下两部分（w × y 和 w × (h − y)）。分配 j 刀给上边，k − 1 − j 刀给下边，更新最小值。

<br>

3. **边界条件：**

-   若蛋糕面积 w × h 小于总块数 k + 1（每块至少 1 单位面积），返回不可能值（INF）。

-   若 k=0（无需再切），返回当前蛋糕面积 w × h。

4. **记忆化：** 避免重复计算已处理的状态。

5. **代码附有详细注释。**


## 代码示例
```cpp
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<unordered_map>
#include<cstring>
#include<cstdio>
#include <cstdlib>
using namespace std;

const int N = 23;          // 蛋糕宽高的最大尺寸
const int INF = 0x3f3f3f3f; // 表示不可能的巨大值
int way[N][N][N * N];       // 记忆化数组：way[w][h][k] 表示w*h蛋糕还需切k刀时的最优解

// DFS函数：计算w*h的蛋糕还需切m刀时，最大蛋糕块的最小面积
int dfs(int w, int h, int m) {
    // 边界1：蛋糕面积 < 总块数(m+1) -> 无法切割
    if (w * h < m + 1)  
        return INF;

    // 边界2：无需再切（m=0），返回当前蛋糕面积
    if (m == 0) 
        return w * h;

    // 记忆化：已计算过则直接返回
    if (way[w][h][m] != -1) 
        return way[w][h][m];

    int mn = INF; // 初始化最小值为极大值

    // 枚举所有竖切位置（垂直切割，沿宽度方向）
    for (int i = 1; i < w; i++) {   // i: 切割位置（左边宽度为i）
        for (int j = 0; j < m; j++) { // j: 分配给左半部分的刀数（0 ~ m-1）
            int leftPart = dfs(i, h, j);          // 左半部分切j刀
            int rightPart = dfs(w - i, h, m - 1 - j); // 右半部分切m-1-j刀
            // 当前方案的最大面积 = max(左半部分结果, 右半部分结果)
            mn = min(mn, max(leftPart, rightPart)); // 更新最小值
        }
    }

    // 枚举所有横切位置（水平切割，沿高度方向）
    for (int i = 1; i < h; i++) {   // i: 切割位置（上半部分高度为i）
        for (int j = 0; j < m; j++) { 
            int upperPart = dfs(w, i, j);          // 上半部分切j刀
            int lowerPart = dfs(w, h - i, m - 1 - j); // 下半部分切m-1-j刀
            mn = min(mn, max(upperPart, lowerPart)); // 更新最小值
        }
    }

    way[w][h][m] = mn; // 记录状态结果
    return mn;
}

int main() {
    int w, h, m;
    while (cin >> w >> h >> m) {
        if (w == 0 && h == 0) break; // 结束条件
        memset(way, -1, sizeof(way)); // 初始化记忆化数组
        // 需要切m块 -> 需切m-1刀，调用dfs(w, h, m-1)
        cout << dfs(w, h, m - 1) << endl;
    }
    return 0;
}

```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>