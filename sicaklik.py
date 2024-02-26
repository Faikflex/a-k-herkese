havasicakligi = float(input("Lütfen hava sicakliğini giriniz:"))

if havasicakligi <= 5:
    print("Soğuk")
elif 6 <= havasicakligi <= 14:
    print("Ilık")
else:
    print("Sıcak")
