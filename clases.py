
import random
from playsound import playsound

class Llanta:
    def __init__(self, marca, traccion, consumo_gasolina):
        self.marca = marca
        self.traccion = traccion
        self.consumo_gasolina = consumo_gasolina

class Motor:
    def __init__(self, tipo, pistones, caballos_fuerza):
        self.tipo = tipo
        self.pistones = pistones
        self.caballos_fuerza = caballos_fuerza

class Carro:
    def __init__(self, velocidad_maxima, aceleracion, llanta, motor):
        self.marca = random.choice(["Ferrari", "Renault", "Toyota", "Chevrolet", "Ford", "BMW"])
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.llanta = llanta
        self.motor = motor
        self.kilometraje = random.randint(1, 50)
        self.nivel_gasolina = random.randint(1, 4)
        self.peso = None
        self.nombre_carro = f"{self.marca} con llantas {self.llanta.marca}"
        self.clima = random.choice(["Soleado", "Lluvioso", "Nieve", "Nublado"])
        self.accidente = self.simular_accidente()
        self.mensaje_equipo = None
        self.equipo_pruebas = None
        self.equipo_seguridad = None

    def aplicar_mejora_motor(self, mejora):
        self.motor.caballos_fuerza += mejora.aumento_aceleracion
        self.velocidad_maxima += mejora.aumento_velocidad_maxima
        print(f"{self.nombre_carro} ha mejorado su motor. Nueva velocidad máxima: {self.velocidad_maxima} Km/h")
    
    def realizar_accion_especial(self):
        pass
    def reproducir_sonido(self, archivo_sonido):
        try:
            playsound(archivo_sonido)
        except Exception as e:
            print(f"No se pudo reproducir el sonido: {str(e)}")


    def asignar_nivel_gasolina(self):
        if self.nivel_gasolina < 2:
            return "¡Necesitas colocar gasolina!"
        else:
            return "Nivel de gasolina adecuado."

    def simular_accidente(self):
        return self.clima in ["Lluvioso", "Nieve"] and random.random() < 0.1
    def adelantar(self):
        if random.random() < 0.3:  # 30% de probabilidad de tener éxito al adelantar
            print(f"{self.nombre_carro} ha logrado adelantar a otro carro.")
        else:
            print(f"{self.nombre_carro} ha intentado adelantar, pero ha tenido un problema y no lo logró.")
            self.accidente = self.simular_accidente()

    def verificar_accidente_adelantando(self):
        if self.accidente:
            print(f"¡{self.nombre_carro} ha tenido un accidente al intentar adelantar!")
            return True
        return False

    def informacion_adicional(self, mi_grua):
        if self.accidente:
            print(f"¡{self.nombre_carro} ha tenido un accidente debido al clima {self.clima}!")

        if self.mensaje_equipo:
            print(f"Mensaje del equipo: {self.mensaje_equipo}")
            resultado_remolque = self.verificar_peso_grua(mi_grua)
            print(f"Capacidad de remolque por la grúa: {resultado_remolque}")
        elif self.equipo_pruebas:
            print(f"Equipo de pruebas: {self.equipo_pruebas}")
        elif self.equipo_seguridad:
            print(f"Equipo de seguridad: {self.equipo_seguridad}")

        consumo_gasolina = self.llanta.consumo_gasolina
        cambio = "aumenta" if consumo_gasolina > 1 else "disminuye"
        diferencia_porcentaje = int((consumo_gasolina - 1) * 100)

        if diferencia_porcentaje != 0:
            mensaje = f"El uso de estas llantas {cambio} el consumo de gasolina en un {diferencia_porcentaje}%."
            print(mensaje)
        print(self.asignar_nivel_gasolina())
        print()
class MejoraMotor:
    def __init__(self, tipo, aumento_velocidad_maxima, aumento_aceleracion):
        self.tipo = tipo
        self.aumento_velocidad_maxima = aumento_velocidad_maxima
        self.aumento_aceleracion = aumento_aceleracion
class DesafioEspecial:
    def __init__(self, nombre, descripcion, efecto_velocidad=None ,recompensa=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.efecto_velocidad = efecto_velocidad
        self.recompensa = recompensa
# Crear instancias de DesafioEspecial
desafio_lluvia = DesafioEspecial("Clima Desafiante - Tormenta Repentina", "Lluvia intensa que afecta la visibilidad y la adherencia", efecto_velocidad=-20)
desafio_velocidad = DesafioEspecial("Desafío de Velocidad", "Aumenta la velocidad máxima temporalmente", efecto_velocidad=30)
class Jugador:
    def __init__(self, nombre, carro, puntos_mejora_motor=0, desafios_completados=[]):
        self.nombre = nombre
        self.carro = carro
        self.puntos_mejora_motor = puntos_mejora_motor
        self.victorias = 0
        self.desafios_completados = desafios_completados
    def completar_desafio(self, desafio):
        self.desafios_completados.append(desafio)
        # Aplicar recompensa del desafío
        if "puntos_mejora_motor" in desafio.recompensa:
            self.puntos_mejora_motor += desafio.recompensa["puntos_mejora_motor"]
        if "velocidad_maxima_temporal" in desafio.recompensa:
            self.carro.velocidad_maxima += desafio.recompensa["velocidad_maxima_temporal"]
            print(f"¡{self.nombre} ha aumentado temporalmente su velocidad máxima debido al desafío!")    
class EquipoDePruebas:
    def __init__(self, equipo_pruebas=None):
        self.equipo_pruebas = equipo_pruebas

class EquipoDeSeguridad:
    def __init__(self, equipo_seguridad=None):
        self.equipo_seguridad = equipo_seguridad

class CarroDeCarreras(Carro, EquipoDePruebas):
    def __init__(self, velocidad_maxima, aceleracion, mensaje_equipo, peso, llanta, motor):
        super().__init__(velocidad_maxima, aceleracion, llanta, motor)
        self.peso = peso
        self.mensaje_equipo = mensaje_equipo
    def realizar_accion_especial(self):
        self.reproducir_sonido("formula1.wav")
        print(f"{self.nombre_carro} ha activado el turbo y aumentado su velocidad temporalmente!")
    def verificar_peso_grua(self, grua):
        return "La grúa puede remolcar el carro." if grua.peso_carga >= self.peso else "La grúa no puede remolcar el carro debido a la carga excesiva."

class CarroDePruebas(Carro, EquipoDePruebas):
    def __init__(self, velocidad_maxima, aceleracion, equipo_pruebas, peso, llanta, motor):
        super().__init__(velocidad_maxima, aceleracion, llanta, motor)
        self.peso = peso
        self.equipo_pruebas = equipo_pruebas
    def realizar_accion_especial(self):
        self.reproducir_sonido("formula1.wav")
        # Lógica específica para Carro de Pruebas
        print(f"{self.nombre_carro} ha iniciado una serie de pruebas. ¡Observa los resultados!")

        # Lógica específica de pruebas (puedes personalizar según tus necesidades)
        resultado_pruebas = self.realizar_pruebas()

        print(f"Resultados de las pruebas: {resultado_pruebas}")
    def realizar_pruebas(self):
        # Lógica de pruebas (simulación de resultados, cálculos, etc.)
        # En este ejemplo, simplemente devuelve un mensaje ficticio.
        return "¡Pruebas completadas con éxito! El rendimiento del carro ha mejorado."

class SafetyCar(Carro, EquipoDeSeguridad):
    def __init__(self, velocidad_maxima, aceleracion, equipo_seguridad, peso, llanta, motor):
        super().__init__(velocidad_maxima, aceleracion, llanta, motor)
        self.peso = peso
        self.equipo_seguridad = equipo_seguridad
    def realizar_accion_especial(self):
        print(f"{self.nombre_carro} ha entrado en la pista para garantizar la seguridad. ¡Todos deben reducir la velocidad!")
        mensaje_luces_sirena = self.activar_luces_y_sirena()
        print(mensaje_luces_sirena)

    def activar_luces_y_sirena(self):
        # Lógica de activación de luces y sirena (simulación)
        return "Luces y sirena del Safety Car activadas. Reduzcan la velocidad y sigan al Safety Car."

class Grua:
    def __init__(self, nivel_gasolina, kilometraje, peso_carga=None):
        self.nivel_gasolina = nivel_gasolina
        self.kilometraje = kilometraje
        self.peso_carga = peso_carga

    def generar_peso_carga_aleatorio(self):
        self.peso_carga = random.randint(800, 1500)

    def remolcar(self, carro):
        return "La grúa ha remolcado el carro con éxito." if self.peso_carga >= carro.peso else "La grúa no puede remolcar el carro debido a la carga excesiva."
    