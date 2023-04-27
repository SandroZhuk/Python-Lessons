# A = 0
# B = 0
#
# f = not (not A or B)
# print(f)


#  a     b       a or 1      b and 0     f3
#  0     0          1           0         1
#  0     1          1           0         1
#  1     0          1           0         1
#  1     1          1           0         1


f1 = (0 or 1) and (0 or 1)
print("f1 = ", f1)

f2 = 0 or 1 and  0 or 1 # note: 0 or 0 or 1
print('f2 = ', f2)

a = 0
b = 0

f3 = (a or 1) or (b and 0)
print('f3 = ', f3)