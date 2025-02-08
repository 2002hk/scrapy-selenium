# Implementing Scrapy-Selenium to scrape quotes
## Libraries install
- Scrapy
- scrapy-selenium
- ipython
- virtualvenv
## Workflow
### Uses SeleniumRequest to Load JavaScript Content
- Since the website loads dynamically, SeleniumRequest ensures JavaScript execution.
### Sends Initial Request to URL
- start_requests() sends a request to https://quotes.toscrape.com/js/.
### Extracts Quotes Data Using XPath & CSS Selectors
- Finds each quote block: //div[@class="quote"]
- Stores Extracted Data in QuoteItem
- ields structured output containing quote, author, and tags.
### Areas for Improvement
- Optimize Selenium Usage
-- Instead of using Scrapy-Selenium, try Scrapy-Splash or Scrapy-Playwright for faster rendering.
- Use Logging Instead of print()
-- Replace print() with self.logger.info() for better debugging.
- Headless Execution
-- Use options.add_argument("--headless") for faster execution.
