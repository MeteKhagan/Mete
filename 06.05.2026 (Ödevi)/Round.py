def round_up(x):
    apx = round(x)
    if apx < x :
        return apx + 1 
    return apx
def round_dw(x):
    apx = round(x)
    
    if apx > x:
        return apx - 1
    return apx

x = float(input("Ondalıklı bir sayı giriniz: "))

print(f"\n--- Sonuçlar ---")
print(f"Girdiğiniz Sayı: {x}")
print(f"Yukarı Yuvarlanmış Hali: {round_up(x)}")
print(f"Aşağı Yuvarlanmış Hali: {round_dw(x)}")