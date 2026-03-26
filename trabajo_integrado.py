ejercicios = int ( input ( "Ingrese un ejercicio del 1 al 5: " ))

match ejercicios:

    case 1: # CAJA DE KIOSCO

# Pedir el nombre al usuario
        nombre = input ( "Ingrese el nombre: " )
# Mientras el nombre este mal vuelve a pedir y verifica que sean solo letras ni numeros ni simbolos
        while not nombre.isalpha():
            print ( "Solo letras y sin espacios" )
            nombre = input ( "Ingrese su nombre: " )

# Pedir al usuario que ingrese la cantidad de productos
        cantidad_de_productos = input ( "Ingrese la cantidad de productos comprados: " )
# Mientras la cantidad ingresada sea invalida o la cantidad 0 vuelve a pedir verifica que sean numeros ni metras ni simbolos ni el 0
        while not cantidad_de_productos.isdigit() or int (cantidad_de_productos) == 0:
            print ( "Solo numeros y numeros mayores a 0" )
            cantidad_de_productos = input ( "Ingrese la cantidad de productos comprados: " )
# Convierte el valor a numero entero
        cantidad_de_productos = int ( cantidad_de_productos )
# Para guardar los totales
        total_sin_descuento = 0
        total_con_descuento = 0
# Recorre cada producto comprado y luego pide el precio del producto
        for i in range ( 1, cantidad_de_productos + 1):
            precio = input ( f"producto { i } - precio: " )
# Mientras el precio sea valido no va a volver a pedir que ingrese de nuevo y verifica que sean solo numeros ni letras ni simbolos
            while not precio.isdigit ():
                precio = input ( " Ingrese solo números positivos: " )
# Convertir a entero
            precio = int ( precio )
# Sumar al total sin descuento
            total_sin_descuento += precio
# Preguntar si tiene descuento
            descuento = input ( "Descuento ( S / N ): " ).lower()
# Validar que sea si y no
            while descuento != "s" and descuento != "n":
                descuento = input ( "Error, ingrese S o N: " ).lower()
# Si tiene descuento, luego aplicar el 10 % de descuento y suma al total con descuento
            if descuento == "s":
                 precio *=  0.9
            total_con_descuento += precio
# Calcular el ahorro y luego el promedio
            ahorro = total_sin_descuento - total_con_descuento
            promedio = total_con_descuento / cantidad_de_productos

            print( f"""
                Cliente: { nombre }
                Cantidad de productos: { cantidad_de_productos }
                Total sin descuentos: ${ total_sin_descuento }
                Total con descuentos: ${ total_con_descuento:.2f}
                Ahorro: ${ ahorro:.2f}
                Promedio por producto: ${ promedio:.2f}
                """ )
            

    case 2: # ACCESO AL CAMPUS Y MENU SEGURO

# Variables iniciales
        usuario_correcto = "alumno"
        clave_correcta = "python123"
# Contador de intentos y variable para saber si logra entrar
        intentos = 0
        acceso = False
# Entrada de maximo 3 intentos suma de a 1 y muestra la cantidad de intentos que te quedan
        while intentos < 3 and not acceso:
            intentos += 1
            print ( f"Intentos { intentos } de 3 " )
# Pide usuario y despues clave
            usuario = input ( "Ingrese su usuario: " )
            clave = input ( "Ingrese su clave: " )
# Verifica la credencial para poder acceder tanto usuario como la clave y luego si es correcto entra al menu
            if usuario == usuario_correcto and clave == clave_correcta:
                print ( "Acceso correcto" )
                acceso = True
            else:
                print ( "Error de usuario o clave" )
# Si fallas los 3 intentos se bloquea la cuenta
        if not acceso:
            print ( "Cuenta bloqueada" )
# El menu y luego elijes una opcion 
        while acceso:
            print ( f"""
                1: Estado
                2: Cambiar clave
                3: Mensaje
                4: Salir
                """ )
            opcion = input ( "opcion: " )
# Verificar que sean numeros ( ni letras ni simbolos ) y si da error vuelve al inicio hasta que ingreses una opcion 
            if not opcion.isdigit ():
                print ( "Error , ingrese un numero valido" )
                continue
# Convierte a entero
            opcion = int ( opcion ) 
# Valida el rango de 1 a 4 para ingresar y si da error vuelve al inicio hasta que elijas una opcion correcta
            if opcion < 1 or opcion > 4:
                print ( "Ingrese una opcion del 1 al 4 " )
                continue
# Opciones
            match opcion:

                case 1:
                    print ( "Inscripto" )
                case 2:
# Pide nueva clave y con un minimo de 6 caracteres usando len
                    nueva_clave = input ( "Ingrese su clave nueva: " )
                    if len ( nueva_clave ) < 6:
                        print ( "minimo 6 caracteres" )
                    else:
                        confirmar = input ( "Confirmar clave: " )
# Verifica que coincidan las claves
                        if nueva_clave == confirmar:
                            clave_correcta = nueva_clave
                            print ( "Clave cambiada correctamente" )
                        else:
                            print ( "Las claves no coinciden" )
                case 3:
# El mensaje "Alentador"
                    print ( "Se paciente tu puedes con la clave" )
                case 4:
                    print ( "Salir" )
# Termina el while
                    break

    case 3: # AGENDA DE TURNOS CON NOMBRES

# Pedir nombre del operador y verifica que sean letras , ni numeros ni simbolos
        operador = input ("Ingrese su nombre: " )
        while not operador.isalpha():
            operador = input ( "Por favor ingrese solo letras: " )
# Turnos vacios de los lunes 4 y los martes 3
        lunes1 = lunes2 = lunes3 = lunes4 = ""
        martes1 = martes2 = martes3 = ""
# Menu, luego pide que elija una opcion
        while True:
            print( f"""
                    1: Reservar 
                    2: Cancelar 
                    3: Agenda 
                    4: Resumen 
                    5: Salir
                    """ )
            opcion = input ( "Ingrese una opcion: " )
# Comprobar que sean numeros y no letras o simbolos en caso de que no ingrese numeros vuelve a pedir
            if not opcion.isdigit ():
                print ( "Ingrese una opcion correcta ni letras ni simbolos" )
                continue
            opcion = int ( opcion )
                
            match opcion:

                    case 1: # RESERVACION

# elejir el dia , pide al usuario que ingrese su nombre luego valida que el nombre sean letras ni simbolos ni numeros
                        dia = input ( "Elija un día: dia 1 = Lunes, dia 2 = Martes: " )
                        nombre = input ( "Ingrese su nombre: " )
                        while not nombre.isalpha ():
                            nombre = input ( "Ingrese letras, ni simbolos ni numeros: " )
# Si es lunes entonces verifica si ya existe luego guarda el primer lugar libre, si no es porque esta ocupado
                        if dia == "1" or dia == "lunes":
                            if nombre in ( lunes1, lunes2, lunes3 ,lunes4 ):
                                print ( "Repetido" )
                            elif lunes1 == "": lunes1 = nombre
                            elif lunes2 == "": lunes2 = nombre
                            elif lunes3 == "": lunes3 = nombre
                            elif lunes4 == "": lunes4 = nombre
                            else: print ( "Ocupado" )
# Si es martes entonces verifica si ya esxiste un lugar y lo guardo, si no es porque esta ocupado
                        elif dia == "2" or dia == "martes":
                            if nombre in ( martes1, martes2, martes3 ):
                                print ( "Repetido" )
                            elif martes1 == "": martes1 = nombre
                            elif martes2 == "": martes2 = nombre
                            elif martes3 == "": martes3 = nombre
                            else: print ( "Ocupado" )
                        
                    case 2: # CANCELACION
# Elije dia, ingresa su nombre y verifica que sea solo letras ni numeros ni simbolos
                        dia = input ( "Elija un día: dia 1=Lunes, dia 2=Martes: " )
                        nombre = input( "Ingrese su nombre: " )
                        while not nombre.isalpha ():
                            nombre = input ( "Ingrese su nombre ni numeros ni simbolos: " )
# verifica si estas, si estas cancela la reserva 
                        if dia == "1" or dia == "lunes":
                            if lunes1 == nombre: lunes1 = ""
                            elif lunes2 == nombre: lunes2 = ""
                            elif lunes3 == nombre: lunes3 = ""
                            elif lunes4 == nombre: lunes4 = ""
                            else: print ( "No tiene reserva" )
                    
                        elif dia == "2" or dia == "martes":
                            if martes1 == nombre: martes1 = ""
                            elif martes2 == nombre: martes2 = ""
                            elif martes3 == nombre: martes3 = ""
                            else: print ( "No tiene reserva" )
                
                    case 3: # VER AGENDA DEL DIA

# Ingrese un dia y verifica que si esta vacio tiene libre
                        dia = input ( "Elije un dia: día 1=Lunes, dia 2=Martes: " )
                    
                        if dia == "1" or dia == "lunes":
                            print ( "Lunes:", lunes1 or "( libre )", lunes2 or "( libre )", lunes3 or "( libre )", lunes4 or "( libre )" )
                        elif dia == "2" or dia == "martes":
                            print ( "Martes:", martes1 or "( libre )", martes2 or "( libre )", martes3 or "( libre )" )

                    case 4: # VER RESUMEN GENERAL

# Muestra que dia tiene mas ocupados y compara los daias lunes o martes 
                        opcion_lunes = ( lunes1 != "" )+ ( lunes2 != "" ) + ( lunes3 != "" ) + ( lunes4 != "" )
                        opcion_martes = ( martes1 != "" ) + ( martes2 != "" ) + ( martes3 != "" )
                        print( f"Lunes: { opcion_lunes } ocupados, { 4 - opcion_lunes } libres" )
                        print( f"Martes: { opcion_martes } ocupados, { 3 -opcion_martes } libres" )
                    
                        if opcion_lunes > opcion_martes: print ( "Más ocupados: Lunes" )
                        elif opcion_martes > opcion_lunes: print ( "Más ocupados: Martes" )
                        else: print ( "Empate" )
                    
                    case 5: # SALIR
                        print ( "Salir" )
                        break

    case 4: # ESCAPE DE ROOM: LA BOVEDA

# Variables iniciales
        energia = 100
        tiempo = 12
        cerraduras_abiertas = 0
        alarma = False
        codigo_parcial = ""
# Variable anti spam
        racha_forzar = 0
# Nombre del agente y verifica que sean solo letras ni numeros ni simbolos
        agente = input ( "Ingrese su nombre agente: " )
        while not agente.isalpha ():
            agente = input ( "Solo letras ni numeros ni simbolos: " )
# Bucle principal
        while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
# Bloque por alarma y termina el juego             
            if alarma and tiempo <= 3:
                print ( "Sistema bloqueado por alarma" )
                break
# Muestra estado 
            print ( f"""
                Energía: { energia } 
                Tiempo: { tiempo } 
                Cerraduras: { cerraduras_abiertas } 
                Alarma: { alarma }
                """ )
# Menu
            print( f"""
                1. Forzar cerradura
                2. Hackear panel
                3. Descansar
                """ )
# Pide una opcio y verifica que sean solo numeros ni letras ni simbolos
            print ( f"Hola agente { agente } " )
            opcion = input ( "Que opción elije ?: " )
            while not opcion.isdigit ():
                opcion = input ( "Ingrese número: " )
# convierte a numero
            opcion = int ( opcion )
# Opcion 1 Forzar cerradura
            if opcion == 1:
                energia -= 20
                tiempo -= 2
                racha_forzar += 1
# Regla anti spam 3 veces seguidas estas en problemas y activa la alrma
                if racha_forzar == 3:
                    print( "Cerradura trabada - Alarma activada" )
                    alarma = True
                else:
# Si la energia es baja hay riesgo y pide validar un numero entre 1 y 3
                    if energia < 40:
                        riesgo = input ( "Riesgo (1-3): " )
                        while not riesgo.isdigit () or int ( riesgo ) not in ( 1,2,3 ):
                            riesgo = input ( "Ingrese 1-3: " )
# Si elije 3 (Alarma)
                        if int ( riesgo ) == 3:
                            alarma = True
                            print ( "Alarma activada" )
# Si no hay alarma abre cerradura
                    if not alarma:
                        cerraduras_abiertas += 1
                        print ( "Cerradura abierta" )
# Hacker gasta energia tiempo y corta la racha de forzar        
            elif opcion == 2:
                energia -= 10
                tiempo -= 3
                racha_forzar = 0  
                print ( "Hackeando..." )
# se repite 4 veces agrega una letra "A" al codigo
                for i in range ( 4 ):
                    codigo_parcial += "A"
# muestra como va creciendo el codogo despues cuando llega a 8 o mas se cumple y solo abre cuando faltan cerraduras 
                    print ( f"Progreso: { codigo_parcial }" )
                if len ( codigo_parcial ) >= 8 and cerraduras_abiertas < 3:
# abre una cerradura y muestra el mensaje
                    cerraduras_abiertas += 1
                    print ( "Cerradura abierta por hackeo" )
# Descansar recupera energia con un limite maximo de 100 pierde tiempo corta racha
            elif opcion == 3:
                energia += 15
                if energia > 100:
                    energia = 100
                tiempo -= 1
                racha_forzar = 0  
# Si hay alarma pierdes 10 de enrgia
                if alarma:
                    energia -= 10
                print ( " Descansando..." )  
# Si abris las 3 cerraduras ganas
        if cerraduras_abiertas == 3:
            print ( " VICTORIA: Bóveda abierta" )
# Si te quedas sin energia y tiempo perdes
        elif energia <= 0 or tiempo <= 0:
            print ( " DERROTA: Sin energía o tiempo" )
# Si se bloquea por alarma perdes
        elif alarma and tiempo <= 3:
            print ( " DERROTA: Sistema bloqueado" )  


    case 5: # LA ARENA DEL GLADIADOR

        print ( "---BIENVENIDO A LA ARENA ROMANA---\n" )
# Inicializa la variable nombre como cadena vacía
        nombre = ""
# Bucle que se repite hasta que el nombre sea válido ni numeros ni simbolos
        while nombre == "" or not nombre.isalpha ():
            nombre = input( "Nombre del Gladiador: " )
            if nombre == "" or not nombre.isalpha ():
                print ( "Solo se permiten letras ni simbolos ni numeros" )
        
        vida_jugador = 100        
        vida_enemigo = 100        
        pociones = 3              
        danio_pesado = 15         
        danio_enemigo = 12        
        turno_jugador = True

        print ( "=== INICIO DEL COMBATE ===\n" )
# Bucle principal del combate ( continúa mientras ambos tengan vida )
        while vida_jugador > 0 and vida_enemigo > 0:
# Muestra información del turno actual
            print ( "=== NUEVO TURNO ===\n" )
            print ( f"{ nombre } ( HP: { vida_jugador } ) vs Enemigo ( HP: { vida_enemigo } ) Pociones: { pociones }" )
# Inicializa la opción elegida
            opcion = ""
# Bucle de validación del menú
            while opcion == "" or not opcion.isdigit () or int ( opcion ) not in [ 1, 2, 3 ]:
# Muestra opciones disponibles
                print( f"""
                    Elige acción
                    1. Ataque Pesado
                    2. Ráfaga Veloz
                    3. Curar
                    """ )
                opcion = input ( "Elija una opción: " )
# Verifica que sea numero ni simbolos ni letras
                if not opcion.isdigit ():
                    print ( "Ingrese un número solo numeros ni letras ni simbolos" )
# Verifica si el número no está entre 1 y 3
                elif int ( opcion ) not in [ 1, 2, 3 ]:
                    print ( "Elija una opción inválida" )
# Convierte la opción a entero
            opcion = int ( opcion )
# ===== ACCIÓN DE ATAQUE PESADO =====
            if opcion == 1:
# Inicializa daño final con daño base
                danio_final = danio_pesado
# Verifica si el enemigo tiene menos de 20 de vida
                if vida_enemigo < 20:
# Aplica golpe crítico multiplicando por 1.5 
                    danio_final = danio_pesado * 1.5  
                    print ( "¡Golpe Crítico!" )
# Resta el daño al enemigo
                vida_enemigo -= int ( danio_final )
# Muestra el daño causado
                print ( f"¡Atacaste al enemigo por { danio_final } puntos de daño!" )
# ===== ACCIÓN DE ATAQUE DE RÁFAGA VELOZ =====
            elif opcion == 2:
                print ( ">> ¡Inicias una ráfaga de golpes!" )
# Bucle que se repite 3 veces y cada golpe quita 5 de vida
                for i in range ( 3 ):
                    vida_enemigo -= 5
                    print ( "> Golpe conectado por 5 de daño" )
# ===== ACCIÓN DE CURACION =====
            elif opcion == 3:
# Verifica si quedan pociones, suma vida al jugador y resta una pocion
                if pociones > 0:
                    vida_jugador += 30
                    pociones -= 1
                    print ( "¡Te curaste 30 puntos de vida!" )
                else:
                    print ( "¡No quedan pociones!" )
# ===== TURNO DEL ENEMIGO =====
# Verifica que el enemigo siga vivo antes de atacar 
            if vida_enemigo > 0:
# Resta vida al jugador
                vida_jugador -= danio_enemigo
                print ( f"¡El enemigo te atacó por { danio_enemigo } puntos de daño!" )
        
        print ( "=== FIN DEL COMBATE ===" )
# Verifica si el jugador ganó
        if vida_jugador > 0:
            print ( f"¡VICTORIA! { nombre } ha ganado la batalla." )
        else:
            print ( "DERROTA. Has caído en combate." )

    case _:
        print ( "Elija un ejercicio del 1 al 5" )