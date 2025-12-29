***
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow><mstyle mathsize="2.49em"><mo>程序设计实践</mo><mi>W</mi><mi>e</mi><mi>e</mi><mi>k</mi><mn>1</mn><mo>题解</mo><mo stretchy="false">(</mo><mo>李胜睿班</mo><mo stretchy="false">)</mo></mstyle></mrow></math>

<br>

# From 林润宸

<br>
<br>
<br>

## 杂言杂语

### **ver1**
**经过前三天与算法的恶战，（~~现在轮到与题解的恶战了~~）终于到了我最喜欢的（？）写题解环节，说实话以前从来没写过题解，连markdown都是刚上手用。羡慕周围大佬得心应手地把题解全写好了QAQ。**
<br>
### ver2
**突然发现题解只`要写20题结果已经写了5题了，决定接下来每一题的题解都要是新算法！老师可以自动忽略从A01到A04的没那么算法的部分（**
<br>
### ver3
**怎么好多人写题解时抄洛谷，好过分TAT虽然我也好不到哪里去让deepseek帮我写题解，我至少会加上我的理解和注解TAT**


<br>
<br>
<br>

# <span id="section1"></span>  <a id="top"></a> 目录

### [1. WEEK1 A01 A+B](#sectionA01)
### [2. WEEK1 A02 完美立方](#sectionA02)
### [3. WEEK1 A03 人的周期](#sectionA03)
### [4. WEEK1 A04 排序考试](#sectionA04)
### [5. WEEK1 A05 假币问题](#sectionA05)

### [6. WEEK1 A08 四数之和](#sectionA08)
### [7. WEEK1 B03 DFS试炼之排列数字](#sectionB03)
### [8. WEEK1 B08 放苹果](#sectionB08)
### [9. WEEK1 B16 熄灯问题](#sectionB16)
### [10. WEEK1 C05 求排列的逆序数](#sectionC05)

### [11. WEEK1 C06 查找指定数 另一种写法](#sectionC06)
### [12. WEEK1 C10 最小预算值](#sectionC10)
### [13. WEEK2 A04 英杰们的蛋糕塔](#section2A04)
### [14. WEEK2 A05 击杀黄金蛋糕人马](#section2A05)
### [15. WEEK2 B05 寻找林克的回忆(2)](#section2B05)

### [16. WEEK2 B07+B08 寻找林克的回忆(4)（这算两道题解吧）](#section2B07)
### [17. WEEK2 C02 波克布林的巡逻范围](#section2C02)
### [18. WEEK2 C06 滚石柱](#section2C06)
### [19. WEEK2 C07 C08 Dijkstra求最短路](#section2C07)
### [20. WEEK3 A02 01背包问题](#section3A02)

### [21. WEEK3 A07 混合背包问题](#section3A07)
### [22. WEEK3 B01 B02 最长上升子序列](#section3B01)
### [23. WEEK3 C02 环形石子合并](#section3C02)
### [24. WEEK3 C05 没有上司的舞会](#section3C05)
### [25. SPECIAL1 KMP字符串](#sectionSP1)

<br>
<br>
<br>
<br>
<br>
<br>

# **A01 A+B** <span id="sectionA01"></span>

## 解题思路
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1+1=2（好吧这行只是我拿来学习markdown的qwq）
## 算法（吗？）
<br>
- 简而言之
<br>
1. - 学会**A+B***就是****开始学习***&nbsp;算法的第一步！ 
<br>
2. - 额我也想不到了，题解在下面啊吧啊吧啊吧。

## 代码示例
```cpp
#include<iostream>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b;
	c = a + b;
	cout << c << endl;
	return 0;
}
```


### [>>>点我返回目录位置<<<](#section1)

<br>
<br>
<br>

# **A02 完美立方** <span id="sectionA02"></span>

## 题目分析

题目要求找出所有满足完美立方等式 $a^3 = b^3 + c^3 + d^3$ 的四元组 $(a, b, c, d)$，其中：

 $1 < b < c < d \leq a \leq N$

 $N \leq 100$

输出按 $a$ 值从小到大排序，$a$ 相同时按 $b,c,d$ 从小到大排序

## 解题思路

### 四重循环枚举

通过四重循环枚举所有可能的 $a, b, c, d$ 组合：

$a$ 从 2 到 $N$

$b$ 从 2 到 $a-1$

$c$ 从 $b+1$ 到 $a-1$

$d$ 从 $c+1$ 到 $a-1$

检查是否满足 $a^3 = b^3 + c^3 + d^3$

## 算法

暴力解决

## 代码示例
```cpp
#include<iostream>
using namespace std;

int main() {
	long long a, b, c,d;
	cin >> a;
	for (int i = 1; i <= a; i++) {
		for (b = 2; b < i; b++) {
			for (c = b; c < i; c++) {
				for (d = c; d < i; d++) {
					if (b * b * b +
                        c* c * c + 
                        d * d * d ==
                        i * i * i) {
						cout << "Cube = " << i << ", 
                        Triple = (" << b << "," << c << "," << d << ")" << endl;
					}
				}
			}
		}
	}
	return 0;
}
//deepseek伟大！我的代码好丑！
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **A03 人的周期** <span id="sectionA03"></span>

## 题目分析

题目要求计算从给定时间 d 之后，下一次三个生理周期（体力23天、情感28天、智力33天）高峰同时出现的日期。输入包含多组数据，每组数据包含四个整数 p, e, i, d，分别表示体力、情感、智力高峰出现的时间和给定时间。


## 解题思路

### 直接枚举法

从给定时间 d+1 天开始向后枚举每一天

检查当前天是否同时满足三个条件：

(当前天 - p) 是 23 的倍数（体力高峰）

(当前天 - e) 是 28 的倍数（情感高峰）

(当前天 - i) 是 33 的倍数（智力高峰）

找到第一个满足所有条件的天数后，计算与给定时间 d 的差值

## 算法

 从给定日期开始的下一天开始枚举，直到找到符合要求的那一天。

## 代码示例1
```cpp
# include<iostream>
using namespace std;
int main(){
	long long a,b,c,d;
	long long x=23,y=28,z=33;
	int cnt=1;
	while(cin>>a>>b>>c>>d && !(a==-1&&b==-1&&c==-1&&d==-1)){
		long long d1=d+1;
		while((d1-a)%x!=0||(d1-b)%y!=0||(d1-c)%z!=0){
			d1++;
		}
	cout<<"Case "<<cnt<<": the next triple peak occurs in "<<d1-d<<" days."<<endl;
	cnt++;
	}
	return 0;
}
```
## 代码示例2（AI优化版本）
```cpp
#include<iostream>
using namespace std;

int main() {
    long long p, e, i, d;
    int cnt = 1;
    
    while (cin >> p >> e >> i >> d && !(p == -1 && e == -1 && i == -1 && d == -1)) {
        long long day = d + 1;
        
        // 先找到下一个体力高峰
        while ((day - p) % 23 != 0) {
            day++;
        }
        
        // 在体力高峰基础上，以23天为步长寻找情感高峰
        while ((day - e) % 28 != 0) {
            day += 23;
        }
        
        // 在体力和情感高峰基础上，以23*28=644天为步长寻找智力高峰
        while ((day - i) % 33 != 0) {
            day += 23 * 28;
        }
        
        cout << "Case " << cnt << ": the next triple peak occurs in " 
             << day - d << " days." << endl;
        cnt++;
    }
    return 0;
}
```
###### btw，AI甚至直接给出了公式解: x = (p*5544 + e*14421 + i*1288) % 21252，无敌了...

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **A04 排序考试** <span id="sectionA04"></span>

## 题目分析
第一行是整数T，表示测试T次

接下来T行，每行有N+1个数，第一个整数表示该行有N个待排序的数字。

说白了就是建数组然后排序。。。

## 解题思路

### 快速排序

用STL标准模板库的sort秒了，或者搞个大数组来写快排

## 算法

STL or 快速排序

### **\*** 快速排序

1. **分治策略：** 将一个大问题分解为小问题解决

2. **基准选择：** 在范围内选择 中间位置 作为"基准"

3. **分区操作：** 将数组分为两部分：

    - 小于基准的元素

    - 大于基准的元素

4. **递归排序：** 对分区后的子数组递归应用相同操作

### 模板
```cpp
void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i++; while (q[i] < x);
        do j--; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }

    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}
```
###### 既然在这里介绍了我就不在C题那边介绍了QWQ

## 代码示例
```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	int cnt;
	cin >> cnt;
	while (cnt--) {
		int b;
		cin >> b;
		vector<int> a(b);
		for (int i = 0; i < b; i++)
			cin >> a[i];
		sort(a.begin(), a.end());
		for (int i = 0; i < b;i++) {
			cout << a[i];
			if (i != b - 1) cout << " ";
		}
		cout << endl;
	}
	return 0;
}
```

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **A05 假币问题** <span id="sectionA05"></span>

## 题目分析

经典的假币检测问题，有12枚硬币（A-L），其中11枚真币重量相同，1枚假币重量不同（可能轻也可能重）。通过三次天平称量结果，需要找出假币并确定它是轻还是重。

## 解题思路

### 枚举验证法

**枚举所有可能性：** 共有24种可能情况（12枚硬币 × 2种状态：A~L * 轻or重）

**验证每种假设：** 对于每种假设（某枚硬币是轻的或重的），检查是否符合三次称量结果（先前成果存放在string数组 left right 和result里面），如果符合就直接跳出循环输出答案

**确定唯一解：** 题目保证有唯一解，找到符合所有称量结果的情况即为答案


## 算法

枚举，注意要找到如何开始枚举，这是所有枚举题目的关键

###### 小插曲与杂言：我当初尝试用数组标记写这道题，结果以失败告终，因为不知道既标记轻又标记重的正常硬币应该如何处理，遂放弃。所以第一次看到题解的时候，是耳目一新的，算法的学习不是一蹴而就的，必须慢慢品味，所以我个人认为教学如此之快不给足够的品味时间并非好事。

## 代码示例
```cpp
#include<iostream>
#include<cstring>
std::string left[3], right[3], result[3];


bool test(char ch, bool islight) {
	std::string c;
	c.push_back(ch);
	int count = 0;
	for (int i = 0; i < 3; i++) {
		std::string l = left[i];
		std::string r = right[i];
		if (islight == false) swap(l, r);
		switch (result[i][0]) {
		case 'e': {
			if (l.find(c) != std::string::npos || r.find(c) != std::string::npos) {
				return false;
			}
			break;
		}
		case 'u': {
			if (r.find(c) == std::string::npos) {
				return false;
			}
			break;
		}
		case 'd': {
			if (l.find(c) == std::string::npos) {
				return false;
			}
			break;
		}
		}
	}
	return true;
}
int main()
{
	int t;
	std::cin >> t;
	while (t--) {
		for (int i = 0; i < 3; i++) {
			std::cin >> left[i] >> right[i] >> result[i];
		}
		for (char ch = 'A'; ch <= 'L'; ch++) {
			if (test(ch, true)) {
				std::cout << ch << " is the counterfeit coin and it is light. " << std::endl; break;
			}
			else if (test(ch, false))
			{
				std::cout << ch << " is the counterfeit coin and it is heavy. " << std::endl; break;
			}
		}
	}
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **A08 四数之和** <span id="sectionA08"></span>

## 题目分析

**给定一个整数数组和一个目标值，找出所有满足 a + b + c + d = target 的四元组 (a, b, c, d)。要求：**

1. 四元组中 a < b < c < d

2. 输出结果按 a 升序排列，a 相同按 b 升序，b 相同按 c 升序

3. 四元组中不能包含重复数字

## 解题思路

### 快速排序 + 双指针

**排序数组：** 先对数组进行排序，方便后续去重和双指针操作

**两层循环枚举前两个数：**

- 外层循环枚举第一个数 a

- 内层循环枚举第二个数 b

- 跳过重复元素避免重复解

**双指针寻找后两个数：**

-  指针指向 b 的下一个位置

- 右指针指向数组末尾

- 根据四数之和与 target 的关系移动指针

**结果处理：**

- 找到有效解时检查是否严格递增

- 跳过重复元素保证结果不重复    
## 算法

### **\*** 双指针

通过两个指针在数据结构中按照特定规则移动，高效地完成搜索、比较或计算任务
1. **同向双指针（快慢指针）**

    - 两个指针从同一端出发，以不同速度移动，对本题适用

2. **对向双指针（左右指针）**
    - 两个指针分别从两端向中间移动，也是本题解使用的方法

3. **分离双指针**

    - 两个指针分别位于不同的数组或链表上(AI这么说的，例子似乎就是归并排序？)

### 模板（同向）
```cpp
for (int i = 0, j = 0; i < n; i ++ )
{
    while (j < i && check(i, j)) j ++ ;
    // 具体问题的逻辑
}
```

### 模板（对向）
```cpp
for (int i = 0, j = n-1; i < n; i ++ )
{
    while (j > i && check(i, j)) j -- ;
    // 具体问题的逻辑
}
```
## 代码示例

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> ans(vector<int>& a, int tar){
	vector<vector<int>> ret;
	sort(a.begin(), a.end());
	a.erase(unique(a.begin(), a.end()), a.end()); 

	for (int i = 0; i < a.size(); i++) {
		for (int j = a.size() - 1; j > i; j--) {
			int l = i + 1, r = j - 1;
			while (l < r) {
				int sum = a[i] + a[l] + a[r] + a[j];
				if (sum == tar) {
					ret.push_back({ a[i], a[l], a[r], a[j] });
					l++;
					r--;
				}
				else if (sum < tar) {
					l++;
				}
				else {
					r--;
				}
			}
		}
	}
	return ret;
}
bool cmp(vector<int>& a, vector<int>& b){
	for (int i = 0; i < a.size(); i++){
		if (a[i] != b[i])
			return a[i] < b[i];
	}
	return true;
}
int main(){
	int tar, n;
	cin >> tar >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++){
		cin >> a[i];
	}
	vector<vector<int>> res = ans(a, tar);
	sort(res.begin(), res.end(), cmp);
	for (auto i : res)
		cout << i[0] << " " << i[1] << " " << i[2] << " " << i[3] << endl;
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **B03 DFS试炼之排列数字** <span id="sectionB03"></span>

## 题目分析

给个数字，然后按字典序输出所有排列方案，每个方案占一行。

通俗点讲就是从小到大排列出1~n的所有排列可能

## 解题思路

### 深度优先搜索

**遍历1~n，选择未被标记的数字加入路径。记录数字是否已使用。递归返回后，撤销选择。**

## 算法

### **\* DFS**

**DFS 是一种用于遍历或搜索数据结构的算法。它的核心策略是 “一条路走到底，碰壁再回头”。**

1. **选择起点：** 从图中任意选择一个节点作为起点。

2. **标记并访问：** 访问该节点，并将其标记为“已访问”（例如，放入一个 visited 集合）。

3. **深入探索邻居：** 对于当前节点的每一个未访问过的邻居节点，递归地调用 DFS 过程（以该邻居节点作为新的起点）。

    - 迭代方式（显式栈）：

        将起点节点压入栈（Stack）中并标记为已访问。

        - 只要栈不为空：

            弹出栈顶元素作为当前节点。

            访问该节点。

            将该节点的所有未访问过的邻居节点压入栈中并标记为已访问。

4. **个人见解：** DFS的递归函数长得看似不够完整，何出此言？因为DFS传入的只是它的深度，并没有告诉你哪些数组里的数已经标记好了，DFS的功能可以不传 **哪些数组已经标记** 的情况下实现递归，理解这一点对于刚开始学习算法的人来说无疑是一个很困难的事情。

### 模板
```cpp
void DFS(int cur){
	if(cur == target){ //target个数已经选完，可以进行输出等相关操作 
		for(int i = 0; i < cur; i++){
			printf("%d ", a[i]);
		} 
		ans++;
		return ;
	}
	
	for(int i = 0; i < n; i++){ //遍历 n 个数，并从中选择target个数 
		if(check(i)){ //如果符合标记条件（eg:N皇后中的递归条件是j从1到cur，a[j] == i || abs(a[j] - i) == abs(j - cur)均不成立。）
			mark[i] = true; //标记已被访问 
			a[cur] = i;  //选定本数，并加入数组 
			DFS(cur + 1);  //递归，cur+1 
			mark[i] = false;  //释放，标记为没被访问，方便下次引用 
		}
	}
}
```

## 代码示例
```cpp
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
int a[20] = { 0 };
bool b[20] = { false };
int n;

void dfs(int u){
	if(u==n) {
		for(int i = 0; i < n; i++) {
			cout << a[i] << " ";
		}
		cout << endl;
		return;
	}
	for (int i = 1; i <= n; i++) {
		if( !b[i]) {
			a[u] = i;
			b[i] = true;
			dfs(u+1);
			b[i] = false;
		}
	}
}
int main(){
	cin >> n;
	dfs(0);
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

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

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **B16 熄灯问题** <span id="sectionB16"></span>

## 题目分析

**有一个5×6的按钮矩阵，每个按钮控制自身及上下左右共5盏灯的状态（边界按钮控制3-4盏）。给定灯的初始状态（0灭1亮），求一个按钮操作方案（1按0不按），使所有灯熄灭。关键约束：**

- 每个按钮最多按一次（按两次等于没按）

- 操作顺序无关

- 需要输出具体的操作矩阵

## 解题思路

### 枚举+递推

1. **枚举第一行（关键决策）：**

    -   第一行有6个按钮，每个按钮有2种选择（按/不按）

    -  共2⁶=64种可能，可暴力枚举

2. **递推中间行：**

    -   根据灯状态确定下一行操作：上一行某灯若亮，则下一行同列按钮必须按下

    -  第i行操作由第i-1行灯的状态唯一确定

 3. **验证最后一行：**

    -  递推得到第5行操作后

    -  检查第5行所有灯是否全灭

## 算法

### **推公式** 

**当第一行的灯的初始状态给出时，我们枚举它所有可能的按/不按情况，因为只有**

1. 第1行第n个灯的初始状态是亮或者暗

2. 第1行第n-1个灯的是否按下（如果存在的话）

3. 第1行第n个灯的是否按下

4. 第1行第n+1个灯的是否按下（如果存在的话）

5. 第2行第n个灯的是否按下

**会影响第一行灯的最终结果，又因为我们输入数据和枚举时已经确定了前四个因素的状态，所以第五个因素也是唯一确定的**

**于是**

**我们可以推得第二行的灯的状态，又因为只有**

1. 第2行第n个灯的初始状态是亮或者暗

2. 第2行第n-1个灯的是否按下（如果存在的话）

3. 第2行第n个灯的是否按下

4. 第2行第n+1个灯的是否按下（如果存在的话）

5. 第3行第n个灯的是否按下

**会影响第二行灯的最终结果，我们就可以递推到所有灯的结果**

**此时，只需要验证第五行是否符合全灭的条件就好了，如果全灭就跳出循环输出结果，否则继续枚举**

容易得到灯的递推公式是
```cpp
turned[i+1][j] = (l[i][j] + turned[i][j] + turned[i-1][j] + turned[i][j-1]+turned[i][j+1]) % 2
```

验证公式是
```cpp
l[5][j] == (turned[5][j] + turned[5][j - 1] + turned[5][j + 1] + turned[4][j])%2
```

## 代码示例 1
```cpp
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include <bitset>
int l[10][10] ;
int turned[10][10] ;

bool solve() {
	for (int i = 1; i < 5; i++) {
		for (int j = 1; j < 7; j++) {
			turned[i+1][j] = (l[i][j] + turned[i][j] + turned[i-1][j] + turned[i][j-1]+turned[i][j+1]) % 2;
		}
	}
	for(int j=1;j<=6; j++) {
		if (l[5][j] != (turned[5][j] + turned[5][j - 1] + turned[5][j + 1] + turned[4][j])%2) {
			return false;
		}
	}
	return true;
}

void process() {
	for (int i = 1; i < 6; i++)
		turned[1][i] = 0;
	while (!solve()) {
		turned[1][1] ++;
		int i = 1;
		while (turned[1][i] > 1) {
			turned[1][i] = 0;
			i++;
			turned[1][i]++;
		}
	}
}

int main() {
	int cnt;
	cin >> cnt;
	for (int cnt1 = 0; cnt1 < cnt; cnt1++) {

		for(int i=0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				l[i][j] = 0;
				turned[i][j] = 0;
			}
		}

		for(int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 6; j++) {
				cin >> l[i][j]; 
			}
		}

		process();

		cout << "PUZZLE #" << cnt1 + 1 << endl;
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 6; j++) {
				cout << turned[i][j] << " ";
			}
			cout << endl;
		}
		
	}
	return 0;
}
```

## 代码示例 2（使用了bitset，把十进制数转换成二进制，很妙）
```cpp
#include<bitset>
#include<cstring>
#include<iostream>
#include<memory>
using namespace std;

bitset<6> source[5],lights[5],res[5],line;
void Output(int t)
{
    cout<<"PUZZLE #"<<t<<endl;
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<6;j++)
            cout<<res[i][j]<<" ";
        cout<<endl;
    }
}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        for(int i=0;i<5;i++)
        {
            for(int j=0;j<6;j++)
            {
                int x;
                cin>>x;
                source[i].set(j,x);
            }
        }
        for(int n=0;n<64;n++)
        {
            for(int i=0;i<5;i++)
                lights[i]=source[i];// 重置灯状态为初始值
            line=n;// 用整数n初始化bitset<6>，代表第一行的操作方案
            for(int i=0;i<5;i++)
            {
				res[i] = line;// 记录当前行操作方案（按下的灯）
                for(int j=0;j<6;j++)
                {
                    if(line.test(j))// 若第j列需按下
                    {
                        if(j>0) lights[i].flip(j-1);// 切换左侧灯
                        lights[i].flip(j);          // 切换自身
                        if(j<5) lights[i].flip(j+1);// 切换右侧灯
                    }
                }
                if(i<4) lights[i+1]^=line;// 切换下一行对应位置（下方灯）
                line=lights[i];// 下一行操作由当前行状态决定
            }
            if(lights[4].none())// 检查最后一行是否全灭
            {
                Output(t);
                break;
            }
        }
    }
    return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **C05 求排列的逆序数** <span id="sectionC05"></span>

## 题目分析

**给定一个由 1 到 n 组成的排列，求该排列的逆序数。**
- 逆序数定义为排列中逆序对的数量，其中逆序对指满足 i < j 且 a[ i ] > a[ j ] 的元素对。

## 解题思路

### 归并排序+逆序数统计
利用归并排序的分治特性，在合并两个有序子数组时统计逆序数：

1.  **分治分解：** 将数组递归地二分为左右子数组

2.  **分别排序：** 对左右子数组分别进行归并排序

3.  **合并统计：** 合并两个有序子数组：

	- 当右边数组选中元素小于左边数组选中元素时，左子数组剩余元素均与该元素构成逆序对,逆序数增加量为 **mid - left + 1**，即左边数组剩余的元素个数。

	- **\* 原因：因为这么排序保证左右数组都是升序的，所以右边数组选中元素小于左边数组选中元素时，左边数组选中元素之后的元素肯定也比右边数组选中元素大。当左边选择结束时，右边剩下的数字都肯定比左边最大的数字大，显然不会再有逆序数。当右边选择结束时，右边没有数字能选择了，也自然不存在能逆序的数字了。**

## 算法

### **\* 归并排序**

**一种基于分治思想的高效排序算法。它将数组递归地分成两半，分别排序后再合并。算法步骤包括：**

1. 分解：将当前数组分成两个子数组

2. 递归：递归地对两个子数组进行归并排序

3. 合并：将两个已排序的子数组合并为一个有序数组

### 模板
```cpp
void mergesort(vector<long long>& a, vector<long long>& b, int l, int r) {//a为目标排序数组，b为临时数组。
	if (l >= r) return;
	int mid = l + (r - l) / 2;
	mergesort(a, b, l, mid);
	mergesort(a, b, mid + 1, r);

	int left = l, right = mid + 1, index = l;
	while (left <= mid && right <= r) {
		if (a[left] <= a[right]) {
			b[index++] = a[left++];
		}
		else {
			b[index++] = a[right++];
		}
	}

	while (left <= mid) {
		b[index++] = a[left++];
	}

	while (right <= r) {
		b[index++] = a[right++];
	}

	for(int i = l; i <= r; i++) {
		a[i] = b[i];
	}
}
```

## 代码示例
```cpp
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include <bitset>
#include<map>
#include<cstdio>
long long ans = 0;
void mergesort(vector<long long>& a, vector<long long>& b, int l, int r) {
	if (l >= r) return;
	int mid = l + (r - l) / 2;
	mergesort(a, b, l, mid);
	mergesort(a, b, mid + 1, r);

	int left = l, right = mid + 1, index = l;
	while (left <= mid && right <= r) {
		if (a[left] <= a[right]) {
			b[index++] = a[left++];
		}
		else {
			ans += mid + 1 - left;
			b[index++] = a[right++];
		}
	}

	while (left <= mid) {
		b[index++] = a[left++];
	}

	while (right <= r) {
		b[index++] = a[right++];
	}

	for(int i = l; i <= r; i++) {
		a[i] = b[i];
	}
}

int main() {
	int n;
	cin >> n;
	vector<long long> v(n),w(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	mergesort(v,w, 0, n - 1);
	cout << ans << endl;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>


# <span id="sectionC06"></span>C06  查找指定数  另一种写法（用map库，原本应该使用快排，会在下面介绍。仅给出写法因为这道题实在没啥好介绍的） 

```cpp
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include <bitset>
#include<map>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int n,x;
	cin >> n;
	map<int, int> v;
	for (int i = 0; i < n; i++) {
		cin >> x;
		v.insert({ x, i });
	}
	int m;
	cin >> m;
	for(int i = 0; i < m; i++) {
		int x;
		cin >> x;
		if (v.find(x) != v.end()) 
			cout << v[x] << endl;
		else
			cout << "-1" << endl;
	}
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **C10 最小预算值** <span id="sectionC10"></span>

## 题目分析

**数组含有n个元素的数组X[n]分成m个连续组，每组和都不超过 Budget。**

## 解题思路

### 二分查找 + 贪心验证
1. 二分查找范围：

	- 下界 left = 单日最大支出（保证任何一天不超预算）

	-  上界 right = 总支出（当 m=1 时的解）

2. 贪心验证函数：

	- 模拟分组过程，尽可能将连续天合并到当前组

	- 若当前组加入下一天会超预算，则开新组

	- 统计分组数是否 ≤ m，如果分组超过m就不符合要求。如果直到X[n]分完还没超过m，则符合要求

3. 二分框架：

	- 若当前 Budget 可行，尝试缩小 Budget

	- 若不可行，增大 Budget

	- 直到遇到小到足够小的Budget，输出答案。

## 算法

**二分查找和贪心**

### **\* 贪心算法** 

**贪心算法（Greedy Algorithm）在每一步选择中都采取当前状态下最优（最有利） 的选择，从而希望导致全局最优解。**

- **详细步骤**

    - **问题分解：** 将问题划分为多个子问题。

    - **贪心选择：** 对每个子问题，做出当前最优选择（不可回退）。

    - **迭代求解：** 基于已做的选择，继续解决剩余子问题。

    - **合并解：** 将所有局部最优解组合为最终解。



### 模板
```cpp
#include <vector>
#include <algorithm>
using namespace std;

// 1. 定义问题相关的数据结构（例如：活动、任务等）
struct Item {
    int attribute1;  // 如：开始时间、权重等
    int attribute2;  // 如：结束时间、价值等
};

// 2. 定义贪心策略的排序函数
bool greedyStrategy(const Item &a, const Item &b) {
    // 根据问题设计排序规则（关键步骤！）
    // 示例：按结束时间升序（活动选择问题）
    return a.attribute2 < b.attribute2;
}

// 3. 贪心算法主函数
vector<Item> greedyAlgorithm(vector<Item> items) {
    // 步骤1：按贪心策略排序
    sort(items.begin(), items.end(), greedyStrategy);
    
    vector<Item> solution;  // 存储最终解
    if (items.empty()) return solution;

    // 步骤2：选择第一个元素（根据策略）
    solution.push_back(items[0]);
    int last_selected = 0;  // 记录最后选择的索引

    // 步骤3：迭代处理剩余元素
    for (int i = 1; i < items.size(); ++i) {
        // 检查当前元素是否与已选解兼容
        if (items[i].attribute1 >= items[last_selected].attribute2) {
            solution.push_back(items[i]);
            last_selected = i;  // 更新最后选择的元素
        }
    }
    return solution;
}
```

## 代码示例
```cpp
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include <bitset>
#include<map>
#include<cstdio>

using namespace std;

int n, m, mincost = 1e9, total = 0;

bool enough(vector<int>& a, int cur) {
	int zu = 1, zutotal = 0;
	for (int i = 0; i < n; i++) {
		if (a[i] > cur) return false;
		if (a[i] + zutotal > cur) {
			zutotal = a[i];
			zu++;
			if (zu > m) return false;
		}
		else {
			zutotal += a[i];
		}
	}
	return true;
}

int solve(vector<int>& a, int n) {
	int l = mincost, r = total;
	int ans = 0;
	while (l < r) {
		int mid = l + r >> 1;
		if (enough(a, mid)) {
			ans = mid;
			r = mid;
		}
		else
			l = mid + 1;
	}
	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> n >> m;
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
		if (mincost > v[i]) {
			mincost = v[i];
		}
		total += v[i];
	}
	int budget = solve(v, n);
	cout << budget << endl;
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

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

# **<span id="section2B07"></span>WEEK2 B07 B08 寻找林克的回忆(4)（这算两道题解吧）**

## 题目分析

**A~P的16*16填数独，绝对是目前学过最难的题目**

1.   每行必须包含所有 16 个字母（不重复）。

2.   每列必须包含所有 16 个字母（不重复）。

3.  每个 4×4 的宫格必须包含所有 16 个字母（不重复）。
	题目保证有唯一解，输出填充完成的数独网格。

## 解题思路

#### ~~抄上一题代码~~，发现完全过不了。怎么办呢

### 那就剪枝剪到死！

## 算法

### 1. **与 寻找林克的回忆（2）相同的基础上**

### **2. \* 疯狂地剪枝** 

1. **唯一数字填充：** 若某空格只有 1 个可选数字，直接填充。

2. **行/列/宫格的唯一性剪枝：**

	- 对每一行，若某字母只能填在一个位置，则直接填入。

	- 对每一列和宫格进行同样操作。

3. **最少选择分支：** 选择可选数字个数最少的空格进行递归尝试，减少分支数。

4. **DFS 回溯：**

	- 保存当前状态以便回溯恢复。

	- 递归尝试可选数字，成功则返回，失败则回溯。

## 或者说我们可以尝试另一种变态的算法： （~~跳舞的林克们~~） 舞蹈链

###### 声明：本人研究了一整个晚上只能勉强看懂舞蹈链的内容，所以觉得不配讲太多。

### 前置知识：https://oi-wiki.org/search/dlx/



### 各个模板

```cpp
// 最大节点数MS
// 矩阵行数(n)和列数(m),// 动态节点计数器(idx)
// 每行第一个节点的索引first, 每列的元素个数siz（用于启发式搜索）
constexpr int MS = 1e5 + 5;         
int n, m, idx, first[MS], siz[MS];  
// 节点的左右上下指针
int L[MS], R[MS], U[MS], D[MS];
//节点所属列索引col,节点所属行索引
int col[MS], row[MS];


//remove(c) 表示在 Dancing Links 中删除第 [c] 列以及与其相关的行和列。
void remove(const int& c) {
	L[R[c]] = L[c];  // 从行链表移除c列
	R[L[c]] = R[c];
	
	// 遍历列c的所有行（从D[c]开始，直到回到c）
	for (int i = D[c]; i != c; i = D[i]) {
		// 遍历当前行的所有节点（从R[i]开始，直到回到i）
		for (int j = R[i]; j != i; j = R[j]) {
			// 将节点j从列链表中移除
			// ！！！注意：移除并不是彻底删除，节点只是脱离了链表，我们还是能找到节点并且装回来
			U[D[j]] = U[j];
			D[U[j]] = D[j];
			siz[col[j]]--;  // 更新所在列的节点计数
		}
	}
}

// 恢复列c及其关联行（remove的逆操作）
void recover(const int& c) {
// 逆序遍历列c的所有行（从U[c]开始向上）
	for (int i = U[c]; i != c; i = U[i]) {
		// 逆序遍历当前行的所有节点（从L[i]开始向左）
		for (int j = L[i]; j != i; j = L[j]) {
			U[D[j]] = j;    // 恢复节点在列链表的位置
			D[U[j]] = j;
			siz[col[j]]++;  // 恢复列计数
		}
	}
	// 将列c重新插入行链表
	L[R[c]] = c;
	R[L[c]] = c;
}

// 初始化舞蹈链（r行c列）
void build(const int& r, const int& c) {
	// 初始化列头节点（0~c）
	n = r, m = c;
	for (int i = 0; i <= c; ++i) {
		L[i] = i - 1, R[i] = i + 1;// 水平双向链表
		U[i] = D[i] = i;// 垂直自环
	}
	L[0] = c, R[c] = 0, idx = c; // 将列头尾连成循环链表
	memset(first, 0, sizeof(first));// 每行第一个节点初始化为0
	memset(siz, 0, sizeof(siz));    // 每列计数清零
}

// 在位置(r, c)插入一个节点
// 即在r的右边c的下方插入
void insert(const int& r, const int& c) {
	row[++idx] = r, col[idx] = c, ++siz[c];
	U[idx] = c, D[idx] = D[c], U[D[c]] = idx, D[c] = idx;
	if (!first[r])
		first[r] = L[idx] = R[idx] = idx;
	else {
		L[idx] = first[r], R[idx] = R[first[r]];
		L[R[first[r]]] = idx, R[first[r]] = idx;
	}
}
//dance() 即为递归地删除以及还原各个行列的过程。
//如果[0] 号结点没有右结点，那么矩阵为空，记录答案并返回；
//选择列元素个数最少的一列，并删掉这一列；
//遍历这一列所有有[1] 的行，枚举它是否被选择；
//递归调用 dance()，如果可行，则返回；如果不可行，则恢复被选择的行；
//如果无解，则返回。

int stk[MS];  // 存储选择的行的栈（需外部声明）
int ans;      // 答案（需外部声明）

bool dance(int dep) {
	int i, j, c = R[0];
	if (!R[0]) {
		ans = dep;  // 记录解的行数
		return true;
	}
	// 启发式：选择节点数最少的列（加速搜索）
	int c = R[0];
	for (int i = R[0]; i != 0; i = R[i])
		if (siz[i] < siz[c]) c = i;
	
	remove(c);  // 删除该列

	// 遍历列c的所有行
	for (int i = D[c]; i != c; i = D[i]) {
		stk[dep] = row[i];  // 记录当前行作为解的一部分
		
		// 删除当前行覆盖的所有列
		for (int j = R[i]; j != i; j = R[j]) 
			remove(col[j]);
		
		// 递归搜索下一层
		if (dance(dep + 1)) return true;
		
		// 回溯：恢复删除的行
		for (int j = L[i]; j != i; j = L[j]) 
			recover(col[j]);
	}
	recover(c);
	return false;
}

```

## 代码示例1  剪枝，爽！
```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 200010;

int m = 16 * 16 * 4;
int r[N],l[N],u[N],d[N],s[N],col[N],row[N],idx;
int ans[N],top;
struct Op
{
	int x, y;
	char z;
}op[N];
char g[20][20];

void init()
{
	for (int i = 0 ; i <= m ; i ++)
	{
		l[i] = i - 1,r[i] = i + 1;
		s[i] = 0;//由于多组数据，所以s要初始化
		u[i] = d[i] = i;
	}

	l[0] = m,r[m] = 0;
	idx = m + 1;
}


//十字链表基本操作
void add (int &hh,int &tt,int x,int y)
{
	row[idx] = x, col[idx] = y, s[y] ++;
	u[idx] = y, d[idx] = d[y], u[d[y]] = idx, d[y] = idx;
	l[idx] = hh,r[idx] = tt,r[hh] = idx,l[tt] = idx;
	tt = idx ++;
}

void Remove(int p)
{
	l[r[p]] = l[p],r[l[p]] = r[p];//将p这一列从表头删去

	for (int i = d[p] ; i != p ; i = d[i])//遍历这一列是一的行
		for (int j = r[i] ; j != i ; j = r[j])//把这一行是一的全删去，因为这一行一定不会被选了
		{
			s[col[j]] --;//这一列的一个数减少
			u[d[j]] = u[j],d[u[j]] = d[j]; //进行删去
		}
}

void resume(int p)//p这一列的恢复，与上个函数相反
{
	for (int i = u[p] ; i != p ; i = u[i])
		for (int j = l[i] ; j != i ; j = l[j])
		{
			u[d[j]] = j,d[u[j]] = j;
			s[col[j]] ++;
		}
	l[r[p]] = p,r[l[p]] = p;
}

bool dfs()
{
	if (!r[0])return true;//表示结束

	int p = r[0];
	for (int i = r[0] ; i ; i = r[i])
		if (s[i] < s[p])
			p = i;//找到列上1个数最小的列

	Remove(p);
	for (int i = d[p] ; i != p ; i = d[i])//遍历选择这一列哪一个1
	{
		ans[++ top] = row[i];//选第i行的1
		for (int j = r[i] ; j != i ; j = r[j])Remove(col[j]);//把第i行有一的列全删去

		if (dfs())return true;//继续深搜

		for (int j = l[i] ; j != i ; j = l[j])resume(col[j]);//恢复现场
		top --;//删去选的行
	}
	resume(p);//恢复现场

	return false;//找不到答案
}

int main()
{
	while (~scanf("%s", g[0]))//处理多组输入
	{
		for (int i = 1; i < 16; i ++ ) scanf("%s", g[i]);
		init();//初始化

		for (int i = 0, n = 1 ; i < 16 ; i ++)//n为所建图的行数
			for (int j = 0 ; j < 16 ; j ++)
			{
				int a = 0,b = 15;//a，b为数独上该格能填的数范围
				if (g[i][j] != '-')a = b = g[i][j] - 'A';//表示该格已被填，只有一种选择

				for (int k = a ; k <= b ; k ++ , n ++)//遍历每一种选择，进行建图
				{
					int hh = idx,tt = idx;
					op[n] = {i, j, k + 'A'};//所建图第n行所代表的信息
					add (hh, tt, n, i * 16 + j + 1);
					add (hh, tt, n, 256 + i * 16 + k + 1);
					add (hh, tt, n, 256 * 2 + j * 16 + k + 1);
					add (hh, tt, n, 256 * 3 + (i / 4 * 4 + j / 4) * 16 + k + 1);
				}
			}

		dfs();

		for (int i = 1 ; i <= top ; i ++)
		{
			auto t = op[ans[i]];
			g[t.x][t.y] = t.z;
		}

		for (int i = 0 ; i < 16 ; i ++)puts(g[i]);
		puts("");

	}
	return 0;
}
```

## 代码示例1  DLX
```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 200010;

int m = 16 * 16 * 4;
int r[N],l[N],u[N],d[N],s[N],col[N],row[N],idx;
int ans[N],top;
struct Op
{
	int x, y;
	char z;
}op[N];
char g[20][20];

void init()
{
	for (int i = 0 ; i <= m ; i ++)
	{
		l[i] = i - 1,r[i] = i + 1;
		s[i] = 0;//由于多组数据，所以s要初始化
		u[i] = d[i] = i;
	}

	l[0] = m,r[m] = 0;
	idx = m + 1;
}


//十字链表基本操作
void add (int &hh,int &tt,int x,int y)
{
	row[idx] = x, col[idx] = y, s[y] ++;
	u[idx] = y, d[idx] = d[y], u[d[y]] = idx, d[y] = idx;
	l[idx] = hh,r[idx] = tt,r[hh] = idx,l[tt] = idx;
	tt = idx ++;
}

void Remove(int p)
{
	l[r[p]] = l[p],r[l[p]] = r[p];//将p这一列从表头删去

	for (int i = d[p] ; i != p ; i = d[i])//遍历这一列是一的行
		for (int j = r[i] ; j != i ; j = r[j])//把这一行是一的全删去，因为这一行一定不会被选了
		{
			s[col[j]] --;//这一列的一个数减少
			u[d[j]] = u[j],d[u[j]] = d[j]; //进行删去
		}
}

void resume(int p)//p这一列的恢复，与上个函数相反
{
	for (int i = u[p] ; i != p ; i = u[i])
		for (int j = l[i] ; j != i ; j = l[j])
		{
			u[d[j]] = j,d[u[j]] = j;
			s[col[j]] ++;
		}
	l[r[p]] = p,r[l[p]] = p;
}

bool dfs()
{
	if (!r[0])return true;//表示结束

	int p = r[0];
	for (int i = r[0] ; i ; i = r[i])
		if (s[i] < s[p])
			p = i;//找到列上1个数最小的列

	Remove(p);
	for (int i = d[p] ; i != p ; i = d[i])//遍历选择这一列哪一个1
	{
		ans[++ top] = row[i];//选第i行的1
		for (int j = r[i] ; j != i ; j = r[j])Remove(col[j]);//把第i行有一的列全删去

		if (dfs())return true;//继续深搜

		for (int j = l[i] ; j != i ; j = l[j])resume(col[j]);//恢复现场
		top --;//删去选的行
	}
	resume(p);//恢复现场

	return false;//找不到答案
}

int main()
{
	while (~scanf("%s", g[0]))//处理多组输入
	{
		for (int i = 1; i < 16; i ++ ) scanf("%s", g[i]);
		init();//初始化

		for (int i = 0, n = 1 ; i < 16 ; i ++)//n为所建图的行数
			for (int j = 0 ; j < 16 ; j ++)
			{
				int a = 0,b = 15;//a，b为数独上该格能填的数范围
				if (g[i][j] != '-')a = b = g[i][j] - 'A';//表示该格已被填，只有一种选择

				for (int k = a ; k <= b ; k ++ , n ++)//遍历每一种选择，进行建图
				{
					int hh = idx,tt = idx;
					op[n] = {i, j, k + 'A'};//所建图第n行所代表的信息
					add (hh, tt, n, i * 16 + j + 1);
					add (hh, tt, n, 256 + i * 16 + k + 1);
					add (hh, tt, n, 256 * 2 + j * 16 + k + 1);
					add (hh, tt, n, 256 * 3 + (i / 4 * 4 + j / 4) * 16 + k + 1);
				}
			}

		dfs();

		for (int i = 1 ; i <= top ; i ++)
		{
			auto t = op[ans[i]];
			g[t.x][t.y] = t.z;
		}

		for (int i = 0 ; i < 16 ; i ++)puts(g[i]);
		puts("");

	}
	return 0;
}

```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **<span id="section2C02"></span>WEEK2 C02 波克布林的巡逻范围**

## 题目分析

**给个方阵，一个人在这个方阵里按照i行j列的所有位数的和小于规定数字走格子，问能走的格子数字**

## 解题思路

 **BFS当然能写，套模板秒了，但是这题的数据**
 ### 有问题！！！
 **不加周围位置检查的遍历也能解决，希望老师能改进下数据**

## 为什么遍历解决是不对的？

### 因为格子太大，k太小时，举个例子。

**假设我们只能到达k<=2的位置，但是暴力遍历会导致我们把(10,10)加入可到达的地方，然而显然我们不能到达。**


## 错误代码示例（能过）
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
const int dx[4] = { 0,0,-1,1 };
const int dy[4] = { 1,-1,0,0 };
typedef pair <int, int> PII;


const int N = 53;
bool a[N][N]; 
int k, m, n, x, y, sum;

bool check(int k, int i, int j)
{
	int ij = i / 10 + i % 10 + j / 10 + j % 10;
	return k >= ij;
}

int main() {
	memset(a, 0,sizeof(a));
	cin >> k >> m >> n;
	for(int i=0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			sum+=check(k, i, j);
			}
		}
	cout << sum;
	return 0;
}
```

## 标准代码示例
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

const int dx[4] = { 0, 0, -1, 1 };  // 方向数组：右、左、上、下
const int dy[4] = { 1, -1, 0, 0 };  // 方向数组：右、左、上、下
typedef pair<int, int> PII;

const int N = 53;
bool visited[N][N];  // 访问标记数组
int k, m, n, sum = 0;

// 检查坐标(i,j)的数位和是否小于等于k
bool check(int i, int j) {
	// 计算行坐标的数位和
	int sum_i = i / 10 + i % 10;
	// 计算列坐标的数位和
	int sum_j = j / 10 + j % 10;
	// 判断总和是否<=k
	return (sum_i + sum_j) <= k;
}

int main() {
	// 初始化访问标记数组
	memset(visited, 0, sizeof(visited));

	// 读取输入：阈值k, 行数m, 列数n
	cin >> k >> m >> n;
	if(m==0||n==0) {
		cout << 0; // 如果行或列为0，直接输出0
		return 0;
	}

	// 初始化BFS队列
	queue<PII> q;
	q.push({ 0, 0 });      // 起点(0,0)入队
	visited[0][0] = true; // 标记起点已访问

	// BFS遍历
	while (!q.empty()) {
		auto t = q.front();  // 获取队首
		q.pop();             // 弹出队首

		// 检查当前坐标是否满足条件
		if (check(t.first, t.second)) {
			sum++;  // 满足条件则计数

			// 遍历四个方向
			for (int i = 0; i < 4; i++) {
				int x = t.first + dx[i];
				int y = t.second + dy[i];

				// 检查新坐标是否有效
				if (x >= 0 && x < m && y >= 0 && y < n &&  // 在边界内
					!visited[x][y]) {      // 未被访问

					visited[x][y] = true;  // 标记为已访问
					q.push({ x, y });        // 入队继续扩展
				}
			}
		}
	}

	// 输出可达格子总数
	cout << sum;
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>

# **<span id="section2C06"></span>WEEK2 C06 滚石柱**

## 题目分析

**推石柱，石柱有三种状态：立着（1格）、竖直放置（2格，上下方向）和水平放置（2格，左右方向）。玩家需要将石柱从起点推到目标点，且石柱必须立着到达目标点。地图包含空地（'.'）、障碍（'E'）、目标点（'O'）和石柱的起始位置（'X'）。起始位置可能有一个或两个相邻的 'X'，分别表示石柱起始为立着或躺着状态。**

## 解题思路

### BFS + 状态转移

-   **箱子的状态用三元组 (x, y, op) 表示：**    

	- **op=1：** 立着，位置为 (x, y)。

	- **op=2：** 竖直放置，占据 (x, y) 和 (x+1, y)。

	- **op=3：** 水平放置，占据 (x, y) 和 (x, y+1)。

#### BFS 从初始状态开始，根据当前状态扩展移动方向：

1. **立着状态（op=1）：** 向四个方向推动箱子，箱子会倒下并占据推动方向的两个连续格子。

2. **竖直放置（op=2）：** 只能左右移动（保持状态），或上下移动（变成立着状态）。

3. **水平放置（op=3）：** 只能上下移动（保持状态），或左右移动（变成立着状态）。

移动时需检查目标格子是否可走（非障碍且在地图内）。使用三维数组 vis[op][x][y] 记录访问状态，避免重复搜索。当石柱立着到达目标点时，返回步数；若队列空仍未找到，则输出 "Impossible"。

**~~噩梦级麻烦的BFS~~**


## 算法

## **BFS（广度优先搜索）猛然发现自己还没介绍过** 

#### BFS（Breadth-First Search）是一种图形搜索算法，它从根节点开始，逐层遍历所有相邻节点，然后再遍历相邻节点的相邻节点。BFS 按照"广度优先"的原则进行搜索，即先访问离根节点最近的节点。

### 核心特性：

1. **层级遍历：** 按照距离起始点的层级顺序遍历节点

2. **最短路径：** 在无权图中能找到最短路径

3. **队列实现：** 使用队列（queue）数据结构存储待访问节点

4. **状态标记：** 需要记录已访问节点避免重复访问

### 模板
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>
using namespace std;

// 定义节点类型（根据实际问题调整）
struct Node {
	int x, y; // 示例：二维坐标
	// 其他必要属性...
};

// BFS 模板函数
int bfs(Node start, Node target) {
	// 1. 初始化队列和访问集合
	queue<Node> q;          // 存储待访问节点
	unordered_set<int> visited; // 记录已访问节点（根据实际情况选择数据结构）
	
	// 2. 起点入队并标记
	q.push(start);
	visited.insert(/* 将节点转换为唯一标识 */);
	
	// 3. 初始化步数（如果需要）
	int step = 0;
	
	while (!q.empty()) {
		// 4. 处理当前层的所有节点
		int size = q.size();
		for (int i = 0; i < size; i++) {
			Node cur = q.front();
			q.pop();
			
			// 5. 检查是否到达目标
			if (cur == target) {
				return step; // 找到目标，返回步数
			}
			
			// 6. 遍历当前节点的所有相邻节点
			vector<Node> neighbors = getNeighbors(cur); // 获取相邻节点
			for (Node neighbor : neighbors) {
				// 7. 检查节点是否有效且未访问
				if (isValid(neighbor) && !visited.count(/* 节点唯一标识 */)) {
					// 8. 入队并标记
					q.push(neighbor);
					visited.insert(/* 节点唯一标识 */);
				}
			}
		}
		
		// 9. 完成当前层遍历，步数增加
		step++;
	}
	
	// 10. 未找到目标
	return -1;
}

// 辅助函数：获取相邻节点（根据实际问题实现）
vector<Node> getNeighbors(Node node) {
	vector<Node> neighbors;
	// 添加相邻节点逻辑...
	return neighbors;
}

// 辅助函数：检查节点有效性（根据实际问题实现）
bool isValid(Node node) {
	// 边界检查、障碍物检查等...
	return true;
}

//没错这都是ai写的...很详细不是吗
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
#include <cstdlib>
using namespace std;
const int N = 503;
struct stone {
	int x, y, op, num;
	// 位置(x,y)，状态op1.立直 2.横放平 3.竖放平，步数num
};
int n, m, a[N][N];// 地图大小和地图数据
int tox, toy, startop, stax[3], stay[3], vis[4][N][N];
// 目标点、初始X计数、初始X坐标、访问数组
char ip;
queue<stone> q;

int BFS() {
	while (q.size()) {
		stone t = q.front();
		q.pop();
		if (vis[t.op][t.x][t.y]) continue;
		vis[t.op][t.x][t.y] = 1;

		if (t.op == 1 && t.x == tox && t.y == toy)
			return t.num;

		if (t.op == 1) {
			// 向右推动：变成横放平，检查(x+1,y)和(x+2,y)
			if (t.x + 2 >= 1 && t.x + 2 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x + 1][t.y] && a[t.x + 2][t.y]) {
					q.push(stone{ t.x + 1, t.y, 2, t.num + 1 });
				}
			}
			// 向左推动：变成横放平，检查(x-1,y)和(x-2,y)
			if (t.x - 2 >= 1 && t.x - 2 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x - 1][t.y] && a[t.x - 2][t.y]) {
					q.push(stone{ t.x - 2, t.y, 2, t.num + 1 });
				}
			}
			// 向上推动：变成竖放平，检查(x,y+1)和(x,y+2)
			if (t.x >= 1 && t.x <= n && t.y + 2 >= 1 && t.y + 2 <= m) {
				if (a[t.x][t.y + 1] && a[t.x][t.y + 2]) {
					q.push(stone{ t.x, t.y + 1, 3, t.num + 1 });
				}
			}
			//向下推动：变成竖放平，检查(x, y - 1)和(x, y - 2)
			if (t.x >= 1 && t.x <= n && t.y - 2 >= 1 && t.y - 2 <= m) {
				if (a[t.x][t.y - 1] && a[t.x][t.y - 2]) {
					q.push(stone{ t.x, t.y - 2, 3, t.num + 1 });
				}
			}
		}
		if (t.op == 2) {
			if (t.x >= 1 && t.x <= n && t.y + 1 >= 1 && t.y + 1 <= m){
				if (a[t.x][t.y + 1] && a[t.x + 1][t.y + 1]){
					q.push(stone{ t.x, t.y + 1, 2, t.num + 1 });
				}
			}
			if (t.x >= 1 && t.x <= n && t.y - 1 >= 1 && t.y - 1 <= m) {
				if (a[t.x][t.y - 1] && a[t.x + 1][t.y - 1]) {
					q.push(stone{ t.x, t.y - 1, 2, t.num + 1 });
				}
			}
			//@(@O)@
			//向右推动：变成立直，检查(x+2,y)是否属于非易碎地面
			if (t.x + 2 >= 1 && t.x + 2 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x + 2][t.y] && a[t.x + 2][t.y] != 2) {
					q.push(stone{ t.x + 2, t.y, 1, t.num + 1 });
				}
			}
			//向左推动：变成立直，检查(x-1,y)是否属于非易碎地面
			if (t.x - 1 >= 1 && t.x - 1 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x - 1][t.y] && a[t.x - 1][t.y] != 2) {
					q.push(stone{ t.x - 1, t.y, 1, t.num + 1 });
				}
			}
		}
		if (t.op == 3) {
			if (t.x + 1 >= 1 && t.x + 1 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x + 1][t.y] && a[t.x + 1][t.y + 1]) {
					q.push(stone{ t.x + 1, t.y, 3, t.num + 1 });
				}
			}
			if (t.x - 1 >= 1 && t.x - 1 <= n && t.y >= 1 && t.y <= m) {
				if (a[t.x - 1][t.y] && a[t.x - 1][t.y + 1]) {
					q.push(stone{ t.x - 1, t.y, 3, t.num + 1 });
				}
			}
			if (t.x >= 1 && t.x <= n && t.y + 2 >= 1 && t.y + 2 <= m) {
				if (a[t.x][t.y + 2] && a[t.x][t.y + 2] != 2) {
					q.push(stone{ t.x, t.y + 2, 1, t.num + 1 });
				}
			}
			//1 @
			//2 @
			//3 O
			//4 @
			if (t.x >= 1 && t.x <= n && t.y - 1 >= 1 && t.y - 1 <= m) {
				if (a[t.x][t.y - 1] && a[t.x][t.y - 1] != 2) {
					q.push(stone{ t.x, t.y - 1, 1, t.num + 1 });
				}
			}
		}
	}
	return 0;
}


int main() {
	while (cin >> n >> m && n && m) {
		memset(a, 0, sizeof(a));
		memset(vis, 0, sizeof(vis));
		startop = 0;
		while (q.size())
			q.pop();

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				cin >> ip;
				if (ip == '.') {// 空地
					a[i][j] = 1;
				}
				if (ip == 'E') {// 易碎地面
					a[i][j] = 2;
				}
				if (ip == 'O'){// 终点
					a[i][j] = 1;
					tox = i;
					toy = j;
				}
				if (ip == 'X'){// 起点
					startop++;
					a[i][j] = 1;
					stax[startop] = i;
					stay[startop] = j;
				}
			}
		}
		if (startop == 1) {
			q.push(stone{ stax[1],stay[1],1,0 });// 立直
		}
		else {
			if (stax[1] != stax[2]) {
				q.push(stone{ stax[1],stay[1],2,0 }); // 横躺着
			}
			else {
				q.push(stone{ stax[1],stay[1],3,0 }); // 竖躺着
			}
		}
		int ans = BFS();
		if (!ans) {
			cout << "Impossible" << endl;
			continue;
		}
		cout << ans << endl;
	}
	return 0;
}
```

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>



# **<span id="section2C07"></span>WEEK2 C07 C08 Dijkstra求最短路**

## 题目分析

给定一个n个点m条边的有向图（图中可能存在重边和自环，所有边权均为正值）请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。

~~（分析笑传之抄抄遍）~~

## 解题思路

### 标准的 朴素Dijkstra算法  or  堆优化+Dijkstra算法

因为是稀疏图边数和点数接近，边权均为正值(应用Dijkstra边权必须要为正数！)，存在重边和自环（不影响）


## 算法



1. **初始化：**

   - 距离数组 dist[] 初始化为无穷大（0x3f3f3f3f）

   - 起点 dist[1] = 0

   - 队列放入起点 { 1, dist[1] }

2. **队列非空时循环：**

	- 弹出队列最小元素（当前距离最小的点 ver），若 ver 已确定最短路径则跳过（去重）

	- 标记 ver 的最短路径已确定

	- 遍历 ver 的所有邻接点进行松弛操作：

		- 若 dist[j] > dist[ver] + w[i]，则更新 dist[j]

		- 将更新后的 {dist[j], j} 压入堆

3. **输出结果：**

	- 若 dist[n] 仍为初始值，输出 -1

	- 否则输出 dist[n]

### **2. 堆优化+Dijkstra算法** 

1. **除了做到上面的Dijkstra内容外，还引入了小根堆**
```cpp
priority_queue<PII, vector<PII>, greater<PII>> q
```
2. **作用在于**:

	-   堆中元素为 {距离, 节点}，确保按距离从顶部到底部从小到大排序

	-   节约了在堆中寻找最小元素的时间。

### 模板和代码一致


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
const int N = 100010;
bool state[510];
int h[510], e[N], ne[N], w[N], idx = 0;
int dist[510];//queue,distance
int n, m;

void add(int a, int b, int c) {
	e[idx] = b;     // 边idx指向b1         p.num=b;
	w[idx] = c;     // 边的权重为c         p.to_next_num=c;
	ne[idx] = h[a]; // idx继承a原来的头边  p.next=head[a]; 
	h[a] = idx;     // a的头边更新为边idx  head[a]=p;
	idx++;          //为下一条边准备
}



void Dijkstra1(){
	memset(dist, 0x3f3f3f3f, sizeof(dist));
	memset(state, false, sizeof(state));
	dist[1] = 0;                    
	for (int i = 0; i < n; i++) {   // *需要确定n个点所以我们不对state[1]进行初始化
		int t = -1;                 // t用于存储当前未访问节点中距离最小的节点
		for (int j = 1; j <= n; j++) {
			// 如果节点j未被访问且距离小于当前最小距离
			if (!state[j] && (t == -1 || dist[j] < dist[t])) {  
				t = j;              // 更新t为当前节点j
			}
		}
		state[t] = true;            // 标记t为已访问

		for (int j = h[t]; j != -1; j = ne[j]) {   // 遍历t的所有邻接节点
			int k = e[j];           // 获取邻接节点k
			dist[k] = min(dist[k], dist[t] + w[j]);// 更新k的最短距离
		}
	}
}






typedef pair<int, int> PII;//堆里存储距离和节点编号

// 1.初始化dist和st 
// 2.找到未访问节点中距离最小的节点t，标记为已访问 
// 3.更新t的所有邻接节点的距离

int dijkstra2()
{
	memset(dist, 0x3f, sizeof dist);//距离初始化为无穷大
	memset(state, false, sizeof(state));
	dist[1] = 0;
	priority_queue<PII, vector<PII>, greater<PII>> heap;//小根堆
	heap.push({ 1 , dist[1] });//插入距离和节点编号

	while (heap.size())
	{
		auto t = heap.top();//取距离源点最近的点
		heap.pop();

		int ver = t.first , distance = t.second; //distance:源点距离ver 的距离,ver:节点编号

		if (state[ver]) continue;//如果距离已经确定，则跳过该点
		state[ver] = true;

		for (int i = h[ver]; i != -1; i = ne[i])//更新ver所指向的节点距离
		{
			int j = e[i];
			if (dist[j] > dist[ver] + w[i])
			{
				dist[j] = dist[ver] + w[i];
				heap.push({ j,dist[j] });//距离变小，则入堆
			}
		}
	}

	if (dist[n] == 0x3f3f3f3f) return -1;
	return dist[n];
}





int main()
{
	memset(h, -1, sizeof(h));
	cin >> n >> m;
	for (int i = 1; i <= m; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		add(a, b, c);
	}

	//Dijkstra1();
	//if(dist[n] == 0x3f3f3f3f) {
	//    cout << "-1" << endl; // 如果无法到达节点n，输出-1
	//} else {
	//    cout << dist[n] << endl; // 输出从节点1到节点n的最短距离
	//}

	//or

	cout << dijkstra2() << endl; // 使用Dijkstra2方法输出最短距离
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>


# **<span id="section3A02"></span>WEEK3 A02 01背包问题**

## 题目分析

**给定N个只能装一次的物品和V的容量的背包以及每个物品的价值，求背包能装下的最大价值的物品。**

## 解题思路

### 线性DP

**其中dp数组代表前i个物品放入容量为j的背包的最大价值。**

1. **输入完数据以后如果当前容量无法容纳第i个物品：**

	-继承前i-1个物品的结果，**dp[i][j] = dp[i - 1][j];**

2. **当前容量可以容纳第i个物品：**

	- 决策：不放入i 或 放入i中取最大值：**dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + p[i])**

3. **关键点：** 第i个物品是否放入和之前做过的决策有关系，dp[i]的状态与dp[i-1]息息相关

4. 参考代码在代码示例1

## 优化

### **1. 滚动数组** 

- **我们发现，每次求背包的新状态时，只会出现i与i-1的dp数组，于是考虑用滚动数组解决这个问题**

	- 关键在于dp数组的状态为dp[2][N]，边输入边处理，参考代码示例2


### **2. 一维数组直接边输入边处理** 

- **我们又发现，每次求背包的新状态时，只要保存好原本的状态就会马上更新，我们只需要最终状态，并不在乎过程如何实现**

	- 于是直接输入时就处理，需要注意的是，此时我们会从大到小遍历背包（避免重复装，变成完全背包问题）



## 代码示例1
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

const int N = 1003;
int n, v;// n-物品数量, v-背包容量
// a[i]-第i个物品的体积, p[i]-第i个物品的价值
// dp[i][j]：前i个物品放入容量为j的背包的最大价值
int a[N], p[N], dp[N][N];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	cin >> n >> v;
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		cin >> p[i];
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= v; j++) {
			if (j < a[i])
				// 当前容量无法容纳物品i
				// 继承前i-1个物品的结果
				dp[i][j] = dp[i - 1][j];
			else
				// 决策：不放入i 或 放入i（取最大值）
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + p[i]);
		}
	}
	cout << dp[n][v] << endl;
	return 0;
}
```

## 代码示例2
```cpp
const int N = 1003;
int v[N];
int w[N];
int f[2][N];
int main(){
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i = 1;i <= n;i ++) cin >> v[i] >> w[i];
	for(int i = 1;i <= n;i ++){
		for(int j = 0;j <= m;j ++){
			f[i & 1][j] = f[i - 1 & 1][j];
			if(j >= v[i]) f[i & 1][j] = max(f[i & 1][j],f[i - 1 & 1][j - v[i]] + w[i]);
		}
	}
	cout << f[n&1][m];
	return 0;
}
```


## 代码示例3
```cpp
const int MAXN = 1003;
int f[MAXN];  //f[i]表示容量为i的背包能获得的最大价值

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int n, m;   // n-物品数量, m-背包总容量
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		int v, w;   // v-当前物品体积, w-当前物品价值
		cin >> v >> w;      // 边输入边处理
		// 关键：从大到小遍历背包容量（逆序）
		for (int j = m; j >= v; j--)
			// 状态转移方程：
			// 选择1：不装当前物品 → f[j] 保持不变
			// 选择2：装当前物品 → f[j-v] + w（腾出v空间后的最优解加上当前物品价值）
			f[j] = max(f[j], f[j - v] + w);
	}
	cout << f[m] << endl;
	return 0;
}
```
### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>



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



# **<span id="section3C05"></span>WEEK3 C05 没有上司的舞会**

## 题目分析

给定一棵树结构表示公司职员的上下级关系，每个节点（职员）有对应的快乐值。要求选择部分职员参加舞会，使得快乐值总和最大，但限制是任何职员不能与其直接上司同时参加，即其直接父节点如果存在子节点不能存在。

## 解题思路

### 树状DP

1. **邻接表建树，同时记录存在父节点的节点**

2. **状态定义：对每个节点 u 定义两个状态：**

- dp[u][0]：不选 u 时，以 u 为根的子树的最大快乐值。

- dp[u][1]：选 u 时，以 u 为根的子树的最大快乐值。

3. **状态转移（关键）：**

- 通过DFS后序遍历树，确保在计算父节点状态前，子节点状态已计算完成。

- **不选 u 时：** 子节点可选可不选，取最大值：

	- 对于所有u的子节点都有 dp[u][0] += max(dp[j][1], dp[j][0])

- **选 u 时：** 所有子节点必须不选： dp[u][1] += dp[j][0]

## 算法

### **1. 树状DP** 

- **树状DP是一种在树形结构上进行动态规划的技术，其核心思想是自底向上递归计算。具有以下特性：**

- **递归结构：** 每个子树独立且结构相似

- **无环性：** 状态转移不可能成环

- **父子依赖：** 节点状态受其子节点状态影响，所以是后序遍历（DFS递归），回溯时用子节点更新父节点状态。

- **常用维度：** dp[u][k] 表示以节点 u 为根的子树在状态 k 下的最优解


### 模板(AI)

```cpp
//以 树的最长路径为例子
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10; // 根据题目调整大小

// 图存储结构
vector<int> g[N];      // 邻接表存树
bool vis[N];           // 访问标记（可选）
int dp[N][2];          // DP状态数组，维度根据问题调整
int w[N];              // 节点权值（根据问题需要）

// 树状DP核心函数
void dfs(int u, int parent) {
	// 初始化状态（根据具体问题设置）
	dp[u][0] = 0; 
	dp[u][1] = w[u];
	
	// 遍历所有子节点
	for (int v : g[u]) {
		if (v == parent) continue;  // 避免回父节点
		
		dfs(v, u);  // 递归处理子树
		
		// 状态转移（根据具体问题设计）
		dp[u][0] += max(dp[v][0], dp[v][1]); // 示例转移
		dp[u][1] += dp[v][0];                // 示例转移
	}
	
	// 可选的额外处理（如合并结果、更新全局答案等）
}

int main() {
	// 初始化图
	int n;
	cin >> n;
	
	// 读入权值（根据问题）
	for (int i = 1; i <= n; i++) cin >> w[i];
	
	// 建树
	for (int i = 1; i < n; i++) {
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u); // 无向图
	}
	
	// 选择根节点（通常取1）
	int root = 1;
	
	// 执行树状DP
	dfs(root, -1); // -1表示根节点的父节点不存在
	
	// 输出结果（根据问题）
	cout << max(dp[root][0], dp[root][1]) << endl;
	
	return 0;
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
#include<unordered_set>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;
//ios::sync_with_stdio(false);
	//cin.tie(nullptr);
	//cout.tie(nullptr);




const int N = 6003;

int h[N], w[N], ne[N], e[N], idx;
;// dp[u][0]:不选u的最大值, dp[u][1]:选u的最大值
int dp[N][2];
bool has_father[N];

// 添加边：a->b (a是b的上司)
void add(int a, int b)
{
	e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}


// DFS遍历树 (u:当前节点)
void dfs(int u){
	dp[u][1] = w[u];    // 选择u节点，初始化为u的权值
	dp[u][0] = 0;       // 不选u节点，初始化为0
	for (int i = h[u]; i != -1; i=ne[i]) {
		int j = e[i];
		dfs(j);// 递归处理子树
		// u不选时，子节点可选可不选
		dp[u][0] += max(dp[j][1], dp[j][0]);
		// u选时，子节点必须不选
		dp[u][1] += dp[j][0];
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	memset(h, -1, sizeof(h));
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> w[i];
	}
	for (int i = 1; i < n; i++)
	{
		int a, b;
		cin >> a >> b;
		has_father[a] = true;
		add(b, a);
	}
	int root = 1;
	// 寻找根节点 (没有父节点的节点)
	while (has_father[root]) root++;
	dfs(root);
	// 答案 = max(不选根节点, 选根节点)
	cout << max(dp[root][0], dp[root][1]) << endl;
	return 0;
}
```

### [>>>点我返回目录位置<<<](#section1)
<br>
<br>
<br>


# **<span id="sectionSP1"></span>SPECIAL1 KMP字符串**

## 没错，附加环节！耶✌

**这道题来自校外实训WEEK1，然而我并没有选上校外实训是自己写的。我苦思冥想一天才学会，写的注释比代码还长，~~太痛苦了~~太有意思了，决定写题解**

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

# 

