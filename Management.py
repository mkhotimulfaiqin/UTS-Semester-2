# Data jadwal bus Malang–Surabaya per hari
daily_schedules = [
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '08:00', 'arrival_time': '12:00', 'price': 10000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '09:30', 'arrival_time': '13:30', 'price': 10000},
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '07:45', 'arrival_time': '11:45', 'price': 10000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '10:00', 'arrival_time': '14:00', 'price': 10000},
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '08:15', 'arrival_time': '12:15', 'price': 10000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '09:00', 'arrival_time': '13:00', 'price': 10000},
    {'bus_id': 'BUS001', 'route': 'Malang-Surabaya', 'departure_time': '07:30', 'arrival_time': '11:30', 'price': 10000},
    {'bus_id': 'BUS002', 'route': 'Malang-Surabaya', 'departure_time': '10:30', 'arrival_time': '14:30', 'price': 10000},
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
    else:
        print(f"\nDitemukan {len(matches)} jadwal per hari untuk Bus ID '{target}':")
        for sched in matches:
            print_schedule(sched)

        # 2) Input jumlah hari dalam bulan ini
        days = int(input("\nMasukkan jumlah hari dalam bulan ini: "))

        # 3) Input perjalanan per hari
        runs_per_day = int(input("Masukkan jumlah perjalanan per hari untuk Bus ID '{target}': "))

        # 4) Hitung total perjalanan dan total pendapatan
        price_each = matches[0]['price']
        total_trips = runs_per_day * days
        total_revenue = runs_per_day * price_each * days

        # 5) Tampilkan laporan
        print(f"\n=== Laporan Bulanan untuk Bus ID '{target}' ===")
        print(f"Total perjalanan per hari  : {runs_per_day}")
        print(f"Jumlah hari               : {days}")
        print(f"Total perjalanan per bulan: {total_trips}")
        print(f"Total pendapatan per bulan: Rp{total_revenue}")
