#
# from tarea import cuentaahorro as ca, cuentacorriente as cc, cuentacheque as ch 
import cuentaahorro as ca
import cuentacorriente as cc
import cuentacheque as ch


# --- CASOS DE PRUEBA ---
ahorro = ca.CuentaAhorro("Carlos Rossi", "285001", 1000)
corriente = cc.CuentaCorriente("María López", "285002", 500, 1000)
cheque = ch.CuentaCheque("Empresa SRL", "285003", 2000, 100)

cuentas = [ahorro, corriente, cheque]

print("--- ESTADO INICIAL ---")
for c in cuentas:
    print(c)

print("\n--- PRUEBA POLIMÓRFICA DE EXTRACCIONES ($800) ---")
for c in cuentas:
    c.extraer(800)
    print("\n--- PRUEBA DE LECTURA Y PROTECCIÓN (@property) ---")
    print(f"Saldo consultado: ${c._saldo}")

print("\n--- PRUEBA DE INTERÉS EN CUENTA AHORRO ---")
ahorro.aplicar_interes()
print (ahorro)

# ahorro.saldo = -500  # Descomentar para verificar que arroja ValueError
print ("ok")
# ahorro.cbu = "999"   # Descomentar para verificar que arroja AttributeError (solo lectura)
print ("ok")