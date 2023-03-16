import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# --------------- VARIABLES ---------------------- #
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "\chromedriver_win32\chromedriver.exe"
TWITTER_USERNAME = "YOURTWITTERUSERNAME"
TWITTER_PASSWORD = "YOURPASSWORD"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options,
                                       service=Service(executable_path="chromedriver.exe", log_path="NUL"))
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        button.click()
        time.sleep(55)
        self.download = self.driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.upload = self.driver.find_element(By.XPATH,
                                           "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up = self.upload.text
        self.down = self.download.text

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        time.sleep(3)
        log_in = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/a")
        log_in.click()
        time.sleep(3)
        log_in2 = self.driver.find_element(By.XPATH,
                                           "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]")
        log_in2.click()
        time.sleep(3)
        user_name = self.driver.find_element(By.XPATH,
                                             "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        user_name.send_keys(TWITTER_USERNAME)
        next_btn = self.driver.find_element(By.XPATH,
                                            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_btn.click()
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
                                            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        final_log_in = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        final_log_in.click()
        time.sleep(4)
        tweet_inp = self.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_inp.click()
        tweet_inp.send_keys(
            f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for 250 down and 30 up?")

        tweet_btn = self.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
