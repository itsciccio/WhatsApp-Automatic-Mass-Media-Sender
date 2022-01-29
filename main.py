from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dialog_window import Dialog_Window
from whatsapp_handler import WhatsApp_Handler
import time

if __name__ == "__main__":
    
    dialog_window = Dialog_Window()
    (promoter_file_path, file_path, text_to_send, cue_toggle, debug_toggle) = dialog_window.run_window()    
    start_time = time.time()

    whatsapp_handler = WhatsApp_Handler(promoter_file_path, file_path, text_to_send, cue_toggle, debug_toggle)
    whatsapp_handler.run_whatsapp_service()
    
    print(f"Process completed successfully in {round(time.time()-start_time,2)}s.")
    
