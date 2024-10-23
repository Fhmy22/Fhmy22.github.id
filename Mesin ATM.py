class ATM:
    def __init__(self):
        self.saldo = 100000  # Saldo awal
        self.pin = "1234"    # PIN default

    def cek_saldo(self):
        print(f"Saldo Anda: Rp {self.saldo}")

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Anda telah menyetor: Rp {jumlah}")
            self.cek_saldo()
        else:
            print("Jumlah setoran tidak valid.")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Anda telah menarik: Rp {jumlah}")
            self.cek_saldo()
        else:
            print("Jumlah penarikan tidak valid atau saldo tidak cukup.")

    def main_menu(self):
        while True:
            print("\n=== Mesin ATM ===")
            print("1. Cek Saldo")
            print("2. Setor Uang")
            print("3. Tarik Uang")
            print("4. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                self.cek_saldo()
            elif pilihan == '2':
                jumlah = int(input("Masukkan jumlah setor: "))
                self.setor(jumlah)
            elif pilihan == '3':
                jumlah = int(input("Masukkan jumlah tarik: "))
                self.tarik(jumlah)
            elif pilihan == '4':
                print("Terima kasih, sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()