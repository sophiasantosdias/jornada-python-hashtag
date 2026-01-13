# Passo a Passo do seu programa
from time import sleep
import pyautogui
import pandas

# Mudando a configuração do PyAutoGui
pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'emailsuperoriginalediferente@gmail.com'
senha = '102938475600'

# Passo 1: Entrar no sistema da empresa
# 1.1: Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(5)
# 1.2: Entrar no site
pyautogui.write(link)
pyautogui.press('enter')
# Pausa para o site carregar
sleep(5)

# Passo 2: Fazer login
# 2.1: Selecionar o campo de E-mail
pyautogui.press('tab')
# 2.2: Digitar o email
pyautogui.write(email)
# 2.3: Mudar para o campo de senha
pyautogui.press('tab')
# 2.4: Preencher senha
pyautogui.write(senha)
# 2.5: Enviar formulário
pyautogui.press('tab')
pyautogui.press('enter')
# Pausa para o site carregar
sleep(5)

# Passo 3: Abrir a base de dados
tabela = pandas.read_csv('dia-1/produtos.csv')

# Passo 5: Repetir o Passo 4 até acabar a lista de produtos
for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    # 4.1: Campo de Código
    pyautogui.click(x=622, y=320)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    # 4.2: Campo de Marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    # 4.3: Campo de Tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    # 4.4: Campo de Categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    # 4.5: Campo de Preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    # 4.6: Campo de Custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    # 4.7: Campo de OBS
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    # 4.8: Enviar
    pyautogui.press('enter') 

    # 4.9: Voltar ao início
    pyautogui.scroll(5000)


