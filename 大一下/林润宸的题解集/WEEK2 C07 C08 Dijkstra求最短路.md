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