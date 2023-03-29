mol = [int(x) for x in input().split()]
print(mol)
n = mol[0]
m = mol[1]
print(n, m)
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
print(k)
for i in k:
    set_1.add(i)
print(set_1)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')