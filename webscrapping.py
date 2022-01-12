from selenium import webdriver

def getImage(key):
    browser = webdriver.Firefox(executable_path='./webdriver/geckodriver.exe')
    #browser.get('https://www.pexels.com/pt-br/')
    browser.get('https://www.google.com.br/imghp?hl=pt-BR&ogbl')
    input = browser.find_element_by_name('q')
    input.clear()
    input.send_keys(key)

    # clicking on seacrh button
    browser.find_element_by_class_name('Tg7LZd').click()