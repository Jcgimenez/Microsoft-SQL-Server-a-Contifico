# Exportador de Datos a Contifico

Este script de Python se utiliza para exportar datos de una tabla específica en SQL Server a través de una solicitud POST a un endpoint en Contifico.

## Configuración

Antes de ejecutar el script, asegúrate de configurar correctamente los siguientes parámetros:

### Configuración de SQL Server

- `server`: Dirección del servidor de SQL Server.
- `database`: Nombre de la base de datos.
- `driver`: Controlador de ODBC para SQL Server.
- `nombre_tabla`: Nombre de la tabla que se desea exportar.

### Configuración de Contifico

- `url_contifico`: URL del endpoint en Contifico para la solicitud POST.
- `api_key`: Clave de API personalizada para la autorización.
- `datos_a_enviar`: JSON que se enviara como informacion. Ver documentacion de contifico (metodo POST).

## Requisitos

Asegúrate de tener instalados los siguientes paquetes de Python antes de ejecutar el script:

```bash
pip install pyodbc requests
```

## Uso

1. Configura los parámetros en la sección de configuración.
2. Ejecuta el script.

## Notas Adicionales

- El script convierte objetos Decimal a float antes de la serialización.
- Asegúrate de tener una conexión válida a SQL Server antes de ejecutar el script.

## Autor

[Juan Cruz Gimenez](https://github.com/Jcgimenez)

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

### Resumen de la Licencia

Permite a cualquier persona:

- Utilizar este software con cualquier propósito, incluso comercialmente.
- Modificar este software.
- Distribuir este software.
- Distribuir versiones modificadas de este software.

Este software se proporciona "tal cual", sin garantía de ningún tipo.
