from tkinter import *
from tkinter import filedialog
import os

class Dialog_Window:

    def __init__(self):
        self.setup_dialog_box()

        self.media_file = None
        self.promoter_file = None
        self.text_message_content = []

    def setup_dialog_box(self):
        self.window = Tk()
        self.window.title('Promoter Media Upload')        
        self.window.geometry("800x350")        
        self.window.config(background = "white")

        self.button_prompt_text_label_promoters = Label(self.window, text = 'Upload promoter .csv file:')
        self.button_explore_promoters = Button(self.window,
                        text = "Browse Files",
                        command = lambda: self.browse_files(type_file="csv") )
        self.promoters_uploaded_text = Label(self.window, text = "")

        self.button_promt_text_label = Label(self.window, text = 'Upload image/video to send:')
        self.button_explore = Button(self.window,
                        text = "Browse Files",
                        command = self.browse_files)
        self.image_uploaded_text = Label(self.window, text = "")

        self.text_label = Label(self.window, text = 'Enter message for promoters: ')
        self.text_message = Text(self.window, width=40, height=10)        
        self.text_message_preview_text = Label(self.window, text = "")

        self.cue_toggle = IntVar(value=1)
        self.cue_toggle_checkbox = Checkbutton(self.window, text="Use Cue", variable=self.cue_toggle)

        self.submit_text_message = Button(self.window,
                        text = "Parse and submit text",
                        command = self.submit_text)
  
        self.button_ok = Button(self.window,
                     text = "Send file via WhatsApp 📩",
                     command = self.window.destroy)

        self.button_exit = Button(self.window,
                     text = "Exit",
                     command = exit)        

        self.debug_toggle = IntVar(value=1)
        self.debug_toggle_checkbox = Checkbutton(self.window, text="Debug", variable=self.debug_toggle)

        self.button_prompt_text_label_promoters.grid(column = 1, row = 1) 
        self.button_explore_promoters.grid(column = 2, row = 1) 
        self.promoters_uploaded_text.grid(column = 3, row = 1) 
        self.button_promt_text_label.grid(column = 1, row = 2) 
        self.button_explore.grid(column = 2, row = 2)  
        self.image_uploaded_text.grid(column = 3, row = 2)
        self.text_label.grid(column = 1,row = 3)
        self.text_message.grid(column = 2,row = 3)
        self.text_message_preview_text.grid(column = 3,row = 3)
        self.cue_toggle_checkbox.grid(column = 2, row = 4, sticky=W)
        self.submit_text_message.grid(column = 2, row = 5)
        self.button_ok.grid(column = 2,row = 6)
        self.button_exit.grid(column = 2, row = 7)
        self.debug_toggle_checkbox.grid(column = 2, row = 8, sticky=W)

    def browse_files(self, type_file=""):
        if(type_file=="csv"):
            self.promoter_file = filedialog.askopenfilename(initialdir = os.getcwd()+"/csv_files/",
                                                title = "Select promoter .csv file",
                                                filetypes = (("CSV Files",
                                                            "*.csv"),))
            
            if self.promoter_file != "":
                self.promoters_uploaded_text.configure(text=f"CSV uploaded! - {self.promoter_file}")
        else:
            self.media_file = filedialog.askopenfilename(initialdir = os.getcwd(),
                                                title = "Select image/video to send to promoters.",
                                                filetypes = (("all files",
                                                        "*.*"),))
            
            if self.media_file != "":
                self.image_uploaded_text.configure(text=f"Image uploaded! - {self.media_file}")

    def submit_text(self):
        current_text = self.text_message.get("1.0", "end-1c")
        
        processed_text = current_text.split("\n")
        self.text_message_content = [line for line in processed_text if line!=""]
        
        text_to_prevew = [line for line in processed_text if line!=""]

        if int(self.cue_toggle.get()) == 1:
            text_to_prevew.insert(0, "[cue] [name] [?xs] [post x]")        
                
        text_to_prevew.insert(0, "Text message preview:")

        text_to_prevew = "\n".join(text_to_prevew)

        self.text_message_preview_text.configure(text=f"{text_to_prevew}")


    def run_window(self):
        self.window.mainloop()     

        debug = True if int(self.debug_toggle.get()) == 1 else False
        use_cue = True if int(self.cue_toggle.get()) == 1 else False

        # if self.promoter_file==None and not debug:
        #     print("CSV data not provided.\nExiting...")
        #     exit()

        return self.promoter_file, self.media_file, self.text_message_content, use_cue, debug

        