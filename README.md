# Web Crawler by Python

Collect Korean data from a website.
  
- [Naver Movie(Review-aggregation website)](https://movie.naver.com/)
    
- [Yes24(Online Book Store)](http://www.yes24.com/Main/default.aspx)

## Goals

- Clipping movie and book summaries(overviews) for recommendation system.

- Extract text data from html and delete unnecessary characters for NLP(natural language process).

- Save data as .txt file

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
