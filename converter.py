from pdf2docx import Converter

class PDFtoDOCX():
    def __init__(self) -> None:
        pass

    @staticmethod
    def pdf_to_word(pdf_file:str, output_file:str):
        """
        PDF dosyasını Word dosyasına dönüştürür.
        Args:
            pdf_file (str): PDF dosyasının yolu.
            output_file (str): Kaydedilecek Word dosyasının yolu.
        Returns:
            tuple: (bool, str) İşlemin durumu ve mesajı.
        """
        try:
            # PDF'den Word'e dönüştürme işlemi
            cv = Converter(pdf_file)
            cv.convert(output_file, start=0, end=None)  
            cv.close()
            return True, "Başarıyla dönüştürüldü."
        except Exception as e:
            return False, f"Hata: {e}"
