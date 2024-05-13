import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FrappeframeworkSpider(scrapy.Spider):
    name = "frappeframework"
    allowed_domains = ["frappeframework.com"]
    start_urls = ["https://frappeframework.com/docs/user/en/prerequisites"]

    # def __inti__(self):
    #     self.service = Service(executable_path="./chromedriver")
    #     self.driver = webdriver.Chrome(service=self.service)
    
    def parse(self, response):
        
        self.service = Service(executable_path="./chromedriver")
        self.driver = webdriver.Chrome(service=self.service)
        
        self.driver.get(response.url)
        
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "from-markdown"))
        ) # After 5 Sec the element we can't able find the element means crash the program or go head for next move

                
        yield {
            "title": response.css(".wiki-title::text").get(),
            "url": response.url,
            # "main_content": response.css(".from-markdown").get(),
            "main_content": self.driver.find_element(By.CLASS_NAME, "from-markdown").text
        }
        
        
        try:
            next_page_section = self.driver.find_element(By.CLASS_NAME, "forward-back")
            
            next_page_url = next_page_section.find_element(By.CLASS_NAME, "pull-right").get_attribute("href")
        except:
            import traceback
            traceback.print_exc()
            
            return None
        
        if next_page_url is not None:
            # next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)
        
        # time.sleep(10)
