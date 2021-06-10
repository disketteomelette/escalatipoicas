cuantia = honorarios = fijo = variable = porcentaje = escalon = 0
print("[#] Honorarios escala tipo ICAS · by JCRueda.com (CC, 2021)")
while True:
    cuantia = round(float(input('[?] Introducir cuantía a la que se va a aplicar la escala tipo: ')), 0)
    porcentaje = input('[?] Porcentaje de la escala (si procede) (ej. 50 para 50%, en blanco para no aplicar porcentaje): ')

    if cuantia in range(0, 300) :
        escalon = 1
        fijo = cuantia * 0.25
        variable = 0

    if cuantia in range(300, 600) :
        escalon = 2
        fijo = 75
        variable = (cuantia - 300) * 0.22

    if cuantia in range(600, 3000) :
        escalon = 3
        fijo = 141
        variable = (cuantia - 600) * 0.15

    if cuantia in range(3000, 6000) :
        escalon = 4
        fijo = 501
        variable = (cuantia - 3000) * 0.13

    if cuantia in range(6000, 18000) :
        escalon = 5
        fijo = 891
        variable = (cuantia - 6000) * 0.11

    if cuantia in range(18000, 30000) :
        escalon = 6
        fijo = 2211
        variable = (cuantia - 18000) * 0.10

    if cuantia in range(30000, 60000) :
        escalon = 7
        fijo = 3411
        variable = (cuantia - 30000) * 0.09

    if cuantia in range(60000, 300000) :
        escalon = 8
        fijo = 6111
        variable = (cuantia - 60000) * 0.08

    if cuantia in range(300000, 600000) :
        escalon = 9
        fijo = 25311
        variable = (cuantia - 300000) * 0.06

    if cuantia in range(600000, 1200000) :
        escalon = 10
        fijo = 43311
        variable = (cuantia - 600000) * 0.04

    if cuantia in range(1200000,3000000) :
        escalon = 11
        fijo = 67311
        variable = (cuantia - 1200000) * 0.03

    if cuantia in range(3000000, 6000000) :
        escalon = 12
        fijo = 121311
        variable = (cuantia - 3000000) * 0.02

    if cuantia > 6000000 :
        escalon = 13
        fijo = 181311
        variable = (cuantia - 6000000) * 0.01

    honorarios = fijo + variable

    if porcentaje != "" :
        ahonorarios = honorarios * (float(porcentaje) / 100)
        msgpor = "· Aplicado " + str(porcentaje) + "%" + " sobre " + str(honorarios) + " €"
        honorarios = ahonorarios
    else:
        msgpor = ""

    print("[!] ### Son ", round(honorarios, 2), "€  ### Escalón num.", escalon,"·", fijo,"€ (fijo) +", round(variable, 2),"€ (variable %)",msgpor)