# **<span id="sectionSP1"></span>SPECIAL1 KMP字符串**

**备注：这道题来自校外实训WEEK1，然而我并没有选上校外实训是自己写的。我苦思冥想一天才学会，写的注释比代码还长，~~太痛苦了~~太有意思了，决定写题解**

## 题目分析

给定一个模式串S，以及一个模板串P，求出模板串P在模式串S中所有出现的位置的起始下标。


## 解题思路

### 爆搜过不了，所以使用KMP算法

## KMP算法

这里copy一下我呕心沥血写了一天的注释，因为我觉得写的很好

-   通常算法下，p[i]从j+1比对失败以后就从j=0开始寻找，浪费了前面大量的比对
-   所以我们想，能不能找到前i个字符的最长公共前后缀长度
-   如abcabd，遇到一个不与d适配的字母x时，我们可以回去看看是否和c适配
-   另一个例子就是就是abcab回到ab的位置比对
-   i始终大于j，因此可以对自身使用KMP。Next[i]不受i后面的串影响

### 1. **求next数组：**

- **！！！精髓** ：Next是前i个字符的最长公共前后缀长度，Next[i] = j可知p[1..j] = p[i-j..i-1]


-   当匹配结束或失败时，因为最长公共前缀和后缀字母是相同的，（比如abcab，next[5]=2，即p[5]匹配完成或失败后，可以直接跳到p[2]的位置，因为从前面看和从后面看都有ab）免去了重复计算这些字符串的过程。

- 匹配成功时，p往下一位走，j++，代表下一个位置的next数组增大。

- 很关键的一点是，i永远大于j，因为每次循环都有i++，却不一定有j++（j会因为使用next数组反而减小），这里有类似递归和双指针的思维，请读者细品。

- 循环结束后，p的next数组也就匹配成功了

### 2. **匹配字符串**

- 代表模式串s的指针i从1开始，代表模板串p的指针j从0开始，因为我们在代码里对j的操作永远都是要看p[j+1]

- 匹配失败，就通过next数组往前找最长公共前后缀长度，直到找到或者0的位置（从头开始）

- 匹配成功，p往下一位走，j++，代表我们往下一个位置匹配

- 匹配完成时，j==n，找到了完整的p串，我们就输出p串的位置（i指针位置-p串长度），然后又通过next数组往前找最长公共前后缀长度，还是为了减少重复匹配次数。

### 3. **对，这就是KMP字符串，一个浑身都是优化的算法！**

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
const int N = 100010;
#define _CRT_SECURE_NO_WARNINGS
const int N = 100010, M = 1000010;

int n, m;
char p[N], s[M];
int Next[N];    //Next是前i个字符的最长公共前后缀长度

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> n >> p + 1 >> m >> s + 1;
    Next[0] = Next[1] = 0;
    for (int i = 2, j = 0; i <= n; i++) {   //P串相对于自己

        // 通常算法下，p[i]从j+1比对失败以后就从j=0开始寻找，浪费了前面大量的比对
        // 所以我们想，能不能找到前i个字符的最长公共前后缀长度
        // 如abcabd，遇到一个不与d适配的字母x时，我们可以回去看看是否和c适配
        // 就是abcab回到ab的位置比对
        // i始终大于j，因此可以对自身使用KMP。Next[i]不受i后面的串影响

        while (j && p[i] != p[j + 1]) j = Next[j]; // Next[Next[Next[...]]]直到0
        //p[i] == p[Next[i-1]+1] 推出 Next[i]=Next[i-1]+1
        if (p[i] == p[j + 1]) j++;  // 直到配对成功，否则j = 0                                   
        Next[i] = j;                // p[1..j] = p[i-j..i-1]
        // 简单情况下 Next[i]=(p[i] == p[j + 1])?(Next[i-1]+1):0
        // 复杂情况下 Next[i]=(p[i] == p[j + 1])?(Next[i-1]+1): 需要看Next[j]
        // 这就是递归...
        // 匹配成功?(Y/N)
        //      N        N   
        //    i --> Next -->   ...  0(唯一不需要+1的
        //    |Y     |Y
        //   j+1    Next[j]+1   Next[Next[j]]+1
        // 
        // cout << " *** " << i << " " << Next[i] << " *** " << endl;
        // eg:abcabd abcabe abcabd abcabf
        // ...如果P串是abcdefg这样不重复的话就不存在什么匹配成功了
    }
    for (int i = 1, j = 0; i <= m; i++) {
        while (j && s[i] != p[j + 1]) j = Next[j];
        if (s[i] == p[j + 1]) j++;
        if (j == n) {               // 完全匹配成功
            printf("%d ", i - n);   // 输出匹配的起始位置（0-indexed）
            j = Next[j];            // 回溯继续寻找下一个匹配
        }
    }
    return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>