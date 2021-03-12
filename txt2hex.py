import sys
import os
import math

addr = 0;
filepath = sys.argv[-1]

filename, fileExtension = os.path.splitext(filepath)

if(fileExtension != ".txt"):
    print(fileExtension)
    exit("Error! File extension is not compatible.")

targetFileName = filename + ".hex"

f = open(filepath, 'r')
fo = open(targetFileName, 'w')
lines = f.readlines()
f.close()
addr_actual_word = len(lines)
addr_ceiled_width = (int(math.ceil(math.log(addr_actual_word,2))))
addr_ceiled_word  = 2**addr_ceiled_width

if(addr_actual_word < 32):
    print("Warning! Word number ceiled to 32.")
    addr_ceiled_word  = 32
    addr_ceiled_width = 5

addr_empty_word = addr_ceiled_word - addr_actual_word
addr_hex_width  = int(math.ceil(math.log(addr_ceiled_word,16)))

def print_report():
    global addr
    str0 = "Success!"
    str1 = "Input file           : " + str(filepath)
    str2 = "Target file          : " + str(targetFileName)
    str3 = "Total word:          : " + str(addr_ceiled_word)
    str4 = "Width (bit)          : " + str(addr_ceiled_width)
    str5 = "Actual Depth (word)  : " + str(addr_actual_word)
    str6 = "Empty Depth (word)   : " + str(addr_empty_word)
    len_list = [len(str0), len(str1), len(str2), len(str3), len(str4), len(str5), len(str6)]
    print("-"*max(len_list))
    print(str0)
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    print(str6)
    print("-"*max(len_list))

for line in lines:
    try:
        val = line.replace('\n', "")
        val = val.replace('\r', "")
        line_actual_width = len(val)
        line_width = int(math.ceil(line_actual_width/4.0))
        data_string = str(format(int(line,2),"0"+str(line_width)+"x"))
        addr_string = str(format(int(addr),"0"+str(addr_hex_width)+"x"))
        fo.write("@"+addr_string+ " " + data_string + "\n")
        addr = addr + 1
    except Exception as e:
        exit(e)

for a in range(0, addr_empty_word):
    data_string = str(format(int(0),"0"+str(line_width)+"x"))
    addr_string = str(format(int(addr),"0"+str(addr_hex_width)+"x"))
    fo.write("@"+addr_string+ " " + data_string + "\n")
    addr = addr + 1

print_report()
fo.close()
