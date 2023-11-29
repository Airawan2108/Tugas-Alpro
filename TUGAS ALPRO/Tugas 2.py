def susun_bilangan():
    bilangan = [21, 45, 17, 25, 10, 99, 77, 5, 55]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)