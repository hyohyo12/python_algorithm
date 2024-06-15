import sys
from collections import defaultdict
input = sys.stdin.readline
'''
    가지 -> 오이
    오이 -> 당근
    당근 -> 가지
'''

def is_possible(n:int,vege:list[str],game_res:list[str])->tuple:
    cnt_dict = collect_count(vege)
    comb = ''
    winner = defaultdict(str)
    for idx,v in enumerate(vege):
        if v == '?':
            result = game_res[idx]
            if result == 'W':
                if cnt_dict['G'] != 0 and cnt_dict['O'] == 0 and cnt_dict['D'] == 0:
                    comb += 'O'
                    cnt_dict['O'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] != 0 and cnt_dict['D'] == 0:
                    comb += 'D'
                    cnt_dict['D'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] == 0 and cnt_dict['D'] != 0:
                    comb += 'G'
                    cnt_dict['G'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] != 0 and cnt_dict['D'] == 0:
                    comb += 'G'
                    cnt_dict['G'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] == 0 and cnt_dict['D'] != 0:
                    comb += 'D'
                    cnt_dict['D'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] != 0 and cnt_dict['D'] != 0:
                    comb += 'O'
                    cnt_dict['O'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] != 0 and cnt_dict['D'] != 0:
                    return (False,())
            elif result == 'L':
                if cnt_dict['G'] != 0 and cnt_dict['O'] == 0 and cnt_dict['D'] == 0:
                    comb += 'O'
                    cnt_dict['O'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] != 0 and cnt_dict['D'] == 0:
                    comb += 'G'
                    cnt_dict['G'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] == 0 and cnt_dict['D'] != 0:
                    comb += 'O'
                    cnt_dict['O'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] != 0 and cnt_dict['D'] == 0:
                    comb += 'G'
                    cnt_dict['G'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] == 0 and cnt_dict['D'] != 0:
                    comb += 'D'
                    cnt_dict['D'] += 1
                elif cnt_dict['G'] == 0 and cnt_dict['O'] != 0 and cnt_dict['D'] != 0:
                    comb += 'O'
                    cnt_dict['O'] += 1
                elif cnt_dict['G'] != 0 and cnt_dict['O'] != 0 and cnt_dict['D'] != 0:
                    return (False,())
        else:
            comb += v


def collect_count(vege:list[str])->defaultdict:
    vege_count = defaultdict(int)
    for v in vege:
        vege_count[v] += 1
    return vege_count


#메인 함수
def main():
    #입력된 테스트 케이스만큼 반복
    for _ in range(int(input())):
        #입력
        #현재 테스트 케이스의 n개의 데이터
        n = int(input())
        #채소의 종류 입력
        vege = list(input().strip())
        #해당 채소의 게임 결과 입력
        game_res = list(input().strip())
        



if __name__ == "__main__":
    main()