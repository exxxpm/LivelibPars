from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

import time

class ReviewsCard:
    def __init__(self, reviews_source):
        self.reviews_source = reviews_source

    def get_book_name(self):
        try: return self.reviews_source.find_element("css selector", "a.lenta-card__book-title").text
        except (AttributeError, TypeError) as error: return "get_book_nameError"

    def get_count_star(self):
        try: return self.reviews_source.find_element("css selector", "span.lenta-card__mymark").text
        except (AttributeError, TypeError) as error: return "get_count_starError"

    def get_reviews_text(self):
        try: return self.reviews_source.find_element("css selector", "div#lenta-card__text-review-full").text
        except NoSuchElementException :return self.reviews_source.find_element("css selector", "div#lenta-card__text-review-escaped").text

def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
    service = Service(executable_path="web_driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    try:
        for page_number in range(1, 2):
            driver.get(url=f"https://www.livelib.ru/reviews/~{page_number}#reviews")
            time.sleep(2)
            driver.find_element("css selector", "div.btn-cookies-agree").click()
            time.sleep(0.5)

            read_more_buttons = driver.find_elements("css selector", "a.read-more__link")
            for read_more_button in read_more_buttons:
                driver.execute_script("arguments[0].scrollIntoView();", read_more_button)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", read_more_button)

            reviews_cards = driver.find_elements("css selector", "article.review-card")

            for reviews_card in reviews_cards:
                reviews_info = ReviewsCard(reviews_card)
                reviews_data = {
                    "name": reviews_info.get_book_name(),
                    "count_star": reviews_info.get_count_star(),
                    "reviews": reviews_info.get_reviews_text(),
                }
                print(reviews_data)

    except Exception as error:
        print(error)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()













