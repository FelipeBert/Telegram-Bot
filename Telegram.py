# Instalação: pip install pytelegrambotapi
# Link Telegram: http://t.me/bertulininho_bot

import telebot

CHAVE_API = "6227139496:AAF4GJm87Sxep8-DO85OTOp7pwEgg9XinNU"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["bolsa"])
def bolsa(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem todo mundo ta pobre aqui!")
    resposta(mensagem)

@bot.message_handler(commands=["matricula"])
def matricula(mensagem):
    bot.send_message(mensagem.chat.id, "200721...")
    resposta(mensagem)

@bot.message_handler(commands=["disciplinas"])
def disciplinas(mensagem):
    bot.send_message(mensagem.chat.id, "Ta Reprovado ja!, VAZA!")
    resposta(mensagem)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que gostaria de consultar:
    /bolsa
    /matricula
    /disciplinas
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Waldemar: @NetuhPires - Twitter")
    resposta(mensagem)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "kk ainda acha que vai ter aula de jaqueline")
    resposta(mensagem)

#isso é a logica de quando o messagen_handler deve ser executado
def verificar(mensagem):
        return True
@bot.message_handler(func=verificar)
def resposta(mensagem):
    texto = """
    Escolha uma opção para continuar:
    /opcao1 realizar consulta
    /opcao2 contato professores
    /opcao3 Jaqueline vai dar aula hj?
    Clique em uma das 3 opções
    """
    bot.send_message(mensagem.chat.id, texto)

bot.polling()