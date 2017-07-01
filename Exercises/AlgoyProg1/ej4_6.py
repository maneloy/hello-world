def que_dia_cae(dia):
    semanas_pasadas = dia // 7
    dias_sobrantes = dia - semanas_pasadas * 7

    if dias_sobrantes == 1:
        print("Lunes")
    elif dias_sobrantes == 2:
        print("Martes")
    elif dias_sobrantes == 3:
        print("Miércoles")
    elif dias_sobrantes == 4:
        print("Jueves")
    elif dias_sobrantes == 5:
        print("Viernes")
    elif dias_sobrantes == 6:
        print("Sábado")
    else:
        print("Domingo") # Al escribir "elif dias_sobrantes == 7: print("Domingo")" no funcionaba. Fijarse por qué.
        

        