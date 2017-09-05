# 함수형으로 구현한 이름 검색
# 파이썬 이산수학

f = open("names.txt", 'w')

file = open("c:/users/yeseul/workspace/discreteMath/names.txt")


data = "yeseul kang\nyeseul Han\neunsu Jang"
data2 = "eunsu JJang\nyeseul JJang\nyeseul KKang."

f.write(data)
f.write(data2)

f.close()

file = open("names.txt")

for line in file:
    if line.startswith("yeseul"):
        print("y")
    else:
        print("Nothing")

# 이름 검색

def reduce(f, sequence, initial):
    result = initial
    for a in sequence:
        result = f(result,a)
    return result


cat = lambda S: reduce(lambda x,y: x+y,S,"")

print(cat(filter(lambda x:x.startswith("yeseul"),open("names.txt"))
          ))

list = [line[7:] for line in open("names.txt") if line.startswith("yeseul ")]


print(list)

