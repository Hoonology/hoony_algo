print("구구단 출력 프로그램입니다.") 
print("원하는 단수를 입력하세요.") 
dan=int(input()) # 단수 입력 

for i in range(1,10): 
    result=dan*i 
    print(dan,'x',i,'=',result)
