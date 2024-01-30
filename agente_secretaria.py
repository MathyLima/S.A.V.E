from treinamento import returnClassifier
from integração_email import extract_email_address
from tkinter import Tk, Label,messagebox
class SecretariaGUI:
    def __init__(self, lista_emails, lista_senhas):
        self.emails = lista_emails
        self.senhas = lista_senhas
        self.emails_importantes = []
        self.current_email_index = 0

        self.root = Tk()
        self.root.withdraw()  # Esconde a janela principal
        self.label = Label(self.root, text="")
        self.label.pack()

        self.verifica_automatica()

    def verifica_emails(self):
        for n, email in enumerate(self.emails):
            self.emails_importantes = []  # Limpar a lista de e-mails importantes
            self.label.config(text=f"Verificando email {email}...")
            mails, ids = extract_email_address(email, self.senhas[n])
            for j, addres in enumerate(mails):
                classifier = returnClassifier(addres)
                if classifier == 1:
                    self.emails_importantes.append([addres, ids[j]])

            n_emails = len(self.emails_importantes)
            if n_emails > 0:
                remetentes = ", ".join([mail[0] for mail in self.emails_importantes])
                mensagem = f"Email {self.emails[n]} possui {n_emails} e-mails importantes. Remetentes: {remetentes}"
                self.label.config(text=mensagem)
                self.root.update()
                self.mostrar_pop_up(mensagem)
                
                
        #reinicia apos 5 minutos
        self.root.after(300000, self.verifica_automatica)


    def mostrar_pop_up(self, mensagem):
        messagebox.showinfo("E-mails Importantes Encontrados", mensagem)


    def verifica_automatica(self):
        self.verifica_emails()
        # self.root.after(60000, self.verifica_automatica)

    def run(self):
        self.root.mainloop()
