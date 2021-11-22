class Write():
    header_field = '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea'
    tags_field = '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/input'
    line_class_name = "CodeMirror-line"

line_xpath = '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]/pre'

class Login():
    btn = '//*[@id="root"]/div[2]/div[1]/div/div[2]/button'
    github_api = '//*[@id="root"]/div[4]/div/div[2]/div[2]/div/div[1]/section[2]/div/a[1]'

class github():
    id_field = '//*[@id="login_field"]'
    pwd_field = '//*[@id="password"]'
    login_submit = '//*[@id="login"]/div[3]/form/div/input[12]'
