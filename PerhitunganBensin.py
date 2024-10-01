def hitung_jarak_tempuh(odometer_awal, odometer_akhir, bbm_full_tank):
    return (odometer_akhir - odometer_awal) / bbm_full_tank

def total_biaya(hasil, harga_bensin):
    return hasil * harga_bensin

def main():
    riwayat_hasil = []
    riwayat_biaya = []
    riwayat_odometer_awal = []
    riwayat_odometer_akhir = []
    riwayat_bbm_full_tank = []
    riwayat_jenis_bensin = []

    pertalite = 10000
    pertamax = 12950
    solar = 6800

    while True:
        print("\nSelamat Datang di Program Perhitungan Bensin")
        print("============================================")
        print("1. Mulai Menghitung")
        print("2. Tentang Program")
        print("3. Lihat Riwayat Perhitungan")
        print("4. Keluar")
        print("============================================")
        pilihan = input("Pilih menu : ")

        if pilihan == '1':
            print("Pilih Jenis Kendaraan")
            print("1. Roda 2")
            print("2. Roda 4 atau lebih")
            pilihan_jenis_kendaraan = input("Pilih Jenis Kendaraan : ")

            if pilihan_jenis_kendaraan == '1':
                print("Silahkan memilih jenis bensin")
                print("============================================")
                print("1. Pertalite = 10000/liter")
                print("2. Pertamax  = 12950/liter")
                print("============================================")
                pilihan_bensin = input("Pilih Bensin : ")

                if pilihan_bensin == '1':
                    harga_bensin = pertalite
                elif pilihan_bensin == '2':
                    harga_bensin = pertamax
                else:
                    print("Pilihan Tidak Valid")
                    continue

            elif pilihan_jenis_kendaraan == '2':
                print("Silahkan memilih jenis bensin")
                print("============================================")
                print("1. Pertalite = 10000/liter")
                print("2. Pertamax  = 12950/liter")
                print("3. Solar     = 6800/liter")
                print("============================================")
                pilihan_bensin = input("Pilih Bensin : ")

                if pilihan_bensin == '1':
                    harga_bensin = pertalite
                elif pilihan_bensin == '2':
                    harga_bensin = pertamax
                elif pilihan_bensin == '3':
                    harga_bensin = solar
                else:
                    print("Pilihan Tidak Valid")
                    continue

            else:
                print("Pilihan Tidak ada di Menu")
                continue

            print("============================================")
            odometer_awal = float(input("Masukkan odometer awal \t\t = "))
            odometer_akhir = float(input("Masukkan odometer akhir \t = "))
            bbm_full_tank = float(input("Masukkan jumlah bbm full tank \t = "))
            print("============================================")

            hasil_perhitungan = hitung_jarak_tempuh(odometer_awal, odometer_akhir, bbm_full_tank)

            print(f"Odometer awal\t = {odometer_awal} km")
            print(f"Odometer akhir\t = {odometer_akhir} km")
            print()
            print("Maka : ")
            print(f"Jarak tempuh = (odometer akhir - odometer awal) / jumlah bbm full tank = "
                  f"({odometer_akhir} - {odometer_awal}) / ({bbm_full_tank})")
            print(f"Jarak tempuh = {hasil_perhitungan} km/liter")
            print()

            biaya_total = total_biaya(hasil_perhitungan, harga_bensin)

            print(f"Total Biaya yang keluar = {biaya_total} IDR")
            print()

            riwayat_hasil.append(hasil_perhitungan)
            riwayat_biaya.append(biaya_total)
            riwayat_odometer_awal.append(odometer_awal)
            riwayat_odometer_akhir.append(odometer_akhir)
            riwayat_bbm_full_tank.append(bbm_full_tank)
            riwayat_jenis_bensin.append(pilihan_bensin)

        elif pilihan == '2':
            print("Program ini adalah program yang digunakan untuk menghitung bensin yang dibutuhkan dalam perjalanan "
                  "dan menghitung total biaya yang dikeluarkan dalam perjalanan")
            print()

        elif pilihan == '3':
            print("Riwayat Perhitungan Anda : ")
            for i in range(len(riwayat_hasil)):
                print(f"Perhitungan ke-{i + 1}")
                print(f"Odometer Awal \t\t = {riwayat_odometer_awal[i]} km")
                print(f"Odometer Akhir \t\t = {riwayat_odometer_akhir[i]} km")
                print(f"Jumlah BBM Full Tank \t = {riwayat_bbm_full_tank[i]} Liter")
                print(f"Jarak Tempuh \t\t = {riwayat_hasil[i]} km/liter")
                print("Jenis Bensin \t\t = ", end="")
                if riwayat_jenis_bensin[i] == '1':
                    print("Pertalite")
                elif riwayat_jenis_bensin[i] == '2':
                    print("Pertamax")
                elif riwayat_jenis_bensin[i] == '3':
                    print("Solar")
                else:
                    print("Tidak Diketahui")
                print(f"Total Biaya \t\t = {riwayat_biaya[i]} IDR")
                print()
            print()

        elif pilihan == '4':
            print("Terima Kasih, Sampai Jumpa Kembali")
            break

        else:
            print("Pilihan tidak valid")
            continue

        ulang = input("Ingin memilih menu lain (Y untuk Iya/T untuk Tidak) : ")
        if ulang.lower() != 'y':
            break

    print("\nTerimakasih :)")

if __name__ == "__main__":
    main()
