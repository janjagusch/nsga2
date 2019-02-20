import warnings
import pickle
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cv2 as cv
from scraping import scrape_player_img
import imageio


SLOT_HEIGHT = 0.2
SLOT_WIDTH = 0.1
PITCH_WIDTH = 30
PITCH_HEIGHT = 20
CIRCLE_RADIUS = 0.2


quality_color_map = {
    'Gold - Rare': "#FFD700",
    'Gold': "#FFD700",
    'Silver - Rare': "#C0C0C0",
    'Silver': "#C0C0C0",
    'Bronze - Rare': "#CD7F32",
    'Bronze': "#CD7F32"
}


revision_color_map = {
    'Icon': "white",
    'Normal': "grey",
    'IF': "black",
    'OTW': "orange",
    'SBC': "pink",
    'Europa Base': "blue",
    np.nan: "grey"
}


link_chemistry_map = {
    0: "red",
    1: "orange",
    2: "yellow",
    3: "green"
}


def get_player_picture(player_id):
    if player_id not in pd.Series(os.listdir("../input/pictures/")).str.replace(".png", ""):
        scrape_player_img(player_id)
    return mpl.image.imread("../input/pictures/{}.png".format(player_id))


def add_player_picture(player_id, ax=None, zoom=1, x=0, y=0):
    if ax is None:
        ax = plt.gca()
    img = get_player_picture(player_id)
    if img is None:
        return False
    if img.shape[:2] != (160, 160):
        w, h, _ = img.shape
        h_new = int(h / w * 160)
        img = cv.resize(img, (160, h_new))
    img = OffsetImage(img, zoom=zoom)
    
    ab = AnnotationBbox(img, (x, y), xycoords="data", frameon=False)
    ax.add_artist(ab)


def plot_formation(formation, position_coordinate_map):
    slot_facecolor = {k: quality_color_map[v.player.data["quality"]] for k, v in formation.slots.items()}
    slot_edgecolor = {k: "grey" if pd.isna(v.player.data["revision"]) else revision_color_map[v.player.data["revision"]] for k, v in formation.slots.items()}
    
    # create links between slots.
    lines = []
    for l in formation.links:
        x, y = position_coordinate_map[l.slot_1.slot_id]
        x1, y1 = position_coordinate_map[l.slot_2.slot_id]
        color = link_chemistry_map[l.get_chemistry()]
        lines.append(mpl.lines.Line2D((x * PITCH_WIDTH, x1 * PITCH_WIDTH), (y * PITCH_HEIGHT, y1 * PITCH_HEIGHT), linewidth=5, color=color, zorder=1))
        
    # create slots.
    slots = []
    for k, (x, y) in position_coordinate_map.items():
        height = SLOT_HEIGHT * PITCH_HEIGHT
        width = SLOT_WIDTH * PITCH_WIDTH
        x = x * PITCH_WIDTH - 0.5 * width
        y = y * PITCH_HEIGHT - 0.5 * height
        slots.append(mpl.patches.Rectangle((x, y), width, height, zorder=2, facecolor=slot_facecolor[k], edgecolor=slot_edgecolor[k], linewidth=3))
        
    # create pitch.
    green = "#53843f"
    fig = plt.figure(figsize=(16, 9), facecolor="black")
    ax = fig.gca()
    ax.set_facecolor(green)
    ax.set_xticks([])
    ax.set_yticks([])
    cirlce = mpl.patches.Circle((PITCH_WIDTH/2, PITCH_HEIGHT), CIRCLE_RADIUS * PITCH_WIDTH, edgecolor='white', facecolor=green, linewidth=5, fill=False, zorder=0)
    ax.add_patch(cirlce)
    rectangle = mpl.patches.Rectangle((PITCH_WIDTH/4, 0), PITCH_WIDTH/2, PITCH_HEIGHT/3, edgecolor='white', facecolor="#53843f", linewidth=5, fill=False, zorder=0)
    ax.add_patch(rectangle)
    for d in ["bottom", "top", "left", "right"]:
        ax.spines[d].set_color("white")
        ax.spines[d].set_linewidth(5)

    # add links.
    for l in lines:
        ax.add_line(l)
        
    # add slots.
    for s in slots:
        ax.add_patch(s)
        
    # add pictures.
    for k, v in formation.slots.items():
        x, y = position_coordinate_map[k]   
        width = SLOT_WIDTH * PITCH_WIDTH
        x = x * PITCH_WIDTH
        y = y * PITCH_HEIGHT
        add_player_picture(v.player.data.player_id, ax, x=x, y=y, zoom=0.5)

    ax.axis("square")
    ax.set_ylim(0, PITCH_HEIGHT)
    ax.set_xlim(0, PITCH_WIDTH)
    plt.tight_layout()
    

def animate(champion_log, position_coordinate_map, gif=True):
    files = []
    for i, c in enumerate(champion_log):
        formation = c.fill()
        plot_formation(formation, position_coordinate_map)
        file = "../images/animation/champion_{}.png".format(i)
        files.append(file)
        plt.savefig(file, facecolor="black", dpi=120)    
        plt.close()
        
    if gif:
        with imageio.get_writer('../images/animation/animation.gif', mode='I', duration=1) as writer:    
            for f in files:
                image = imageio.imread(f)
                writer.append_data(image)
                
    else:
        make_video(files)


def make_video(images, fps=3, size=None, is_color=True, format="XVID", outvid='../images/animation/animation.avi'):
        from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
        fourcc = VideoWriter_fourcc(*format)
        vid = None
        for image in images:
            if not os.path.exists(image):
                raise FileNotFoundError(image)
            img = imread(image)
            if vid is None:
                if size is None:
                    size = img.shape[1], img.shape[0]
                vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
            if size[0] != img.shape[1] and size[1] != img.shape[0]:
                img = resize(img, size)
            vid.write(img)
        vid.release()
        return vid
