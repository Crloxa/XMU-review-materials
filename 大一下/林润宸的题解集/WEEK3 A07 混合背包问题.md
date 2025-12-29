# **<span id="section3A07"></span>WEEK3 A07 混合背包问题**

## 题目分析

~~大家好啊我是拼好题~~

**给定N个物品和V的容量的背包以及每个物品的价值，求背包能装下的最大价值的物品。（其中物体可以装一次或有限次或无限次）**

## 解题思路

### 线性DP

**我们需要对各个情况分开讨论处理，~~所以这道题就是纯纯拼好题~~ ，放在这里是为了讲01背包，完全背包和多重背包的一维优化的区别**


1. **对于01背包的处理：** 

    - 请看上篇题解，这里仅仅是多了把它放进数组以后再处理而已。

2. **对于完全背包的处理：**

    - 看上去几乎和01背包的代码完全一致，但是区别在于遍历顺序从小到大，为什么呢？ 因为这么做才能保证重复选取的实现（体积小的背包先更新，体积小的背包会影响体积大的背包的状态）。

3. **对于多重背包的处理：**

    - 从放入一个开始选直到超过物体个数或者背包放不下（k <= s[i] && k * v[i] <= j），其他的和01背包没有任何区别。


## 代码示例
```cpp
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

const int N = 2003;
//f[i]就是所有物品背包容量 i 下的最大价值。
int f[N];
int v[N], w[N], s[N];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> v[i] >> w[i] >> s[i];
    }

    for (int i = 1; i <= n; i++) {
        if (s[i] == -1) {
            for (int j = m; j >= v[i]; j--)
                f[j] = max(f[j], f[j - v[i]] + w[i]);
        }
        else if (s[i] == 0) {
            for (int j = v[i]; j <= m; j++)
            {
                f[j] = max(f[j], f[j - v[i]] + w[i]);
            }
        }
        else {
            for (int j = m; j >= v[i]; j--) {
                for (int k = 1; k <= s[i] && k * v[i] <= j; k++) {
                    f[j] = max(f[j], f[j - k * v[i]] + k * w[i]);
                }
            }
        }
    }
    cout << f[m] << endl;
    return 0;
}
```

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>