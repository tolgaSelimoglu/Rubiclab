import pandas as pd

# CSV dosyasını oku
dosya_yolu = 'data.csv'  # Dosya yolunu kendi dosya yolunuzla değiştirin
veri = pd.read_csv(dosya_yolu)

# Label'ı 'Green' olan satırları bul ve indekslerini al
silme_indeksleri = veri[veri['label'] == 'Green'].index[:900]

# Belirtilen indekslere sahip satırları sil
veri = veri.drop(silme_indeksleri)

# Sonucu kaydet (isterseniz kaydetmeyebilirsiniz)
veri.to_csv('yenidata.csv', index=False)

print(f"{len(silme_indeksleri)} adet 'Green' label'ına sahip satır silindi.")
