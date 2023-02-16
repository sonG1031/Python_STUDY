# import calcpkg.operation as op
# import calcpkg.geometry as geo

# print(op.add(10, 20))
# print(op.mul(10, 20))

# print(geo.triangle_area(30, 40))
# print(geo.rectangle_area(30, 40))

# calcpkg의 __init__.py에서 하위 모듈을 함께 가져오게 만들었으므로 
# import calcpkg로 패키지만 가져와도 calcpkg.operation.add(10, 20)처럼 사용할 수 있습니다.
# import calcpkg

# print(calcpkg.operation.add(10,20))
# print(calcpkg.operation.mul(10, 20))

# print(calcpkg.geometry.triangle_area(30, 40))
# print(calcpkg.geometry.rectangle_area(30, 40))

from calcpkg import *

print(dir()) # dir 함수를 호출하여 현재 네임스페이스(namespace, 이름공간)를 확인

print(add(10, 20))    
print(mul(10, 20))    
 
print(triangle_area(30, 40))    
print(rectangle_area(30, 40))   