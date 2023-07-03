import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke

rekreasi = pd.read_csv('data.csv')
data = rekreasi['wilayah'].value_counts()
ab=b = data.sort_values()
a = ab.index
b = ab
y = [i * 0.9 for i in range(len(a))]

BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#a2a2a2"


fig, ax = plt.subplots(figsize=(12, 7))

ax.barh(y, b, height=0.55, align="edge", color= BLUE);

ax.xaxis.set_ticks([i * 20 for i in range(0, 16)])
ax.xaxis.set_ticklabels([i * 20 for i in range(0, 16)], size=16, fontweight=100)
ax.xaxis.set_tick_params(labelbottom=False, labeltop=True, length=0)

ax.set_xlim((0, 300))
ax.set_ylim((0, len(a) * 0.9 - 0.2))

# Set whether axis ticks and gridlines are above or below most artists.
ax.set_axisbelow(True)
ax.grid(axis = "x", color="#A8BAC4", lw=1.2)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_lw(1.5)
# This capstyle determines the lines don't go beyond the limit we specified
# see: https://matplotlib.org/stable/api/_enums_api.html?highlight=capstyle#matplotlib._enums.CapStyle
ax.spines["left"].set_capstyle("butt")

# Hide y labels
ax.yaxis.set_visible(False)

PAD = 0.3
for name, count, y_pos in zip(a, b, y):
    x = 0
    color = "white"
    path_effects = None
    if count < 10:
        x = count
        color = BLUE    
        path_effects=[withStroke(linewidth=2, foreground="white")]
    
    ax.text(
        x + PAD, y_pos + 0.5 / 2, name, 
        color=color, fontsize=18, va="center",
        path_effects=path_effects
    ) 

# Make room on top and bottom
# Note there's no room on the left and right sides
fig.subplots_adjust(left=0.005, right=0.97, top=0.8, bottom=0.1)

# Add title
fig.text(
    0, 0.925, "Data Jenis Usaha di Jakarta", 
    fontsize=22, fontweight="bold"
)
# Add subtitle
fig.text(
    0, 0.875, "Banyaknya Wilayah yang memiliki Jenis Usaha", 
    fontsize=20
)

# Add caption
source = "Sources: 2020 Dinas Komunikasi, Informatika, dan Statistik - All Rights Reserved"
fig.text(
    0, 0.06, source, color=GREY, 
    fontsize=14
)

# Add authorship
fig.text(
    0, 0.005, "Data Jakarta", color=GREY,
    fontsize=16
)

# Add line and rectangle on top.
fig.add_artist(lines.Line2D([0, 1], [1, 1], lw=3, color=RED, solid_capstyle="butt"))
fig.add_artist(patches.Rectangle((0, 0.975), 0.05, 0.025, color=RED))

# Set facecolor, useful when saving as .png
fig.set_facecolor("white")
fig