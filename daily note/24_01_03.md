# Numbers

# Numerical caclulations
a = 3 + 4*5

print(a)

b =23.45 / 1e-02

print(b)

# Numbers에 있는 작은 메소드 세트

c = 1172.5

# as_integer_ration()는 파이썬의 'float' 객체에서 정수 비율을 제공하는 메서드
print(c.as_integer_ratio())
# is_integer()는 'float'객체에 속하는 메서드로, 해당 부동 소수점 숫자가 정수인지 여부를 확인한다.
print(c.is_integer())

# numerator는 파이썬의 'fractions'모듈이나 Fraction 클래스에 사용되는 속성
# 이 속성은 분자의 분자를 나타내는 정수 값을 반환한다.

d = 12345
print(d.numerator)

from fractions import Fraction

fraction = Fraction(3,4)
numerator_value = fraction.numerator

print(numerator_value)

# denominator는 분수의 속성 중 하나로, 분모를 나타낸다.
print(d.denominator)

# bit_length()는 정수형 데이터 타입에 해당하는 숫자의 이진 표현에서 필요한 비트 수를 반환하는 메서드
print(d.bit_length())


# String 조작

symbols = 'AAPL IBM MSFT YHOO SCO'

# 인덱스를 활용한 문자열 추출
print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])  # Last character
print(symbols[-2])  # 2nd from last character


print(symbols[:4])  # 인덱스 3의 값까지 추출
print(symbols[-3:])  # 끝에서 3번째 값까지 추출
print(symbols[5:8])  # 인덱스 5의 값부터 7의 값까지 추출

# 문자열은 읽기 전용이다. symbols의 첫 번째 문자를 'a'로 변경하면 에러가 발생
# symbols[0] = 'a'
# print(symbols)

# 문자열 연결
# 두가지 예시 모두 완전히 새로운 문자열이 생성되며 변수이름은 결과에 바인딩
# 이전 문자열은 더 이상 사용되지 않으므로 삭제된다.
symbols += ' GOOG'
print(symbols)

symbols = 'HPQ ' + symbols
print(symbols)

# 연산자를 사용하여 in 부분 문자열을 확인할 수 있다.
print('IBM' in symbols)
print('AA' in symbols)
print('CAT' in symbols)

#  lower() 메서드를 통해 symbols를 모두 소문자로 바꿨지만, 문자열은 항상 읽기 전용이므로 작업결과를 저장하려면 변수에 저장해야한다.
print(symbols.lower())
print(symbols)

# lower()메서드를 변수에 저장 후 출력
lowersyms = symbols.lower()
print(lowersyms)

# find()메서드는 문자열에서 지정된 부분 문자열의 첫번째 발생 인덱스를 반환한다.
# 문자열이 발견되지 않으면 '-1'을 반환한다.
print(symbols.find("MSFT"))

# 인덱스를 활용한 문자열 추출
print(symbols[13:17])

# replace() 메서드를 활용하여 지정 문자열을 다른 문자열로 대체 
symbols = symbols.replace('SCO', '')
print(symbols)


# List 조작

symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
print(symbols)

# split() 메서드는 문자열을 지정된 구분자를 기준으로 분리하여 리스트로 반환한다.
# 구분자를 지정하지 않을 경우 기본적으로 공백을 사용하여 문자열을 분리합니다.
symlist = symbols.split()
print(symlist)

# 해당 리스트는 숫자 인덱스로 요소를 조회하고 수정할 수 있는 배열처럼 작동한다.
print(symlist[0])
print(symlist[1])
print(symlist[-1])
print(symlist[-2])

# 항목 재할당
symlist[2] = 'AIG'
print(symlist)

# 리스트 항복에 대한 반복
# symlist를 순회하면서 해당 요소들을 print함
for s in symlist:
    print('s =', s)

# 연산자를 사용하여 리스트에 AIG와 AA가 있는지 확인
print('AIG' in symlist)

# 문자열과 달리 리스트의 항목에서는 정확히 일치해야 True값 반환
print('AA' in symlist)

# 리스트에 항목 추가, 삽입, 삭제

# 추가
symlist.append('RHT')
print(symlist)

# insert(인덱스, 삽입할 항목) 메서드를 통해 항목 삽입 가능
symlist.insert(1, 'AA')
print(symlist)

# remove()를 통해 지정 항목 삭제 가능
symlist.remove('MSFT')
print(symlist)

# remove()를 할 때 항목을 찾을 수 없다면
# ValueError: list.remove(x): x not in list 가 발생
# symlist.remove('MSFT')
# print(symlist)

# index()를 통해 위치를 찾을 수 있다.
print(symlist.index('YHOO'))
print(symlist[4])

# 목록을 정렬하고 싶을 경우 sort()를 통해 실행 가능
symlist.sort()
print(symlist)

# 역순 정렬시 sort(reverse=True)

symlist.sort(reverse=True)
print(symlist)


# 리스트에서는 다른 리스트를 포함하여 모든 종류의 개체가 포함될 수 있다.

nums = [101, 102, 103]
items = [symlist, nums]
print(items)

# 인덱스를 중첩해서 리스트조회 가능
print(items[0])
print(items[0][1])
print(items[0][1][2])
print(items[1])
print(items[1][1])

# Dictionary

prices =  {'IBM':91.1, 'GOOG': 490.1, 'AAPL':312.23}

# 조회 가능
print(prices['IBM'])

# 수정 및 추가 가능
prices['IBM'] = 123.45
prices['HPQ'] = 26.15
print(prices)

# key값 list를 얻는 방법
print(list(prices))

# key 값을 삭제하는 방법
del prices['AAPL']
print(prices)