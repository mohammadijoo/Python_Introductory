import bitstring

def main():
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin)
    

if __name__ == "__main__":
    main()
