# CSV 파일로 부터 사전 생성하기

f = open("addressBook.csv", 'w')

# Don't write down whole directory path
file = open("addressBook.csv")

data = "yeseul, yesel6089@naver.com\n eunsu, silve@naver.com \n Jinyoung, Jin@gmail.com"

f.write(data)

f.close()

# line.strip은 line의 양쪽 공백지우기.

def streamOfTuple(filename):
    return (line.strip().split(",") for line in open(filename))

streamOfTuple("addressBook.csv")

address = {name : email for (name,email) in streamOfTuple("addressbook.csv")}

print(streamOfTuple("addressBook.csv"))
print(address)
