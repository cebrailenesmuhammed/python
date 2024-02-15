# Ürün listesi ve fiyatları
urunler = {"Elma": 5, "Armut": 4, "Muz": 6, "Portakal": 3}
# Sipariş listesi ve toplam tutar
siparis = {}
tutar = 0

# Kullanıcıya ürünleri ve fiyatlarını göster
print("Ürün Listesi:")
for urun, fiyat in urunler.items():
    print(f"{urun} - {fiyat} TL")

# Kullanıcıdan ürün seçmesini iste
while True:
    secim = input("Sipariş vermek istediğiniz ürünü girin (Çıkmak için q): ")
    # Eğer q girilirse, siparişi tamamla
    if secim == "q":
        print("Siparişiniz tamamlandı.")
        break
    # Eğer ürün listesinde yoksa, uyarı ver
    elif secim not in urunler:
        print("Böyle bir ürün bulunmuyor. Lütfen tekrar deneyin.")
    # Eğer ürün listesinde varsa, adet sor
    else:
        adet = int(input("Kaç adet istiyorsunuz? "))
        # Sipariş listesine ekle
        siparis[secim] = adet
        # Toplam tutarı güncelle
        tutar += urunler[secim] * adet
        print(f"{secim} ürününden {adet} adet sipariş verdiniz.")

# Sipariş listesini ve toplam tutarı göster
print("Sipariş Listesi:")
for urun, adet in siparis.items():
    print(f"{urun} - {adet} adet")
print(f"Toplam Tutar: {tutar} TL")
