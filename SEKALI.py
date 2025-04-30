# Data jadwal bus Malang–Surabaya per hari
daily_schedules = [
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '08:00', 'arrival_time': '12:00', 'price': 20000},
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '08:00', 'arrival_time': '17:00', 'price': 5000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '09:30', 'arrival_time': '13:30', 'price': 25000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '09:30', 'arrival_time': '15:30', 'price': 10000},
    {'bus_id': 'BUS003', 'route': 'Malang-Surabaya', 'departure_time': '07:45', 'arrival_time': '11:45', 'price': 30000},
    {'bus_id': 'BUS003', 'route': 'Malang-Surabaya', 'departure_time': '07:45', 'arrival_time': '18:45', 'price': 14000},
    {'bus_id': 'BUS004', 'route': 'Malang-Surabaya', 'departure_time': '10:00', 'arrival_time': '14:00', 'price': 35000},
    {'bus_id': 'BUS004', 'route': 'Malang-Surabaya', 'departure_time': '10:00', 'arrival_time': '20:00', 'price': 17000},
    {'bus_id': 'BUS005', 'route': 'Malang-Surabaya', 'departure_time': '08:15', 'arrival_time': '12:15', 'price': 40000},
    {'bus_id': 'BUS005', 'route': 'Malang-Surabaya', 'departure_time': '08:15', 'arrival_time': '22:15', 'price': 19000},
]

# Fungsi mencetak satu jadwal
def print_schedule(item):
    print(f"Bus ID: {item['bus_id']} | Rute: {item['route']} | "
          f"Berangkat: {item['departure_time']} | Sampai: {item['arrival_time']} | Harga: Rp{item['price']}")

if __name__ == "__main__":
    # 1) Input Bus ID dan cari jadwal
    target = input("Masukkan Bus ID (misal BUS001): ")
    matches = [sched for sched in daily_schedules if sched['bus_id'] == target]

    if not matches:
        print(f"\nBus ID '{target}' tidak ditemukan.")
        exit()

    # 2) Tampilkan semua jadwal untuk bus yang dipilih
    print(f"\nDitemukan {len(matches)} jadwal per hari untuk Bus ID '{target}':")
    for sched in matches:
        print_schedule(sched)

    # 3) Input jumlah penumpang
    jalan = int(input("\nMasukkan jumlah penumpang dari sekali jalan: "))

    # 4) Input waktu keberangkatan yang diinginkan
    time_choice = input("Masukkan waktu Sampai yang dipilih (HH:MM): ")

    # 5) Cari jadwal sesuai waktu yang dipilih
    selected = next((sched for sched in matches if sched['arrival_time'] == time_choice), None)
    if not selected:
        print(f"\nTidak ada jadwal dengan waktu berangkat {time_choice} untuk Bus ID '{target}'.")
        exit()

    # 6) Hitung total pendapatan berdasarkan harga per kursi dan jumlah penumpang
    price_each = selected['price']
    total_revenue = jalan * price_each

    # 7) Tampilkan laporan lengkap
    print(f"\n=== Laporan Perjalanan untuk Bus ID '{target}' pada {time_choice} ===")
    print_schedule(selected)
    print(f"Total penumpang  : {jalan}")
    print(f"Total pendapatan : Rp {total_revenue}")
    print("--" * 30)