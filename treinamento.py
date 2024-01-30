import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split



def returnClassifier(email):
    # Gerando dados fictícios, mas com uma estrutura esperada para e-mails importantes
    n = 0
    lista_emails = []
    for i in range(10000):
        if n == 0:
            lista_emails.append([f"exemplo{i}@ci.ufpb.br", 1])
            n += 1
        elif n == 1:
            lista_emails.append([f"exemplo{i}@academico.ufpb.br", 1])
            n += 1
        elif n == 2:
            lista_emails.append([f"exemplo{i}@algumacoisa.ufpb.br", 1])
            n += 1
        else:
            lista_emails.append([f"exemplo{i}@gmail.com.br", 0])
            n =0
        
    
    # Adicionando o novo e-mail à lista
    lista_emails.append([email, -1])  # O rótulo -1 é apenas um marcador para o novo e-mail
    # Converter a lista de e-mails em um array do NumPy
    lista_treinamento=[]
    for i in lista_emails:
        treinamento = i[0].split("@")
        lista_treinamento.append([treinamento[1],i[1]])
    matriz_emails = np.array(lista_treinamento, dtype=object)
    # Separar os dados em recursos (X) e rótulos (y)
    X_emails = matriz_emails[:, 0]
    y = matriz_emails[:, 1].astype(int)  # Convertendo para inteiros

    # Inicializar o vetorizador de texto
    vectorizer = CountVectorizer()
    # Transformar os endereços de e-mail em vetores numéricos
    X = vectorizer.fit_transform(X_emails).toarray()

    # Índice do novo e-mail na matriz
    indice_novo_email = len(matriz_emails) - 1


    # Inicializar o classificador de Árvore de Decisão
    clf = KNeighborsClassifier(n_neighbors=1)

    # Treinar o modelo
    clf.fit(X[:indice_novo_email], y[:indice_novo_email])

    # Fazer previsões para o novo e-mail
    novo_email = X[indice_novo_email].reshape(1, -1)  # Reshape para garantir que tenha o formato correto
    y_pred = clf.predict(novo_email)

    return y_pred

