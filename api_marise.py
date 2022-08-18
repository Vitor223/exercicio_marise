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