from email.mime.text import MIMEText
from pydoc import plain
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

mail_content='''ANY MESSAGE YOU WANT"
'''

file = 'ARCHIVEPATH.xlsx'
username='YOUREMAIL'
password='PASSWORD'
send_from = '...'
send_to = '...'
Cc = '...'

msg = MIMEMultipart()
msg['From'] = '...'
msg['To'] = '...'
msg['Cc'] = '...'
msg['Subject'] = '...'
server = smtplib.SMTP('SMTP.TEST',587)

msg.attach(MIMEText(mail_content,'plain'))
fp = open(file, 'rb')
part = MIMEBase('application','vnd.ms-excel')
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='ARCHIVE.xlsx')
msg.attach(part)
smtp = smtplib.SMTP('smtp.office365.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(username,password)
smtp.sendmail(send_from, send_to.split(',') + msg['Cc'].split(','), msg.as_string())
smtp.quit()



