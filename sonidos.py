from playsound import playsound

def reproducir_sonido(archivo_sonido):
    try:
        playsound(archivo_sonido)
    except Exception as e:
        print(f"No se pudo reproducir el sonido: {str(e)}")