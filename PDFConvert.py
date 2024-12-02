import tkinter as tk
from tkinter import filedialog, messagebox
from converter import PDFtoDOCX 

class GUI():
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Dönüştürücü")
        self.root.geometry("500x200")  
        self.root.iconbitmap("logo.ico")
          
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

        self.create_widget()
        
    def create_widget(self):
        # Pencere arka planı
        self.root.configure(bg=self.bg_color)
        
        # PDF Dosya Yolu Etiketi
        tk.Label(self.root, text="PDF Dosya Yolu:", bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.pdf_path, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Seç", command=self.select_pdf, bg=self.button_color, fg=self.button_fg_color).grid(row=0, column=2, padx=10, pady=10)
        
        # Kaydedilecek Yer Etiketi
        tk.Label(self.root, text="Kaydedilecek Yer:", bg=self.bg_color, fg=self.fg_color).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.save_path, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Seç", command=self.select_save_location, bg=self.button_color, fg=self.button_fg_color).grid(row=1, column=2, padx=10, pady=10)
        
        # Dönüştür Butonu
        tk.Button(self.root, text="Dönüştür", command=self.convert_pdf, bg="green", fg="white").grid(row=2, column=1, pady=20)

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
    
        success, message = self.pdfconvert.pdf_to_word(pdf_file, output_file)
        if success:
            messagebox.showinfo("Başarılı", message)
        else:
            messagebox.showerror("Hata", message)


if __name__ == "__main__":
    root = tk.Tk()  # Sadece burada root penceresini oluşturun
    app = GUI(root)
    root.mainloop()
