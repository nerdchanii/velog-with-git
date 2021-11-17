# 외부 패키지 임포트
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# 부차적인 파일 임포트
import auth
import sys
from login import login
import time


def init():
    print('hi')


def open_velog():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get('https://velog.io/write')
    return browser


def loggin(browser, id, pwd):
    # print(browser.title)
    print('hi')


def read_file(browser, file):
    # Header
    header_xpath = '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea'
    header = browser.find_element("xpath", value=header_xpath)

    # tags
    tags_xpath = '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/input'
    tags_input_element = browser.find_element('xpath', value=tags_xpath)

    for line in file.readlines():

        if line == '\n':
            continue

        if not line.startswith("\'\'\'"):
            input_text(line, browser)

        else:
            meta_type, meta_value = line.lstrip("\'").rstrip('\n').split(":")

            if meta_type == '제목':
                header.send_keys(meta_value)
            elif meta_type == '태그':
                meta_value = meta_value.split(",")

                for tag in meta_value:
                    tags_input_element.send_keys(tag + Keys.ENTER)

            elif meta_type == '시리즈':
                series = meta_value

    # print(tags)
    # print(browser.find_element("xpath", value= ))


def input_text(line, browser):
    code = """
    function inputText(line){
    let spanNode= document.createElement('span');
    spanNode.setAttribute('role', 'presentation');
    let preNode = document.createElement('pre');
    preNode.setAttribute('class', 'CodeMirror-line');
    preNode.setAttribute('role','presentation');
    spanNode.innerText =  line;
    preNode.appendChild(spanNode);
    document.getElementsByClassName('CodeMirror-code')[0].appendChild(preNode);
    }
    inputText(arguments[0])
    """

    browser.execute_script(code, line)



if __name__ == '__main__':
    filename = open(sys.argv[1], encoding="UTF-8")

    browser = open_velog()
    time.sleep(2)

    # loggin(browser, auth.user_id, auth.user_passwd)
    read_file(browser, filename)
    print(browser.page_source.replace("<", "\n<"))

    init()
