# Nesse código:

# - Importamos as bibliotecas webbrowser e time.
# - Definimos uma função abrir_google_e_gmail() que abre as duas páginas.
# - Usamos webbrowser.open() para abrir a página do Google.
# - Aguardamos 2 segundos com time.sleep(2) para garantir que a página do Google seja carregada antes de abrir o Gmail.
# - Abrimos a página do Gmail.


import webbrowser
import time
def abrir_google_e_gmail():
    url_google = 'https://www.google.com'
    url_gmail = 'https://mail.google.com'
    
    webbrowser.open(url_google)
    time.sleep(2)
    webbrowser.open(url_gmail)

abrir_google_e_gmail()