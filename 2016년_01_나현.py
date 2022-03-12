def solution(a, b):
    # 전체 일수 구하기
    totallist = [0,31,29,31,30,31,30,31,31,30,31,30]
    total = sum(totallist[:a]) 
    total = total +b
    # 리스트 만들고 전체 일수 7로 나눠서 뽑기
    list = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    num = total%7
    answer = list[num]
    return answer