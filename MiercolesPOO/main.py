from COSAS import alumno,Perro

def main():
    al1=alumno("jose",19,"ICO")
    print(vars(al1))
    al1.__nombre="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("------tostring----")
    print(al1)
    al1.estudiar(4)
    print("------perro------")
    perro1=Perro("podle",2,0.35)
    print(vars(perro1))
    perro1.raza="De la calle" #version de notacion estilo pythonic
    print(vars(perro1))
    perro1.__raza="otra"
    print(vars(perro1))
    perro1.edad=12
    perro1.estatura=0.43
    print(perro1.__str__())
    cachorro=Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes=Perro.perro_Grande(0.8)
    print(danes)
main()