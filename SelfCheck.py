from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from os import path

import os
import time

# To Build : pyinstaller --onefile SelfCheck.py

mainlink = 'https://hcs.eduro.go.kr'


def StartCheck(school_level, school_name, NAME, BIRTH, PW):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')      # 크롬창 안 뜨게
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("lang=ko_KR") # 한국어

        driver = webdriver.Chrome('./chromedriver.exe', options=options)

        try:
                driver.get(mainlink)

                ### Main ###
                driver.implicitly_wait(3)
                # closeBtn = driver.find_element(By.CLASS_NAME, 'closeBtn')
                # if (closeBtn):  closeBtn.click()
                driver.find_element(By.ID, 'btnConfirm2').click()
                driver.implicitly_wait(3)

                ### Login ###
                input_text_common = driver.find_elements(By.CLASS_NAME, 'input_text_common')
                # 0 : 학교, 1 : 성명, 2 : 생년월일
                input_text_common[0].click()

                ### 학교 선택창 ###
                print('학교 선택중...')
                # 지역 선택 : 서울특별시
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[2]').click()
                # 학교급 선택
                num = str(int(school_level) + 1)
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[' + num + ']').click()
                # 학교명 입력
                input_schoolName = driver.find_element(By.CLASS_NAME, 'searchArea')
                input_schoolName.send_keys(school_name)
                input_schoolName.send_keys(Keys.ENTER)
                driver.implicitly_wait(3)
                # 학교 선택
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a').click()
                # 찾기 완료 버튼
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

                ### Login ###
                input_text_common[1].send_keys(NAME)
                input_text_common[2].send_keys(BIRTH)
                driver.find_element(By.ID, 'btnConfirm').click()
                # driver.find_element(By.ID, 'btnConfirm').send_keys(Keys.ENTER)

                ### Password ###
                print('비밀번호 입력중...')
                driver.implicitly_wait(3)
                time.sleep(0.5)
                driver.find_elements(By.CLASS_NAME, 'input_text_common')[0].send_keys(PW)
                driver.find_element(By.ID, 'btnConfirm').click()
                time.sleep(1)

                ### 진단 참여 창 ###
                driver.find_element(By.CLASS_NAME, 'btn').click()
                driver.implicitly_wait(3)

                ### SELF CHECK ###
                print('진단 체크중...')
                for i in range(1, 6):
                        xpath = '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[{0}]/dd/ul/li[1]/label'.format(i)
                        driver.find_element_by_xpath(xpath).click()
                driver.find_element(By.ID, 'btnConfirm').click()

        except NoSuchElementException:
                print('\n사이트 구조가 변경된 것 같습니다.')
                print('개발자에게 문의해주세요 :)')
                driver.quit()
                return
        except BaseException as e:
                print(e)
                print('\n사이트를 불러오면서 오류가 발생했습니다')
                print('info.txt 파일을 확인하고 다시 실행해주세요.')
                driver.quit()
                return

        if path.exists('confirm.png'):
                os.remove('confirm.png')
        driver.get_screenshot_as_file('confirm.png')

        print('자가진단 완료! (confirm.png)')
        driver.quit()



def CreateFile():
        level = input('1: 유치원, 2: 초등학교, 3: 중학교, 4: 고등학교, 5: 특수학교\n(숫자 하나) >> ')
        school = input('학교이름 (정확히) >> ')
        name = input('이름 >> ')
        birth = input('생년월일 (YYMMDD) >> ')
        pw = input('로그인 비밀번호 (숫자 4자리) >> ')
        
        with open('info.txt', 'w', encoding='utf8') as file:
                info = [level+'\n', school+'\n', name+'\n', birth+'\n', pw+'\n']
                file.writelines(info)

def LoadFile():
        with open('info.txt', 'r', encoding='utf8') as file:
                return file.readlines()


if path.exists('chromedriver.exe'):
        if path.exists('info.txt'):
                info = LoadFile()

                level = info[0][:-1]
                school = info[1][:-1]
                name = info[2][:-1]
                birth = info[3][:-1]
                pw = info[4][:-1]

                print('자가진단 시작')
                StartCheck(level, school, name, birth, pw)
        else:
                CreateFile()
                print('정보가 저장되었습니다. 프로그램을 다시 실행하시면 자가진단이 시작됩니다.')

else:
        print('크롬드라이버를 실행파일과 같은 폴더에 설치해주세요\n(https://github.com/XxCtrlZxX/SelfCheck)')

os.system("pause")
os._exit(0)