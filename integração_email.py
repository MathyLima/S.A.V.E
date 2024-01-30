import imaplib
import email
import re
import webbrowser

def get_email_remetentes(login, senha, num_mensagens=10):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(login, senha)
    # Selecionar caixa de entrada
    mail.select("inbox")

    _, messages = mail.search(None, 'UNSEEN')
    message_ids = messages[0].split()
    remetentes = []
    ids = []
    
    for message_id in message_ids[-num_mensagens:]:
        _, msg_data = mail.fetch(message_id, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        sender_address = msg.get("From")
        message_id_str = message_id.decode("utf-8",errors='ignore')  # Decodificando bytes para string
        remetentes.append(sender_address)
        ids.append(message_id_str)
        
    return remetentes, ids

def extract_email_address(login, senha, num_mensagens=10):
    full_strings = get_email_remetentes(login, senha, num_mensagens)[0]
    pattern = r'<([^>]+)>'
    mail_boxes = []
    id = get_email_remetentes(login, senha, num_mensagens)[1]
    for mail in full_strings:
        match = re.search(pattern, mail)
        if match:
            mail_boxes.append(match.group(1))
    return mail_boxes,id

def open_email_link():
    email_link = f"https://mail.google.com/mail/u/0/#inbox/"
    webbrowser.open(email_link)




