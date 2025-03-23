import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_count_nexign():
    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  

    driver = webdriver.Chrome(options=chrome_options)
    
    start_time = time.time()
    driver.get("https://nexign.com/ru")

    time.sleep(5)  

    page_text = driver.page_source.lower()
    count = page_text.count("nexign".lower())

    end_time = time.time()
    print(f"Количество упоминаний 'Nexign': {count}")
    print(f"Время выполнения теста: {end_time - start_time:.2f} секунд")

    driver.quit()
