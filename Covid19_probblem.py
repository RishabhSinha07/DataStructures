
def check_for_covid(no_of_people,distance):
    temp = []
    size = 1
    for i in range(no_of_people-1):
        if distance[i+1] - distance[i] < 3:
            size+=1
        else:
            temp.append(size)
            size = 1
    temp.append(size)
    return  temp

no_of_cases = int(input())
a = []
b = []
for _ in range(no_of_cases):
    no_of_people = int(input())
    distance = list(map(int,input().split(' ')))
    a.append(no_of_people)
    b.append(distance)

for a1,b1 in zip(a,b):
     z = check_for_covid(a1,b1)
     print(min(z),max(z))