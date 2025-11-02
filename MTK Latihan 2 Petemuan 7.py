print("""
Nama    : Andi Ramli Hidayat
NIM     : 312510385
Kelas   : TI.25 C.5
Tugas   : 2. Pembuktian Kontradiksi Sederhana (Logika Matematis)
""")

def is_odd(n):
    return n % 2 == 1

def proof_by_contradiction():
    for n in range(1, 10):
        if is_odd(n**2) and not is_odd(n):
            print(f"Kontradiksi ditemukan pada n={n}!")
            return False
    print("Tidak ada kontradiksi ditemukan → pernyataan benar (jika n² ganjil maka n ganjil).")
    return True

proof_by_contradiction()
