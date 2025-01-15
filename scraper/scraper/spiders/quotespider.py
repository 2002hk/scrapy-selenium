import scrapy
from shutil import which
from scrapy_selenium import SeleniumRequest
from scraper.items import QuoteItem
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService



class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    #allowed_domains = ["quotes.toscrape.com"]
    #start_urls = ["https://quotes.toscrape.com/js/"]
    def start_requests(self):
        url="https://quotes.toscrape.com/js/"
        yield SeleniumRequest(url=url,callback=self.parse)
    
    def parse(self, response):
        
        #print(response.request.meta['driver'].title)
        quote_item=QuoteItem()
        quotes=response.xpath('//div[@class="quote"]')
        print(quotes)
        for quote in quotes:
            print(quote)
            quote_item['text']=quote.xpath('.//span[@class="text"]/text()').get()
            quote_item['author']=quote.xpath('.//small[@class="author"]/text()').get()
            quote_item['tags']=quote.css('div.tags a.tag::text').getall()

            yield quote_item
