# **<span id="section2B05"></span>WEEK2 B05 寻找林克的回忆(2)**

## 题目分析

**数独求解问题：** 给定一个9×9的数独初始状态（空格用.表示），要求填充空格使得：

1.    每行包含1-9且不重复

2.  每列包含1-9且不重复

3.  每个3×3宫格包含1-9且不重复

输入格式：单行81字符的字符串（行优先排列），以"end"结束输入

## 解题思路

### DFS + 回溯搜索 + 位运算优化

1. **状态压缩：** 使用9位二进制数表示数字使用情况（1表示可用，0表示已用）
    - 维护三个数组：row[9]（行状态）、col[9]（列状态）、block[3][3]（宫格状态）

2. **启发式搜索：** 每次选择可填数字最少的位置进行填充（最小可能性优先）

3. **回溯算法：** 尝试所有可能的数字，遇到冲突则回溯

4. **位运算优化：**       

-  使用lowbit快速枚举可用数字

-  预处理LOG表快速获取数字索引

-  预处理ones表快速计算可选数字数量

## 算法

### **\* 1.位运算优化** 

**位运算优化是一种高效处理状态信息的技巧，特别适合解决状态空间受限的问题（如数独）。**

**\*核心思想：状态压缩**

使用二进制位表示数字的使用状态：

-  1表示数字可用

-  0表示数字已被使用

相比传统数组的优势在于位运算的状态查询，状态更新，空间复杂度都是1，枚举数字的复杂度也远小于正常数组。

2. **数据结构**

```cpp
int ones[1<<9];  // 记录每个二进制数中1的个数（0~511）
int LOG[1<<9];   // 记录2^k对应的k值（用于快速获取数字）
int row[9];      // 每行的可用数字掩码
int col[9];      // 每列的可用数字掩码
int block[3][3]; // 每个3x3宫格的可用数字掩码
```

3. **关键操作**

```cpp
//获取位置(i,j)的可用数字,即9*i+j
inline int get(int x, int y) {
    return row[x] & col[y] & block[x / 3][y / 3];
}
//枚举可用数字：
    for (int i = get(x, y); i; i -= lowbit(i)) {
        int t = LOG[lowbit(i)];
    //...
    }

```

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

using namespace std;
#define _CRT_SECURE_NO_WARNINGS

int ones[1 << 9], LOG[1 << 9];  //0~511
int row[9], col[9], block[3][3];
string str;

inline int lowbit(int x) {
    return x & -x;
}

void init() {
    for (int i = 0; i < 9; i++) 
        row[i] = col[i] = (1 << 9) - 1; // 511
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            block[i][j] = (1 << 9) - 1;
        }
    }
}

inline int get(int x, int y) {
    //通过位与(&)操作合并行、列、宫格状态
    //结果中的1表示该数字在三个约束下都可用
    return row[x] & col[y] & block[x / 3][y / 3];
}


bool dfs(int cnt) {
    // 获取当前最少可选数字数量及其位置（从可选数字小开始推可以有效减少dfs总数量
    if (!cnt) return true;
    int minv = 10;              // 初始化最小候选数计数器
    int x, y;                   // 记录最优位置坐标
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (str[i * 9 + j] == '.') {// 检查是否空格
                int t = ones[get(i, j)];// 获取当前位置可选数字数量
                if (t < minv) {         // 发现更少候选数的位置
                    minv = t;           // 更新最小候选数
                    x = i, y = j;       // 记录最优位置
                }
            }
        }
    }
    for (int i = get(x, y); i; i -= lowbit(i)) {
        int t = LOG[lowbit(i)];
        //将对应位置0（数字被占用）
        row[x] -= 1 << t;
        col[y] -= 1 << t;
		block[x / 3][y / 3] -= 1 << t; 
        str[x * 9 + y] = '1' + t;
        if (dfs(cnt - 1)) return true;
		// 回溯，将对应位置恢复为1（数字可用）
        row[x] += 1 << t;
        col[y] += 1 << t;
        block[x / 3][y / 3] += 1 << t;
        str[x * 9 + y] = '.';
    }
    return false;
}

int main() {
	for (int i = 0; i < 9; i++) LOG[1 << i] = i; // LOG[2^k] = k
    for (int i = 0; i < (1 << 9); i++) {
        int s = 0;
        for (int j = i; j; j -= lowbit(j)) s++;
		ones[i] = s; //计算每个二进制数的1的数量
    }
    while (cin >> str, str[0] != 'e') {
        init();
        int cnt = 0;
        for (int i = 0, k = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++, k++) {
                if (str[k]!= '.') {
                    int t = str[k] - '1';
                    row[i] -= 1 << t;
                    col[j] -= 1 << t;
                    block[i / 3][j / 3] -= 1 << t;
                }
                else
                    cnt++;
            }
        }
        dfs(cnt);
        cout << str << endl;
    }
    return 0;
}
```
###### 杂言杂语：预处理好多第一次写不可能想出来吧。能想出lowbit处理数独的肯定是个天才。

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>