import xlrd
import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from fuzzywuzzy import process
from fuzzywuzzy import fuzz


def Config():
    username = '362532200309266113'
    name = '吴正文'
    return(username,name)


def dumpTk():
    data = xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\(更正版20230529）2023年党的基本知识（1500道题）(1).xls")
    table = data.sheets()[0]
    d = []
    for i in range(table.nrows):
        list = table.row_values(i)
        d.append(list[1])
        d.append(list[-2])
    print(d)
    with open("C:\\Users\\Administrator\\Desktop\\tk.json",'w',encoding='utf-8') as f:
       json.dump(d,f,ensure_ascii=False)


def FuckQuestions():
    with open('.\\tk.json','r',encoding='utf8')as fp:
        tk_data = json.load(fp)
    username = Config()[0]
    name = Config()[1]
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    driver.get(r'https://exam-jytv.jxeduyun.com/login')
    driver.find_element(by=By.ID, value='id_card').send_keys(username)
    driver.find_element(by=By.ID, value='name').send_keys(name)
    driver.find_element(by=By.ID, value='id_submit').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//button[@class='nut-button nut-button--primary nut-button--normal nut-button--round']").click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//*[@id='/question?stamp=1']/view[5]/view[2]/div[1]/view[1]/view[3]/button[2]").click()
    time.sleep(3)
    for i in range(30):
        q = driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/taro-view-core[1]").text
        for x in range(0,len(tk_data),2):
            if fuzz.ratio(q, tk_data[x]) > 70:
                a = tk_data[x+1]
                break
            else:
                a = 'B'
        if a == 'A':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
        elif a == 'B':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'C':
            try:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
            except:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'D':
            try:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            except:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'AB':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'AC':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
        elif a == 'AD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
        elif a == 'BC':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'BD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'CD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
        elif a == 'ABC':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'ABD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'BCD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
        elif a == 'ABCD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
        elif a == 'ACD':
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
            driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
        elif a == 'ABCDE':
            try:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[5]/view[1]").click()
            except:
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[4]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[2]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[1]/view[1]").click()
                driver.find_element(by=By.XPATH, value="//*[@id='question--box-"+str(i)+"']/view[1]/view[3]/view[1]").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value="//*[@id='/question?stamp=1']/taro-view-core[1]/taro-view-core[3]/button[2]").click()
    driver.find_element(by=By.XPATH, value='//*[@id="/question?stamp=1"]/view[2]/view[2]/div[1]/view[1]/view[3]/button[2]').click()
if __name__ == "__main__":
    FuckQuestions()
