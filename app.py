import panel as pn
import numpy as np
import random
import pandas as pd
import datetime as dt
pn.extension(sizing_mode="stretch_width",notifications=True)




title = dt.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
button =pn.widgets.Button(name = 'save data')
def button_click(event):
    df = pd.DataFrame(np.random.randint(0,100,size=(50, 3))) # 生成50行3列的dataframe
    df.to_csv(f'{title}.csv')
    print('saved')
    pn.state.notifications.success('This is a success notification.')
button.on_click(button_click)

pn.Column(button).servable();
