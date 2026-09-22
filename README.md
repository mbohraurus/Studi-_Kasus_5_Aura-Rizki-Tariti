# Studi-_Kasus_5_Aura-Rizki-Tariti

Nama: Aura Rizki Tariti
Kelas: A
Angkatan: 2026
NIM: 2609116032
Soal: Genap

Sebenarnya saya punya dua versi kode untuk studi kasus ini, yang saya upload dalam bentuk file Python di repository ini adalah sistem yang menghitung tarif parkir berdasarkan jenis kendaraan dan durasi `dalam hitungan jam`.
Saya punya satu versi lagi yang menghitung tarif berdasarkan durasi `dalam hitungan menit`, tapi kurang akurat karena ada bilangan seperti patokan tarif parkir mobil yang jadi bilangan desimal dan bukan integer.

Untuk versi kode yang berbasis durasi parkir dalam hitungan jam, saya menggunakan function `hitung` dengan parameter `jenis` kendaraan dan `durasi` parkir. Jadi, kegunaan fungsi ini adalah fokus pada proses pengolahan input yang butuh operasi aritmetika, sedangkan perintah input dan outputnya sendiri disusun seperti biasa dalam perulangan `while`.
<img width="902" height="748" alt="Screenshot 2026-09-22 211054" src="https://github.com/user-attachments/assets/88faab37-fffa-43fa-8b22-8dfd2cbb9e93" />

Contoh input dan output untuk kategori mobil dan motor masing-masing 1 saja:
<img width="717" height="522" alt="Screenshot 2026-09-22 211015" src="https://github.com/user-attachments/assets/8f37dab3-ab72-40bc-a907-20e0386c545e" />

Oiya, function `hitung` cuma dipanggil jika jenis kendaraan yang diinput adalah motor atau mobil karena hanya dua kendaraan itu yang ada standar tarif parkirnya menurut ketentuan studi kasus ini. Jika jenis kendaraan yang diinput bukan motor atau mobil, sistem akan menyatakan dengan output bahwa pengurusan parkir kendaraan tersebut tidak bisa diproses. Gambar di bawah ini menunjukkan contoh hasil output untuk input jenis kendaraan berupa `truk` dan berhentinya progran ketika pengguna tidak ingin melanjutkan proses.
<img width="615" height="117" alt="Screenshot 2026-09-22 211023" src="https://github.com/user-attachments/assets/56499633-2fbd-420b-9077-e3e9505ff725" />

Nah, ini adalah versi penghitungan `durasi parkir berdasarkan menit`, agak ribet karena ada statement kondisi untuk jam masuk dan keluar agar hasil penjumlahan menitnya akurat. Pengguna parkir yang durasi parkirnya di bawah 1 jam, proses penghitungan total durasinya beda dari pengguna parkir yang durasi parkirnya setara 1 jam atau lebih.
<img width="826" height="901" alt="Screenshot 2026-09-22 220842" src="https://github.com/user-attachments/assets/97663db1-3c8a-45f1-b21f-476942f595d0" />

Hasil output buat program versi 'gak resmi' ini:
<img width="696" height="896" alt="Screenshot 2026-09-22 213133" src="https://github.com/user-attachments/assets/316963d1-5c8e-4945-a1e3-15649099c2df" />

Dan ini contoh akibat dari pemrosesan tarif parkir mobil dalam 1 jam yang seharusnya Rp.5000, malah jadi Rp.4900an aja.
<img width="607" height="126" alt="Screenshot 2026-09-22 213149" src="https://github.com/user-attachments/assets/f200d4dc-8b97-46b0-9fea-c3e9e127cb76" />
