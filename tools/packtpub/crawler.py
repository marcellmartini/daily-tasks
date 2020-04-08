"""
função para pegar o nome dos livros
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_free_ebook_title(url=None, xpath=None):
    """
    Pega titulo do ebook
    """
    driver_url = url or 'https://www.packtpub.com/free-learning'
    xpath_element = xpath or '//*[@id="free-learning-dropin"]/div/div/div/div/div[2]/div[2]/h1'

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(driver_url)

    element = driver.find_element_by_xpath(xpath_element)
    ebook_tittle = element.text.split(':')[-1].strip()

    return ebook_tittle
