import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'
rcParams["legend.borderaxespad"] = 0.01
rcParams["legend.labelspacing"] = 0.02
# rcParams["legend.columnspacing"] = 0.03
rcParams["legend.borderpad"] = 0.2
rcParams["legend.handlelength"] = 1.3
import numpy as np
import pickle

# data_file = "F:/PhD/Coding/MyAlgoUpdate-FeatureDecay/venv/data/Tweets-T-timeseries.csv"
data_file = "F:/PhD/Coding/MyAlgoUpdate-FeatureDecay/venv/data/News-T-N-timeseries.csv"

setting = {"left": 0.06, "bottom": 0.11, "right":0.96, "top":0.99, "figsize":(7.1, 5.2)}
fig, ax = plt.subplots()
plt.subplots_adjust(left=setting["left"], bottom=setting["bottom"], right=setting["right"], top=setting["top"])
cluster_name = ["A-B","C-D", "E-F", "G-H", "I-J"]

tick_font_size = 32
legend_size= 28
with open(data_file) as input:
    counter = 0
    for line in input:
        counter +=1

        if(counter % 2 == 1):
            x_data = [int(e) if e.isdigit() else e for e in line.split(',')]
        else:
            y_data = [int(e) if e.isdigit() else e for e in line.split(',')]
            # ax.scatter( x_data,y_data, label=cluster_name[0]) #tweets
            ax.scatter(y_data, x_data, label=cluster_name[0]) #news
            cluster_name = cluster_name[1:]

ax.set_yticks([])
# plt.xticks([0,10000, 20000],labels=['0K','10K', '20K'],fontsize=tick_font_size) #tweets
plt.xticks([0,5000, 10000],labels=['0K','5K', '10K'],fontsize=tick_font_size) #news
plt.xlabel("Stream", fontsize=tick_font_size)
# plt.legend(loc='lower left', prop={'size': legend_size}, ncol=1 , handletextpad=-0.1, bbox_to_anchor=(0.01, 0.01))
plt.legend(loc='upper left', prop={'size': legend_size}, ncol=1 , handletextpad=-0.1, bbox_to_anchor=(0.0, 0.98))
plt.show()

