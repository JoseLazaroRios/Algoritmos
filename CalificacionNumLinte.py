print("Calculadora de Calificaciones Literales")


calificacion_numerica = float(input("Ingrese la calificación numérica del estudiante: "))


if calificacion_numerica >= 9.1:
    calificacion_literal = "A Excelente"
elif calificacion_numerica >= 8.1:
    calificacion_literal = "B Muy bien"
elif calificacion_numerica >= 7.5:
    calificacion_literal = "C Bien"
else:
    calificacion_literal = "R Reprobado"


print("La calificación asignada es:", calificacion_literal)
