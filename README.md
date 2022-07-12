# string_to_hex

ctf에서 string를 hex형태로 바꾸고 싶은데 그때마다 코드짜기 귀찮아서 만들었습니다

# use

Usage: python string_to_hex [OPTION]... [BYTES]... [STRING]...
substitution the string with hexadecimal.

==================== for instance ====================
 > 'flag' -> 0x66, 0x6c, 0x61, 0x67 = 0x67616c66

 > python string_to_hex.py flag -> 0x67616c66

 > python string_to_hex.py 8 flag -> 0x0000000067616c66

 > python string_to_hex.py --reverse 8 0x0000000067616c66 -> reversed : flag

======================= OPTION =======================
--help : show this programe option and explain

--reverse : Converts hexadecimal to string.
