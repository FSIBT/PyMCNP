# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:49:08 2021

@author: mauricio
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, TextBox, Button
from mcnptools import transformations as tr
from mcnptools import mcnpio as io

class Geometry:
    def __init__(self, color, name, h_menu, soil=False, fig=None, ax_3d=None,
                 ax_menu=None):
        # initialize figure
        self.color = color
        self.name = name
        self.soil = soil
        self.fig = fig
        self.ax_3d = ax_3d
        self.ax_menu = ax_menu
        self.object = None
        
        ## rotation sliders
        if soil == False:
            axcolor = 'lightgoldenrodyellow'
            # X-rotation
            # h_menu = 0.89
            self.ax_rotx = plt.axes([0.77, h_menu, 0.2, 0.03],
                                    facecolor=axcolor)
            self.s_rotx = Slider(self.ax_rotx, "Rotation-x", 0, 360,
                            valinit=0, valfmt="%1d")
            self.ax_rotx.set_title(name, color=self.color)
            # Y-rotation
            self.ax_roty = plt.axes([0.77, h_menu-0.05, 0.2, 0.03],
                                    facecolor=axcolor)
            self.s_roty = Slider(self.ax_roty, "Rotation-y", 0, 360,
                            valinit=0, valfmt="%1d")
            # Z-rotation
            self.ax_rotz = plt.axes([0.77, h_menu-2*0.05, 0.2, 0.03],
                                    facecolor=axcolor)
            self.s_rotz = Slider(self.ax_rotz, "Rotation-z", 0, 360,
                            valinit=0, valfmt="%1d")
            
            ## translation text boxes
            self.ax_box1 = plt.axes([0.77, h_menu-3*0.05, 0.04, 0.03])
            self.text_box1 = TextBox(self.ax_box1, "X-tr", initial="0",
                                color="lightblue")
            
            self.ax_box2 = plt.axes([0.85, h_menu-3*0.05, 0.04, 0.03])
            self.text_box2 = TextBox(self.ax_box2, "Y-tr", initial="0",
                                color="lightblue")
            
            self.ax_box3 = plt.axes([0.93, h_menu-3*0.05, 0.04, 0.03])
            self.text_box3 = TextBox(self.ax_box3, "Z-tr", initial="0",
                                color="lightblue")
            
        else: 
            # write to MCNP
            self.ax_bmcnp = plt.axes([0.88, 0.05, 0.1, 0.05],
                                      facecolor="lightgreen")
            self.bmcnp = Button(self.ax_bmcnp, "write to MCNP",
                                color="lightgreen",
                                hovercolor="lightblue")

        self.xlm = self.ax_3d.get_xlim()
        self.ylm = self.ax_3d.get_ylim()
        self.zlm = self.ax_3d.get_zlim()
        
        
        
    def make_object(self, x0, y0, z0, height, radius, axis):
        self.object = tr.Transformation()
        self.object.make_cylinder(x0=x0, y0=y0, z0=z0, height=height,
                                  radius=radius, axis=axis)
        if self.soil:
            self.object.plot_surf(self.ax_3d, color=self.color,
                                  soil=True, plot_axes=True)
        else: 
            self.object.plot_surf(self.ax_3d, color=self.color)
            
    def reset_matrix(self):
        self.object.mcnp = np.array([[1,0,0], [0,1,0], [0,0,1]])
            


        
class Transform:
    def __init__(self, file_path, geom_lst):
        self.geom_lst = geom_lst
        self.file_path = file_path
        # commands
        for g in geom_lst:
            if g.soil == False:
                # sliders
                #self.g = g
                g.s_rotx.on_changed(self.update)
                g.s_roty.on_changed(self.update)
                g.s_rotz.on_changed(self.update)
                # text box
                g.text_box1.on_submit(self.submit_xtrans)
                g.text_box2.on_submit(self.submit_ytrans)
                g.text_box3.on_submit(self.submit_ztrans)
            else:
                g.bmcnp.on_clicked(self.write_mcnp)
    
    def keep_zoom(self):
        g = self.geom_lst[0] # usually the soil
        xlm = g.ax_3d.get_xlim()
        ylm = g.ax_3d.get_ylim()
        zlm = g.ax_3d.get_zlim()
        g.ax_3d.clear()
        g.ax_3d.set_xlim(left=xlm[0], right=xlm[1])
        g.ax_3d.set_ylim(bottom=ylm[0], top=ylm[1])
        g.ax_3d.set_zlim(bottom=zlm[0], top=zlm[1])
        
        
    def update(self, val):
        for g in self.geom_lst:
            if g.soil == False:     
                xval = g.s_rotx.val
                yval = g.s_roty.val
                zval = g.s_rotz.val
                trans = g.object.trans
                g.object.make_transformation(alpha=xval, beta=yval,
                                                  gamma=zval, trans=trans)
            
                
        self.keep_zoom()
        for g in self.geom_lst:
            if g.soil:
                g.object.plot_surf(g.ax_3d, color=g.color, soil=True,
                                plot_axes=True)    
            else:
                g.object.plot_surf(g.ax_3d, color=g.color)      
            g.fig.canvas.draw_idle()

    def submit_xtrans(self, text):
        for g in self.geom_lst:
            if g.soil == False:
                xtrans = eval(g.text_box1.text)
                trans = g.object.trans
                trans[0] = xtrans
                g.object.make_transformation(alpha=g.object.alpha,
                                                  beta=g.object.beta,
                                                  gamma=g.object.gamma,
                                                  trans=trans)
        self.keep_zoom()
        for g in self.geom_lst:
            if g.soil:
                g.object.plot_surf(g.ax_3d, color=g.color,
                                    soil=True, plot_axes=True)
            else: 
                g.object.plot_surf(g.ax_3d, color=g.color)
        g.fig.canvas.draw_idle()

    def submit_ytrans(self, text):
        for g in self.geom_lst:
            if g.soil == False:
                ytrans = eval(g.text_box2.text)
                trans = g.object.trans
                trans[1] = ytrans
                g.object.make_transformation(alpha=g.object.alpha,
                                          beta=g.object.beta,
                                          gamma=g.object.gamma,
                                          trans=trans)
        self.keep_zoom()
        for g in self.geom_lst:
            if g.soil:
                g.object.plot_surf(g.ax_3d, color=g.color,
                                    soil=True, plot_axes=True)
        else: 
            g.object.plot_surf(g.ax_3d, color=g.color)
        
        g.fig.canvas.draw_idle()

    def submit_ztrans(self, text):
        for g in self.geom_lst:
            if g.soil == False:
                ztrans = eval(g.text_box3.text)
                trans = g.object.trans
                trans[2] = ztrans
                g.object.make_transformation(alpha=g.object.alpha,
                                                  beta=g.object.beta,
                                                  gamma=g.object.gamma,
                                                  trans=trans)
        self.keep_zoom()
        for g in self.geom_lst:
            if g.soil:
                g.object.plot_surf(g.ax_3d, color=g.color,
                                    soil=True, plot_axes=True)
            else:
                g.object.plot_surf(g.ax_3d, color=g.color)
        g.fig.canvas.draw_idle()
        
    def write_mcnp(self, event):
        Rmatrices = []
        translations = []
        for g in self.geom_lst:
            if g.soil == False:
                m = g.object.mcnp
                m2 = str(m.flatten())[1:-1]
                m2 = " ".join(m2.split())
                Rmatrices.append(m2)
                t = np.array(g.object.trans)
                t2 = str(t)[1:-1]
                t2 = " ".join(t2.split())
                translations.append(t2)
        idx, num = io.read_inp_TR(self.file_path)
        with open(self.file_path, "r") as myfile:
            file = myfile.readlines()
        
        for n, i in enumerate(idx):
            file[i] = f"TR{num[n]} {translations[n]} {Rmatrices[n]}\n"
        
        with open(self.file_path, "w") as myfile:
            myfile.writelines(file)
