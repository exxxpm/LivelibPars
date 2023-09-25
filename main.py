from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
    service = Service(executable_path="web_driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url=f"https://www.livelib.ru/reviews/~{page_number}#reviews")
    except Exception as error:
        print(error)
    finally:
        time.sleep(9999)
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()
