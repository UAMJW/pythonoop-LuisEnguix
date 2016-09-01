class Humano:
    def __init__(self,edad,estatura):
    	self.edad = edad
    	self.estatura = estatura

    def hablar(self,mensaje):
    	print mensaje

juan = Humano(21,1.68)
ernesto = Humano(20,1.73)

print 'Soy Juan tengo', juan.edad, 'y mido', juan.estatura
print 'Soy Ernesto tengo', ernesto.edad, 'y mido', ernesto.estatura

juan.hablar('Hola')

ernesto.hablar('Hola, Juan!')
