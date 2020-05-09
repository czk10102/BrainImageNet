import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
 
def send(address, attachment):
    fromaddr = 'brainimagenet@deepbrain.com'
    password = ''
    toaddrs = address
 
    content = 'Dear BrainImageNet user:\n\nThank you very much for your interest in our work. The online sex prediction has finished based on the brain imaging data you uploaded. Please check the attachment for the results. Note for the prediction results, 1: Male   0: Female (Prediction close to 1 means male).\n\nBest,\n\nThe BrainImageNet Team (The R-fMRI Lab http://rfmri.org)'
    textApart = MIMEText(content)
 
#         imageFile = '1.png'
#         imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
#         imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
#  
#         pdfFile = '算法设计与分析基础第3版PDF.pdf'
#         pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
#         pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    
 
    File = attachment
    attachApart = MIMEApplication(open(File, 'rb').read())
    attachApart.add_header('Content-Disposition', 'attachment', filename=File)
 
    m = MIMEMultipart()
    m.attach(textApart)
#         m.attach(imageApart)
#         m.attach(pdfApart)
    m.attach(attachApart)
    m['Subject'] = 'BrainImageNet: Sex Prediction Results'
 
    try:
        server = smtplib.SMTP('smtp.exmail.qq.com')
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:',e) 
# eaddress=['562853606@qq.com', 'changzk@deepbrain.com']
# attachment='transdoc.py'
# send(eaddress,attachment)
