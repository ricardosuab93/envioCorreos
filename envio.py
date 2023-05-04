import smtplib
import os
import glob

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

smtp_server = "mail.nordigesa.com"
smtp_port = 25  # Por ejemplo, 587 para SMTP de Gmail
email_address = "sigeco@nordigesa.com"
password = "nordigesa123*"

def enviar_correo(destinatario, asunto, cuerpo, adjuntos):

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo, 'plain'))

    for adjunto in adjuntos:
        nombre_adjunto = os.path.basename(adjunto)

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(adjunto, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {nombre_adjunto}")
        msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, password)
            server.send_message(msg)
        print(f"Correo enviado a {destinatario} con asunto {asunto}")
    except Exception as e:
        print(f"No se pudo enviar el correo a {destinatario}. Error: {str(e)}")

carpeta_archivos = "carpeta" #carpeta donde tienes las facturas para enviar 
archivos_pdf = glob.glob(carpeta_archivos + "/*.pdf")
archivos_xml = glob.glob(carpeta_archivos + "/*.xml")

contador = 0

if len(archivos_pdf) != len(archivos_xml):
    print("La cantidad de archivos PDF y XML no coincide.")
else:
    for i in range(len(archivos_pdf)):
        pdf = archivos_pdf[i]
        xml = archivos_xml[i]

        nombre_pdf = os.path.splitext(os.path.basename(pdf))[0]

        destinatario = "correo" #aqui pones el correo del distanatario
        asunto = f"NORDIGESA - Envio automatico de comprobante electronico: {nombre_pdf}"
        cuerpo = f"Estimado cliente, se adjunta documento electrónico {nombre_pdf}, en formato PDF Y XML"

        adjuntos = [pdf, xml]
        enviar_correo(destinatario, asunto, cuerpo, adjuntos)
        contador += 1  # Incrementar el contador cada vez que se envíe un correo

print(f"Se enviaron {contador} correos.")
