import unittest
from selenium import webdriver
import time

class TestOne(unittest.TestCase):

	def setUp(self):
		self.startTime = time.time() 
		self.driver = webdriver.PhantomJS(service_log_path='/tmp/ghostdriver.log')
		self.driver.set_window_size(1120, 550)


	def test_local(self):
		self.driver.get("http://172.16.3.13/")
		self.assertIn("OPPA", self.driver.title)

	def tearDown(self):
		t= time.time() - self.startTime
		print "%s: %.3f" % (self.id(), t)
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()