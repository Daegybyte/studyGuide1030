#Bit rate = samples per second * bits per sample

print(str("Bitrate AKA Bits Per Second\n"))

samples = int(input("Samples per second: "))
bits = int(input("Bits per sample: " ))

bitrate = (samples*bits)
print(str("\nBitrate = ")+str(bitrate))

quit()