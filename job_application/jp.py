import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email')
msg['Subject'] = 'Test Email'
msg['From'] = 'echendujosh@gmail.com'
msg['To'] = 'echendujosh@gmail.com'

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # Can help with some servers
        server.starttls()
        server.ehlo()  # Can help with some servers
        server.login('echendujosh@gmail.com', 'echendujosh@gmail.com')
        server.sendmail('echendujosh@gmail.com', ['echendujosh@gmail.com'], msg.as_string())
        print('Email sent successfully')
except Exception as e:
    print(f'Error: {e}')
