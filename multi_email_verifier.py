from verify_email_class import CheckEmail
import threading

emails = """yesheykamal.89@gmail.com
yesheykamal.889@gmail.com
02190138.cst@rub.edu.bt
02190139.cst@rub.edu.bt
02190138.cst@rub.edu.btt
02190150.cst@rub.edu.bt
02190150.cst@rub.eduuuu.bt
kazkkamal@gmail.com"""


emails = emails.split('\n')
# print(emails)

for email in emails:
    print('Verifying :', email, "====================")
    verifier = CheckEmail()
    try:
        t = threading.Thread(target=verifier.verify_email(email))
        t.start()
    except:
        print("Threading Exception")
    