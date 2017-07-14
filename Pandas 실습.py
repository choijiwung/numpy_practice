## Pandas 실습
import pandas as pd
s = pd.Series([99887766,88776655,11223344,22448866], index=["서울","부산","인천","대구"])

##print(s)

b =pd.Series(range(10,14))
##print(b)

##print(s.index)
##print(s.values)

s.name = "인구"  ## value 의 값을 지정
s.index.name = "도시" ## index의 값을 지정
##print(s)

## 시리즈 연산
## 인덱스 라벨에는 영향을 끼치지 않는다.
## numpy 처럼 1차원 배열과 종일하게 벡터화 연산을 할 수 있다.
##print(s/100000)

##print(s[1])
##print(s["부산"])

##print(s[3])
##print(s["대구"])

## 배열 인덱싱을 하면 자료의 순서를 바꾸거나 특정한 자료만 선택할 수 있따.

##print(s[[0,3,1]])

##print(s[["서울","대구","부산"]])

##문자열 라벨을 이용한 슬라이싱을 하는 경우 콜론(:) 기호 뒤에 오는 인덱스에 해당하는 값도 포함된다는 점이 일반적인 인덱싱과 다르다.

print(s[(25000 < s) & (s < 44444444)])
