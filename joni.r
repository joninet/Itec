# Crear un data frame
df <- data.frame(
  nombres = c("Ana", "Luis", "María"),
  edades = c(28, 22, 35),
  alturas = c(1.65, 1.75, 1.60)
)
#print(df)

# Acceder a una columna
print(paste("nombres:", df$nombres))

# Filtrar filas
df_mayores_25 <- df[df$edades > 25, ]
print(df_mayores_25)

# Crear un gráfico de dispersión
# Crear un histograma
# Calcular la media
media_edades <- mean(df$edades)
print(media_edades)

# Calcular la desviación estándar
desviacion_estandar <- sd(df$edades)
print(desviacion_estandar)
