from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pdfplumber
import PyPDF2
from voice_rss_api import ConvertTextAduioAPI

file = None

THEME_FONT = ("Arial", 20, "bold")
THME_FONT_TEXT = ("Arial", 12)
THEME_COLOR = '#FFF'

class AudioBook:
    
    def __init__(self) -> None:
        self.text_convert = ''
        
        self.window = Tk()
        self.window.title('CONVERT PDF TO ADUIOBOOK')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        
        self.title_init = Label(text="INSERT A PDF", fg="black", bg=THEME_COLOR, font=THEME_FONT)
        self.title_init.grid(row=0, column=0, columnspan=2)

        self.text_label = Label(text=self.text_convert, fg="black", bg=THEME_COLOR, font=THME_FONT_TEXT)
        self.text_label.grid(row=1, column=0, columnspan=2)

        
        self.upload_pdf = Button(text='Upload PDF', highlightthickness=0, command=self.insert_pdf)
        self.upload_pdf.grid(row=2, column=0, columnspan=2)
        
        self.window.mainloop()
        
    def insert_pdf(self):
        global file
        file_path = filedialog.askopenfilename(filetypes=[("Pdf files", "*.pdf")])
        if file_path:  # Verifica si se seleccionó un archivo
            f = open(file_path, "rb")
            pdf_reader = PyPDF2.PdfReader(f)  # Cambia a PdfReader
            pages = pdf_reader.pages
            text = ''
            with pdfplumber.open(file_path) as pdf:
                for i in range(len(pages)):
                    page = pdf.pages[i]
                    text += page.extract_text()
            self.text_convert = text
            self.text_label.config(text=self.text_convert)
            
            # Elimina el botón de "Cargar PDF"
            self.upload_pdf.grid_forget()
            
            # Añade el botón de "Convertir a Audio"
            self.upload_pdf = Button(text='Convert to Audio', highlightthickness=0, command=self.convert_text_audio)
            self.upload_pdf.grid(row=2, column=0, columnspan=2)

    def convert_text_audio(self):
        if self.text_convert:
            
            api = ConvertTextAduioAPI(text=self.text_convert, filename='audio')
            
            api.convert_audio()
            messagebox.showinfo("Nice", "The text was converted to audio perfectly, filename='audio.mp3', in the same working folder.")
        else:
            messagebox.showwarning("Warning", "Not found text to pdf.")