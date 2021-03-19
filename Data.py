import json
import os

cities = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', 
    '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', 
    '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'
]

class UserData:
    def __init__(self):
        self.data = dict()
        self.driverPath = './chromedriver.exe'

    def init(self):
        for i in range(1, len(cities) + 1):
            print(f'{i}. {cities[i - 1]}')

        while True:
            a = int(input('\n(숫자 하나) >> '))
            if not 0 < a <= len(cities):    # 조건을 만족시킬 때까지 반복
                print('유효한 값을 입력해주세요.')
                continue
            self.data['cities'] = a
            break;

        # 콘솔 화면 초기화
        os.system('cls')
        print(f'{a}. {cities[a - 1]}\n')

        self.data['school_level'] = int(input('1: 유치원, 2: 초등학교, 3: 중학교, 4: 고등학교, 5: 특수학교\n(숫자 하나) >> '))
        self.data['school_name'] = input('학교이름 (정확히) >> ')
        self.data['name'] = input('이름 >> ')
        self.data['birth'] = input('생년월일 (yyMMdd) >> ')
        self.data['password'] = input('로그인 비밀번호 (숫자 4자리) >> ')
        self.data['chromeDriverPath'] = self.driverPath
        self.saveDataAsFile()

    def saveDataAsFile(self):
        with open('./info.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent='\t', ensure_ascii=False)    # ensure_ascii : 한글 깨짐 방지

    def getData(self):
        # TODO: convert json to class
        with open('./info.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
            
        self.driverPath = self.data['chromeDriverPath']
        self.cities = self.data['cities']
        self.school_level = self.data['school_level']
        self.school_name = self.data['school_name']
        self.name = self.data['name']
        self.birth = self.data['birth']
        self.password = self.data['password']

    def modifyDriverPath(self, driverPath):
        self.data['chromeDriverPath'] = self.driverPath = driverPath
        self.saveDataAsFile()
