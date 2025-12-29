# **A05 假币问题** 

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
<br>
<br>
<br>