# Envio de Correos

Este es un tutorial basico para poder enviar de manera automatizada los correos de los comprobantes electronicos.

### Requisitos
- Instalar [Python](https://www.python.org/downloads/) desde su pagina principal.
- Clonar este repositorio: 
```bash
git clone https://github.com/ricardosuab93/envioCorreos.git
```
- En el archivo envio.py modificar lo siguiente:
```python
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Por ejemplo, 587 para SMTP de Gmail
email_address = "correo@gmail.com"
password = "pasasword"
```
- Ademas:
```python
carpeta_archivos = "carpeta" #carpeta donde tienes las facturas para enviar 

destinatario = "correo" #aqui pones el correo del distanatario
```

### Ejecutar envio:
Antes de ejecutar el envio asegurarse que la configuracion del correo para envio, la carpeta que contiene las facturas, el destinatario esten correctos, puedes tambien cambiar el asunto y el cuerpo del correo

### **Posicionarse en el mismo directorio donde esta el archivo envio.py y ejecutar**
```bash
python envio.py
```