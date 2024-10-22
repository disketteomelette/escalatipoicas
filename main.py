def calcular_honorarios(cuantia):
    escalones = [
        (300, 0.25, 0), 
        (600, 75, 0.22), 
        (3000, 141, 0.15), 
        (6000, 501, 0.13), 
        (18000, 891, 0.11), 
        (30000, 2211, 0.10), 
        (60000, 3411, 0.09), 
        (300000, 6111, 0.08), 
        (600000, 25311, 0.06), 
        (1200000, 43311, 0.04), 
        (3000000, 67311, 0.03), 
        (6000000, 121311, 0.02), 
        (float('inf'), 181311, 0.01)
    ]

    for i, (limite, fijo, tasa_variable) in enumerate(escalones):
        if cuantia < limite:
            escalon = i + 1
            variable = (cuantia - (escalones[i-1][0] if i > 0 else 0)) * tasa_variable
            return escalon, fijo, variable, fijo + variable

print("[#] Honorarios escala tipo ICAS · by JCRueda.com (CC, 2021)")

while True:
    try:
        cuantia = round(float(input('[?] Introducir cuantía: ')), 0)
        porcentaje = input('[?] Porcentaje de la escala (ej. 50 para 50%, en blanco para no aplicar): ')

        escalon, fijo, variable, honorarios = calcular_honorarios(cuantia)

        if porcentaje:
            honorarios *= float(porcentaje) / 100
            msgpor = f"· Aplicado {porcentaje}% sobre {round(honorarios, 2)} €"
        else:
            msgpor = ""

        print(f"[!] ### Son {round(honorarios, 2)} € ### Escalón num. {escalon} · {fijo} € (fijo) + {round(variable, 2)} € (variable %) {msgpor}")

    except ValueError as e:
        print(f"[!] Error: {e}. Intenta de nuevo.")
