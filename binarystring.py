# binarystring.py lai
def bincon(decimal):
    print("BINARY\n")
    print(decimal)
    binstr=""
    for i in range(8):
        bin = decimal % 2
        binstr = binstr + str(bin)
        decimal = decimal // 2
        print (bin)
    print(binstr)

def main():
    print("INPUT A -1 TO EXIT THE LOOP")
    print("INPUT AN INTEGER LESS THAN 256 AND GREATER THAN -1")
    done = 0;
    while (done >= 0):
        dec = input("INPUT AN INTEGER : ")
        bincon(dec)
main()
