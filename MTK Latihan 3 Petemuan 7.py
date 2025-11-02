print("""
Nama    : Andi Ramli Hidayat
NIM     : 312510385
Kelas   : TI.25 C.5
Tugas   : 3. Uji Tautologi dengan table kebenaran
""")

import itertools

def implies(p, q):
    return (not p) or q

def check_tautology():
    tautology = True
    for p, q in itertools.product([True, False], repeat=2):
        result = implies(p and q, p)
        print(f"p={p}, q={q}, (p ∧ q) → p = {result}")
        if not result:
            tautology = False
    print("\nKesimpulan:", "TAUTOLOGI" if tautology else "BUKAN tautologi")

check_tautology()
