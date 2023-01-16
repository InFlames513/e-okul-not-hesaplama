ders = int(input("Kaç adet ders gireceksin: "))
ort = 0
bol = 0
for x in range(ders):
    zaman = int(input("Ders saati: "))
    bol = bol + zaman
    not_sayi = int(input("Kaç notun girildi: "))
    tplm = 0
    for y in range(not_sayi):
        tplm = tplm + int(input(f"{y+1}. notun: "))
    ort = ort + (tplm/not_sayi)*zaman

print(f"Ortalaman: {ort/bol}")
while True: pass
