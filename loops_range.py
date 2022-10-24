num = [1,2,3,4,5,6,9]
# for i in num:
#     print(i)

print('length of num',len(num))

i = 0
while i < len(num):
    print(num[i])
    i = i + 1

# range()
num = range(5,10,2)
for i in num:
    print(i)
# without var set to range()
for j in range(0,7,2):
    print(j)