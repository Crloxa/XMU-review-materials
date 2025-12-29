# **<span id="section2A04"></span>WEEK2 A04 英杰们的蛋糕塔** 

## 题目分析

**题目要求制作一个体积为 Nπ、层数为 M 的蛋糕，每层都是圆柱体，从下往上半径和高度递减。需要最小化蛋糕的外表面积（不包括最底层的底面）。表面积由两部分组成：**

1. 所有层的侧面积之和
2. 整个蛋糕的上表面暴露部分（即最底层的上表面面积，值为πr^2）

## 解题思路

### 二分查找 + 贪心验证
1. **可行性剪枝：** 预处理每层最小体积和最小侧面积，若当前体积加上剩余层最小体积超过 NN 则剪枝

2. **最优性剪枝：**

	- 当前表面积加上剩余层最小侧面积超过当前最优解则剪枝

	- 利用公式 **2×(剩余体积)/当前半径** 估计剩余部分最小侧面积，超过最优解则剪枝

3. **枚举范围优化：**

	- 半径范围：从下一层半径-1递减到当前层数（保证上层半径递减）

	- 高度范围：由剩余体积和最小体积约束计算最大值，同时不超过下一层高度-1

### 关键点

- 最底层的上表面面积等于整个蛋糕的上表面暴露部分

- 搜索时单独处理底层：初始化表面积包含底面积

- 预处理最小体积和侧面积数组加速剪枝

## 算法

**DFS + 剪枝优化**

**精髓在于怎么找到剪枝，对于初学者来说是地狱（**


## 代码示例
```cpp
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int m, n, mn = 0x3f3f3f3f;
int a[30], b[30];   // a[i]表示i层的最小表面积，b[i]表示i层的最小体积

inline void dfs(int r, int h, int cnt, int s, int v) {
    //得到结果时使用贪心
    if (cnt == 0) {
        if(v== n) 
            mn = min(mn, s);
        return;
    }

    //如果预估搭建剩余层所需的最小体积大于剩余可用体积，则说明规定的体积不够用，返回
    if(v + b[cnt] > n) 
        return;
    //如果预估搭建剩余层所需的最小面积大于已知最小答案，则说明不是最优解，返回
    if(s + a[cnt] > mn)
        return;
    //如果预估蛋糕的最小面积大于前面所确立最小面积，则说明不是最优解，返回
    //(n - v) <= r * r * h
    if(s + 2 * (n - v) / r > mn) 
        return;
    for (int i = r - 1; i >= cnt; i--) {
        if (cnt == m) s = i * i;
        int maxr = min( (n - v - b[cnt - 1]) / (i * i), h - 1);
        for (int j = maxr; j >= cnt; j--) {
            dfs(i, j, cnt - 1, s + 2 * i * j, v + i * i * j);
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
	cin >> n >> m;  // n为体积，m为层数
    a[0] = b[0] = 0;
    for (int i = 1; i <= m; i++) {
        a[i] = a[i - 1] + 2 * i * i;
		b[i] = b[i - 1] + i * i * i;
    }
    dfs(sqrt(n) + 1, sqrt(n) + 1, m, 0, 0);//剪枝优化开始位置
    if(mn == 0x3f3f3f3f) {
        cout << "0" << endl;
    } else {
        cout << mn << endl;
	}
    return 0;
}

```

###### ps:这道题我debug了3小时，最后丢给ai莫名其妙对了。

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>