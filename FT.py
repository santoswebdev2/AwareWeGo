#from selenium import webdriver
#import unittest
#from selenium.webdriver.common.keys import Keys
#import time

#class PageTest (unittest.TestCase):
 #   def setUp (self):
     #  self.browser = webdriver.Firefox()
    #def tearDown (self):
   #     self.browser.quit()
  #  def test_start_list_and_retrieve_it(self):
    #    self.browser.get('http://localhost:8000')
     #   self.assertIn('TOUR',self.browser.title)
    #    header_text = self.browser.find_element_by_tag_name('h1').text
   #     self.assertIn('TOUR' , header_text)
  #      inputbox = self.browser.find_element_by_id('Place')
       # self.assertEqual(inputbox.get_attribute('placeholder'),'Type Your Place You Want To Visit')
        #inputbox.send_keys('BATANGAS')
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(5)
'''        table = self.browser.find_elements_by_id('idlisttable')
        rows - table.time_element_tag_name('tr')
        self.asserTrue (any(row.text == 'Judrie Santos'))'''

# if __name__=='__main__':
#	unittest.main(warnings='ignore')
	
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class PageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

#   def tearDown(self):
#       self.browser.quit()

    
    def check_for_row_in_listtable(self, row_text):
        table = self.browser.find_element_by_id('listTable')
        rows = table.find_element_by_tag_name('tr')
#       self.assertIn(row_text,[row.text for row in rows])
    

    def test_start_list_and_retrieve_it(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Contact Tracing List', self.browser.title)
        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Contact Tracing', headerText)
        
        inputbox = self.browser.find_element_by_id('personEntry')
        self.assertEqual(inputbox.get_attribute('placeholder'), "You have contact for more than 15 minutes")

        carrier = self.browser.find_element_by_id('newPatient')
        carrier.click()
        time.sleep(1)
        carrier.send_keys('Jesper Johansson')
        time.sleep(1)
        carResidence = self.browser.find_element_by_id('carResidence')
        carResidence.click()
        time.sleep(1)
        carResidence.send_keys('Smeerensburg, North Pole')
        time.sleep(1)
        inPerson = self.browser.find_element_by_id('personEntry')
        inPerson.click()
        time.sleep(1)
        inPerson.send_keys('Mickey Mouse')
        time.sleep(1)
        inPlace = self.browser.find_element_by_id('placeEntry')
        time.sleep(1)
        inPlace.click()
        time.sleep(1)
        inPlace.send_keys('Disney Wonderland')
        time.sleep(1)
        btnConfirm = self.browser.find_element_by_id('btnConfirm')
        btnConfirm.click()
        time.sleep(2)
        self.check_for_row_in_listtable('1: Mickey Mouse in Disney Wonderland')

        inPerson = self.browser.find_element_by_id('personEntry')
        time.sleep(1)
        inPerson.click()
        time.sleep(1)
        inPerson.send_keys('Red Shoes White')
        inPlace = self.browser.find_element_by_id('placeEntry')
        time.sleep(1)
        inPlace.click()
        time.sleep(1)
        inPlace.send_keys("King White's Palace")
        btnConfirm = self.browser.find_element_by_id('btnConfirm')
        time.sleep(1)
        btnConfirm.click()
        time.sleep(2)
        self.check_for_row_in_listtable('1: Mickey Mouse in Disney Wonderland')
        self.check_for_row_in_listtable("2: Red Shoes White in White's King Palace")

#       table = self.browser.find_element_by_id('listTable')
#       rows = table.find_element_by_tag_name('tr')
#       self.assertIn('1: Mickey Mouse in Disney Wonderland', [row.text for row in rows])
#       self.assertIn("2: Red Shoes White in White's King Palace", [row.text for row in rows])


        
if _name__=='__main_':
    unittest.main()
