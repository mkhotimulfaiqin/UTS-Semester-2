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

# (Asumsikan daily_schedules sudah terdefinisi seperti di atas)
def print_schedule(item):
    print(f"Bus ID: {item['bus_id']} | Rute: {item['route']} | "
          f"Berangkat: {item['departure_time']} | Sampai: {item['arrival_time']} | Harga: Rp{item['price']}")

# Minta input Bus ID
target_id = input("Masukkan Bus ID (misal BUS001): ")

# Cari dan tampilkan semua jadwal yang matching
matches = [sched for sched in daily_schedules if sched['bus_id'] == target_id]

if matches:
    print(f"\nDitemukan {len(matches)} jadwal untuk Bus ID '{target_id}':")
    for sched in matches:
        print_schedule(sched)
else:
    print(f"\nBus ID '{target_id}' tidak ditemukan.")
