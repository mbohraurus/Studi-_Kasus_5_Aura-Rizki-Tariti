print("Simulasi Sistem Penghitungan Biaya Parkir di Kawasan Pusat Perbelanjaan")
# (no pungli)

def hitung(jenis, durasi):
    if jenis == "mobil":
        biaya = 5000 * durasi    # durasi parkir dihitung per jam
        return biaya
    else:
        biaya = 3000 * durasi    # durasi parkir dihitung per jam
        return biaya

while True:
    print()
    jenis = input("Tipe kendaraan (motor/mobil): ")
    if jenis == "motor" or jenis == "mobil":
        jam_masuk = int(input("Mulai masuk pada pukul (contoh: 7): "))
        jam_keluar = int(input("Lalu keluar sejak pukul (contoh: 7): "))
        durasi = jam_keluar - jam_masuk    # Asumsikan aja gak ada kendaraan yang parkir lebih dari 24 jam
        biaya = hitung(jenis, durasi)
        print()
        print("=========================")
        print("Struk Parkir Elektronik: ")
        print("Jenis kendaraan: ", jenis)
        print("Parkir sejak pukul:", jam_masuk, "hingga pukul:", jam_keluar)
        print("Durasi parkir di sini: ", durasi, "jam")
        print("Tarif parkir: Rp", biaya)
        print("=========================")
        print()
    else:
        print("Kantung parkir tidak tersedia untuk kendaraan selain motor dan mobil")
    klik = input("Ketik 'next' untuk lanjut (jika masih ada pengunjung lain di sini): ")
    if klik == "next":
        continue
    else:
        print()
        print("Kosong ya? Waktunya sistem rehat bentar")
        break