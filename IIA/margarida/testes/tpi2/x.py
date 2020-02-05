class P:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "(" + self.x + "," + self.y + ")"

a = P(1,2)
b = P(1,2)

print(a==b)

lst = [1,3,4,26,13,10]

for x in lst:
    if x%13==0:
        break
print(x)

