import numpy as np
import cv2 as cv

import panel as pn
import holoviews as hv
from holoviews import opts

from PIL import Image
import io
pn.extension()
hv.extension('bokeh')
pn.extension(sizing_mode = 'stretch_width')
info = pn.pane.HTML("""
<center>This is a exmaple code of online canny edge detection<br>
The Website this power by hololiz panel and host by heroku(or google cloud).<br>
The Canny edge detection is power by opencv</center>
""",style = {'font-size':'20px'})


int_range_slider = pn.widgets.IntRangeSlider(
    name='Lower and Upper Threshold ',
    start=0, end=1000, value=(150, 255), step=10)
selector = pn.widgets.Select(options = ['gray','PiYG','flag','Set1'])
L2gradient = pn.widgets.Toggle(name='L2gradient', button_type='success')


file_input = pn.widgets.FileInput(accept='.png,.jpg')
#update = pn.widgets.Button(name= 'check',button_type = 'success')


@pn.depends(int_range_slider,selector,L2gradient,file_input)
def plot_img(intrange,selector,L2gradient,file_input):
    if file_input == None:
        img = cv.imread('img.png')
    else:
        try:
            img = np.array(Image.open(io.BytesIO(file_input)).convert('RGB') ) 
            
        except Exception as e:
            print(f'read failed{e}')
    edges = cv.Canny(img,intrange[0],intrange[1],L2gradient  = L2gradient)
    return hv.Image(img).opts(cmap = selector)+hv.Image(edges).opts(cmap = selector)
    
app = pn.Row(
    pn.Spacer(height  = 1)
    ,
    pn.Column(
        info,
        file_input,
        int_range_slider,
        pn.Row(
            selector,
            L2gradient
        ),
        pn.Row(plot_img)
    )
    ,
    pn.Spacer(height  = 1)
)
bootstrap = pn.template.BootstrapTemplate(title='Canny Edge Decetion online with python Demo')
bootstrap.main.append(app)
bootstrap.servable();
