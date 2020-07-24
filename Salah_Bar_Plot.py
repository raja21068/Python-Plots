import matplotlib.pyplot as plt
import matplotlib as mtplt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.pyplot import figure
rcParams['font.family'] = 'Times New Roman'
rcParams['mathtext.default']='regular'


def drawPlot(groups,legend, data, y_label, t_ticks, y_limit):
    data = np.transpose(data)
    left = 0.105
    bottom= 0.24
    right=0.98
    top=0.97
    bar_width = 0.14
    legend_size = 18
    xytick_font_size =24
    space_bt_bars = 0.01
    fig, ax = plt.subplots(figsize=(9.8, 4.6))
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top)
    r1 = np.arange(len(groups))

    # colors = ['#000000', '#808080', '#A9A9A9', '#D3D3D3', '#FFE4E1']
    colors = ['#B54F4F','#A76243','#E5953D','#3E405E','#65BAB7','#FA8072']
    # colors = ['#F15C58', '#17B582', '#14A5E4', '#926FFF', '#65BAB7', '#F83ECD']
    # colors = ['#20B2AA', '#66CDAA', '#00FA9A', '#87CEFA', '#65BAB7', '#F83ECD']
    for i, val in enumerate(legend):
        rects1 = ax.bar(r1, data[i], width=bar_width-space_bt_bars, label=val, color=colors[i], edgecolor='#3a3838') #
        r1 = [x + bar_width for x in r1]


    plt.ylabel(y_label, fontsize=xytick_font_size)
    plt.xticks([r + bar_width+(space_bt_bars*len(groups)) for r in range(0,len(groups))], fontsize=xytick_font_size-2)
    ax.set_xticklabels(groups)
    ax.set_ylim(y_limit)
    plt.yticks(t_ticks, fontsize=xytick_font_size)
    plt.legend(loc='lower center', bbox_to_anchor=(0.47, -0.35), prop={'size': legend_size}, ncol=5, handletextpad=0.05)
    plt.show()





groups = ['Spam','GSD','HAR','KDDcup','FCT','IoTBotnet','MNIST']
legend = ['Our_5','Our_10','Our_20','ARF','SAMkNN']
data1 = [[93.28,93.93,94.61,90.06,88.80],
[88.14,90.14,93.14,79.61,91.87],
[84.48,86.57,87.33,81.36,89.14],
[98.24,98.55,98.79,99.30,99.24],
[79.58,81.63,83.29,89.91,90.48],
[97.70,98.63,99.17,99.63,99.38],
[79.15,84.17,87.65,72.98,87.63]]

data2 = [[86.36,87.95,89.26,85.94,84.24],
[87.27,89.13,92.58,79.00,91.37],
[84.66,86.88,87.58,81.72,89.34],
[23.55,27.78,32.57,40.90,38.94],
[67.86,69.79,72.22,81.75,84.73],
[98.20,98.90,99.01,99.66,99.12],
[78.79,83.89,87.48,72.97,87.84]]



drawPlot(groups, legend, data1, "Accuracy", [70, 85, 100], [70,100])
# drawPlot(groups, legend, data2, "F1-Score", [20, 60, 100], [20,102])