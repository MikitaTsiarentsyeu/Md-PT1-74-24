
l = [1,2,3,4,5]

l = [[1,2,3], [4,5,6], [7,8,9]]
print(l[0], l[1], l[2])
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = (l, "test")
t[0][0][0] = 'one'
print(t)

d = {(1,2,3):"one two three"}
print(d)
print(d[(1,2,3)])

# d[t] = "new value"
# print(d)