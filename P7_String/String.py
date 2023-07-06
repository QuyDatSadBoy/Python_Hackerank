s = ["28tech", "python", "C++"]
t = ','.join(s)
print(t)
u = '##'.join(s)
print(u)

s = "28TeCH jAVa PyThon"
s1 = s.upper()
print(s1)
s2 = s.lower()
print(s2)
s3 = s.swapcase()
print(s3)
s4 = s.title()
print(s4)
s5 = s.capitalize()
print(s5)

# • upper(): Chuyển sang in hoa.
# • lower(): Chuyển sang in thường.
# • capitalize(): Viết hoa chữ cái đầu của xâu.
# • swapcase(): Chuyển chữ hoa thành thường
# và ngược lại.
# • title(): Viết hoa chữ cái đầu của từng từ,các
# kí tự còn lại viết thường

print('{:.2f}'.format(20, 1))

# -str.format()
s = '{0} is {1} years old !'.format('CR7', 37)
print(s)

# -f-String
name = "CR7"
age = 37
s = f'{name} is {age} years old !'
print(s)
