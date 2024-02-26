kalinansure = float(input("Otoparkta kaç saat kaldınız? "))


if kalinansure <= 1:
    ücret = 5
elif 1 < kalinansure <= 5:
    ücret = 5 + (kalinansure - 1) * 4
else:
    ücret = 5 + 4 * 4 + (kalinansure - 5) * 3

print("Ödenecek Miktar:", ücret, "TL")
