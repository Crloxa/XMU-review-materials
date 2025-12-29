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