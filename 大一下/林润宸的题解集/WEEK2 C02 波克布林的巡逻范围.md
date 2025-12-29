# **<span id="section2C02"></span>WEEK2 C02 波克布林的巡逻范围**

## 题目分析

**给个方阵，一个人在这个方阵里按照i行j列的所有位数的和小于规定数字走格子，问能走的格子数字**

## 解题思路

 **BFS当然能写，套模板秒了，但是这题的数据有问题，不加检查遍历也能解决，希望老师能改进**

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