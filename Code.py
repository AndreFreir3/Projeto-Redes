#biblioteca do protocolo de transferência de e-mail
import smtplib 

#para criar o servidor e enviar o e-mail

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

#STARTAR o servidor SMTP

host = "smtp.gmail.com"
port = "587"
login = "grupoone060@gmail.com"
senha = "p1234q567"

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(login,senha)

# Construir o e-mail tipo mime (montando o e-mail)

corpo_email = "teste de implementação do protocolo SMTP"
email_msg = MIMEMultipart()
email_msg['From'] = "login"
email_msg['To'] = "login"
email_msg['Subject'] = " Meu email teste "
email_msg.attach(MIMEText(corpo_email,'plain'))

#enviar o e-mail do tipo mime pelo SMTP

server.sendmail(login, login , email_msg.as_string())

# encerrando a conexão com o servidor

server.quit()
