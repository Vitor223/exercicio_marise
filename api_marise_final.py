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
    "[0] Ver os Graficos de memoria" + "\n" + "[1] Sair")

    escolha = input("Resposta: ")
    
    if escolha == '0':
                dash = HSplit(
    VSplit(
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

                    #DISCO

                    disc_dash = dash.items[1]
                    disc_percent_dash = disc_dash.items[0]
                    disc_use = disk_usage('/').percent
                    disc_percent_dash.value = disc_use
                    disc_percent_dash.title = f'DISCO {disc_use}%'


                

                    try:
                        dash.display()
                        sleep(.5)
                    except KeyboardInterrupt:
                        break  

    elif escolha == '1':
        break

print("\n" + "Volte sempre")