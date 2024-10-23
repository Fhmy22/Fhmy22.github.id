#include <stdio.h>
#include <string.h>

int main() {
    // Daftar harga wahana
    const int harga_rumah_hantu = 15000;
    const int harga_roller_coaster = 20000;
    const int harga_tong_setan = 5000;
    const int harga_terusan = 30000;
    const int harga_tiket_masuk = 2500;

    int jumlah_tiket;
    char terusan[2];
    int total_wahana = 0;

    // Input jumlah tiket
    printf("Berapa tiket yang ingin Anda beli? ");
    scanf("%d", &jumlah_tiket);

    // Input apakah ingin membeli terusan
    printf("Apakah ingin membeli terusan? (y/n): ");
    scanf("%s", terusan);

    if (strcmp(terusan, "y") == 0 || strcmp(terusan, "Y") == 0) {
        total_wahana += harga_terusan;
        printf("Anda membeli terusan seharga %d\n", harga_terusan);
    } else {
        // Pilihan wahana
        char rumah_hantu[2], roller_coaster[2], tong_setan[2];

        printf("Apakah ingin bermain di Rumah Hantu? (y/n): ");
        scanf("%s", rumah_hantu);
        if (strcmp(rumah_hantu, "y") == 0 || strcmp(rumah_hantu, "Y") == 0) {
            total_wahana += harga_rumah_hantu;
            printf("Anda memilih Rumah Hantu seharga %d\n", harga_rumah_hantu);
        }

        printf("Apakah ingin bermain di Roller Coaster? (y/n): ");
        scanf("%s", roller_coaster);
        if (strcmp(roller_coaster, "y") == 0 || strcmp(roller_coaster, "Y") == 0) {
            total_wahana += harga_roller_coaster;
            printf("Anda memilih Roller Coaster seharga %d\n", harga_roller_coaster);
        }

        printf("Apakah ingin bermain di Tong Setan? (y/n): ");
        scanf("%s", tong_setan);
        if (strcmp(tong_setan, "y") == 0 || strcmp(tong_setan, "Y") == 0) {
            total_wahana += harga_tong_setan;
            printf("Anda memilih Tong Setan seharga %d\n", harga_tong_setan);
        }
    }

    // Total pembayaran untuk satu tiket
    int total_bayar_per_tiket = harga_tiket_masuk + total_wahana;

    // Total pembayaran untuk semua tiket
    int total_bayar = total_bayar_per_tiket * jumlah_tiket;

    // Output total
    printf("\n--- Rincian Pembayaran ---\n");
    printf("Jumlah Tiket: %d\n", jumlah_tiket);
    printf("Tiket Masuk (per tiket): %d\n", harga_tiket_masuk);
    printf("Total Harga Wahana/Terusan (per tiket): %d\n", total_wahana);
    printf("Total Bayar (semua tiket): %d\n", total_bayar);

    return 0;
}
