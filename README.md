# Text to Hex Converter for Memory Initialization
This script is for text binary format to hexadecimal (with address value on each line) conversion to create  memory initialization file.




## Limitations

Excepted file extension is only **".txt"** format.
Minimum  word count is limited to **32**.
Address width must be base of **2**. Address width is automatically ceiled.


## How to Run
```
python txt2hex.py <filename> #file name must be txt format only.
```


## Example Run

Run script:
```
python txt2hex.py example.txt
```
Log file output:
```
----------------------------------
Success!
Input file           : example.txt
Target file          : example.hex
Total word:          : 64
Width (bit)          : 6
Actual Depth (word)  : 33
Empty Depth (word)   : 31
----------------------------------
```
