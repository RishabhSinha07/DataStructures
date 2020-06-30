# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

if __name__ == "__main__":
    inp = [int(x) for x in input().split()]

    # 'sp' to keep the count for max selling price
    # temp to compare values to sp

    sp = 0
    temp = 0

    # for i in range(len(inp)):
    #     for j in range(i, len(inp)):
    #         if inp[j] - inp[i] > temp:
    #             temp = inp[j] - inp[i]
    # print(temp)

    i = j = 0
    while i<=len(inp)-1 and j<=len(inp)-1:
        if inp[j] - inp[i] >= temp:
            temp = inp[j] - inp[i]
            j+=1
            continue
        if inp[j] - inp[i] < 0:
            i += 1
            continue
        i+=1
    print(temp)