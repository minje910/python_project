# 반복문 : while문, for문

# while문
# 1~10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break
else:
    print("while문 종료")

nums = [1,3,5,7,9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print("find")
        break
    i += 1
else:
    print("not find")

# if not found:
#     print(f"{target} not found")

# 1~10까지의 합
# sum = 55
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(f"sum: {tot}")

tot = 0
i = 1

while i <= 10:
    if i %  2 == 1:
        i += 1
        continue 
    tot += i
    i += 1
print(f"sum: {tot}")