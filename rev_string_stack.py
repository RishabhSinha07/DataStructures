
def rev(inp):
    inp_ = []
    for i in range(len(inp)):
        inp_.append(inp.pop())
    return inp_

a = []
a.append('a')
a.append('b')
a.append('c')
a.append('d')
a.append('e')
print(a)
print(rev(a))