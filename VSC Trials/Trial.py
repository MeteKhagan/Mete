def round_up(sayi):
    # Sayıyı varsayılan şekilde yuvarla
    yuvarlanmis = round(sayi)
    # Eğer yuvarlanmış hal, orijinal sayıdan küçükse (örneğin 3.1 -> 3), 1 ekleyerek yukarı yuvarla
    if yuvarlanmis < sayi:
        return yuvarlanmis + 1
    # Zaten yukarı yuvarlanmışsa veya tam sayıysa direkt döndür
    return yuvarlanmis

def round_down(sayi):
    # Sayıyı varsayılan şekilde yuvarla
    yuvarlanmis = round(sayi)
    # Eğer yuvarlanmış hal, orijinal sayıdan büyükse (örneğin 3.9 -> 4), 1 çıkararak aşağı yuvarla
    if yuvarlanmis > sayi:
        return yuvarlanmis - 1
    # Zaten aşağı yuvarlanmışsa veya tam sayıysa direkt döndür
    return yuvarlanmis

# Fonksiyonları Test Edelim:
print("Yukarı Yuvarlama Testi:")
print(f"3.1 -> {round_up(3.1)}")  # Beklenen: 4
print(f"3.9 -> {round_up(3.9)}")  # Beklenen: 4

print("\nAşağı Yuvarlama Testi:")
print(f"3.1 -> {round_down(3.1)}") # Beklenen: 3
print(f"3.9 -> {round_down(3.9)}") # Beklenen: 3