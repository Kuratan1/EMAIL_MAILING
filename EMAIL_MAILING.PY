from email.mime.text import MIMEText
from pydoc import plain
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

mail_content='''Boa Tarde,
Segue em anexo o saldo dos clientes "Is Núcleo Antecipa"
'''

file = 'C:\\Users\\GUSTAVOK\\Desktop\\CLIENTES_ERROTECGOL.xlsx'
username='gustavo.kuratani@martins.com.br'
password='teamolu@45'
send_from = 'gustavo.kuratani@martins.com.br'
send_to = 'gustavo.kuratani@martins.com.br '
Cc = 'recipient'

msg = MIMEMultipart()
msg['From'] = 'gustavo.kuratani@martins.com.br'
msg['To'] = 'gustavo.kuratani@martins.com.br'
msg['Cc'] = ''
msg['Subject'] = 'MAILING TESTE'
server = smtplib.SMTP('smtp.office365.com',587)

msg.attach(MIMEText(mail_content,'plain'))
fp = open(file, 'rb')
part = MIMEBase('application','vnd.ms-excel')
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='CLIENTES_ERROTECGOL.xlsx')
msg.attach(part)
smtp = smtplib.SMTP('smtp.office365.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(username,password)
smtp.sendmail(send_from, send_to.split(',') + msg['Cc'].split(','), msg.as_string())
smtp.quit()



