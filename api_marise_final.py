from operator import truediv
from re import A
from shutil import disk_usage
from turtle import title
from dashing import HSplit, VSplit, VGauge, HGauge
from psutil import (
    virtual_memory,
    disk_usage,
     cpu_percent
)

from time import sleep



while True:
    print("Analise de dados da maquina" + '\n' + '\n')

    print("Escolha um dado para ser analisado: " + "\n" + "\n" +
    "[0] Ver Uso da memória RAM" + "\n" + "[1] Ver Uso da Memória de disco" + "\n" + "[2] Ver uso da CPU" + "[3] Sair")

    escolha = input("Resposta: ")
    
    if escolha == '0':
                dash = HSplit(
            HSplit(
                HGauge(title='Ram'),
                title='memória',
                border_color=3
                ),
                VSplit(
                    HGauge(),
                    title='DISCO',
                        border_color=5,
                ),
            )
                while True:
                    mem_dash= dash.items[0]

                    #memoria RAM
                    ram_dash = dash.items[0].items[0]
                    ram_dash= mem_dash.items[0]
                    ram_dash.value = virtual_memory().percent
                    ram_dash.title = f'RAM {ram_dash.value}%'

                    try:
                        dash.display()
                        sleep(.5)
                    except KeyboardInterrupt:
                        break 
    
    elif escolha == '1':
        dash = VSplit(
            HGauge(),
            title='DISCO',
                border_color=5,
        ),
        
        while True:
            disc_dash = dash.items[0]

            #Memoria DISCO
            disc_percent_dash = disc_dash.items[0]
            disc_use = disk_usage('/')
            disc_percent_dash.value = disc_use
            disc_percent_dash.title = f'DISCO {disc_use}%'

            try:
                dash.display()
                sleep(.5)
            except KeyboardInterrupt:
                break
     
    elif escolha == '2':
        dash = VSplit(
            HGauge(),
            title='CPU',
                border_color=6,
        ),

        while True:
            cpu_dash = dash.items[0]

            #Memoria CPU
            cpu_percent_dash = cpu_dash.items[0]
            cpu_use = cpu_percent()
            cpu_percent_dash.value = cpu_use
            cpu_percent_dash.title = f'cpu {cpu_use}%'

            try:
                dash.display()
                sleep(.5)
            except KeyboardInterrupt:
                break



        

            


            