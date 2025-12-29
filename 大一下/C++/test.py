N=int(input())
 
a=[0]+list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
 
dp=[[0 for i in range(N+2)] for j in range(N+2)]
 
for i in range(1,N+1):
    maxv=1
    for j in range(1,N+1):
        dp[i][j]=dp[i-1][j]
        if a[i]==b[j]:
            dp[i][j]=max(dp[i][j],maxv)
        if b[j]<a[i]:
            maxv=max(maxv,dp[i-1][j]+1)  #为什么这样更新最大值其实我没有很懂
                                        #后面懂了，因为k是对j的枚举，对代码的等价变形，先看看上面朴素法三重循环有maxv版
 
print(max(dp[N]))