sueldo_basico, km_totales, km_leader = float(input("Introduzca el sueldo básico por kilometro recorrido: ")), float(input("número total de kilómetros recorridos: ")), float(input("número de kilómetros recorridos con la camiseta de líder: ")) 

pago_total = sueldo_basico * km_totales
if km_leader > 1800:
    recargo = 0.25 * sueldo_basico * (km_leader - 1800)
    pago_total += recargo
if km_totales >= 3277:
    print("Has ganado la vuelta españa!! Te pagaremos 700 millones de pesos + tu sueldo básico {} millones de pesos".format(pago_total/1000000))
else:
    print("El valor a pagar total es de {} millones de pesos".format(pago_total/1000000))
