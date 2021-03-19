import json
import os

class UserData:
    def __init__(self):
        self.data = dict()
        self.driverPath = './chromedriver.exe'

    def init(self):
        self.data['school_level'] = input('1: 유치원, 2: 초등학교, 3: 중학교, 4: 고등학교, 5: 특수학교\n(숫자 하나) >> ')
        self.data['school_name'] = input('학교이름 (정확히) >> ')
        self.data['name'] = input('이름 >> ')
        self.data['birth'] = input('생년월일 (yyMMdd) >> ')
        self.data['password'] = input('로그인 비밀번호 (숫자 4자리) >> ')
        self.data['chromeDriverPath'] = self.driverPath
        self.saveDataAsFile()
        # os.system('cls')  # 콘솔 화면 초기화

    def saveDataAsFile(self):
        with open('./info.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent='\t', ensure_ascii=False)    # ensure_ascii : 한글 깨짐 방지

    def getData(self):
        # TODO: convert json to class
        with open('./info.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
            
        self.driverPath = self.data['chromeDriverPath']
        self.school_level = self.data['school_level']
        self.school_name = self.data['school_name']
        self.name = self.data['name']
        self.birth = self.data['birth']
        self.password = self.data['password']

    def modifyDriverPath(self, driverPath):
        self.data['chromeDriverPath'] = self.driverPath = driverPath
        self.saveDataAsFile()
