jenis_barang = ["MPPF FORM 5X1000X900mm","CONTROL HORN [10 SET]","PUSH ROD WIRE [10 SET]","BRUSHLESS MOTOR","LINKAGE STOPPER [10 SET]","ESC(SW50A)","RECEIVER(IA10B RX)","CARBON FIBER ROD [16 SET]","SERVO 9G","RC LIPO BATTERY","PROPELLER","FLYSKY-I6X REMOTE CONTROL"]
harga_barang = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11,12]

print("                                                      ")
print("                          KAILAN RC SHOP              ")
print("                     MARILAH BELI DI KEDAI KAMI       ")

print("\n TERDAPAT PELBAGAI JENIS BARANG RC JET DI KEDAI KAMI:")

print ("\n HARGA MPPF FORM 5X1000X900mm=RM23,CONTROL HORN=RM3,PUSH ROD WIRE=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER=RM12,ESC(SW50A)=RM67,RECEIVER(IA10B RX)=RM61,CARBON FIBER ROD 3mm=RM25.30,SERVO 9G=RM5.20,RC LIPO BATTERY=RM57.56,PROPELLER=RM5.50,FLYSKY-I6X REMOTE CONTROL=RM161")    
a=int (input("Masukkan tempahan untuk MPPF FORM 5X1000X900mm:"))
b=int (input("Masukkan tempahan untuk CONTROL HORN:"))
c=int (input("Masukkan tempahan untuk PUSH ROD WIRE:"))
d=int (input("Masukkan tempahan untuk BRUSHLESS MOTOR:"))
e=int (input("Masukkan tempahan untuk LINKAGE STOPPER:"))
f=int (input("Masukkan tempahan untuk ESC(SW50A):"))
g=int (input("Masukkan tempahan untuk RECEIVER(IA10B RX):"))
h=int (input("Masukkan tempahan untuk CARBON FIBER ROD 3mm:"))
i=int (input("Masukkan tempahan untuk SERVO 9G:"))
j=int (input("Masukkan tempahan untuk RC LIPO BATTERY:"))
k=int (input("Masukkan tempahan untuk PROPELLER:"))
l=int (input("Masukkan tempahan untuk FLYSKY-I6X REMOTE CONTROL:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga() :
    for i in range (12) :
        jumlah [i] = harga_barang[i]*tempahan[i]
    return(jumlah)

def cetak() :
    print("\n\nTempahan anda ialah:")
    print(a,"barang", jenis_barang[0])
    print(b,"barang", jenis_barang[1])
    print(c,"barang", jenis_barang[2])
    print(d,"barang", jenis_barang[3])
    print(e,"barang", jenis_barang[4])
    print(f,"barang", jenis_barang[5])
    print(g,"barang", jenis_barang[6])
    print(h,"barang", jenis_barang[7])
    print(i,"barang", jenis_barang[8])
    print(j,"barang", jenis_barang[9])
    print(k,"barang", jenis_barang[10])
    print(l,"barang", jenis_barang[11])

    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()