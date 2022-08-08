# 문자열 한 줄을 여러 줄로 입력하고 싶을때
# \를 사용하여 줄바꿈을 한 뒤 다음 줄에서 문자열을 계속 입력할 수 있습니다.
s = 'Fortunately, however, for the reputation of Asteroid B-612, \
a Turkish dictator made a law that his subjects, under pain of death, \
should change to European costume. \
So in 1920 the astronomer gave his demonstration all over again, \
dressed with impressive style and elegance. \
And this time everybody accepted his report.'

print(s)

price = int(input())
coupon = input()

if coupon == 'Cash3000':
    print(price - 3000)
if coupon == 'Cash5000':
    print(price - 5000)