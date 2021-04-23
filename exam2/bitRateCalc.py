#Bit rate = samples per second * bits per sample

print(str("Bitrate AKA Bits Per Second\n"))

samples = int(input("Samples per second: ")) #Typically 44100
bits = int(input("Bits per sample: " ))

bitrate = (samples*bits)
print(str("\nBitrate = ")+str(bitrate))

quit()