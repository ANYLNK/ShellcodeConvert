import sys
 
def bin_to_shellcode(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        
        # Byte to int, split with ","
        shellcode = ', '.join(str(byte) for byte in binary_data)
        return shellcode
    except FileNotFoundError:
        print(f"Error: File path {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error: Unknown {e}")
        return None
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bin_to_shellcode.py <bin_file_path>")
        sys.exit(1)
    bin_file = sys.argv[1]
    result = bin_to_shellcode(bin_file)
    if result:
        # Write to file with C code style.
        with open('shellsource.c', 'w') as output_file:
            output_file.write(f"unsigned char shellcode[] = {{{result}}};\n")
        print("Shellcode write to shellsource.c success.")