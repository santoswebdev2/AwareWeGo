from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):

  def wait_for_table(self, row_text):
      start_time = time.time()
      while True:
          try:
              table = self.browser.find_element_by_id('JudrieTable')
              rows = table.find_elements_by_tag_name('tr')
              self.assertIn(row_text, [row.text for row in rows])
              return
          except (AssertionError, WebDriverException) as e:
              if time.time() - start_time > MAX_WAIT:
                  raise e
                  time.sleep(0.5)  
                 
  def setUp(self):
      self.browser = webdriver.Firefox()

  def test_browser_title(self):
      self.browser.get('http://localhost:8000/')
      #self.browser.get(self.live_server_url)
      self.assertIn('EZTOUR',self.browser.title)
      header_text = self.browser.find_element_by_tag_name('h2').text
      self.assertIn('EZTOUR', header_text)
         
       
      inputfname = self.browser.find_element_by_id('fname')
      self.assertEqual(inputfname.get_attribute('placeholder'),'Enter your First Name')
      inputfname.click()
      time.sleep(1)
      inputfname.send_keys('Judrie')
         
      time.sleep(1)
         
         
      inputlname = self.browser.find_element_by_id('lname')
      self.assertEqual(inputlname.get_attribute('placeholder'),'Enter your Last Name')
      inputlname.click()
      time.sleep(1)
      inputlname.send_keys('Santos')
      time.sleep(1)
         
         
      inputaddress = self.browser.find_element_by_id('address')
      self.assertEqual(inputaddress.get_attribute('placeholder'),'Enter your Email Address')
      inputaddress.click()
      time.sleep(1)
      inputaddress.send_keys('Judriesnts@gmail.com')
      time.sleep(1)
      
      btnContinue = self.browser.find_element_by_id('btnContinue')
      btnContinue.click()
      time.sleep(2)

        
      inputjPlaces = self.browser.find_element_by_id('jPlaces')
      self.assertEqual(inputjPlaces.get_attribute('placeholder'),'Place you want to visit in CALABARZON')
      inputjPlaces.click()
      time.sleep(1)
      inputjPlaces.send_keys('Cavite')
      time.sleep(1)
         
         
      inputjNumber = self.browser.find_element_by_id('jNumber')
      self.assertEqual(inputjNumber.get_attribute('placeholder'),'Enter your current number')
      inputjNumber.click()
      time.sleep(1)
      inputjNumber.send_keys('09615555958')
      time.sleep(1)

      inputjDate = self.browser.find_element_by_id('jDate')
      self.assertEqual(inputjDate.get_attribute('placeholder'),'MM/DD/YYYY')
      inputjDate.click()
      time.sleep(1)
      inputjDate.send_keys('07/20/2021')
      time.sleep(1)
         
      btnContinue = self.browser.find_element_by_id('btnContinue')
      btnContinue.click()
      time.sleep(2)