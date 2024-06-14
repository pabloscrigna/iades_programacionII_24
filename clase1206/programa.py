import sys

# nombre = "Juan"

print(f"len: {len(sys.argv)}")
print(f"sys.argv: {sys.argv}")

if len(sys.argv) != 2:
    print("Error")
    print("programa.py <nombre>")
    exit(1)


print(f"Hola {sys.argv[1]}")
exit(0)




print(f"sys.argv: {sys.argv}")

