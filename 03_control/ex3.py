# for문

# for (int i = 0; i < 10; i++)
# for i in iterable객체:

# while문과 달리 for문은 iterable객체를 순회하며 반복한다.

for i in range(5):
    print(i, end=" ")
print()

a = range(5)

print(a.start, a.stop, a.step)


for i in range(1,6,1):
    print(i, end=" ")
print()

# 0~10중에 짝수 출력
for i in range(0, 11, 2):
    print(i, end=" ")
print()
# 5 4 3 2 1 출력
for i in range(5, 0, -1):
    print(i, end=" ")

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"\nsum: {tot}")

print(sum(range(1,11))) # 내장함수 sum() 사용

# 1 ~ 10까지의 합
sum = 0
for i in range(1, 11):
    sum += i
else:
    print(f"\nsum: {sum}")

# print(sum(range(1,11))) # 내장함수 sum() 사용 *위에 변수로 선언되면 내장함수로 존재 불가

# s = "hi12한글韓國😊3️⃣"

# for c in s:
#     print(c, end=" ")
# print()
# print(len(s))

# 구구단 출력
# 2 * 1 = 2
# 2 * 2 = 4
#...
# 9 * 9 = 81

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j: <5d}", end= "")
    print()
else:
    print("end")