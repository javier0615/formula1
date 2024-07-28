
import random
from clases import Llanta, Motor, Carro, MejoraMotor, DesafioEspecial, Jugador, EquipoDePruebas, EquipoDeSeguridad, CarroDeCarreras, CarroDePruebas, SafetyCar, Grua
from sonidos import reproducir_sonido

def determinar_ganador(jugadores):
    ganador = None
    mejor_kilometraje = -1  # Inicializar con un valor que garantice que se actualice

    print("\nPosiciones finales:")
    for jugador in jugadores:
        print(f"{jugador.nombre} - {jugador.carro.kilometraje} km")

        if not jugador.carro.verificar_accidente_adelantando() and jugador.carro.kilometraje > mejor_kilometraje:
            ganador = jugador
            mejor_kilometraje = jugador.carro.kilometraje

    if ganador:
        print(f"\n¡{ganador.nombre} es el ganador de la carrera!")
        
    else:
        print("\nTodos los jugadores tuvieron accidentes al adelantar. No hay ganador.")
def menu(desafio_lluvia, desafio_velocidad):
    while True:
        print("Seleccione un carro para ver su información:")
        print("1. Carro de Carreras")
        print("2. Carro de Pruebas")
        print("3. Safety Car")
        print("4, Comprar Mejoras De Motor")
        print("5, Elegir Desafío Especial")
        print("6. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            # Imprimir información del carro del Jugador 1
            imprimir_informacion_carro(jugador1.carro, mi_grua)
            decision_adelantar = input("Jugador 1, ¿deseas intentar adelantar? (s/n): ")
            if decision_adelantar.lower() == "s":
                jugador1.carro.adelantar()
                if jugador1.carro.verificar_accidente_adelantando():
                    print("¡Tu carro ha tenido un accidente al intentar adelantar! ¡Cuidado!")
                jugador1.carro.realizar_accion_especial()

        elif opcion == "2":
            # Imprimir información del carro del Jugador 2
            imprimir_informacion_carro(jugador2.carro, mi_grua=None)
            decision_adelantar = input("Jugador 2, ¿deseas intentar adelantar? (s/n): ")
            if decision_adelantar.lower() == "s":
                jugador2.carro.adelantar()
                if jugador2.carro.verificar_accidente_adelantando():
                    print("¡Tu carro ha tenido un accidente al intentar adelantar! ¡Cuidado!")
                jugador2.carro.realizar_accion_especial()

        elif opcion == "3":
            # Imprimir información del carro del Jugador 3
            imprimir_informacion_carro(jugador2.carro, mi_grua=None)
            decision_adelantar = input("Jugador 3, ¿deseas intentar adelantar? (s/n): ")
            if decision_adelantar.lower() == "s":
                jugador3.carro.adelantar()
                if jugador3.carro.verificar_accidente_adelantando():
                    print("¡Tu carro ha tenido un accidente al intentar adelantar! ¡Cuidado!")
                jugador3.carro.realizar_accion_especial()
        elif opcion == "4":
            # Comprar Mejora de Motor
            puntos_disponibles = jugador1.puntos_mejora_motor
            print(f"Tienes {puntos_disponibles} puntos para mejorar el motor de tu carro.")
            opcion_mejora_motor = input("¿Quieres gastar puntos en mejorar el motor? (s/n): ")

            if opcion_mejora_motor.lower() == "s":
                # Aplicar mejora al motor del carro del Jugador 1
                mejora_elegida = MejoraMotor("Mejora Potencia", aumento_velocidad_maxima=10, aumento_aceleracion=5)
                jugador1.carro.aplicar_mejora_motor(mejora_elegida)
                jugador1.puntos_mejora_motor -= 1
                print("Motor mejorado exitosamente.")
        elif opcion == "5":
            # Elegir Desafío Especial
            print("Desafíos Especiales Disponibles:")
            print("1. Clima Desafiante - Enfrenta una tormenta repentina")
            print("2. Desafío de Velocidad - Aumenta la velocidad máxima temporalmente")
            opcion_desafio = input("Elige un desafío especial (1/2): ")

            if opcion_desafio == "1":
                jugador1.completar_desafio(desafio_lluvia)
                print(f"{jugador1.nombre} ha enfrentado con éxito el desafío climático.")
                
            elif opcion_desafio == "2":
                jugador1.completar_desafio(desafio_velocidad)
                print(f"{jugador1.nombre} ha superado el desafío de velocidad.")        
        elif opcion == "6":
            print("Terminando la carrera. Determinando al ganador...")
            determinar_ganador(jugadores)
            break

# ... (resto del código)

# Ejecutar el menú pasando desafio_lluvia como argumento

# Crear instancias de llantas con tracción y consumo de gasolina
llanta_michelin = Llanta("Michelin", "buena", 1.1)
llanta_pirelli = Llanta("Pirelli", "excelente", 1.05)
llanta_goodyear = Llanta("Goodyear", "regular", 1.2)
llanta_bridgestone = Llanta("Bridgestone", "regular", 0.7)

# Crear instancias de motores con tipo, pistones y caballos de fuerza
motor_v6 = Motor("Motor V6", pistones=6, caballos_fuerza=350)
motor_v8 = Motor("Motor V8", pistones=8, caballos_fuerza=450)
motor_v12 = Motor("Motor V12", pistones=12, caballos_fuerza=600)
motor_electrico = Motor("Motor eléctrico", pistones=0, caballos_fuerza=450)

# Crear instancias de los carros y la grúa con diferentes llantas y motores
mi_carro_de_carreras = CarroDeCarreras(velocidad_maxima=200, aceleracion=10, mensaje_equipo="¡Preparados para la carrera!", peso=random.randint(800, 1500), llanta=llanta_michelin, motor=motor_v8)
mi_carro_de_carreras.asignar_nivel_gasolina()


mi_carro_de_pruebas = CarroDePruebas(velocidad_maxima=180, aceleracion=8, equipo_pruebas="Equipo de pruebas 1", peso=random.randint(800, 1500), llanta=llanta_pirelli, motor=motor_v6)
mi_carro_de_pruebas.asignar_nivel_gasolina()

mi_safety_car = SafetyCar(velocidad_maxima=160, aceleracion=7, equipo_seguridad="Equipo de seguridad 1", peso=random.randint(800, 1500), llanta=llanta_goodyear, motor=motor_v6)
mi_safety_car.asignar_nivel_gasolina()

mi_grua = Grua(nivel_gasolina=3, kilometraje=100)
mi_grua.generar_peso_carga_aleatorio()
desafio_lluvia = DesafioEspecial("Clima Desafiante - Tormenta Repentina", "Lluvia intensa que afecta la visibilidad y la adherencia", efecto_velocidad=-20, recompensa={"puntos_mejora_motor": 2})
desafio_velocidad = DesafioEspecial("Desafío de Velocidad", "Aumenta la velocidad máxima temporalmente", efecto_velocidad=30, recompensa={"aumento_poder": 5})
jugador1 = Jugador("Jugador 1", mi_carro_de_carreras)
jugador2 = Jugador("Jugador 2", mi_carro_de_pruebas)
jugador3 = Jugador("Jugador 3", mi_safety_car)

# Agregar jugadores a la lista de jugadores
jugadores = [jugador1, jugador2, jugador3]

def imprimir_informacion_carro(carro, mi_grua):
    print(f"Nombre del carro: {carro.nombre_carro}")
    print(f"Marca de llanta: {carro.llanta.marca}")
    print(f"Tracción de la llanta: {carro.llanta.traccion}")
    print(f"Tipo de motor: {carro.motor.tipo}")
    print(f"Número de pistones: {carro.motor.pistones}")
    print(f"Caballos de fuerza: {carro.motor.caballos_fuerza}")
    print(f"Velocidad Máxima: {carro.velocidad_maxima} Km/h")
    print(f"Aceleración: {carro.aceleracion} Km/h2")
    print(f"Kilometraje: {carro.kilometraje}")
    print(f"Nivel de gasolina: {carro.nivel_gasolina}")
    print(f"Peso: {carro.peso}")
    print(f"Clima: {carro.clima}")

    carro.informacion_adicional(mi_grua)
# Ejecutar el menú
menu(desafio_lluvia, desafio_velocidad)