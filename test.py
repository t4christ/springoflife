import sys
nums_squared_lc = [i * 2 for i in range(10)]

cnum = list(nums_squared_lc)

print(nums_squared_lc)
print(cnum)
nums_squared_lc.append(20)

print(nums_squared_lc)
print(cnum)

nums_squared_lc[0]=1


print(nums_squared_lc)
print(cnum)
# print(nums_squared_lc)
# nums_squared_gc = (i * 2 for i in range(10000))
# print(nums_squared_gc)

# x,y = 4,5
# temp = x 
# x = y
# y = temp


# a=["faith","kola","fred","glory"]

# b = iter(a)

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     print("temp1",temp)
#     reversed_num = 0

#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#         print("temp2",temp,reversed_num)
#     if num == reversed_num:
#         return num
#     else:
#         return False


# print(is_palindrome(121))