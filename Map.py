
# map function define


def f(x):
    return x+x

def map(f,sequence):

    result = ()

    # map 은 시퀀스의 모든 인수에 인수가 하나인 함수를 적용하고 결괏값을 튜플로 생성

    for a in sequence:
        result += (f(a),)
    return result

sequence = ("apple","banana","peach")

print(map(f,sequence))

# 숫자 list (sequence)를 str으로 바꾸어 tuple을 생성하는 map
print(map(str,[1,2,3]))

print(', '.join(map(str,[4,5,6])))





