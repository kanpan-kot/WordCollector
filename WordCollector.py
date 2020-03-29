import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

gojuon = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に",
          "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ",
          "ん"]

driver.get('https://gaccag.com/kotodaman/dictionary/')
print(driver.title)

start_button = driver.find_element_by_css_selector('.container .form-row .form-group .form-check #left')
start_button.click()

aimai_button = driver.find_element_by_id('aimai')
aimai_button.click()

theme = driver.find_element_by_id('thema')
theme_select = Select(theme)
theme_select.select_by_value('205')

len = driver.find_element_by_id('length')
len_select = Select(len)

search_box = driver.find_element_by_class_name('form-control')
search_button = driver.find_element_by_id('search')

tmp = ''

for i in range(6):
    length = str(i + 2)
    len_select.select_by_value(length)
    print(length + '文字')
    for character in gojuon:
        print(character)
        search_box.clear()
        search_box.send_keys(character)
        search_button.click()

        time.sleep(1)

        if '一致する単語はありません' in driver.find_element_by_id('systemMsg').text:
            continue

        for word in driver.find_elements_by_css_selector('.container table tbody tr .kana'):
            tmp += word.text + '\n'

try:
    with open('suidou_word.txt', mode='x', encoding='utf-8') as f:
        f.write(tmp)
except FileExistsError:
    pass

# driver.set_window_size(1280, 720)
# driver.save_screenshot('search_results.png')
driver.quit()
