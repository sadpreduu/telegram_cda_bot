
import logging
from shutil import register_unpack_format
from tkinter.messagebox import NO

from telegram import Update
from telegram.ext import * 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import Constants as keys 

import mysql.connector as mariadb

import Response as CDB

#isso aqui era uma tentaiva de puxar os dados direto de um banco, ainda funciona mas os dados eles vem se formatação
mariadb_connection = mariadb.connect(user='root', password='zbnlk007', database ='cda1', host ='localhost', port =3306)

create_cursor = mariadb_connection.cursor()
comando_sql = 'SELECT * from cliente'
create_cursor.execute(comando_sql)
retorno = create_cursor.fetchall()

# Enable logging, faz a inicialização passando os dados
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO 
) #Isso serve como um sinal de vida do bot e mostra pra gente no terminal o status dele.

logger = logging.getLogger(__name__)

command_list = """ 

Lista dos Comandos Programados
/help - obtenha a lista dos comandos
/clientes - obtenha os dados de todos os clientes 
/cliente <cliente_id> - obtenha o dados de um cliente
/total - obtenha o valor de todas as vendas referente a ultimo mês

"""
#uma 'list'/arary simples pra poder enviar como resosta uma tabela com os clientes existentes
table_clientes = [
['ID_CLIENTE | NOME_CLIENTE'], 
["21856 | Jar Jar Binks"], 
["39550 | R2D2"], 
["44993 | C-3PO"],
["49400 | Jabba the Hutt"]
]

#essa função ela serve pra montar uma tabela fora do comando, basicamente ela monta e aguarda a ativação dentro do comando. 
def load_table(table_clientes) -> None:
    
    output = ""
    for item in table_clientes[0]:
        output += "| " + str(item) + " |"

        output += "\n"    
    
    for item in table_clientes[1:]:
        for table_dados in item:
            output += "\n" + "| " + str(table_dados) + " |"

  
    #table_clientes = [['090, SadBoy'], ['069, Thanso'], ['000, zValdinei']]
    return output 

table_vendas = ['121.433,76'] #array vergonhosa de venda com 1 total apenas kkkkk 
#por algum motivo eu não tava conseguindo passar o valor junto com texto no bot ent eu tive que transformar em str pra ele passar
total_vendas = table_vendas[0]

def start(update: Update, context: CallbackContext) -> None: #primeiro comando, Greeting e Get Started basicamente
    
    update.message.reply_text('Olá! Tudo bom? Vamo trabalhar\n /help para ver comandos.')

def help(update: Update, context: CallbackContext) -> None: #bem básico aqui ele só mostra a string que eu fiz no inicio
    
    update.message.reply_text(command_list)    

def clientes(update: Update, context: CallbackContext) -> None: #segunda função, essa ela roda a outra função feita lá em cima

    #text = str(update.message.text)
    response = load_table(table_clientes)

    update.message.reply_text('TABLEA DOS CLIENTES CADASTRADOS:')
    update.message.reply_text(response)  
    
    
#Scrap, isso foi uma tentativa de fazer uma busca por cliente simples mas eu não consegui fazer
#um reading da mensagem e usar ela como parametro pra fazer uma busca dentro de uma array
def cliente(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text("Digite em seguida o ID_Cliente, caso não saiba o id basta /clientes.")

def total(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text("Valor da venda do mês: R$" + total_vendas)   

def handle_cliente(update, context):
    text = str(update.message.text)
    response = CDB.search_sample(text)

    update.message.reply_text(response)     

#função que inicia o bot e ativa os receptores
def main():
    
    updater = Updater(keys.API_KEY, use_context=True)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("total", total))
    dispatcher.add_handler(CommandHandler("clientes", clientes))
    dispatcher.add_handler(CommandHandler("cliente", cliente))   

    dispatcher.add_handler(MessageHandler(Filters.text, handle_cliente)) 


    updater.start_polling()
    updater.idle()

main()    