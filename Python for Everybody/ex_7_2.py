# Use the file name mbox-short.txt as the file name
count = 0
s = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sline = line.rstrip()
    sline_1 = sline.find('0')
    sline_2 = sline[sline_1:sline_1+6]
    sline_3 = float(sline_2)
    count = count + 1
    s = s + sline_3
    #print(sline_2)
    #print(s, count)
    #print('\n \n', s / count)
print(s / count)

