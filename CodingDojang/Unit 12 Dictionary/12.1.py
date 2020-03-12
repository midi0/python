# key : value 로 구분

# key가 중복될 경우 가장 뒤의 값을 사용하며, 중복되는 키는 저장하지 않는다
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}

#다양한 방식의 딕셔너리 자료형 정의
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
y = dict() # 보통은 y = {} 로 쓴다
print(lux3)


