import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from converter import PDFtoDOCX

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Dönüştürücü")
        self.root.geometry("500x200")
        self.root.resizable(False, False)  # Boyutlandırmayı kapat
        
        # Karanlık tema renkleri
        self.bg_color = "#2e2e2e"
        self.fg_color = "#f0f0f0"
        self.button_color = "#4a4a4a"
        self.button_fg_color = "#ffffff"
        self.entry_bg_color = "#3a3a3a"
        self.entry_fg_color = "#f0f0f0"
        
        self.pdf_path = tk.StringVar()
        self.save_path = tk.StringVar()
        
        self.pdfconvert = PDFtoDOCX()
        
        image_path = self.resource_path("image/logo.ico")
        
        self.root.iconbitmap(image_path)
        
        self.create_widget()
        
    def resource_path(self, relative_path):
        """Get the absolute path to a resource, works for dev and for PyInstaller."""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
  
    def create_widget(self):
        self.root.configure(bg=self.bg_color)
        
        # PDF Dosya Yolu Etiketi
        tk.Label(self.root, text="PDF Dosya Yolu:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.pdf_path, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Seç", command=self.select_pdf, bg=self.button_color, fg=self.button_fg_color).grid(row=0, column=2, padx=10, pady=10)
        
        # Kaydedilecek Yer Etiketi
        tk.Label(self.root, text="Kaydedilecek Yer:", bg=self.bg_color, fg=self.fg_color).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.save_path, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Seç", command=self.select_save_location, bg=self.button_color, fg=self.button_fg_color).grid(row=1, column=2, padx=10, pady=10)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=480)
        self.progress.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Dönüştür Butonu
        tk.Button(self.root, text="Dönüştür", command=self.convert_pdf, bg="green", fg="white",width=10,height=2).grid(row=3, column=1, pady=10)

    def select_pdf(self):
        self.pdf_path.set(filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")]))
    
    def select_save_location(self):
        self.save_path.set(filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")]))

    def convert_pdf(self):
        pdf_file = self.pdf_path.get()
        output_file = self.save_path.get()
    
        if not pdf_file:
            messagebox.showerror("Hata", "PDF dosyası seçilmedi!")
            return
    
        if not output_file:
            messagebox.showerror("Hata", "Kayıt yeri seçilmedi!")
            return
        
        self.start_progress_bar(callback=lambda: self.show_result(pdf_file, output_file))
    
    def start_progress_bar(self, callback):
        self.progress["value"] = 0
        max_value = 100
        step_delay = 50  # ms cinsinden adım aralığı
        
        def update_progress(current_value=0):
            if current_value <= max_value:
                self.progress["value"] = current_value
                self.root.after(step_delay, update_progress, current_value + 1)
            else:
                callback()  # Progress bar tamamlanınca callback'i çalıştır
        
        update_progress()

    def show_result(self, pdf_file, output_file):
        # Dosyayı dönüştür
        success, message = self.pdfconvert.pdf_to_word(pdf_file, output_file)
        if success:
            messagebox.showinfo("Başarılı", "PDF başarıyla dönüştürüldü!")
        else:
            messagebox.showerror("Hata", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
