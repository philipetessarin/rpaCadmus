import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

class EnviarEmail:
    def __init__(self):
        pass

    def envio(self):
        self.host = "smtp.gmail.com"
        self.porta = "587"
        self.login = "rpa.cadmus@gmail.com"
        self.senha = "Rpa2022!@"

        self.servidor = smtplib.SMTP(self.host, self.porta)

        self.servidor.ehlo()
        self.servidor.starttls()
        self.servidor.login(self.login, self.senha)

        self.data = date.today().strftime("%d/%m/%Y")

        self.mensagem = f"Segue em anexo a planilha com as vagas em aberto do dia {self.data}."

        self.email_msg = MIMEMultipart()
        self.email_msg['From'] = self.login
        self.email_msg['To'] = self.login
        self.email_msg['Subject'] = f"Vagas em aberto do dia {self.data}"
        self.email_msg.attach(MIMEText(self.mensagem, 'plain'))

        self.caminho_arquivo = "./Vagas_Cadmus.xlsx"
        self.anexo = open(self.caminho_arquivo, 'rb')

        self.anexar = MIMEBase('application', 'octet-stream')
        self.anexar.set_payload(self.anexo.read())
        encoders.encode_base64(self.anexar)

        self.anexar.add_header('Content-Disposition', f'anexo; filename=Vagas_Cadmus.xlsx')
        self.anexo.close()

        self.email_msg.attach(self.anexar)

        self.servidor.sendmail(self.email_msg['From'], self.email_msg['To'], self.email_msg.as_string())
        self.servidor.quit()

if __name__ == '__main__':
    email = EnviarEmail()









