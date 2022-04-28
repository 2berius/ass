from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # time.sleep(3)
        driver.get("https://forms.gle/7DnCzbXQDubhp7Q47")
    except:
        print("[!] Update chromedriver [!]")

    _ = input("Enter anything once you log in to your Google account: ")

    while 1:
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()


if __name__ == "__main__":
    main()
