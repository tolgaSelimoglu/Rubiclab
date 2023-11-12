import serial
import time


def yazdir():
    data = ser.readlines()  # Arduinodan bir satır veri oku
    print(data)  # Veriyi ekrana yazdır


# Seri port nesnesi oluştur
ser = serial.Serial('COM11', 9600, timeout=1, bytesize=8, parity='N', stopbits=1)
time.sleep(2)  # Seri portun açılması için 2 saniye bekle
# buffer = [a,b,c,d,e,f] data dizi oluştur
buffer = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
          b'r']  # a - r arası tüm ingilizce karakterler dizisi
counter = 0

# Arduinodan gelen verileri oku
for i in range(0, 18):
    ser.write(buffer[i])  # Arduinoya 1 gönder
    print(i)
    yazdir()

# Seri portu kapat
ser.close()
