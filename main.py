# VisionPass - Biyometrik Ücretlendirme Algoritma Taslağı
# Zeynep Keskin - Ankara Üniversitesi

def yolcu_dogrula(v_imza, istasyon):
    """
    Kamera verisinden gelen matematiksel imzayı (vector) kontrol eder.
    KVKK gereği ham görüntü saklanmaz.
    """
    print(f"--- {istasyon} Durağı: Yolcu Analiz Ediliyor ---")
    # Paycell API sorgusu burada simüle edilir
    print(f"[LOG] İşlem Onaylandı. Paycell ile ödeme tetiklendi.")
    return True

if __name__ == "__main__":
    # Örnek Bir Geçiş Senaryosu
    test_imza = "vec_827364" 
    yolcu_dogrula(test_imza, "Kızılay Metro")
