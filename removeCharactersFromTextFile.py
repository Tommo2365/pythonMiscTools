# Open selected file and remove speical characters and spaces

#infile = "txtfile.txt"
outfile = timestamp + "Data.txt"

delete_list = ["\x03", "\x02", "\x01"," "] # choose strings to replace with, " "
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
       line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()