f = open("cs.txt", 'w')

# Don't write down whole directory path

file = open("cs.txt")

data = "yeseul kang\neunsu Jang\nJinYoung kwon\nHyukJun Kwon"

f.write(data)
f.close()

f2 = open("ee.txt", 'w')
file2 = open("ee.txt")
data2 = "Amy\nJack\nNick\nJames"

f2.write(data2)
f2.close()

f3 = open("years4.txt",'w')
file3 = open("years4.txt")
data3 = "Amy\nJack"

f3.write(data3)
f3.close()

f4 = open("goodgrade.txt",'w')
file4 = open("goodgrade.txt")
data4 = "yeseul kang\neunsu Jang\nAmy"

f4.write(data4)
f4.close()


# 주요 연산1 함수로 구현
def SetOfNames(filename):
    return {line.strip() for line in open(filename)}

# Data를 자료구조 set으로 만들기
year4 = SetOfNames("years4.txt")
print(year4)

cs = SetOfNames("cs.txt")
ee = SetOfNames("ee.txt")
goodgrade = SetOfNames("goodgrade.txt")

# 주요 연산2(조건에 맞는 사람찾기) 함수로 구현

#candidate = {student for student in year4
#            if (student in cs or student in ee)
#            and student in goodgrade}

candidates = year4 & (cs | ee) & goodgrade

print(candidates)

for student in candidates:
    print(student)


