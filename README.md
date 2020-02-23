# Web Crawling by Python

Crawl Korean data from web site.
  
- [Naver Movie(Review-aggregation website)](https://movie.naver.com/)
    
- [Yes24(Online Book Store)](http://www.yes24.com/Main/default.aspx)

## Goals

- Collect movie and book summaries(overviews) for recommendation system based on natural launguage process.

- Extract text data from html and delete an unnecessary characters.

## Main Libraries

- Selenium

- bs4(BeautifulSoup)

## Technics

#### Selenium

- Implicit_wait VS Explicitly_wait

- driver.find_element_by_xpath()

#### BeautifulSoup

- BeautifulSoup('url', 'html.parser')

- prettify

- find('tag', class_=' ', href_=' ', id=' ', style=' ')

## References

- [https://wkdtjsgur100.github.io/selenium-does-not-work-to-click/](https://wkdtjsgur100.github.io/selenium-does-not-work-to-click/)

- [https://kmkidea.tistory.com/49](https://kmkidea.tistory.com/49)
