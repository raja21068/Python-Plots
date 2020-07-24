import matplotlib.pyplot as plt
import matplotlib as mtplt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'
rcParams['mathtext.default']='regular'

# ALPHA Variant
# x_data = [0.001,0.01,0.03,0.05,0.07,0.09,0.1,0.3,0.5,0.7,0.9]
x_data = [r'$9e^{-3}$',r'$1^{e-2}$',r'$3^{e-2}$',r'$5^{e-2}$',r'$7^{e-2}$',r'$9e^{-2}$',r'$1^{e-1}$',r'$3^{e-1}$',r'$5^{e-1}$',r'$7^{e-1}$',r'$9e^{-1}$',]
nmi_values= [0.839195479,0.84166465,0.842250047,0.842147959,0.841545834,0.842011107,0.841505864,0.836929276,0.836741238,0.835881513,0.832398627]
vm_values = [0.83414992,0.835325155,0.835122823,0.834717973,0.833641915,0.834057313,0.8335185,0.828084342,0.827552863,0.826361936,0.822907456]
ho_values = [0.936712953,0.951942817,0.959710209,0.962257931,0.965683255,0.966602206,0.966345933,0.968519482,0.97106612,0.972752778,0.968787635]
pu_values = [0.891530902,0.914220698,0.927115626,0.930182706,0.937273267,0.9386584,0.938097751,0.941956335,0.945485126,0.948222413,0.93918607]
acc_values = [0.664830816,0.709913594,0.758821977,0.764362509,0.778840446,0.787019326,0.786854429,0.78527142,0.790152365,0.814886881,0.830123343]
titlee = "Tweets_Alpha_evolution"

# Beta Variant
# x_data = [0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009,0.001,0.0011,0.0012,0.0013,0.0014,0.0015,0.0016,0.0017,0.0018,0.0019,0.002]
# x_data = [r'$1e^{-4}$', r'$2^{e-4}$', r'$3^{e-4}$',  r'$5^{e-4}$', r'$7^{e-4}$', r'$8^{e-4}$', r'$9^{e-4}$',r'$1e^{-3}$', r'$11^{e-4}$',r'$12^{e-4}$', r'$14^{e-4}$', r'$18^{e-4}$',  r'$1e^{-2}$']
# nmi_values= [0.498207378,0.795910334,0.836654806,0.839827693,0.836750592,0.834042978,0.829379623,0.826929232,0.825403716,0.823230068,0.819161865,0.814707004,0.812321937]
# vm_values = [0.462661163,0.795547843,0.832650484,0.833276649,0.828347112,0.824875881,0.819393478,0.816081921,0.814068154,0.81140117,0.806481759,0.800724948,0.797683465]
# ho_values = [0.337474203,0.820302467,0.922829971,0.951946099,0.964729752,0.968001002,0.969366862,0.97319521,0.975119756,0.976312127,0.977872151,0.981847453,0.983565094]
# pu_values=[0.329991425,0.765285931,0.873919926,0.911483411,0.934997691,0.939219049,0.941626542,0.949574566,0.95247675,0.954125717,0.956863004,0.96319504,0.96626212]
# acc_values=[0.220236132,0.503528791,0.647912407,0.730789526,0.776630829,0.794868412,0.787744872,0.822900864,0.835004287,0.856671724,0.872864587,0.89364158,0.914847306]
# titlee = "Tweets_Beta_evolution"

# LAMBDA Variant
# x_data = [r'$9e^{-4}$', r'$7e^{-4}$',r'$5e^{-4}$', r'$1e^{-4}$', r'$9e^{-5}$',r'$7e^{-5}$',r'$5e^{-5}$',  r'$1e^{-6}$',  r'$3e^{-6}$', r'$9e^{-6}$']
# nmi_values= [0.804534282,0.813406885,0.810465953,0.832844712,0.837457832,0.841218446,0.839503544,0.837270452,0.832526038,0.827902459]
# ho_values = [0.907681929,0.915147064,0.901206853,0.924869907,0.93128048,0.933625631,0.932473011,0.93498587,0.933850472,0.930485076]
# pu_values = [0.840775674,0.851955676,0.842820394,0.879559396,0.885726535,0.889881934,0.888331904,0.889288306,0.885231845,0.878701933]
# acc_values = [0.724259613,0.717696722,0.722940439,0.719906339,0.737352417,0.743816371,0.70397731,0.662621199,0.670800079,0.619253347]
# vm_values = [0.798715893,0.807790524,0.805923289,0.828291457,0.832758233,0.836670093,0.834894366,0.832195282,0.827065154,0.822286138]
# titlee = "Tweets_lambda_evolution"

marker_size=13
markerwidth=1.4
line_width=1

fig, ax = plt.subplots()
plt.subplots_adjust(top=0.99)
fig.canvas.set_window_title(titlee)


ax.plot(x_data, nmi_values , '-', label = 'NMI', marker='o', markersize=marker_size, fillstyle='none',  color='#DC267F', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(x_data, ho_values, '-',  label = 'Ho', marker='s', markersize=marker_size, fillstyle='none',   color='k', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(x_data, pu_values, '-', label = 'Pu', marker='D', markersize=marker_size, fillstyle='none',  color='#785EF0', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(x_data, acc_values, '-', label = 'Acc',  marker='>', markersize=marker_size, fillstyle='none', color='#800080', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(x_data, vm_values, '-',  label = 'VM', marker='x', markersize=marker_size-3, fillstyle='none', color='#155660', linewidth=line_width, markeredgewidth=markerwidth)


leg = ax.legend(prop={'size': 27}, ncol=2, handletextpad=0.1)   # show legends

# label the x and y axes
# plt.xlabel(r'$1^{e-4}$')
# plt.ylabel('Score', fontsize=30)


tmp = [r'$9e^{-3}$',r'$9e^{-2}$',r'$9e^{-1}$']
# r = [0.001, 0.5, 0.9]

# tmp = [r'$1e^{-4}$', '$1e^{-3}$', r'$1e^{-2}$']
# r = [0.001,0.0025, 0.005,0.0075, 0.01]

# tmp = [r'$9e^{-4}$', r'$9e^{-5}$', r'$9e^{-6}$']

fontProperties = {'family':'Times New Roman'}

plt.xticks(tmp, fontsize=32)
# np.arange(min(x_data), max(x_data)+0.00006, step=0.0005)
plt.ylim(0.3, 1.1)
plt.yticks([0.3,0.5,0.7,0.9], fontsize=32)



plt.show()


# plt.title('A Simple Scatterplot')
# plt.legend(loc='best')  # legend text comes from the plot's label parameter.
# plt.show()









# ================    ===============================
# character           description
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