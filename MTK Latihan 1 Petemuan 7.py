print("""
Nama    : Andi Ramli Hidayat
NIM     : 312510385
Kelas   : TI.25 C.5
Tugas   :1. Simulasi Tabel Kebenaran (Truth Table)
""")
import itertools

def implies(p, q):
    return (not p) or q

print(f"{'p':<5}{'q':<5}{'p and q':<10}{'p or q':<10}{'¬p':<5}{'p→q':<8}")


for p, q in itertools.product([True, False], repeat=2):
    print(f"{p!s:<5}{q!s:<5}{(p and q)!s:<10}{(p or q)!s:<10}{(not p)!s:<5}{implies(p, q)!s:<8}")
