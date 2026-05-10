class Node:
    def __init__(self, nama, uts, uas):
        self.nama = nama
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = (uts + uas) / 2

        # Penentuan Grade & Status
        if self.nilai_akhir >= 80:
            self.grade, self.status = "A", "Lulus"
        elif self.nilai_akhir >= 70:
            self.grade, self.status = "B", "Lulus"
        elif self.nilai_akhir >= 60:
            self.grade, self.status = "C", "Lulus"
        else:
            self.grade, self.status = "D", "Tidak Lulus"
            
        self.next = None


class LinkedListMahasiswa:
    def __init__(self):
        self.awal = None

    # INSERT DEPAN
    def insert_depan(self, nama, uts, uas):
        baru = Node(nama, uts, uas)
        baru.next = self.awal
        self.awal = baru
        print(f"\n[Sistem] {nama} berhasil ditambahkan di depan.")

    # INSERT TENGAH
    def insert_tengah(self, nama, uts, uas, posisi):
        if posisi <= 1 or self.awal is None:
            self.insert_depan(nama, uts, uas)
            return

        baru = Node(nama, uts, uas)
        bantu = self.awal
        
        for i in range(1, posisi - 1):
            if bantu.next is not None:
                bantu = bantu.next
            else:
                break
        
        baru.next = bantu.next
        bantu.next = baru
        print(f"\n[Sistem] {nama} berhasil ditambahkan di posisi {posisi}.")

    # REMOVE DEPAN
    def remove_depan(self):
        if self.awal is None:
            print("\n[Sistem] Data kosong.")
        else:
            hapus = self.awal
            self.awal = self.awal.next
            print(f"\n[Sistem] {hapus.nama} berhasil dihapus dari depan.")

    # REMOVE BERDASARKAN NAMA
    def remove_nama(self, nama):
        bantu = self.awal
        prev = None

        if bantu is not None and bantu.nama == nama:
            self.awal = bantu.next
            print(f"\n[Sistem] {nama} berhasil dihapus.")
            return

        while bantu is not None and bantu.nama != nama:
            prev = bantu
            bantu = bantu.next

        if bantu is None:
            print(f"\n[Sistem] {nama} tidak ditemukan.")
            return

        prev.next = bantu.next
        print(f"\n[Sistem] {nama} berhasil dihapus.")

    # TAMPILKAN DATA
    def tampilkan(self):
        print("\n" + "="*45)
        print(f"{'REKAPITULASI NILAI MAHASISWA':^45}")
        print("="*45)
        
        bantu = self.awal
        if not bantu:
            print("Daftar masih kosong.")
            return
        
        no = 1
        while bantu:
            print(f"{no}. Nama: {bantu.nama:<15} | NA: {bantu.nilai_akhir:>5.2f} | Status: {bantu.status}")
            bantu = bantu.next
            no += 1
        print("-"*45)


# --- UJI COBA ---
list_mhs = LinkedListMahasiswa()

# Tambah data
list_mhs.insert_depan("aal", 80, 85)
list_mhs.insert_depan("una", 90, 95)

# Insert tengah
list_mhs.insert_tengah("siti", 70, 75, posisi=2)

# Tampilkan awal
list_mhs.tampilkan()

# Hapus depan
list_mhs.remove_depan()

# Hapus berdasarkan nama
list_mhs.remove_nama("siti")

# Tampilkan setelah hapus
list_mhs.tampilkan()