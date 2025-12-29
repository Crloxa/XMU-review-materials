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