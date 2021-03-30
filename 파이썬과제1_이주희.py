dict_answer = {
    '현숙' : '이화여대 멋사 대표님',
    '두희' : '멋사 창립자',
    '세은' : '파이썬 세션 튜터',
    '마루' : '야옹'
}
for key, value in dict_answer.items():
    print('다음은 누구에 대한 설명일까요?\n{}\n1.현숙 2.세은 3.두희 4.마루'.format(value))
    answer1 = input()
    if answer1 == key:
        print('정답입니다!\n')
    else :
        print('오답입니다!\n')