# Chrome arguments see: https://peter.sh/experiments/chromium-command-line-switches/
from selenium import webdriver

url = "https://www.nytimes.com"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=socks://127.0.0.1:1080')
chrome_options.add_argument('--window-size=1920,3840')
chrome_options.add_argument('headless')
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.get_screenshot_as_file('screen.png')
browser.close()
