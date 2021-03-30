class info:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return '{}은(는) {}세이고, {}입니다.'.format(self.name, self.age, self.gender)

char1 = info('짱구',5,'남자')
char2 = info('도라에몽',14,'남자')
char3 = info('코난',8,'남자')
char4 = info('쇼콜라',15,'여자')
char5 = info('아무',12,'여자')
char6 = info('가영',16,'여자')

print(char1)
print(char2)
print(char3)
print(char4)
print(char5)
print(char6)