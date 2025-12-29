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