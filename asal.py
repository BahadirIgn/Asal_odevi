import math
sayac = 0
asallar = 0
for k in range(5): 
    sayi = int(input("Sayiyi giriniz: \n"))

    for i in range(2, sayi+1):    
        if sayi%i == 0:
            if sayi == i:
                print("Sayi asaldir")
                sayac += 1
                asallar += sayi
                
                break
            else:
                print("Sayi asal degildir.")   
                print("Bu sayıyı bölen sayılar: ")
                for j in range(2, int(math.sqrt(sayi))):          #Bölenleri bulmak için yeni bir döngü/ # "sayi" kısmını nasıl kare içine alırım?
                    if sayi%j == 0:
                        print(f"{j}")
                break  
ortalama = asallar / sayac
print(f"Asal sayilarin ortalamsası = {ortalama}")               