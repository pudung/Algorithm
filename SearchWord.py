# 문자로 구성된 파일에서 특정 단어 찾기

# 많은 단어가 포함된 전자 문서에서 어떤 단어를 검색해 찾고자 한다.
# 프로그램은 찾으려는 단어를 문서에서 검색해 해당 단어와 함께 단어가 포함된 모든 줄의 번호를 표시해야함
# 문서의 filename is "document.txt" and target word is saved in file "targets.txt".

f = open("document.txt",'w')
file = open("document.txt")
data = "Wants pawn term dare worsted ladle gull hoe lift wetter murder inner\n ladle cordage honor itch offer lod, dock ladle gull\n orphan ladle rat ladle hut\nLadle Rate Rotten Hut."
f.write(data)
f.close()

f2 = open("targets.txt",'w')
file2 = open("targets.txt")
data2 = "ladle\ngull\nhut"
f2.write(data2)
f2.close()

# targets이라는 set을 생성
targets = {line.strip() for line in open("targets.txt")}

# 각 줄을 읽으면서 줄 번호를 매긴다, 모든 값을 원소가 2개인 튜플로 산출
# 아래 함수는 generator 함수로 yield가 있다.

def wordsAndLineNumbers(fileName):
    punctuation = ".,:;'" + '"'
    lineno = 0
    file = open(fileName)
    for line in file:

        lineno += 1
        words = line.strip().split()

        for word in words:
            yield (word.strip(punctuation),lineno)

# targets의 각 단어를 공집합 set()과 맵핑하여 초기화
linesFoundOn = {t: set() for t in targets}

# targets에 있는 단어(키)에 lineno(value) 맵핑.

for (word,lineno) in wordsAndLineNumbers("document.txt"):
    if word in targets:
        linesFoundOn[word].add(lineno)


def formatted(numberSet):
    # ,로 구분한다
    separator = ", "
    return separator.join(map(str,sorted(numberSet)))

# map(str,sorted(numberSet)) : [1,2,3]과 같이 숫자 리스트를 str으로,

for t in targets:
    print(t + " " + formatted(linesFoundOn[t]))



