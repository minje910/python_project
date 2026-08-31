# 변수
a =  2
b = 3
print(a,b)

a = 2; b = 3; print(a,b)  # 권장하지 않음
a,b = 2,3 # 권장
print(a,b)  # a = (2,3), b = 3


# 값 swap

temp = a
a = b
b = temp
print(a,b)

a,b = b,a  # 권장
print(a,b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 예약어 금지
# 대소문자 구분
하이 = 10
print(하이)  # 한글 변수명 가능(비권장)


# name! = "뽀로로"  # 특수문자 불가
# 2name = "크롱"
_age = 23

print(_age)  # _로 시작하는 변수명 가능

# class = "클래스"  # 예약어 금지

student_name = "크롱" #snake_case
SudentName = "뽀로로" #camelCase

MAX_SCORE = 100 # 상수(변경 불가) 권장 대문자