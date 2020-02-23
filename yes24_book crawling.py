from selenium import webdriver
from konlpy.tag import Mecab
from bs4 import BeautifulSoup
import requests


def single_line(raw_str):
    return " ".join(raw_str.split())


tokenizer = Mecab()

driver = webdriver.Firefox(executable_path='/Users/vctr/Desktop/geckodriver')
count = 1
page = 1


while 1:
    if page > 50:
        break

    path = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001047&sumgb=03&PageNumber=" + str(page)

    driver.implicitly_wait(10)
    driver.get(path)

    for i in range(0, 20):
        xpath = '//*[@id="category_layout"]/tbody/tr[' + str((2*i)+1) + ']/td[3]/p[1]/a[1]'
        driver.implicitly_wait(10)
        URL = driver.find_element_by_xpath(xpath).get_attribute("href")
        soup = BeautifulSoup(requests.get(URL).text, 'html.parser')

        content = soup.find('textarea', class_='txtContentText')

        if not content:
            driver.back()
            count = count + 1
            continue

        if not content.get_text():
            driver.back()
            count = count + 1
            continue

        overview = ' '.join(content.get_text().split())

        driver.implicitly_wait(10)
        element = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].click();", element)

        driver.implicitly_wait(10)
        title = driver.find_element_by_xpath('//*[@id="yDetailTopWrap"]/div[2]/div[1]/div/h2').text.strip()

        if not title:
            print('title error')

        driver.implicitly_wait(10)
        poster = driver.find_element_by_xpath('//*[@id="yDetailTopWrap"]/div[1]/div[1]/span/em/img').get_attribute("src")

        if not poster:
            print('poster error')

        with open("book_novel.txt", 'a', encoding='utf-8') as f:
            f.write(title + '\u241E' + URL + '\u241E' + ' '.join(tokenizer.nouns(overview)) + '\u241E' + poster + '\n')

        print(overview)
        book_info = {"Np.": count,
                     "PAGE": page,
                     "URL": URL,
                     "TITLE": title,
                     "IMG_SRC": poster}
        print(book_info)
        print('========================================================================================================================================================================================================================================================')

        count = count + 1
        driver.back()
    page = page + 1

