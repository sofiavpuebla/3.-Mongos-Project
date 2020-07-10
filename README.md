# 3.-Mongos-Project

# ¿Cuál es la ubicación óptima para mi empresa?

Recientemente hemos creado una empresa de videojuegos y aún no sabemos donde ubicar la sede.

## Herramientas utilizadas

Para realizar este cometido se utilizan bases de datos en MongoDB a las cuales se realizan distintas queries entre las cuales se incluyen las geoqueries. La información se extrae de un dataset de compañias americanas y de requests a la API de FourSquare para obtener la ubicación de lugares.

## Requerimientos

Dado que para el buen funcionamiento de una empresa es necesario la satisfacción de los trabajadores de la misma, el objetivo es intentar conseguir una ubicación que reúna el mayor número de preferencias de los trabajadores posible. Son los siguientes:
    * Los directivos de la empresa son apasionados de Starbucks, tienen que poder tomarse un café en los descansos.
    * El 30% de los empleados tienen hijos, debe haber un colegio cerca.
    * Los directivos viajan mucho para poder conocer todos los avances de cerca, debe haber un aeropuerto cerca.
    * Cada vez más, los empleados se están volviendo veganos, debe haber sitios donde oferten comida vegana

¿Cuál es la sede perfecta?

### Problemas en la ejecución del proyecto

Tras haber hecho las requests a la API FourSquare y haber importado los datos a MongoDB creando los índices geoespaciales, se intentan hacer geoqueries a Mongo para obtener el número de establecimientos que se encuentren en un radio determinado de una ubicación concreta. Cuando se ejecuta el código da el siguiente error:
    OperationFailure: error processing query: ns=companies.airportTree: GEONEAR  field=geopoint maxdist=500 isNearSphere=0
    Sort: {}
    Proj: {}
    planner returned error :: caused by :: unable to find index for $geoNear query

Se ha intenado solventar creando de nuevo los índices y probando a hacer las geoqueries a otra base de datos creada (aeropuertos, starbucks, colegios, establecimientos con comida vegana) pero de nuevo no detecta el índice geoespacial de mongo y en consecuencia imposibilita hacer queries geoespaciales.
