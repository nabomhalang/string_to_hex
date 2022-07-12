from sys import argv

option_handle_list = ['--help', '--reverse']
options = {}

def help():
    print("Usage: python string_to_hex [OPTION]... [BYTES]... [STRING]...")
    print("substitution the string with hexadecimal.")
    print()
    print("==================== for instance ====================")
    print(" > 'flag' -> 0x66, 0x6c, 0x61, 0x67 = 0x67616c66 ")
    print()
    print(" > python string_to_hex.py flag -> 0x67616c66")
    print()
    print(" > python string_to_hex.py 8 flag -> 0x0000000067616c66")
    print()
    print(" > python string_to_hex.py --reverse 8 0x0000000067616c66 -> reversed : flag")
    print()
    print("======================= OPTION =======================")
    print("--help : show this programe option and explain")
    print()
    print("--reverse : Converts hexadecimal to string.")
    print()

if len(argv) == 3:
    if argv[1] in option_handle_list:
        option = option_handle_list[option_handle_list.index(argv[1])].replace("--", "")
        if option == 'help':
            help()
        elif option == 'reverse':
            print("Usage: python string_to_hex --reverse [BYTES]... [STRING]...")
            
    elif '--' in argv[1]:
        option = argv[1].replace("--", "")
        print(f"{argv[0]}: invalid option -- '{option}' ")
        print("Try 'python string_to_hex --help' for more information.")
    else:
        ann = [str(hex(ord(i)))[2:] for i in argv[2]]
        ann.reverse()
        print(f"input : {argv[2]}")
        try:
            result = "".join(ann)
            result = "0x" + ((int(argv[1]) * 2) - len(result)) * "0" + "".join(ann)
        except ValueError:
            print("Try 'python string_to_hex --help' for more information.")
            print("Please put in the correct value")
            exit(0)
        print(result)
        
elif len(argv) >= 3:
    for option_handle in option_handle_list:
        options[option_handle[2:]] = argv[argv.index(option_handle) + 1] if option_handle in argv else None
    
    for a, b in options.items():
        if b != None:
            option = a
            
    if options['reverse'] != None:
        if not '0x' in argv[3][0:2]:
            print("Usage: python string_to_hex --reverse [BYTES]... [STRING]...")
            print("Please put in the correct value")
            exit(0)
        try:
            _input = argv[3].replace("0x", "")
            arr = ["0x" + _input[i:i+2] for i in range(0, len(_input), 2)]
            arr.reverse()
            print(f"input : {argv[3]}")
            print(f"reversed : "+"".join(chr(int(i, 16)) for i in arr))
        except ValueError:
            print("Usage: python string_to_hex --reverse [BYTES]... [STRING]...")
            print("Please put in the correct value")
    elif '--' in argv[1]:
        option = argv[1].replace("--", "")
        print(f"{argv[0]}: invalid option -- '{option}' ")
        print("Try 'python string_to_hex --help' for more information.")
    else:
        print("Usage: python string_to_hex --reverse [BYTES]... [STRING]...")
        exit(0)

elif len(argv) == 2:
    if argv[1] in option_handle_list:
        option = option_handle_list[option_handle_list.index(argv[1])].replace("--", "")
        if option == 'help':
            help()
        elif option == 'reverse':
            print("Usage: python string_to_hex --reverse [BYTES]... [STRING]...")
            
    elif '--' in argv[1]:
        option = argv[1].replace("--", "")
        print(f"{argv[0]}: invalid option -- '{option}' ")
        print("Try 'python string_to_hex --help' for more information.")
    else:
        ann = [str(hex(ord(i)))[2:] for i in argv[1]]
        ann.reverse()
        print(f"input : {argv[1]}")
        result = "0x" + "".join(ann)
        print(result)
else:
    print("Usage: python string_to_hex [OPTION]... [BYTES]... [STRING]...")