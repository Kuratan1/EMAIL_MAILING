from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import configparser

def envia_email(file, filenamee, mail_content, subject, username, password, destiny, Cc):

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = destiny
    msg['Cc'] =  Cc
    msg['Subject'] = subject
    server = smtplib.SMTP('smtp.office365.com',587)

    msg.attach(MIMEText(mail_content,'plain'))
    fp = open(file, 'rb')
    part = MIMEBase('application','vnd.ms-excel')
    part.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(part)
    part.add_header('content-disposition', 'attachment', filename = filenamee)
    msg.attach(part)
    smtp = smtplib.SMTP('smtp.office365.com',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(username, destiny.split(',') + msg['Cc'].split(','), msg.as_string())
    smtp.quit()

def load_config():
    config = configparser.ConfigParser()
    config.read("configmailing.ini")
    return config


config = load_config()

user = config['ftp']['username']
passwd = config['ftp']['password']
subject = config['subject']['subject']

file_path = config['path_file']['simtech']
filename = config["filename"]["simtech"]    
mail_content = config['mail_content']['simtech']
dest = config["dest"]["simtech"]
Cc = config['Cc']['simtech']
envia_email(file_path,filename,mail_content,subject,user,passwd,dest,Cc)

file_path = config['path_file']['nucleoant']
filename = config["filename"]["nucleoant"]    
mail_content = config['mail_content']['nucleoant']
dest = config["dest"]["nucleoant"]
Cc = config['Cc']['nucleoant']
envia_email(file_path,filename,mail_content,subject,user,passwd,dest,Cc)


