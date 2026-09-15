produk = {
    "nama": "keyboard",
    "harga": "200000",
    "stok": "15"
}

while True:
    print("menu pengelolaan data produk")
    print("1. lihat data produk")
    print("2. tambah data kategori")
    print("3. ubah harga")
    print("4. hapus kategori")
    print("5. keluar")

    menu = input("pilih menu: ")

    if menu == "1":
        print("data produk:")
        print(produk)

    elif menu == "2":
        kategori = input("masukkan kategori: ")
        produk["kategori"] = kategori
        print("kategori berhasil ditambahkan")

    elif menu == "3":
        harga_baru = int(input("masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("harga telah diubah")

    elif menu == "4":
        del produk["kategori"]
        print("kategori sudah dihapus")

    elif menu == "5":
        print("selesai")
        print("data produk akhir")
        print(produk)
        break

    else:
        print("tidak ada menu tersebut")
