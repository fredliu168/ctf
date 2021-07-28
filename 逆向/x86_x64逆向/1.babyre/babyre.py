'''

mov     byte ptr [esp+2Fh], 66h
mov     byte ptr [esp+2Eh], 6Ch
mov     byte ptr [esp+2Dh], 61h
mov     byte ptr [esp+2Ch], 67h
mov     byte ptr [esp+2Bh], 7Bh
mov     byte ptr [esp+2Ah], 72h
mov     byte ptr [esp+29h], 65h
mov     byte ptr [esp+28h], 76h
mov     byte ptr [esp+27h], 65h
mov     byte ptr [esp+26h], 72h
mov     byte ptr [esp+25h], 73h
mov     byte ptr [esp+24h], 65h
mov     byte ptr [esp+23h], 49h
mov     byte ptr [esp+22h], 73h
mov     byte ptr [esp+21h], 46h
mov     byte ptr [esp+20h], 75h
mov     byte ptr [esp+1Fh], 6Eh
mov     byte ptr [esp+1Eh], 21h
mov     byte ptr [esp+1Dh], 7Dh
'''
b = [0x66,
     0x6C,
     0x61,
     0x67,
     0x7B,
     0x72,
     0x65,
     0x76,
     0x65,
     0x72,
     0x73,
     0x65,
     0x49,
     0x73,
     0x46,
     0x75,
     0x6E,
     0x21,
     0x7D]

flag = ''.join(chr(v) for v in b)

print(flag) # flag{reverseIsFun!}
