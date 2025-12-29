# **<span id="section3B01"></span>WEEK3 B01 B02 最长上升子序列**

## 题目分析

给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。（不一定要递增）

## 解题思路

1. **状态定义：** f[i] 表示以第 i 个元素结尾的最长上升子序列的长度。

2. **状态转移：**

- 遍历 i 之前的所有位置 j（1 ≤ j < i）

- 如果 w[i] > w[j]（满足上升条件），则尝试更新状态：
f[i] = max(f[i], f[j] + 1)

3. **细节：** 每个位置 f[i] 至少为 1（仅包含自身的情况）。



## 优化

- **我们发现，对于每次遍历前面的位置，我们都得遍历全部前面的元素，对于较大的数据其实会造成不小的时间浪费，所以想到或许可以用二分选择需要的元素，那么我们就需要创造一个单调上升的序列，所以如何创造这样的序列呢？**

### 1. 关键：改变f[N]数组状态

- 原始代码 f[i] = 以 w[i] 结尾的 LIS 长度

- 现在代码 f[i] = 长度为 i 的 LIS 的最小末尾值

### 2. 贪心维护f数组：

- **当 a[i] > f[res]：** a[i]大于所有末尾元素，扩展序列长度 res++, f[res] = a[i]。

- **当 a[i] <= f[res]：** 在f[1..res]中二分查找第一个≥a[i]的位置，用a[i]替换找到的位置的值，改变最小末尾元素值。这样这个位置的f[j]就可以匹配数字更小的f[i]


## 代码示例1
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


const int N = 1003;
int n, m;
int w[N], f[N];// f[i]表示以w[i]结尾的最长上升子序列长度
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> w[i];
    // 初始化结果（最小上升子序列长度为1）
    int res = 1;

    for (int i = 1; i <= n; i++) {
        // 初始状态：每个元素自身构成长度为1的子序列
        f[i] = 1;
        for (int j = 1; j < i; j++) {
            if (w[i] > w[j]) {
                f[i] = max(f[i], f[j] + 1);
                res = max(res, f[i]);   // 更新全局最大值
            }
        }
    }
    cout << res << endl;
    return 0;
}
```


## 代码示例2
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

const int N = 1e5 + 3;
int n, m;
int a[N], f[N];// f[i]表示长度为i的上升子序列的最小末尾元素值
int res = 1;// 当前最长上升子序列的长度（也是f数组的有效长度）

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    // 初始化：第一个元素作为长度为1的子序列的最小末尾值
    f[1] = a[1];     
    for (int i = 2; i <= n; i++) {
        // 当前元素大于所有末尾元素 → 扩展最长序列
        if (a[i] > f[res]) f[++res] = a[i];
        else {
            // 当前元素小于最大末尾元素
            // 在f[1..res]中查找第一个≥a[i]的位置
            int l = 1, r = res;
            while (l < r) {
                int mid = l + r >> 1;
                if (f[mid] >= a[i]) r = mid;
                else l = mid + 1;
            }
            // 用a[i]替换找到的位置的值，改变最小末尾元素值
            f[l] = a[i];
        }
    }
    cout << res << endl;
    return 0;
}
```

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>