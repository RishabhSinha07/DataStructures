# You want to buy a laptop. Each laptop has two parameters: Rating & Price. Your task is to buy a laptop with the
# highest rating within a given price range. Given Q tasks, each query consisting of price range required,
# you have to print the highest rated laptop that can be bought within that price range.


# The first line contains N denoting the number of inputs.
# The following N lines contain P & R denoting price and range of a laptop.
# Next line contains Q denoting the number of queries.
# The following Q lines contain two integers X & Y denoting the price range (inclusive).
# input
# 5
# 1000 300
# 1100 400
# 1300 200
# 1700 500
# 2000 600
# 3
# 1000 1400
# 1700 1900
# 0 2000
# output
# 400
# 500
# 600

temp = int(input())
dict = {}
for _ in range(temp):
    i = list(map(int,input().split()))
    dict.update({i[0]:i[1]})
q = int(input())
for _ in range(q):
    result = []
    z = list(map(int,input().split()))
    for val in dict.keys():
        if val >= z[0] and val <= z[1]:
            result.append(dict[val])
    print(result)


