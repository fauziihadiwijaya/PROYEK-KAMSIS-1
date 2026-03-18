import os #HANYA UNTUK  IV RANDOM, BUKAN LIBRARY


# PROGRAM ENKRIPSI DAN DEKRIPSI CBC MODE


BLOCK_SIZE = 16
KEY = b"fauzihadiwijaya4"   # key default 16 byte



# Fungsi XOR dua blok

def xor_block(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x ^ y)
    return bytes(result)



# Padding agar data kelipatan 16 byte

def pad(data):
    while len(data) % BLOCK_SIZE != 0:
        data += b' '
    return data



# Membagi data menjadi blok

def split_blocks(data):
    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        blocks.append(data[i:i + BLOCK_SIZE])
    return blocks



# ENKRIPSI CBC

def encrypt_cbc(plaintext, key, iv):

    plaintext = pad(plaintext)
    blocks = split_blocks(plaintext)

    ciphertext = b''
    previous = iv

    for block in blocks:

        xored = xor_block(block, previous)

        encrypted = xor_block(xored, key)

        ciphertext += encrypted

        previous = encrypted

    return ciphertext, len(blocks)



# DEKRIPSI CBC

def decrypt_cbc(ciphertext, key, iv):

    blocks = split_blocks(ciphertext)

    plaintext = b''
    previous = iv

    for block in blocks:

        decrypted = xor_block(block, key)

        plain_block = xor_block(decrypted, previous)

        plaintext += plain_block

        previous = block

    return plaintext



# MENU

def menu():

    print()
    print("====================================")
    print("        PROGRAM ENKRIPSI CBC MODE   ")
    print("====================================")
    print()
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Ciphertext")
    print("3. Keluar")
    print()



# PROGRAM UTAMA

def main():

    while True:

        menu()

        pilihan = input("Pilih menu: ")

        
        # ENKRIPSI
        
        if pilihan == "1":

            pesan = input("\nMasukkan pesan rahasia : ").encode()

            iv = os.urandom(16)

            cipher, jumlah_blok = encrypt_cbc(pesan, KEY, iv)

            print("\n------------- HASIL -------------")
            print("Key (default)    :", KEY.decode())
            print("PLAINTEXT (HEX)  :", pesan.hex())
            print("IV (HEX)         :", iv.hex())
            print("CIPHERTEXT (HEX) :", cipher.hex())
            print()
            print("Jumlah blok data :", jumlah_blok)
            print("---------------------------------")

        
        # DEKRIPSI
        
        elif pilihan == "2":

            cipher_hex = input("\nMasukkan ciphertext (HEX): ")
            iv_hex = input("Masukkan IV (HEX): ")

            ciphertext = bytes.fromhex(cipher_hex)
            iv = bytes.fromhex(iv_hex)

            hasil = decrypt_cbc(ciphertext, KEY, iv)

            print("\n------------- HASIL -------------")
            print("Key (default) :", KEY.decode())
            print("PLAINTEXT     :", hasil.decode().strip())
            print("---------------------------------")

        
        # KELUAR
        
        elif pilihan == "3":

            print("\nProgram selesai.")
            break

        else:
            print("Menu tidak valid!")

        ulang = input("\nApakah ingin menjalankan lagi? (y/n): ")

        if ulang.lower() != "y":
            break


# menjalankan program
main()