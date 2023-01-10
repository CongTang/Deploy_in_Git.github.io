import panel as pn
pn.extension(notifications=True)

import pandas as pd

file_input = pn.widgets.FileInput()
update = pn.widgets.Button(name= 'check',button_type = 'success')
table = pn.widgets.Tabulator()
def update_click(event):
    if file_input.value != None:
        try:
            pn.state.notifications.info('reading')
            table.value = pd.read_excel(file_input.value)
            pn.state.notifications.clear()
            pn.state.notifications.success('successful')
        except Exception as e:
            pn.state.notifications.clear()
            pn.state.notifications.warning(f'{e}')
    else:
        pn.state.notifications.clear()
        pn.state.notifications.warning(f'No File')        
update.on_click(update_click)
        
pn.Column(
    pn.Row(
    file_input,update
    ),
    table
).servable();
