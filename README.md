# DATA COMPRESS

Realiza el despliegue de las lambdas y sus respectivas configuraciones.

1. `npm i`

Para correr el lambda en local antes de hacer un push a la rama de despliegue `master`, se debe instalar SLS.

1. sls invoke local -f `<FUNCTION NAME>`
2. en consola te genera los datos de salida.

Si quieres levantar un ambiente local para probar las api gateway, ejecuta:

1. `sls offline`
2. Ve en consola el endpoint generado.
3. Prueba
