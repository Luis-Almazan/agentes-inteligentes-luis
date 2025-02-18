def diagnostico():
    print("Bienvenido al sistema experto de diagnóstico médico.")
    sintomas_opciones = [
        "Fiebre", "Tos", "Dificultad para respirar", "Dolor de cabeza", "Dolor muscular",
        "Dolor de garganta", "Náuseas", "Dolor abdominal", "Fatiga", "Congestión nasal"
    ]
    
    print("Seleccione los síntomas que tiene:")
    sintomas_usuario = []
    for i, sintoma in enumerate(sintomas_opciones, 1):
        print(f"{i}. {sintoma}")
    
    seleccion = input("Ingrese los números de los síntomas separados por comas: ")
    seleccion = [int(num.strip()) for num in seleccion.split(',') if num.strip().isdigit()]
    sintomas_usuario = [sintomas_opciones[i-1].lower() for i in seleccion if 1 <= i <= len(sintomas_opciones)]
    
    if "fiebre" in sintomas_usuario and "tos" in sintomas_usuario and "dificultad para respirar" in sintomas_usuario:
        print("Diagnóstico: Posible infección respiratoria grave. Consulte a un médico de inmediato.")
    elif "fiebre" in sintomas_usuario and "dolor de cabeza" in sintomas_usuario and "dolor muscular" in sintomas_usuario:
        print("Diagnóstico: Posible gripe.")
    elif "dolor de garganta" in sintomas_usuario and "tos" in sintomas_usuario:
        print("Diagnóstico: Posible resfriado común.")
    elif "dolor abdominal" in sintomas_usuario and "náuseas" in sintomas_usuario:
        print("Diagnóstico: Posible infección estomacal.")
    elif "fatiga" in sintomas_usuario and "congestión nasal" in sintomas_usuario:
        print("Diagnóstico: Posible alergia o resfriado leve.")
    else:
        print("Diagnóstico: No se encontró un diagnóstico claro. Consulte con un médico.")

if __name__ == "__main__":
    diagnostico()