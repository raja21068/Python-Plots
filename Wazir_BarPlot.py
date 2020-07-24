import matplotlib.pyplot as plt
import matplotlib as mtplt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.pyplot import figure
rcParams['font.family'] = 'Times New Roman'
rcParams['mathtext.default']='regular'


left = 0.08
bottom= 0.11
right=0.98
top=0.98
marker_size = 11
markerwidth = 2.4  # 2
line_width = 2
legend_size = 26
xylabel_size=26
xytick_font_size =28
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top)
y_ticks_label = "Epoch"
x_ticks_label = "F-Score"
load_file = pd.read_csv("F:/Wazir Ali/F+score+of+all+the+model+each+datasets.csv") #F+score+of+all+the+model+each+datasets.csv, results for plot.csv

legends = load_file.columns

last_val_for_each_col = {}

for idx in range(0, len(legends)- 1):
    x_label = legends[idx]
    x_data = load_file[x_label].values.tolist()
    last_val_for_each_col[x_label] = x_data[-1]

for k,v in last_val_for_each_col.items():
    ax.bar(k.replace("-","\n"),v, color='#1E88BA',edgecolor='k')
    ax.text(k.replace("-","\n"), v + .10, str(v), color='k', fontweight='bold', fontsize=xytick_font_size-4, horizontalalignment='center')


plt.yticks([94,96,98], fontsize=xytick_font_size)
plt.xticks( fontsize=xytick_font_size, wrap=True) #
plt.ylim(94,99)

plt.ylabel(x_ticks_label, fontsize=xytick_font_size)
# plt.xlabel(y_ticks_label, fontsize=xytick_font_size+1)
#
# plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.7), prop={'size': 20}, ncol=2, handletextpad=0.1)
plt.grid(axis="y", which="minor")
plt.show()

# ================    ===============================
# Markers           description
# ================    ===============================
#    -                solid line style
#    --               dashed line style
#    -.               dash-dot line style
#    :                dotted line style
#    .                point marker
#    ,                pixel marker
#    o                circle marker
#    v                triangle_down marker
#    ^                triangle_up marker
#    <                triangle_left marker
#    >                triangle_right marker
#    1                tri_down marker
#    2                tri_up marker
#    3                tri_left marker
#    4                tri_right marker
#    s                square marker
#    p                pentagon marker
#    *                star marker
#    h                hexagon1 marker
#    H                hexagon2 marker
#    +                plus marker
#    x                x marker
#    D                diamond marker
#    d                thin_diamond marker
#    |                vline marker
#    _                hline marker
# ================    ===============================