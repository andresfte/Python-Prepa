import sys
#se verifica que se introdusca 3 argumentos y no mas de esta cantidad
if len(sys.argv) == 4:
    print("Argumento 1:", sys.argv[1])
    print("Argumento 2:", sys.argv[3])
    print("Argumento 3:", sys.argv[3])
else:
    print("Se introducjo una cantidad distinta de argumentos")
    print("debe contener exactamente 3, ejemplo a, b, c")