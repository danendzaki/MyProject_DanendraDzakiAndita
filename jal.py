def luas_segiempat(x0, y0, x1, y1):
    """ Menghitung luas segi empat berdasarkan koordinat 2 titik: 
    pojok kiri bawah (x0, y0), dan kanan atas (x1, y1) """
    
    deltax = x1 - x0
    deltay = y1 - y0
    return deltax * deltay

# Pemanggilan fungsi
segi4_1 = luas_segiempat(1, 1, 3, 3) # Hasil: 2 * 2 = 4
segi4_2 = luas_segiempat(2, 4, 3, 3) # Hasil: 1 * -1 = -1 (Terjadi Logic Error)

print(segi4_1 + segi4_2)