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