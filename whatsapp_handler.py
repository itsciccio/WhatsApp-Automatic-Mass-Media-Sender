import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv_reader import CSV_Reader
from confirm_window import Confirm_Window
import time
import copy
import random

class WhatsApp_Handler:

    def __init__(self, promoter_file_path, file_path, text_to_send, cue_toggle, debug_toggle):
        self.promoter_file_path = promoter_file_path
        self.file_path = file_path
        self.text_to_send = text_to_send
        self.cue_toggle = cue_toggle
        self.debug_toggle = debug_toggle

        if(self.file_path==None and self.text_to_send=="" and self.debug_toggle==False):
            raise Exception("Please upload an image and/or set the text message.")
            exit()

        if(self.promoter_file_path==None or self.promoter_file_path==''):
            test_promoter = json.load(open('debug/test_user.json'))     
            self.promoter_details = test_promoter
            print("WARNING: Using hard-coded data: "+ str(self.promoter_details))
        else:
            csv_reader = CSV_Reader(self.promoter_file_path)
            self.promoter_details = csv_reader.extract_details()        

        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(2)  

    def run_whatsapp_service(self):

        confirm_window = Confirm_Window(self.promoter_file_path, self.file_path, self.text_to_send, self.cue_toggle, self.debug_toggle)

        if(not confirm_window.run_window()):
            print("User cancelled program.")
            exit()

        for name, items in self.promoter_details.items():

            self.search_for_contact(name)
            
            time.sleep(0.5)

            if self.check_if_exists(name) == False:
                print(f"{name} not found in WhatsApp!")

                self.return_to_home_screen()     
                
                continue
            else:
                self.send_msg_to_contact(name, items['Nickname'], items['Gender'])
        
        if self.debug_toggle: print("Debug test success!")

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

    def send_msg_to_contact(self, name, nickname, gender):
        contact_found = self.driver.find_element_by_xpath('//span[contains(@title, "{}")]'.format(name))
        contact_found.click()        

        list_texts = copy.deepcopy(self.text_to_send)

        if self.cue_toggle:
            intro_cue = self.personalize_texts(nickname, gender)            
            list_texts.insert(0,intro_cue)
        
        if self.debug_toggle: return

        if self.text_to_send!="":
            for text in list_texts:
                text_box = self.driver.find_element_by_xpath('//div[@role="textbox" and @data-tab="10"]')
                text_box.send_keys(text)
                text_box.send_keys(Keys.ENTER)
        if self.file_path!=None:
            attach_button = self.driver.find_element_by_xpath('//div[@role="button" and @title="Attach"]')
            attach_button.click()

            # self.driver.find_element_by_css_selector('input[accept="*"]').send_keys(self.file_path)
            self.driver.find_element_by_css_selector('input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(self.file_path)            

            send_image = self.driver.find_element_by_xpath('//span[@data-testid="send"]')
            send_image.click()

    def personalize_texts(self, nickname, gender):
        greeting = ["heyy", "oyy", "aww"]
        xs = ["xxx", "xx", "x"]
        post_x = ["", "isma", "xanna"]

        if gender == 'F':
            intro = random.choice(greeting)+" "+nickname+" "+random.choice(xs)+" "+random.choice(post_x)
        else:
            intro = random.choice(greeting)+" "+nickname+" "+random.choice(post_x)
        
        print(intro)
        return intro