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