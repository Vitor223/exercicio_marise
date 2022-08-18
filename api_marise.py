from shutil import disk_usage
from turtle import title
from dashing import HSplit, VSplit, VGauge, HGauge
from psutil import (
    virtual_memory,
    disk_usage,
     cpu_percent
)

from time import sleep

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
        VSplit(
            HGauge(),
            title='CPU',
                border_color=6,
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


    #Memoria CPU
    cpu_dash = dash.items[2]
    cpu_percent_dash = dash.items[0]
    cpu_use = cpu_percent()
    cpu_percent_dash.value = cpu_use
    cpu_percent_dash.title = f'CPU {cpu_percent_dash.value}%'

    try:
        dash.display()
        sleep(.5)
    except KeyboardInterrupt:
        break    