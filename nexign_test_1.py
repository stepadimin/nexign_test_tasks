import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_nexign_navigation():
    print("[INFO] Запуск браузера в режиме разработчика...")

    chrome_options = Options()
    chrome_options.add_argument("--auto-open-devtools-for-tabs")  
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://nexign.com/ru")

    wait = WebDriverWait(driver, 15)  
    time.sleep(3)  

    try:
        action = ActionChains(driver)

        print("[INFO] Наведение на 'Продукты и решения'...")
        products_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Продукты и решения')]")))
        action.move_to_element(products_menu).perform()
        time.sleep(2)  

        print("[INFO] Клик по 'Инструменты для ИТ-команд'...")
        it_tools = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Инструменты для ИТ-команд')]")))
        it_tools.click()
        print("[SUCCESS] Переход в 'Инструменты для ИТ-команд' выполнен!")
        time.sleep(3)  

        print("[INFO] Клик по 'Nexign Nord'...")
        nexign_nord = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Nexign Nord')]")))
        nexign_nord.click()
        print("[SUCCESS] Переход в 'Nexign Nord' выполнен!")
        time.sleep(3)  
        print("[SUCCESS] Тест завершён успешно!")
    except Exception as e:
        print(f"[ERROR] Ошибка во время теста: {e}")

    print("[INFO] Закрытие браузера...")
    driver.quit()

