# **<span id="section2C05"></span>WEEK2 C06 滚石柱**

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