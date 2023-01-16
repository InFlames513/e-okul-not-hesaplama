ders = int(input("Kaç adet ders gireceksin: "))
ort = 0
bol = 0
for x in range(ders):
    zaman = int(input("Ders saati: "))
    bol = bol + zaman
    tplm = float(input(f"Ortalaman: "))
    ort = ort + tplm*zaman

print(f"Ortalaman: {ort/bol}")
while True: pass
