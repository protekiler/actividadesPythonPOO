class alumno:
    facultad="fes aragon"

    def __init__(self,nom,ed,carr):
        self.__nombre=nom
        self.__edad=ed
        self.__carrera=carr
    def set_nombre(self,nom):
        self.__nombre=nom
    def get_nombre(self):
        return self.__nombre
    def set_edad(self,ed):
        if ed>=8 and ed<120:
            self.__edad=ed
        else:
            print("Edad no correcta")
            self.__edad=0
    def get_edad(self):
        return self.__edad
    def set_carrera(self,carr):
        self.__carrera=carr
    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena=" nombre:"+self.__nombre
        cadena=cadena+"\n edad:"+str(self.__edad)
        cadena=cadena+"\n carrera:"+self.__carrera
        cadena=cadena+"\n ________________"
        return cadena

    def estudiar(self,horas=1):
        print(f"El alumno {self.__nombre} esta estudiando por {horas}")


class Perro:
    reino="canino"
    def __init__(self,raza,edad,estatura):
        self.__raza=raza
        self.__edad=edad
        self.__estatura=estatura

    #Aqui ya estamos definiendo un metodo de acceso get
    @property
    def raza(self):
        return self.__raza

    # Aqui ya estamos definiendo un metodo de acceso set
    @raza.setter
    def raza(self,la_raza):
        self.__raza=la_raza
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,edad):
        if edad>0 and edad<20:
            self.__edad=edad
        else:
            print("Edad demasiado alta")
            self.__edad = 0
    @property
    def estatura(self):
        return self.__estatura
    @estatura.setter
    def estatura(self,estatura):
        if estatura>0.1 and estatura<1.1:
            self.__estatura=estatura
        else:
            print("Estatura no valida")
            self.__estatura = 0.1

    def __str__(self):
        return f"""
        -------------------------------------
        |Raza: {self.__raza}                
        |Edad:{self.__edad}                 
        |Estatura{self.__estatura}          
        -------------------------------------
        """
    @staticmethod
    def es_cachorro(edad):
        return edad<3
    @staticmethod
    def dormir(veces=5):
        for n in range(veces):
            print(f"dando vueltas{n+1}")
        print("zzzzzzzzz")
    @classmethod
    def perro_Grande(cls,est):
        if est>0.79:
            return cls("",0,est)