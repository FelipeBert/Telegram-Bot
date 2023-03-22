import telebot
import pandas as pd
from cripto import generate_keypair, encrypt, decrypt

CHAVE_API = "chave"

bot = telebot.TeleBot(CHAVE_API)

#df = pd.read_csv('dados_uf.csv')

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    /Grade Completa
    /Filtros
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Teste
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    Teste
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["adm"])
def adm(mensagem):
    p = valor de p
    q = valor de q
    public_key, private_key = generate_keypair(p, q)

    bot.send_message(mensagem.chat.id, "Digite a senha de admin: ")

    @bot.message_handler(func=lambda mensagem: True, content_types=['text'])
    def get_senha(mensagem):
        senha_criptografada = encrypt(public_key, mensagem.text.strip())
        bot.send_message(mensagem.chat.id, f"A senha criptografada é: {senha_criptografada}")
        bot.remove_message_handler(get_senha)
        bot.register_next_step_handler(mensagem, after_senha)

    bot.register_next_step_handler(mensagem, get_senha)

def after_senha(mensagem):
    # Aqui você pode inserir o código que deve ser executado após o usuário inserir a senha
    pass

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def resposta(mensagem):
    texto = """
    Escolha uma opção para continuar:
    /opcao1 Consultar Grade
    /opcao2 Consultar Bolsas
    /adm
    Clique em uma das 3 opções
    """
    bot.send_message(mensagem.chat.id, texto)

bot.polling()
