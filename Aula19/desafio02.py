# Abre o URL no navegador padrão(apenas abre algum site)
# import webbrowser
#
# url = 'https://pudim.com.br/'
#
# try:
#     webbrowser.open(url)
#     print(f'Site Pudim está acessível!!')
# except Exception as e:
#     print('Site Pudim não está acessível no momento :(')


# Acessa o Site e confirma se esta acessivel ou não
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')