import telebot
import pandas as pd
from cripto import generate_keypair, encrypt, decrypt

CHAVE_API = "chave"

bot = telebot.TeleBot(CHAVE_API)

public_key = chavinha
private_key = chavinha 2

df = pd.read_csv('arquivo_atualizado.csv')

@bot.message_handler(commands=["grade"])
def opcao1(mensagem):
    texto = """
    /Grade Completa
    /Filtros
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Filtros"])
def filtros(mensagem):
    texto = """
    /Professor
    /Grade
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Grade"])
def Grade(mensagem):
    bot.send_message(mensagem.chat.id, 'Digite a disciplina: ')

    @bot.message_handler(func=lambda mensagem: True, content_types=['text'])
    def get_grade(mensagem):
        for index, texto in df.iterrows():
            if mensagem.text.strip() in texto['cadeira']:
                 bot.send_message(mensagem.chat.id, texto['professor'])
                 bot.send_message(mensagem.chat.id, texto['horario'])
                 bot.send_message(mensagem.chat.id, texto['dias'])
                 bot.send_message(mensagem.chat.id, 'Digite algo para Prosseguir')
                 bot.register_next_step_handler(mensagem, after_grade)

    bot.register_next_step_handler(mensagem, get_grade)

def after_grade(mensagem):
    texto = """
        /Grade Novamente
        /Menu
        """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Bolsas"])
def Bolsas(mensagem):
    bot.send_message(mensagem.chat.id, 'Digite o Tipo de Bolsa: ')

    @bot.message_handler(func=lambda mensagem: True, content_types=['text'])
    def get_bolsa(mensagem):
        for index, texto in df.iterrows():
            if mensagem.text.strip() in texto['texto']:
                 bot.send_message(mensagem.chat.id, texto['titulo'])
                 bot.send_message(mensagem.chat.id, texto['data'])
                 bot.send_message(mensagem.chat.id, texto['texto'])
                 bot.send_message(mensagem.chat.id, texto['link'])
                 bot.send_message(mensagem.chat.id, 'Digite algo para Prosseguir')
                 bot.register_next_step_handler(mensagem, after_bolsa)

    bot.register_next_step_handler(mensagem, get_bolsa)

def after_bolsa(mensagem):
    texto = """
        /Bolsas Novamente
        /Menu
        """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Professor"])
def professor(mensagem):
    bot.send_message(mensagem.chat.id, 'Digite o Nome do Professor: ')

    @bot.message_handler(func=lambda mensagem: True, content_types=['text'])
    def get_professor(mensagem):
        for index, nome in df.iterrows():
            if mensagem.text.strip() == nome['professor']:
                bot.send_message(mensagem.chat.id, nome['cadeira'])
                bot.send_message(mensagem.chat.id, nome['horario'])
                bot.send_message(mensagem.chat.id, nome['dias'])
                bot.send_message(mensagem.chat.id, 'Digite algo para Prosseguir')
                bot.register_next_step_handler(mensagem, after_professor)

    bot.register_next_step_handler(mensagem, get_professor)


def after_professor(mensagem):
    texto = """
        /Professor Novamente
        /Menu
        """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["adm"])
def adm(mensagem):
    bot.send_message(mensagem.chat.id, "Digite a senha de admin: ")

    @bot.message_handler(func=lambda mensagem: True, content_types=['text'])
    def get_senha(mensagem):
        senha_criptografada = encrypt(public_key, mensagem.text.strip())
        if senha_criptografada == df['senha'][0]:
            bot.send_message(mensagem.chat.id, f"{senha_criptografada}")
            bot.register_next_step_handler(mensagem, after_senha)
        else:
            bot.send_message(mensagem.chat.id, "Senha Incorreta")
            Menu(mensagem)

    bot.register_next_step_handler(mensagem, get_senha)


def after_senha(mensagem):
    # Aqui você pode inserir o código que deve ser executado após o usuário inserir a senha
    bot.send_message(mensagem.chat.id, "teste")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def Menu(mensagem):
    texto = """
    Escolha uma opção para continuar:
    /grade
    /Bolsas
    /adm
    Clique em uma das 3 opções
    """
    bot.send_message(mensagem.chat.id, texto)


bot.polling()
