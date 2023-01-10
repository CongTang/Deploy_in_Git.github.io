import panel as pn
pn.extension(notifications=True)

import pandas as pd


txt = pn.widgets.TextInput()
check = pn.widgets.Button(name= 'check',button_type = 'success')
add = pn.widgets.Button(name= 'add',button_type = 'success')

def check_click(event):
    df = pd.read_csv('user_list.csv')
    if txt.value in list(df['User']):
        pn.state.notifications.clear()
        pn.state.notifications.success('name checked successful')
    else:
        pn.state.notifications.clear()
        pn.state.notifications.warning('name checked failed.')
def add_click(event):
    df = pd.read_csv('user_list.csv')
    try:
        df.loc[len(df)] = txt.value
        pn.state.notifications.clear()
        pn.state.notifications.success('name added successful')
    except Exception as e:
        pn.state.notifications.clear()
        pn.state.notifications.warning(f'name checked failed./n{e}')
check.on_click(check_click)        
add.on_click(add_click) 
pn.Column(
    txt,
    pn.Row(
    check,add
    )
).servable();
