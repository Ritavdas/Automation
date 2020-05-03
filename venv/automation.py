from selenium import webdriver

edge_browser = webdriver.Edge('msedgedriver.exe')
edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
edge_browser.maximize_window()
show_msg_btn = edge_browser.find_element_by_class_name('btn')
# print(element.get_attribute('innerHTML'))
# print(element)
assert 'Show Message' in edge_browser.page_source

user_message = edge_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am a disco dancer')
show_msg_btn.click()
displayed_msg = edge_browser.find_element_by_id('display')
assert "I am a disco dancer" in displayed_msg.text
edge_browser.close()
edge_browser.quit()
