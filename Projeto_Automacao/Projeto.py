import webbrowser
import time
def abrir_google_e_gmail():
    url_google = 'https://www.google.com'
    url_gmail = 'https://mail.google.com'
    
    webbrowser.open(url_google)
    time.sleep(2)
    webbrowser.open(url_gmail)

abrir_google_e_gmail()