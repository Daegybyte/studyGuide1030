minutesPerCd = int(input("Minutes: "))
secondsPerCd = int(input("Seconds: "))

lengthCdSecs = ((minutesPerCd*60)+secondsPerCd)

sizeOfCdInMB = int(input("Size of CD in MB: "))
bytesPerCd = ((2**20)*sizeOfCdInMB)
bitsPerCd = (bytesPerCd*8)
bitsPerSample = int(input("Bits Per Sample: "))
bitsPerSecond = (bitsPerCd/lengthCdSecs)
maxSamplesPerSecond = (bitsPerSecond/bitsPerSample)
samplesPerSecond =int(input("Samples Per Second: "))

def outputs():
    print(str(int(lengthCdSecs))+str(" seconds"))
    print(str(int(bytesPerCd))+str(" bytes"))
    print(str(int(bitsPerCd))+str(" bits"))
    print(str(int(bitsPerSample))+str(" bits per sample"))
    print(str(float(bitsPerSecond))+str(" bits per second"))
    print(str(int(samplesPerSecond))+str("hz"))
    print(str(float(maxSamplesPerSecond))+str(" maximum samples per second"))

if samplesPerSecond<= maxSamplesPerSecond:
    outputs()
    print("You may increase bits per sample")
else:
    outputs()
    print("You must decrease bits per sample")

