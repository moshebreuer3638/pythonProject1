from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Use headless option to not open a new browser window
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
chrome_options.headless = True  # also works

# dates = today

website = 'https://app.rakenapp.com/'

path = 'C:\\Users\\moshe\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get(website)

# login
username_btn = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
password_btn = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
username_btn.send_keys("mbreuer@galaxycm.com")
password_btn.send_keys("Keepgrinding1!")
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/section/div/form/div/div[3]/button').click()

'''
payload = {'username': 'mbreuer@galaxycm.com', 'password': 'Keepgrinding1!'}
url = 'https://app.rakenapp.com/login'
requests.post(url, data=payload)

time.sleep(25)'''
report_page = 'https://app.rakenapp.com/project/695463/worklog'
driver.get(report_page)

time.sleep(25)


class Myspider(CrawlSpider):
    name = 'rakenscrapper'
    allowed_domains = report_page
    start_urls = report_page

    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),
             )

    def parse_item(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
