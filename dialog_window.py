from tkinter import *
from tkinter import filedialog

class Dialog_Window:

    def __init__(self):
        self.setup_dialog_box()

        self.media_file = None

    def setup_dialog_box(self):
        self.window = Tk()
        self.window.title('Promoter Media Upload')        
        self.window.geometry("500x100")        
        self.window.config(background = "white")

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
        
        self.button_promt_text_label.grid(column = 1, row = 1) 
        self.button_explore.grid(column = 2, row = 1)  
        self.image_uploaded_text.grid(column = 3, row = 1)
        self.text_label.grid(column = 1,row = 2)
        self.text_message.grid(column = 2,row = 2)
        self.button_ok.grid(column = 2,row = 3)
        self.button_exit.grid(column = 2, row = 4)

    def browse_files(self):
        self.media_file = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select image/video to send to promoters.",
                                            filetypes = (("all files",
                                                        "*.*"),("Text files",
                                                        "*.txt*")))
        
        if self.media_file != "":
            self.image_uploaded_text.configure(text="Image uploaded!")

    def run_window(self):
        self.window.mainloop()
        return self.media_file, self.text_var.get()

        