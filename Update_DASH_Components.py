#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# DASH
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

def Update_DASH_Components(path_2_pngs_roi, path_2_pngs_amap):
    
    sesList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    
    AMAP_carrusel_updated = []
    ROI_carrusel_updated = []
    checklist_updated = []
    init_val = []
    count_of_slides_per_session = []
    run_list = []
    
    # COMPUTE ROIS 
    for ses in sesList:
        path_to_png = f"{path_2_pngs_roi}/ses-{ses}"

        ROI_items = []
        user_options = []
        for_init_val= []
        user_option_value = 0
        for_run_list = []
        
        if os.path.exists(path_to_png):
            for png in sorted(os.listdir(path_to_png)):
                split_filename = png.split("_")
                run = split_filename[2]
                for_run_list.append(run)
                
                full_path = f"{path_to_png}/{png}"

                # GET THE ITEMS PARAMETER PER RUN

                if int(run[4:]) < 10:
                    ROI_items.append({"src": f"{full_path}", "img_style": {"max-height": "500px"}},) #"key": f"{run[5:]}", 
                    user_options.append({"label": f"{run}", "value": user_option_value},)
                    for_init_val.append(0)
                    user_option_value += 1
                    
                elif int(run[4:]) >= 10:
                    ROI_items.append({"src": f"{full_path}", "img_style": {"max-height": "500px"}},) #"key": f"{run[4:]}", 
                    user_options.append({"label": f"{run}", "value": user_option_value},)
                    for_init_val.append(0)
                    user_option_value += 1
        else:
            nodata_img_path = f"assets/nodataAvailablev3.png"
            ROI_items.append({"src": f"{nodata_img_path}", "img_style": {"max-height": "500px"}},) #"key": 1, 
            for_init_val.append(None)
   
        ROI_carrusel_updated.append(ROI_items)
        checklist_updated.append(user_options)
        init_val.append(for_init_val[0])
        count_of_slides_per_session.append(user_option_value)
        run_list.append(for_run_list)
        
    # COMPUTE AMAPS 
    for ses in sesList:
        AMAP_items = []
        path_to_png = f"{path_2_pngs_amap}/ses-{ses}"
        if os.path.exists(path_to_png):
            for png in sorted(os.listdir(path_to_png)):
                split_filename = png.split("_")
                run = split_filename[2]

                full_path = f"{path_to_png}/{png}"

                # GET THE ITEMS PARAMETER PER RUN
                if int(run[4:]) < 10:
                    AMAP_items.append({"src": f"{full_path}", "img_style": {"max-height": "500px"}},) #"key": f"{run[5:]}", 

                elif int(run[4:]) >= 10:
                    AMAP_items.append({"src": f"{full_path}", "img_style": {"max-height": "500px"}},) #"key": f"{run[4:]}", 
        else:
            current_ses_idx = sesList.index(ses)
            if count_of_slides_per_session[current_ses_idx] > 0:
                for slide_counted in range(0, count_of_slides_per_session[current_ses_idx]):
                    nodata_img_path = f"assets/nodataAvailablev3.png"
                    AMAP_items.append({"src": f"{nodata_img_path}", "img_style": {"max-height": "500px"}},) #"key": 1, 
            elif count_of_slides_per_session[current_ses_idx] == 0:
                    nodata_img_path = f"assets/nodataAvailablev3.png"
                    AMAP_items.append({"src": f"{nodata_img_path}", "img_style": {"max-height": "500px"}},)

        AMAP_carrusel_updated.append(AMAP_items)
        
    return (ROI_carrusel_updated, AMAP_carrusel_updated, checklist_updated, init_val, run_list)
    

