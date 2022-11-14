#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import numpy as np

# DASH
import dash
from dash import ctx
from dash import html, dcc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

# MY FUNCTIONS 
from DASH_png_feeder import DASH_png_feeder
from Update_DASH_Components import Update_DASH_Components

from datetime import datetime


# In[2]:


# CORE PATHS
subID = "sub-DZ17BH"
pngs_path_roi = f"assets/ROIs/{subID}"
pngs_path_amap = f"assets/actmaps/{subID}"

[ROI_carrusel,AMAP_carrusel, checklist, run_list] = DASH_png_feeder(pngs_path_roi,pngs_path_amap)


# In[3]:


sublist = ["sub-DZ17BH", "sub-ND73ZG", "sub-HP93SR", "sub-PL92SP", "sub-RG57AA"]

ROI_data4update = []
AMAP_data4update = []
CHECK_data4update = []
CHECK_init_val = []
RUN_lists = []
for sub in sublist:
    pngs_path_roi = f"assets/ROIs/{sub}"
    pngs_path_amap = f"assets/actmaps/{sub}"
    [updated_CarouRoi, updated_CarouAMAP,updated_checklist, init_val, run_List] = Update_DASH_Components(pngs_path_roi, pngs_path_amap)
    ROI_data4update.append(updated_CarouRoi)
    AMAP_data4update.append(updated_CarouAMAP)
    CHECK_data4update.append(updated_checklist)
    CHECK_init_val.append(init_val)
    RUN_lists.append(run_List)


# In[4]:


print(len(ROI_data4update[0]))


# In[5]:


subjects =  html.Div([dbc.RadioItems(options=[
                {"label": "sub-DZ17BH", "value": 1},
                {"label": "sub-ND73ZG", "value": 2},
                {"label": "sub-HP93SR", "value": 3},
                {"label": "sub-PL92SP", "value": 4},
                {"label": "sub-RG57AA", "value": 5}],

        id= "Subjects",
        value = 1,
        className="btn-group",
        inputClassName="btn-check",
        labelClassName="btn btn-outline-warning",
        labelCheckedClassName="active")],className="btn-group")


# In[23]:


app = Dash(__name__, update_title=None)
server = app.server

r = []
app.layout = html.Div([
    # HEADER
     dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('BRAIN PLASTICITY PROJECT - ROIs QC'),
                ])
            ], className='text-center')], width = 12),
        ], className='p-1 align-items-stretch'),
    
    # SUBJECT SWITCHER 
     dbc.Row([
        dbc.Col([
                subjects,
        ], width= {"size": 12, 'offset': 0 }),
    ], className='p-3 align-items-stretch text-center'),
    
    # SESSION 1 
    dbc.Row([dbc.Col([checklist[0],], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[0]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[0]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 2 
    dbc.Row([dbc.Col([checklist[1]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    
    # TEXT AREA
    dbc.Row([
        dbc.Col([
            dcc.Textarea(id="textBox", persistence = True, persistence_type = "session",
         style={'width': "13%", "height": "14%", "z-index": "1000", 
                "position":"fixed",
                "background-color": "rgba(0,0,0,0.5)",
                "color":"white",
                "left": "79%",
                "top":"77%",
                "resize": "vertical",
               }),
            ], ), 
        ]),
    
    # DOWNLOAD DATA BUTTON
    dbc.Row([
        dbc.Col([
            html.Button("Save QC Notes", id="btn-download-txt", className= "btn",
         style={'width': "13%", "height": "4%", "z-index": "1000", 
                "position":"fixed", 
                "left": "79%",
                "top":"92%",
                "color": "white",
               }),
            dcc.Download(id="download-text"),
            ]), 
        ]),
    
    # SESSION 2 
    dbc.Row([dbc.Col([AMAP_carrusel[1]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[1]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 3 
    dbc.Row([dbc.Col([checklist[2]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[2]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[2]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 4 
    dbc.Row([dbc.Col([checklist[3]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[3]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[3]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 5 
    dbc.Row([dbc.Col([checklist[4]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[4]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[4]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 6 
    dbc.Row([dbc.Col([checklist[5]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[5]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[5]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 7 
    dbc.Row([dbc.Col([checklist[6]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[6]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[6]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 8 
    dbc.Row([dbc.Col([checklist[7]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[7]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[7]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 9
    dbc.Row([dbc.Col([checklist[8]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[8]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[8]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 10
    dbc.Row([dbc.Col([checklist[9]], width= {"size": 12, 'offset':0})],className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[9]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[9]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 11
    dbc.Row([dbc.Col([checklist[10]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[10]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[10]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 12
    dbc.Row([dbc.Col([checklist[11]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[11]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[11]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 13
    dbc.Row([dbc.Col([checklist[12]], width= {"size": 12, 'offset':0})],className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[12]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[12]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 14
    dbc.Row([dbc.Col([checklist[13]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[13]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[13]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 15
    dbc.Row([dbc.Col([checklist[14]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[14]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[14]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 16
    dbc.Row([dbc.Col([checklist[15]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[15]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[15]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 17
    dbc.Row([dbc.Col([checklist[16]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[16]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[16]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 18
    dbc.Row([dbc.Col([checklist[17]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[17]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[17]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 19
    dbc.Row([dbc.Col([checklist[18]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[18]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[18]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),
    # SESSION 20
    dbc.Row([dbc.Col([checklist[19]], width= {"size": 12, 'offset':0})], className='align-items-stretch text-center'),
    dbc.Row([dbc.Col([AMAP_carrusel[19]], width= {"size": 6, 'offset':0}),
             dbc.Col([ROI_carrusel[19]], width= {"size": 6, 'offset':0})], className='p-3 align-items-stretch'),

])

@app.callback(
    Output({"type":"ses", "index":ALL},"options"),
    Output({"type":"ses", "index":ALL},"value"),
    Output({"type":"carousel_ROI", "index":ALL},"items"), 
    Output({"type":"carousel_AMAP", "index":ALL},"items"), 
    Input('Subjects', 'value'),
    prevent_initial_call=True
)

def update_subjectdata(subindex):
    return CHECK_data4update[subindex-1], CHECK_init_val[subindex-1], ROI_data4update[subindex-1], AMAP_data4update[subindex-1]


@app.callback(
    Output({"type":"carousel_ROI", "index":ALL},"active_index"), 
    Output({"type":"carousel_AMAP", "index":ALL},"active_index"), 
    Input({"type":"ses", "index":ALL},"value"),
    prevent_initial_call=True
)

def switch_carouselRun(run_chosen):
    return run_chosen, run_chosen

@app.callback(
    Output('textBox', "value"),
    Input({"type":"ses", "index":ALL},"value"),
    Input('Subjects', 'value'),
    State('textBox', 'value'),
)   

def update_textbox(run, subjindx, textbox):
    trig = dash.callback_context.triggered
    runTrigerred = ctx.args_grouping
    sesList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    subj = sublist[subjindx-1]
    text = str(textbox)
    
    if trig[0]['value'] == None:
        raise PreventUpdate
    else:
        for ses_run in runTrigerred[0]:
            if ses_run['value'] != None and ses_run["triggered"] == True:
                session = f"ses-{sesList[ses_run['id']['index'] - 1]}"
                run_chosen = RUN_lists[subjindx-1][ses_run['id']['index'] - 1][ses_run["value"]]

        s = f"[{subj}][{session}][{run_chosen}]: "
        k = str(text).split()

        if len(k) < 2:
            txt_update = s
        else:
            txt_update = f"{text} {s}"

    return txt_update
    

# GET CURRENT DATE AND TIME FOR FILENAME
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

@app.callback(
    Output("download-text", "data"),
    [Input("btn-download-txt", "n_clicks")],
    [State('textBox', 'value')],
    prevent_initial_call=True,
)
def func(n_clicks, text):
    return dict(content='\n{}'.format(text), filename=f"QC_BrainPlasticity_ROIs_{date_time}.txt")

if __name__ == '__main__':
    app.run_server(debug=True)
    
# In[ ]:




