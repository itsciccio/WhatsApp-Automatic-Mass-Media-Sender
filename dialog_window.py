from tkinter import *
from tkinter import filedialog
import os

class Dialog_Window:

    def __init__(self):
        self.setup_dialog_box()

        self.media_file = None
        self.promoter_file = None

    def setup_dialog_box(self):
        self.window = Tk()
        self.window.title('Promoter Media Upload')        
        self.window.geometry("400x150")        
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
        self.text_var = StringVar()
        self.text_message = Entry(self.window,
                        textvariable = self.text_var)
  
        self.button_ok = Button(self.window,
                     text = "Send file via WhatsApp 📩",
                     command = self.window.destroy)

        self.button_exit = Button(self.window,
                     text = "Exit",
                     command = self.window.destroy)        

        self.debug_toggle = IntVar()
        self.debug_toggle_checkbox = Checkbutton(self.window, text="Debug", variable=self.debug_toggle)

        self.button_prompt_text_label_promoters.grid(column = 1, row = 1) 
        self.button_explore_promoters.grid(column = 2, row = 1) 
        self.promoters_uploaded_text.grid(column = 3, row = 1) 
        self.button_promt_text_label.grid(column = 1, row = 2) 
        self.button_explore.grid(column = 2, row = 2)  
        self.image_uploaded_text.grid(column = 3, row = 2)
        self.text_label.grid(column = 1,row = 3)
        self.text_message.grid(column = 2,row = 3)
        self.button_ok.grid(column = 2,row = 4)
        self.button_exit.grid(column = 2, row = 5)
        self.debug_toggle_checkbox.grid(column = 2, row = 6, sticky=W)

    def browse_files(self, type_file=""):
        if(type_file=="csv"):
            self.promoter_file = filedialog.askopenfilename(initialdir = os.getcwd()+"/csv_files/",
                                                title = "Select promoter .csv file",
                                                filetypes = (("CSV Files",
                                                            "*.csv"),))
            
            if self.promoter_file != "":
                self.promoters_uploaded_text.configure(text="CSV uploaded!")
        else:
            self.media_file = filedialog.askopenfilename(initialdir = os.getcwd()+"/csv_files/",
                                                title = "Select image/video to send to promoters.",
                                                filetypes = (("all files",
                                                        "*.*"),))
            
            if self.media_file != "":
                self.image_uploaded_text.configure(text="Image uploaded!")


    def run_window(self):
        self.window.mainloop()     

        debug = True if int(self.debug_toggle.get()) == 1 else False

        if self.promoter_file==None or self.media_file==None:
            print("Not enough data provided.\nExiting...")
            exit()

        return self.promoter_file, self.media_file, self.text_var.get(), debug

        