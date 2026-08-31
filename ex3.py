# 불리언 (bool)
a = True
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("apple" > "apble")

# bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([10]))
print(bool([]))

# None 자료형
a = None
print(a, type(a))
print(bool(a))  # None은 False로 취급

if a is None:
    print("값이 없습니다.")