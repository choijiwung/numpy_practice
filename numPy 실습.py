import numpy as np
a =  np.array([0,1,2,3,4,5,6,7,8,9])
##print(a)

##print(type(a))

b = []

for ai in a:
    b.append(ai * 2)
##print(b)

x = np.array(a)
##print(x)

##print(x +2)

##L = [0,1,2,3,4,5,6,7,8,9]
##print(2*L)
## 일반적으로 리스트에는 리스트가 2번 반복된다.

##a = np.array([1,2,3])
##b = np.array([10,20,30])

## print(2 * a + b)

##print(np.exp(a)) ## 자연로그 e의 X승

##print(np.log(b)) ## log 를 취한다

##print(np.sin(a)) ## 1도 2도 3도 sin함수 값구하기

##b = np.array([[0,1,2],[3,4,5]])
##print(b)
##print(len(b)) row = 행의 갯수
##print(len(b[1])) row = 열의 갯수

##연습문제 1
## 2 x 4 array

a = np.array([[10,20,30,40],[50,60,70,80]])
## print(a)

c = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
                 ,[[11,12,13,14],[15,16,17,18],[19,20,21,22]]])

##print(c)
##print(len(c))
##print(len(c[0]))
##print(len(c[0][0]))

##print(c.ndim) ##차원의 갯수
##print(c.shape) ## 배열의 모양

##a = np.array([[0,1,2],[3,4,5]])
##print(a)

##print(a[0,0])  ##첫번째 행(row)의 첫번째 열(column)
##print(a[1,1]) ## 두번쨰 행(row)의 두번쨰 열(column)
##print(a[0,1])  ## 첫번쨰 행(row) 의 두번쨰 열(column)

a = np.array([[0,1,2,3],[4,5,6,7]])
##print(a)

##print(a[0,:]) ## 첫번째 행(row) 전체
##print(a[:,0]) ## 첫번째 열(column) 전체

##print(a[1,:]) ## 두번째 행(row) 전체
##print(a[:,2]) ## 세번째 열(column) 전체

##print(a[1,1:]) ## 두번째 행 2번째 열부터 전체
##print(a[0:,2:]) ## 두번째 열부터 2번째 행끝까지

m = np.array([[ 0, 1, 2, 3, 4],
              [5 ,6 ,7 ,8, 9],
              [10,11,12,13,14]])
##문제 1번
##print(m[1,2])
##print(m[2,4])
##print(m[1,1:3])
##print(m[1:,2:3])
##print(m[0:2,3:6])

a = np.array([0,1,2,3,4,5,6,7,8,9])
idx = np.array([True, False, True, False, True, False, True,False,True,False ])
##print(a[idx])

##print(a[a%2 ==0])
##a = np.array([0,1,2,3,4,5,6,7,8,9]) * 10
##idx = np.array([0,2,4,6,8])
##print(a[idx])

##a = np.array([0,1,2,3]) * 10
##idx = np.array([0,0,0,0,1,1,1,2,2,2,3,3,3])
##print(a[idx])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = [True,False,False,True]
print([a[:,b]])



