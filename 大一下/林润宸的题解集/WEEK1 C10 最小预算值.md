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