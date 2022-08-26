n = int(input())    # 输入人数

dic = {}   # 创建数组

for _ in range(n):
     D, x, y = input().split()
     dic[D] = int(x)**2 + int(y)**2

end = max(list(dic.values()))
first = min(list(dic.values()))
dic_re = {}
for k, v in dic.items():
    dic_re[v] = k

print(dic_re[first], dic_re[end])



""""
 3
 000 1 2
 001 2 2
 002 2 5
 
 
 """