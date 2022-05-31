# 문제
# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

a = input().upper()
letterNum = {} # 빈 딕셔너리 만들기

for i in a : # for문을 돌면서 채울거야 딕셔너리를
    if i in letterNum.keys() : # .keys는 딕셔너리의 키 값들을 싹 가져 오는 것
        letterNum[i] += 1
    else :
        letterNum[i] = 1 # 처음 만났으니 1로 초기화


# for key,value in dic.items()   items()는 키와 밸류를 싹 다 가져오는 것
maxCount = 0 #처음이니깐, 0으로 초기화
for k,v in letterNum.items():
    # print(k,v)
    if  maxCount < v:
        answer = k
        maxCount = v
    elif maxCount == v:
        answer = "?"

print(answer)