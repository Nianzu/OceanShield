from tkinter import *
from typing import MappingView
import data_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import functools
import tkintermapview
from PIL import Image, ImageTk
import time

colors = ["red", "green", "blue", "yellow", "orange"]
def clear_markers():
        for marker in marker_list:
            marker.delete()

def plot(item):
    map_widget.set_position(item[0], item[1])
    map_widget.set_zoom(6)
    clear_markers()
    marker_list.append(map_widget.set_marker(deg_x= item[0], deg_y= item[1], text="Waste Discovered"))
    canvas.draw()
    boatsInArea = data_handler.get_boats_in_area(item[0], item[1], item[2])
    ships = data_handler.get_boat_tracks(boatsInArea)
    selected_color = 0
    for ship in ships:
        
        for i in range(1, len(ship)):
            marker_2 = map_widget.set_marker(ship[i-1][0],ship[i-1][1])
            marker_3 = map_widget.set_marker(ship[i][0],ship[i][1])
            marker_list.append(map_widget.set_path([marker_2.position, marker_3.position], color = colors[selected_color]))
            marker_2.delete()
            marker_3.delete()
        marker_list.append(map_widget.set_marker(deg_x= ship[len(ship)-1][0], deg_y= ship[len(ship)-1][1], text="Ship"))
        selected_color += 1;
    load = Image.open(item[3])
    load = load.resize((int(640*0.6),int(480*0.6)),Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img.configure(image = render)
    img.image = render
    roverCoords2.config(text = str(item[0]) +", "+str(item[1]))
    eventClassification2.config(text = "Commercial waste")
    discoveryTime2.config(text = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item[2])))
    

# get ship positions from marinetracker
            #long   lat    time
locations=[[25.25, -122.25, 1664636729, "Trash1.png", "AUV - Baja California"],
           [25.22, -122.05, 1664636047, "Trash2.png", "AUV - Baja California"],
           [25.69, -122.20, 1664636481, "Trash3.png", "AUV - Baja California"],
           [25.46, -122.54, 1664636403, "Trash4.png", "AUV - Baja California"],
           [25.30, -122.79, 1664636779, "Trash5.png", "AUV - Baja California"],
           [25.47, -122.82, 1664636009, "Trash6.png", "AUV - Baja California"],
           [25.05, -122.45, 1664636466, "Trash7.png", "AUV - Baja California"],
           [25.97, -122.67, 1664636443, "Trash1.png", "AUV - Baja California"],
           [25.61, -122.38, 1664636175, "Trash2.png", "AUV - Baja California"],
           [25.03, -122.07, 1664636567, "Trash3.png", "AUV - Baja California"],
           
           [24.25, -84.25, 1664636729, "Trash1.png", "AUV - Gulf of Mexico"],
           [24.22, -84.05, 1664636047, "Trash2.png", "AUV - Gulf of Mexico"],
           [24.69, -84.20, 1664636481, "Trash3.png", "AUV - Gulf of Mexico"],
           [24.46, -84.54, 1664636403, "Trash4.png", "AUV - Gulf of Mexico"],
           [24.30, -84.79, 1664636779, "Trash5.png", "AUV - Gulf of Mexico"],
           [24.47, -84.82, 1664636009, "Trash6.png", "AUV - Gulf of Mexico"],
           [24.05, -84.45, 1664636466, "Trash7.png", "AUV - Gulf of Mexico"],
           [24.97, -84.67, 1664636443, "Trash4.png", "AUV - Gulf of Mexico"],
           [24.61, -84.38, 1664636175, "Trash5.png", "AUV - Gulf of Mexico"],
           [24.03, -84.07, 1664636567, "Trash6.png", "AUV - Gulf of Mexico"],
           
           [57.25, 7.25, 1664636729, "Trash1.png", "AUV - Scandinavia"],
           [57.22, 7.05, 1664636047, "Trash2.png", "AUV - Scandinavia"],
           [57.69, 7.20, 1664636481, "Trash3.png", "AUV - Scandinavia"],
           [57.46, 7.54, 1664636403, "Trash4.png", "AUV - Scandinavia"],
           [57.30, 7.79, 1664636779, "Trash5.png", "AUV - Scandinavia"],
           [57.47, 7.82, 1664636009, "Trash6.png", "AUV - Scandinavia"],
           [57.05, 7.45, 1664636466, "Trash7.png", "AUV - Scandinavia"],
           [57.97, 7.67, 1664636443, "Trash7.png", "AUV - Scandinavia"],
           [57.61, 7.38, 1664636175, "Trash1.png", "AUV - Scandinavia"],
           [57.03, 7.07, 1664636567, "Trash2.png", "AUV - Scandinavia"],]


marker_list = []
root = Tk()
p1 = PhotoImage(file = "Icon.png")
root.iconphoto(False, p1)
root.iconbitmap(default='Icon.ico')
root.title('Ocean Shield')
root.geometry("1700x600")
frame_container=Frame(root,width=20)
frame_map = Frame(root)

my_label = LabelFrame(root)
frame_data = Frame(root,width=20)
frame_container.pack(side = LEFT)
my_label.pack(pady=10,padx=10, side= LEFT)
frame_data.pack(side = LEFT)
canvas_container=Canvas(frame_container,height = 800)
frame2=Frame(canvas_container)
myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
canvas_container.create_window((0,0),window=frame2,anchor='nw')

for item in locations:
    button = Button(frame2,text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item[2])) + "\n" + item[4],width=30,height=4,command=functools.partial(plot,item))
    button.pack()

frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                            #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                            #width 0 because we only scroll verticaly so don't mind about the width.
canvas_container.pack(side=RIGHT)
myscrollbar.pack(side=LEFT, fill = Y)


# the figure that will contain the plot
fig = Figure(figsize = (5, 5), dpi = 100)

# list of squares
map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=800, corner_radius=10)
canvas = FigureCanvasTkAgg(fig, master = frame_map) 

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack(side=RIGHT, fill = BOTH)
map_widget.pack()

# creating the Tkinter canvas
# containing the Matplotlib figure

frame_data_img = Frame(frame_data)
frame_data_coord = Frame(frame_data)
frame_data_classification = Frame(frame_data)
frame_data_time = Frame(frame_data)
frame_data_img.pack(side=TOP)
frame_data_coord.pack(side=TOP)
frame_data_classification.pack(side=TOP)
frame_data_time.pack(side=TOP)

load = Image.open("trash1.png")
load = load.resize((int(640*0.6),int(480*0.6)),Image.Resampling.LANCZOS)
render = ImageTk.PhotoImage(load)
img = Label(frame_data_img, image=render)
img.image = render
img.pack(side=TOP)



roverCoords1 = Label(frame_data_coord,text="Event Co-Ordinates: ")
roverCoords1.pack(side=LEFT)
roverCoords2 = Label(frame_data_coord,text="roverCoords")
roverCoords2.pack(side=LEFT)

eventClassification1 = Label(frame_data_classification,text="Event classification:")
eventClassification1.pack(side=LEFT)
eventClassification2 = Label(frame_data_classification,text="eventClassification")
eventClassification2.pack(side=LEFT)

discoveryTime1 = Label(frame_data_time,text="Discovery time:")
discoveryTime1.pack(side=LEFT)
discoveryTime2 = Label(frame_data_time,text="discoveryTime")
discoveryTime2.pack(side=LEFT)

discoveryTime1 = Label(frame_data_time,text="Target ship name:")
discoveryTime1.pack(side=LEFT)
discoveryTime2 = Label(frame_data_time,text="discoveryTime")
discoveryTime2.pack(side=LEFT)


plot(locations[len(locations)-1])
# Front end
# needs list of time stamps and coord for trash found
# ship positions for each trash event

# select which trash event to plot

# draw map on screen centered around oil barel




mainloop()

# draw location of oil barrel

# draw a radius of possible drop locations (transparent)

# draw current location of all ships that were in the area in the past x time

# draw paths of ships