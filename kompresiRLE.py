import sys

def compress_rle(text):
    if not text:
        print("Teks kosong. Masukkan teks yang valid.")
        sys.exit()

    compressed_text = ""
    count = 1

    # Iterasi melalui teks
    for i in range(1, len(text)):
        # Jika karakter sama dengan karakter sebelumnya, tambahkan ke count
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Jika karakter berubah, tambahkan karakter dan count ke teks terkompresi
            compressed_text += text[i - 1] + str(count)
            count = 1

    # Menambahkan karakter terakhir dan count ke teks terkompresi
    compressed_text += text[-1] + str(count)

    return compressed_text

if __name__ == "__main__":
    # Dapatkan teks input
    input_text = input("Masukkan teks: ")

    if not input_text:
        print("Teks kosong. Masukkan teks yang valid.")
        sys.exit()

    try:
        compressed_result = compress_rle(input_text)
    except Exception as e:
        print(f"Terjadi kesalahan saat mengompres teks: {e}")
        sys.exit()

    # Menghitung ukuran teks asli dan teks terkompresi dalam satuan byte
    original_size = sys.getsizeof(input_text)
    compressed_size = sys.getsizeof(compressed_result)

    # Tampilkan hasil
    print("Teks Asli:", input_text)
    print("Ukuran Teks Asli:", original_size, "byte")
    print("Teks Terkompresi:", compressed_result)
    print("Ukuran Teks Terkompresi:", compressed_size, "byte")