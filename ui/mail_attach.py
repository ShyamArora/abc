import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import time



def mailsend(domain,body,subject):
    
   
    msg = MIMEMultipart()
    pwd = "Meon@1234"
    fromaddr ="stephen@meon.co.in"
    path = 'static/uploads/'

    '''for files in attachment_name:
        filename = files
        attachment = os.path.join(path,files)
        print(files,attachment)
        attachment = open(attachment, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)'''
    def login():
        if 'gmail.com' in domain:
            s = smtplib.SMTP('smtp.gmail.com', 587)
        else:
            
            s = smtplib.SMTP('mail.'+domain, 587)
        s.starttls()
        s.login(fromaddr,pwd)
        return s
    def mail(toaadr,s):
        #msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        #msg.attach(p)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
    s =login()
    toaddr = "mohitmeon@gmail.com"
   
    try :
        mail(toaddr.strip(),s)
        print("success")
    except:
        print("Failed")
        pass
    s.quit()
    return "your mail is sent to our person"
