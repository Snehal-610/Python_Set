# # 4. Create a function that will take unlimited arguments and should add all the arguments which are passed.
def add(*args):
    res = 0
    for i in args:
        for j in i:
            res += j
        return res
n = []
while True:
    UnlimitedArgs = int(input("Enter your input for adition: "))
    if not UnlimitedArgs:
        break
    n.append(UnlimitedArgs)
res = add(n)
print(res)