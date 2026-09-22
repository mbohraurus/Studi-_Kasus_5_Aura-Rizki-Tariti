print("Simulasi Sistem Penghitungan Biaya Parkir")
# (no pungli-pungli club)

def hitung(jenis, durasi):
    if jenis == "mobil":
        biaya = 83.3 * durasi    # durasi dihitung per menit (60 menit / Rp5000)
        return biaya
    else:
        biaya = 50 * durasi      # durasi dihitung per menit (60 menit / Rp3000)
        return biaya

while True:
    print()
    jenis = input("Tipe kendaraan (motor/mobil): ")
    if jenis == "motor" or jenis == "mobil":
        print("Mulai masuk pada:")
        jam_masuk = int(input("Pukul: "))
        menit_masuk = int(input("Lewat (berapa menit?): "))
        print("Lalu keluar sejak: ")
        jam_keluar = int(input("Pukul: "))
        menit_keluar = int(input("Lewat (berapa menit?): "))
        if jam_masuk == jam_keluar:
            durasi = menit_keluar - menit_masuk
        else:
            berapa_jam = jam_keluar - jam_masuk
            durasi = menit_keluar + ((60 * berapa_jam) - menit_masuk)
        biaya = hitung(jenis, durasi)
        print()
        print("=========================")
        print("Struk Parkir Elektronik: ")
        print("Jenis kendaraan: ", jenis)
        print("Parkir sejak pukul: ", jam_masuk,":",menit_masuk)
        print("Hingga pukul: ", jam_keluar,":",menit_keluar)
        print("Durasi parkir di sini: ", durasi, "menit")
        print("Tarif parkir: ", biaya)
        print("=========================")
        print()
    else:
        print("Kantung parkir tidak tersedia untuk kendaraan selain motor dan mobil")
    klik = input("Ketik 'next' untuk lanjut (jika masih ada pengunjung lain yang parkir): ")
    if klik == "next":
        continue
    else:
        print("Kosong ya? Waktunya sistem rehat bentar")
        break