import sys
input = sys.stdin.readline

def who_win(money:int,seq:list[int])->str:
    jun_money ,seong_money = money,money #준영 성민 각각 돈
    inc_flag ,dec_flag,jun_stock,seong_stock  = 1,1,0,0 #며칠동안 증가했는지 감소했는지 각각 inc_flag,dec_flag에 저장 그리고 각각 보유 주식 수 각 사람의stock변수에 저장

    for i,price in enumerate(seq): #리스트 탐색
        if price <= jun_money: #현재 가격이 준형이가 가지고있는 돈보다 작다면
            stock = (jun_money//price) #주식 매수
            jun_stock += stock 
            jun_money -= (stock * price) #매수 주식 수 * 가격 만큼 가지고 있는 돈 빼준다.

        if price <= seong_money: #성민이가 가지고 있는 돈이 더 크다면 현재가격보다
            if dec_flag >= 3: #전일 감소가 3일 이상이면
                stock = (seong_money//price) #주식 매수
                seong_stock += stock 
                seong_money -= (stock * price) #매수한만큼 돈 하락
                inc_flag = 1 #증가 flag 초기화

        if inc_flag >= 3 and seong_stock != 0: #증가flag가 3일 이상 지속됐고 가지고 있는 주식수가 0개가 아니라면
            seong_money += (seong_stock*price) #모두 매도
            seong_stock = 0
            dec_flag = 1#감소 flag 초기화
        
        if i != 0:#인덱스 에러 방지
            if seq[i-1] < price:#전일 가격보다 현재 가격이 크다면
                inc_flag += 1#증가 flag 증가시킨다
                dec_flag = 1#하락 flag는 1로 초기화
            elif seq[i-1] > price: #전일 가격보다 현재 가격이 작다면
                dec_flag += 1 #하락 flag 증가
                inc_flag = 1#증가 flag 초기화
            else: #전일과 같다면 모든 flag 초기화
                dec_flag = 1
                inc_flag = 1
    
    
    #비교를 위해 보유 주식 현금화
    jun_money += (jun_stock*seq[-1])
    seong_money += (seong_stock*seq[-1])
    
    if jun_money == seong_money:#둘이 같다면 SAMESAME 리턴
        return 'SAMESAME'
    return "BNP" if jun_money > seong_money else "TIMING" #jun이 크다면 BNP seong이 크다면 TIMING





if __name__ == "__main__":
    money = int(input())
    price_seq = list(map(int,input().split()))
    print(who_win(money,price_seq))