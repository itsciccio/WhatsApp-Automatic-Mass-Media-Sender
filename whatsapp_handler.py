from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv_reader import CSV_Reader
import time

class WhatsApp_Handler:

    def __init__(self, promoter_file_path, file_path, text_to_send, debug_toggle):
        self.promoter_file_path = promoter_file_path
        self.file_path = file_path
        self.text_to_send = text_to_send
        self.debug_toggle = debug_toggle

        if(self.file_path==None or self.text_to_send==""):
            raise Exception("Please upload an image and set the text message.")
            exit()

        csv_reader = CSV_Reader(self.promoter_file_path)
        self.promoter_names = csv_reader.extract_names()
        self.debug = False

        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(2)   

        input('Wait for QR Code... [Press Enter]')

    def run_whatsapp_service(self, debug_toggle=False):

        for name in self.promoter_names:

            self.search_for_contact(name)
            
            time.sleep(0.5)

            if self.check_if_exists(name) == False:
                print(f"{name} not found in WhatsApp!")

                self.return_to_home_screen()     
                
                continue
            else:
                self.send_msg_to_contact(name, debug_toggle)
        
        if debug_toggle: print("Debug test success!")

    def search_for_contact(self, name):
        new_message_button = self.driver.find_element_by_xpath('//div[@role="button" and @title="New chat"]')
        new_message_button.click()

        search_contanct = self.driver.find_element_by_xpath('//div[@role="textbox"]')
        search_contanct.send_keys(name) 

    def check_if_exists(self, name) -> bool:
        if len(self.driver.find_elements_by_xpath('//div[@data-testid="contact-list-key"]'))==0:
            return False
        else:
            return True

    def return_to_home_screen(self):
        back_button = self.driver.find_element_by_xpath('//button[@aria-label="Back"]')
        back_button.click()

    def send_msg_to_contact(self, name, debug=False):
        contact_found = self.driver.find_element_by_xpath('//span[contains(@title, "{}")]'.format(name))
        contact_found.click()
        
        if debug: return

        text_box = self.driver.find_element_by_xpath('//div[@role="textbox" and @data-tab="9"]')
        text_box.send_keys(self.text_to_send)
        text_box.send_keys(Keys.ENTER)

        attach_button = self.driver.find_element_by_xpath('//div[@role="button" and @title="Attach"]')
        attach_button.click()

        self.driver.find_element_by_css_selector('input[type="file"]').send_keys(self.file_path)

        send_image = self.driver.find_element_by_xpath('//span[@data-testid="send"]')
        send_image.click()

