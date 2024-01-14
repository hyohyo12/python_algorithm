def get_palindrome(string:list[str])->str:
    from collections import Counter #문자열의 문자의 개수를 카운트하기 위해 counter import
    string.sort() #사전순으로 출력해야하므로 정렬
    count = 0 #개수가 홀수인 문자가 2개이상이면 펠린드롬 만들 수 없음 ABCC 이러면 CABC 이런 느낌?
    res = "" #결과를 저장할 변수
    center = "" #개수가 홀수인 문자를 하나 저장해 그것을 가운데로 보내기위한 변수
    string_count = Counter(string) #Counter 함수로 문자를 key 문자의 개수를 value 값으로 하는 딕셔너리
    for i in string_count:#위에 만든 딕셔너리를 탐색하여
        if string_count[i] % 2 == 1: #문자의 개수가 홀수 이면
            count += 1 #카운트 증가시킴
            center+=i #중간문자 하나 추가
            if count > 1: #만약 개수가 홀수인 문자가 2개이상이면
                return "I'm Sorry Hansoo" #펠린드롬 불가하므로 결과값 리턴
    else: #약속대로 홀수인 문자가 1개 이하여서 무사히 for문을 빠져나온다면
        for k,v in string_count.items(): #딕셔너리의 아이템을 k,v에 대치하는 for문
            res += (k * (v//2)) #펠린드롬은 앞뒤가 같으므로 문자를 개수절반만 res에 추가
        return res + center + res[::-1] #앞 홀수문자 뒤 이렇게 반환


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    string = input().strip()
    print(get_palindrome(list(string)))