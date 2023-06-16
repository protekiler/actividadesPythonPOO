from COSAS import *

def main():
    per1=Persona("jose",19)
    print(per1)
    print(Persona.descripcion)

    print("________herencia alumno_____")
    al1=Alumno("jose",19,"320226359","ICO")
    print(al1)
    print(Alumno.descripcion)
    al2=Alumno.constructor_defecto()
    print(al2)
    al2.nombre="juan"
    print(al2)
    al2.dormir()

    print("-------herencia profe-----")

    profe1=Profesor("jesus",30+16,7953,"herencia de software")
    print(profe1)
    profe1.dormir()

    print("-------herencia ayudante profe-----")
    ayudante=AyudanteProfesor("Adrian",18,"23424524","ICO",23232,"ing en software",4)
    ayudante.dormir()
    ayudante.nombre="abraham"
    print(ayudante)

main()