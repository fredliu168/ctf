
# babyre

使用IDA逆向

得到如下汇编代码：

```
; Attributes: bp-based frame
; int __cdecl main(int argc, const char **argv, const char **envp)
public _main
_main proc near
; __unwind {
push    ebp
mov     ebp, esp
and     esp, 0FFFFFFF0h
sub     esp, 30h
call    ___main
mov     dword ptr [esp], offset aHiThisIsABabyr ; "Hi~ this is a babyre"
call    _printf
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
mov     eax, 0
leave
retn
; } // starts at 401460
_main endp

```

可以看到main函数中，在打印出Hi~ this is a babyre字符串后有一串16进制，猜想此处应该是flag，将16进制数据copy并装换为ASCII码字符，这里用C语言，也可用python或其他编程语言。

```python

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


```

