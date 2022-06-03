
a = 12

def parametros(*args, **kwargs):
     for pos, arg in enumerate(kwargs):
        print(arg)
        print(kwargs[arg])

parametros(hola = 12,bien = 13)