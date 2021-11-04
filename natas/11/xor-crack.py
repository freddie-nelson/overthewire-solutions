data = bytearray("UK\"H+O%pSWh]UZ-T%UhR^,^h", "utf-8")

key_max = 0xffffff
key = 0x01

decrypted = bytearray("", "utf-8")
known = bytearray("bgcolor", "utf-8")

while key < key_max:
    decrypted = ""

    for i in range(0, len(data) - 1):
        decrypted += data[i] ^ key[i % ]

    if known in decrypted:
        print(decrypted)

    key += 1
