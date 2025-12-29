# **<span id="section3C02"></span>WEEK3 C02 环形石子合并**

曾几何时，刚开始看到DP的我以为环形DP是非常高大上的东西，直到我发现它只是把数组翻倍了而已。。。

## 题目分析

在一个环形排列的 n 堆石子中，每次选择相邻的两堆合并，合并代价为这两堆石子的数量之和。求将所有石子合并成一堆的 最小总代价 和 最大总代价。

## 解题思路

### 区间 DP + 环形处理

1. **环形问题转化为线性问题：**

- 需要把石子排列成环形（首尾相连），那么就通过复制数组将环形转化为线性

    - 将原数组 a[1..n] 复制到 a[n+1..2n]

    - 这样环形序列的所有可能区间都包含在 a[1..2n] 中

2. **定义动态规划：**

- **f[i][j]：** 合并区间 [i, j] 石子的 最大总代价

- **g[i][j]：** 合并区间 [i, j] 石子的 最小总代价

3. **状态转移方程：**

- 枚举分割点 k（i ≤ k < j），将区间 [i, j] 拆分为：

    - 左子区间 [i, k]

    -  右子区间 [k+1, j]

    - 合并代价为 左右子区间各自合并的代价 + 合并两个子区间的代价（即当前区间石子总和）

```cpp
//s[i]为前缀和
f[i][j] = max(f[i][j], f[i][k] + f[k+1][j] + (s[j]-s[i-1]))
g[i][j] = min(g[i][j], g[i][k] + g[k+1][j] + (s[j]-s[i-1]))
```

## 算法

### **1. 区间DP** 

#### 区间 DP 是一种针对 区间型问题 的动态规划方法，其状态定义通常与区间 [i, j] 相关。它通过解决小区间问题逐步推导出大区间问题的解，最终得到整个区间的最优解。

**核心特征**

1. **状态定义：** dp[i][j] 表示区间 [i, j] 上的最优解

2. **转移方式：** 通过枚举区间分割点 k 进行状态转移

3. **求解顺序：** 区间长度len从小到大递推

4. **初始化：** 长度为 1 的区间作为基础状态

### 模板
```cpp
//输入数据，计算前缀和，初始化
 for (int i = 1; i <= n; i++) {
     cin >> a[i];
     s[i] += s[i - 1] + a[i];
     dp[i][i] = 0;
 }
 for (int len = 2; len <= n; len++) {// 从小到大枚举区间长度      
     for (int i = 1; i + len - 1 <= n; i++) {    
         int j = i + len - 1;        // 计算起点和终点
         // 枚举分割点k (i ≤ k < j)
         for (int k = i; k <= j - 1; k++) {
             // 状态转移：这里按照石子合并的公式，正常状态下的dp公式需要推理。
             // 即dp[i][j]和dp[i][k] + dp[k + 1][j]有关的公式
             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[j] - s[i - 1]);
         }
     }
 }
```

### **2. 环形DP** 

- **当问题从线性结构变为环形结构（首尾相连）时，传统的区间 DP 无法直接处理起点和终点的连接关系。**

- **解决方案：** 通过 复制数组 将环形问题转化为线性问题

    1. 将原数组 a[1..n] 复制到 a[n+1..2n]

    2. 在新数组 a[1..2n] 上做区间 DP

    3. 最终结果在所有长度为 n 的区间中选取

## 代码示例
```cpp
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<unordered_map>
#include<unordered_set>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;
//ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //cout.tie(nullptr);


const int N = 403;
int n;
int a[N], s[N];
int f[N][N], g[N][N];
int mx = 0, mn = 0x3f3f3f3f;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> n;
    memset(f, 0, sizeof f);
    memset(g, 0x3f3f3f3f, sizeof g);
    for (int i = 1; i <= n * 2; i++) {
        if (i <= n) {
            cin >> a[i];
            a[i + n] = a[i];
        }
        s[i] = s[i - 1] + a[i];
        f[i][i] = g[i][i] = 0;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 1, j; j = i + len - 1, j <= n * 2; i++) {
            for (int k = i; k < j; k++) {
                f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + s[j] - s[i - 1]);
                g[i][j] = min(g[i][j], g[i][k] + g[k + 1][j] + s[j] - s[i - 1]);
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        mx = max(mx, f[i][i + n - 1]);
        mn = min(mn, g[i][i + n - 1]);
    }
    cout << mn << endl << mx << endl;
    return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>