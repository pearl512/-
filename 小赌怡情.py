''' 常言道“小赌怡情”。
这是一个很简单的小游戏：
   首先由计算机给出两个整数；然后玩家下注赌第二个整数将会比第一个数大还是小；玩家下注t个筹码后，计算机进行运算。
   玩家猜对了，则系统奖励玩家t个筹码；否则扣除玩家t个筹码。
   注意：玩家下注的筹码数不能超过自己帐户上拥有的筹码数。当玩家输光了全部筹码后，游戏就结束。
bug: n1 n2 小概率会相等，此处未进行处理。
'''

import random as r    # 导入自动生成数字的库

T, n = map(int, input().split())    # T为初始筹码数，n为进行次数

temp = 0

for _ in range(n):
    n1 = r.randint(0, 20)
    n2 = r.randint(0, 20)
    b, t = map(int, input().split())
    if T < t:
        print("筹码不足。")
        continue
    if n1 > n2:      # 0赌后面的小，1赌后面的大
        temp = 0
    elif n1 <= n2:
        temp = 1
    if temp == b:
        T += t
        print("胜利！获得筹码%d，当前持有%d筹码" % (t, T))
        print("数字为：%d,%d" % (n1, n2))
    else:
        T -= t
        print("失败！失去筹码%d，当前持有%d筹码" % (t, T))
        print("数字为：%d,%d" % (n1, n2))
    if T == 0:
        print("您当前筹码不足，无法继续游戏！")
        continue
