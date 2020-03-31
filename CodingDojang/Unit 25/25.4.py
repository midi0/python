'''
중첩 딕셔너리 사용하기

딕셔너리 안에 들어있는 딕셔너리에 접근하려면 딕셔너리 뒤에
[ ](대괄호)를 단계만큼 붙이고 키를 지정해주면 됩니다.

딕셔너리[키][키]
딕셔너리[키][키] = 값
여기서는 딕셔너리가 두 단계로 구성되어 있으므로 대괄호를 두 번 사용합니다.
그래서 금성(Venus)의 반지름(mean radius)를 출력하려면 다음과 같이 먼저 'Venus'를 찾아가고
다시 'mean_radius'의 값을 가져오면 됩니다.
'''
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
print(terrestrial_planet['Venus']['mean_radius'])  # 6051.8