# input : No of items fit in the bags , Weight the bag can hold
# After this we have: Price of the item and the weight of the item.
# The weight should not exceed the weight mentioned and the price should be maximum.
# # Calculate for all fixed weight by changing the number of items in the bag from lower to upper.
# For the problem :
#
# 3, 50
# 60, 20
# 100, 50
# 120, 30
#
# Now since we have 3 as max no of items, we will calculate for 1 item with 50kgs weight. Then move to 2 and so on!.
import collections

[inb, mw] = map(int, input().split(','))

weighted_input = collections.defaultdict(int)

for _ in range(inb):
    temp = list(map(int, input().split(',')))
    weighted_input[temp[0]] = temp[1]

print(weighted_input)

dp = [[] for _ in range(inb)]

for i in range(inb):
    weight = 0
    temp = i+1
    if temp == 1:
        for j in weighted_input.keys():
            if weighted_input[j] <= mw and j > weight:
                weight = j
                dp[i] = [j, weighted_input[j]]
    else:
        weight1 = mw-dp[temp-1][1]
        if weight1 <= 0:
            dp[temp] = dp[temp-1]
        else:
            for j in weighted_input.keys():
                if weighted_input[j] <= weight1 and j > weight:
                    weight = j
                    new = [j, weighted_input[j]]
            dp[i].append(new)

print(dp)



