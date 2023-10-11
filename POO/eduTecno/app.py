import json

class Email:
    from2 = []
    subject = None
    body = None

    def changeSubject(self, subjct: str) -> None:
        self.subject = subjct

    def changeBody(self, body: str) -> None:
        self.body = body


class Gmail:
    name = 'Gemail'
    

class Hotmail:
    name = 'Hotmail'
    
    
class EmailManagment:
    emailProvider = None
    
    def send(self, to: list, text: str)->int:
        emails = ",".join(to)
        print("Email para: {} con texto: {} con el proveeder de email : {}".format(emails, text, self.emailProvider.name))
        return 0
    
    def checkbox(self)->dict:
        emails = []
        emailTmp = Email()
        emailTmp.from2 = ["email1@gmail.com", "email2@gmail.com"]
        emailTmp.changeSubject('subject1')
        emailTmp.changeBody("Saludos para todos")
        emails.append(emailTmp)
        
        emailTmp = Email()
        emailTmp.from2 = ["email2@gmail.com", "email2@gmail.com"]
        emailTmp.changeSubject('subject2')
        emailTmp.changeBody("Saludos para todos")
        emails.append(emailTmp)
        
        emailTmp = Email()
        emailTmp.from2 = ["email3@gmail.com", "email2@gmail.com"]
        emailTmp.changeSubject('subject3')
        emailTmp.changeBody("Saludos para todos")
        emails.append(emailTmp)
     
        return emails
    
    
emailManagment = EmailManagment()
emailManagment.emailProvider = Hotmail()

emails = emailManagment.checkbox()

print(json.dumps(emails, default= lambda obj : obj.__dict__, sort_keys=True, indent=4))

resultado = emailManagment.send(["email1@hotmail.com", "email2@gmail.com"], 'Saludos !!!')

print("\n\nResultados : {resultado}\n")