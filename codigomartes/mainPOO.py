from cosas import alumno
def main():
    """"
    al1=alumno()
    print(al1)
    al2 = alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)

    print("-----------")
    alumno.facultad="Fes aragon EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(alumno.facultad)
    print("-------un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print("-------modificar atributos publicos")
    al1.edad=999
    print(vars(al1))
    print(vars(al2))
    """
    al1=alumno("diego",18,"ICO")
    al2=alumno("montse",20,"Derecho")
    print(vars(al1))
    al1.__edad=333
    print(al1.__edad)
    print(vars(al1))



main()


