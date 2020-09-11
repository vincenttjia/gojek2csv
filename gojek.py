import sys
from os.path import isfile

input_file = "./input.txt"
output_file = "./gojek.csv"

def get_csv(string):
	a = string.replace("Berikut adalah laporan harian dari outlet ","")
	b = a.split(" tanggal ");
	nama = b[0].replace(","," -")
	c = b[1].split(".Hari ini, outlet Anda telah berhasil menyelesaikan ")
	tanggal = c[0]
	d = c[1].split(" pesanan, dengan rincian sebagai berikut:")
	pesanan=d[0]
	e = d[1].split("Total Harga	")
	f = e[2].split("\t")
	Harga = f[0].replace("IDR ","").replace("Total Biaya","").replace(".","")
	Biaya = f[1].replace("IDR ","").replace("Total Pendapatan","").replace(".","")
	g = f[2].split("Klik di sini")
	Pendapatan = g[0].replace("IDR ","").replace(".","")

	csv = tanggal+","+nama+","+pesanan+","+Harga+","+Biaya+","+Pendapatan+"\n"

	return csv

def main():
	global input_file,output_file
	if(isfile(output_file)):
		while(True):
			selection = input("Output.csv ada apakah anda ingin lanjut(Y/N)")
			selection = selection.upper()
			if(selection=="Y"):
				break
			elif(selection=="N"):
				sys.exit(0)

	f = open(input_file,"r").read().replace('\n', '')
	strings=f.split("Halo Mitra Usaha Gojek,")

	output = open(output_file,"w+")
	output.write("Tanggal,Nama,Total Pesanan,Total Harga,Total Biaya,Total Pendapatan\n")
	strings.pop(0)

	for string in strings:
		output.write(get_csv(string))

	# output = open(output_file,"w+")
	# output.write("Tanggal,Nama,Total Pesanan,Total Harga,Total Biaya,Total Pendapatan\n")
	# print(f)

	
	

	

if __name__ == "__main__":
	main()