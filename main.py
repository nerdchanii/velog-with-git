# 외부 패키지 임포트
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# 부차적인 파일 임포트
import auth
import sys
# from login import log_in
import time
from velog_path import *


def init():
    print('hi')


def open_browser():
    # options = Options()
    # options.headless = True
    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()

    return browser


def log_in(browser, user_id, pwd):
    browser.get('https://velog.io')
    login_modal = browser.find_element('xpath', Login.btn)
    login_modal.click()
    github_login = browser.find_element('xpath', Login.github_api)
    print(github_login)
    time.sleep(1)
    github_login.click()
    time.sleep(1)
    id_field = browser.find_element('xpath', github.id_field)
    pwd_filed = browser.find_element('xpath', github.pwd_field)

    id_field.click()
    id_field.clear()
    id_field.send_keys(user_id)

    pwd_filed.click()
    pwd_filed.clear()
    pwd_filed.send_keys(pwd)

    browser.find_element('xpath', github.login_submit).click()


def read_file(browser, file):
    # Header

    header = browser.find_element("xpath", value=Write.header_field)

    # tags

    tags_input_element = browser.find_element('xpath', value=Write.tags_field)

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
    spanNode.setAttribute('style', 'padding-right: 0.1px');
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


# def input_text(line, browser):
#     text_span = browser.find_element('xpath', '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]/pre/span')
#     text_pre = browser.find_element('xpath', '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]/pre')
#
#     text_span.click()
#     text_pre.click()
#     text_line = browser.find_element('xpath', line_xpath)
#     text_line.click()
#
#     text_line.send_keys(line)
#     # text_line. = 'hi'

if __name__ == '__main__':
    filename = open(sys.argv[1], encoding="UTF-8")

    browser = open_browser()

    time.sleep(1)
    log_in(browser, auth.user_id, auth.user_passwd)
    time.sleep(1)
    browser.get('https://velog.io/write')
    read_file(browser, filename)
    # print(browser.page_source.replace("<", "\n<"))

    init()
