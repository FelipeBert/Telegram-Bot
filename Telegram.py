# Instalação: pip install pytelegrambotapi
# Link Telegram: http://t.me/bertulininho_bot

import telebot
import pandas as pd

CHAVE_API = "6227139496:AAF4GJm87Sxep8-DO85OTOp7pwEgg9XinNU"

bot = telebot.TeleBot(CHAVE_API)

df = pd.read_csv("dados_uf.csv")

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

    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["admin"])
def admin(mensagem):
    texto = """

    """
    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
        return True
@bot.message_handler(func=verificar)
def resposta(mensagem):
    texto = """
    Escolha uma opção para continuar:
    /opcao1 Consultar Grade
    /opcao2 Consultar Bolsas
    Clique em uma das 3 opções
    """
    bot.send_message(mensagem.chat.id, texto)

bot.polling()