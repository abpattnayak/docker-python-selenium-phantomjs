# encoding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS(service_log_path='/tmp/ghostdriver.log')
#driver = webdriver.Chrome()
driver.get("http://www.oppa.com.br")
assert "Moveis e Objetos de Design Online | OPPA" in driver.title
driver.close()