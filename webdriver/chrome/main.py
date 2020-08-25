#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# Optional argument, if not specified will search path.
chrome_option = webdriver.ChromeOptions()
chrome_option.binary_location = "/home/wangyi/bin/chrome"
driver = webdriver.Chrome('/home/wangyi/tools/chromedriver',
                          options=chrome_option,
                          desired_capabilities=chrome_options.to_capabilities(),
                          )
driver.get('http://10.0.0.11/blog/web/crawler_detect/index.html')
# time.sleep(5)  # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)  # Let the user actually see something!
# driver.quit()
