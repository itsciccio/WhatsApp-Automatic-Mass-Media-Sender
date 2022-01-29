from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

class Confirm_Window:

    def __init__(self, promoter_file_path, file_path, text_to_send, cue_toggle, debug_toggle):
        self.promoter_file_path = promoter_file_path
        self.file_path = file_path
        self.text_to_send = text_to_send
        self.cue_toggle = cue_toggle
        self.debug_toggle = debug_toggle
        
        if (self.debug_toggle):
            self.setup_debug_box()
        else:
            self.setup_dialog_box()        

        self.confirm = True


    def setup_debug_box(self):
        self.window = Tk()
        self.window.title('Instance Preview')        
        self.window.geometry("50x50")        
        self.window.config(background = "white")
        self.window.protocol("WM_DELETE_WINDOW", self.handle_close)

        self.is_debug_text_title = Label(self.window, text = 'Debug Mode:')
        debug_text = "OFF"
        if self.debug_toggle:
            debug_text = "ON"
        self.is_debug_text = Label(self.window, text = debug_text)

        self.button_ok = Button(self.window,
                     text = "Start",
                     command = self.window.destroy)

        self.button_exit = Button(self.window,
                     text = "Exit",
                     command = self.handle_close) 
        
        self.is_debug_text_title.grid(column=1,row=1)
        self.is_debug_text.grid(column=2,row=1)
        
        self.button_ok.grid(column = 2,row = 2)
        self.button_exit.grid(column = 2, row = 3)



    def setup_dialog_box(self):
        self.window = Tk()
        self.window.title('Instance Preview')        
        self.window.geometry("400x550")        
        self.window.config(background = "white")
        self.window.protocol("WM_DELETE_WINDOW", self.handle_close)
        
        self.promoter_file_path_text_title = Label(self.window, text = 'Promoter File Path:')
        self.promoter_file_path_text = Label(self.window, text = self.promoter_file_path)
        
        self.text_message_title = Label(self.window, text = 'Text Message Preview:')        
        
        text_prev = []
        if self.cue_toggle:
            text_prev.append("[cue] [name] [xs]")   
        text_prev = text_prev + self.text_to_send        
        text_preview = "\n".join(text_prev)        
        self.text_message_text = Label(self.window, text = text_preview)

        if self.file_path != None and "MP4" not in self.file_path:
            self.image_preview_text = Label(self.window, text = 'Image Preview:')        
            self.image = ImageTk.PhotoImage(Image.open(self.file_path).resize((200,200), Image.ANTIALIAS))
            self.image_preview = Label(self.window, image = self.image)

        self.is_debug_text_title = Label(self.window, text = 'Debug Mode:')
        debug_text = "OFF"
        if self.debug_toggle:
            debug_text = "ON"
        self.is_debug_text = Label(self.window, text = debug_text)

        self.button_ok = Button(self.window,
                     text = "Start",
                     command = self.window.destroy)

        self.button_exit = Button(self.window,
                     text = "Exit",
                     command = self.handle_close)        

        self.promoter_file_path_text_title.grid(column=1, row=1)
        self.promoter_file_path_text.grid(column=2, row=1)

        self.text_message_title.grid(column=1, row=2)
        self.text_message_text.grid(column=2, row=2)


        if self.file_path != None and "MP4" not in self.file_path:
            self.image_preview_text.grid(column=1,row=3)
            self.image_preview.grid(column=2,row=3)
        
        self.is_debug_text_title.grid(column=1,row=4)
        self.is_debug_text.grid(column=2,row=4)
        
        self.button_ok.grid(column = 2,row = 5)
        self.button_exit.grid(column = 2, row = 6)

    def handle_close(self):
        self.confirm = False
        self.window.destroy()

    def run_window(self):
        self.window.mainloop()     

        return self.confirm

        