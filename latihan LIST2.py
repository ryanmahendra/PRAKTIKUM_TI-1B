#   program list buku

list_buku = []
while True:
    print("masukan data buku")
    judul = input("judul buku\t: ")
    penulis = input("nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print(buku_baru)