# if (E,W) print "-"
# if (N,S) print "|"
# if (SE,NW) print "\"
# if (SW,NE) print "/"

DIRECTION = input().split()
STEPS = input().split()
spaces = 0
for direction,steps in zip(DIRECTION,STEPS):
    if direction in ["E","W"]:
        print("|",end="")
        print(" "*(spaces-1),end="")
        print("-"*int(steps),end="")
        spaces += int(steps)-1
    if direction in ["N","S"]:
        print("")
        for _ in range(int(steps)):
            print("|",end="")
            print(" "*(spaces),end="")
            print("|")
    if direction in ["NE","SW"]:
        for _ in range(int(steps)):
            print("|",end="")
            print(" "*(spaces-2),end="")
            spaces-=1
            print("/")
    if direction in ["SE","NW"]:
        for _ in range(int(steps)):
            print("|",end="")
            print(" "*(spaces),end="")
            spaces+=1
            print("\\")