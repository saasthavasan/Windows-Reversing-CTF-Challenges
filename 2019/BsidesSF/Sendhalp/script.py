def bufferCreation(cpuid):
	buffer = []
	for i in range(249):
		buffer.append(i)
	
	counter = 0
	v3 = 0
	temp1 = 0
	temp2 = 0
	while counter < 249:
		temp1 = counter % len(cpuid)
		temp2 = buffer[counter]
		counter = counter + 1
		v3 = (v3 + ord(cpuid[temp1]) + temp2) % 249
		buffer[counter -1] = buffer[counter -1] ^ buffer[v3]
		buffer[v3] = buffer[v3] ^ buffer[counter -1]
		buffer[counter -1] = buffer[counter -1] ^ buffer[v3]
	return buffer

def decrypt(buffer):
	file1 = open("C:\\Users\\malicious\\Desktop\\bside\\flag.txt.enc", "r")
	encrypted = file1.read()
	decrypted = ""
	temp = 0
	counter = 0
	main_counter = len(encrypted)
	v7 = 0 #loop counter
	
	while (v7 < len(encrypted)):
		v7 = v7 + 1
		counter = (counter + 1) % 249
		temp = (temp + buffer[counter]) % 249
		temp1 = buffer[counter]
		buffer[counter] = buffer[temp]
		buffer[temp] = temp1
		decrypted = decrypted + chr(ord(encrypted[v7 -1]) ^ buffer[((buffer[counter] + buffer[temp])%249)])
	return decrypted
	

def main():
	#Given cpuid is AMDisbetter!
	cpuid = "AMDisbetter!"
	buffer = bufferCreation(cpuid)
	decrypted = decrypt(buffer)
	print decrypted
	
if __name__ == "__main__":
	main()