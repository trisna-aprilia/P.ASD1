class PeralatanRumahSakit:
    def __init__(self, nama, kategori, kualitas, kondisi, lokasi):
        self.nama = nama
        self.kategori = kategori
        self.kualitas = kualitas
        self.kondisi = kondisi
        self.lokasi = lokasi

class IventoriPeralatanRumahSakit:
    def __init__(self):
        self.peralatan = []

    def tambah_peralatan(self, peralatan):
        self.peralatan.append(peralatan)

    def hapus_peralatan(self, peralatan):
        self.peralatan.remove(peralatan)

    def update_peralatan(self, nama_peralatan, kualitas, kondisi):
        for peralatan in self.peralatan:
            if peralatan.nama == nama_peralatan:
                peralatan.kualitas = kualitas
                peralatan.kondisi = kondisi
                return
        print("Peralatan tidak ditemukan.")

    def tampilkan_chart(self):
        data = [(peralatan.nama, peralatan.kategori, peralatan.kualitas, peralatan.kondisi, peralatan.lokasi) for peralatan in self.peralatan]
        return data

    def tampilkan_peralatan(self):
        print("Seluruh Peralatan Rumah Sakit:")
        for peralatan in self.peralatan:
            print(f"Nama: {peralatan.nama}, Kategori: {peralatan.kategori}, Kualitas: {peralatan.kualitas}, Kondisi: {peralatan.kondisi}, Lokasi: {peralatan.lokasi}")

# Membuat objek IventoriPeralatanRumahSakit
inventory = IventoriPeralatanRumahSakit()

# Menambahkan beberapa objek PeralatanRumahSakit ke inventaris
peralatan1 = PeralatanRumahSakit("Termometer", "Diagnosis", "Bagus", "Digunakan", "Room A")
peralatan2 = PeralatanRumahSakit("MRI Machine", "Diagnosis", "Sempurna", "Digunakan", "Room B")
peralatan3 = PeralatanRumahSakit("Endoscopy Sistem", "Diagnosis", "Good", "Baru", "Room C")
peralatan4 = PeralatanRumahSakit("Tensimeter", "Diagnosis", "Sempurna", "Digunakan", "Room D")
peralatan5 = PeralatanRumahSakit("Stetoskop", "Diagnosis", "Bagus", "Baru", "Room E")

inventory.tambah_peralatan(peralatan1)
inventory.tambah_peralatan(peralatan2)
inventory.tambah_peralatan(peralatan3)
inventory.tambah_peralatan(peralatan4)
inventory.tambah_peralatan(peralatan5)

# Menampilkan seluruh peralatan
inventory.tampilkan_peralatan()

# Menampilkan chart sebelum perubahan
print("\nChart sebelum perubahan:")
data = inventory.tampilkan_chart()
for peralatan in data:
    print(f"Nama: {peralatan[0]}, Kategori: {peralatan[1]}, Kualitas: {peralatan[2]}, Kondisi: {peralatan[3]}, Lokasi: {peralatan[4]}")

# Update peralatan
inventory.update_peralatan("Termometer", "Sempurna", "Baru")

# Menampilkan chart setelah perubahan
print("\nChart setelah perubahan:")
data = inventory.tampilkan_chart()
for peralatan in data:
    print(f"Nama: {peralatan[0]}, Kategori: {peralatan[1]}, Kualitas: {peralatan[2]}, Kondisi: {peralatan[3]}, Lokasi: {peralatan[4]}")

# Hapus peralatan
inventory.hapus_peralatan(peralatan2)

# Menampilkan chart setelah penghapusan
print("\nChart setelah penghapusan:")
data = inventory.tampilkan_chart()
for peralatan in data:
    print(f"Nama: {peralatan[0]}, Kategori: {peralatan[1]}, Kualitas: {peralatan[2]}, Kondisi: {peralatan[3]}, Lokasi: {peralatan[4]}")
