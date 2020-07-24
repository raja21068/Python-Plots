import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

def reduce_points(array, number_of_points = 10):
    size = array.__len__()
    array_to_return = []
    skip_points_float = size/number_of_points
    skip_points_int = int(skip_points_float)
    skipped = skip_points_int
    for item in array:
       if skipped >= skip_points_int:
           array_to_return.append(item)
           skipped = 0
       else:
           skipped += 1
    return array_to_return

# LAMDA Variant on tweets
x_data = [0, 0.500,1,1.500,2,2.5,3.000,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
speed_mstreamf= [0,39.12841191,59.51584521,79.90327852,102.6174307,117.7882056,132.9589805,165.0061604,176.4593109,187.9124615,209.2565082,223.9457571,238.635006,274.4673437,296.7891278,319.110912,345.1774691,370.0691955,394.9609219,433.6936231,453.0599736]
speed_mstreamf_o = [0,29.12841191,49.51584521,69.90327852,29.12841191,39.32212856,59.70956186,49.51584521,34.22527024,49.51584521,54.61270354,41.87055772,41.87055772,52.06427438,48.24163063,41.87055772,46.96741605,50.1529525,45.05609418,44.41898689,48.56018428]
speed_dtm = [0,25.18294504,36.42460673,47.66626842,59.05373499,67.38943885,75.72514271,96.24551971,143.0232415,189.8009633,256.3676075,279.8054809,303.2433542,355.3103843,386.4452347,417.5800851,490.3131223,522.9660743,555.6190263,627.2102748,658.6002838]
speed_sodim = [0,34.12841191,54.51584521,74.90327852,97.61743067,112.7882056,127.9589805,160.0061604,176.4593109,187.9124615,163.0842283,171.8655403,174.8303853,174.4231538,171.0508269,173.0424766,173.3367107,172.963292,133.5844488,163.231732,160.7790459]
speed_sumblr = [0,298.096127,443.7677967,589.4394663,832.5119474,965.6716697,1098.831392,1372.118317,1521.033621,1669.948925,1946.315375,2096.194407,2246.073439,2534.474562,2691.828455,2849.182348,3158.383114,3291.30787,3424.232626,3675.418782,3821.625821]
speed_dmm = [0, 19.12841191,39.51584521,49.90327852,19.12841191,29.32212856,49.70956186,39.51584521,24.22527024,36.51584521,41.61270354,28.87055772,28.87055772,39.06427438,35.24163063,28.87055772,33.96741605,37.1529525,32.05609418,31.41898689,35.56018428]

marker_size = 11
markerwidth = 2.4  # 2
line_width = 2

fig, ax = plt.subplots()
ax.plot(reduce_points(x_data), reduce_points(speed_dtm) , '-', label='DTM', marker='o', markersize=marker_size, fillstyle='none',  color='b', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(reduce_points(x_data), reduce_points(speed_mstreamf), '-', label='MF-G', marker='v', markersize=marker_size, fillstyle='none',   color='r', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(reduce_points(x_data), reduce_points(speed_mstreamf_o), '-', label='MF-O', marker='D', markersize=marker_size, fillstyle='none',  color='m', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(reduce_points(x_data), reduce_points(speed_sumblr), '-', label='Sb', marker='>', markersize=marker_size, fillstyle='none', color='#b32d00', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(reduce_points(x_data), reduce_points(speed_dmm), '-', label='DMM', marker='x', markersize=marker_size, fillstyle='none', color='#0086b3', linewidth=line_width, markeredgewidth=markerwidth)
ax.plot(reduce_points(x_data), reduce_points(speed_sodim), '-', label='OSDM', marker='s', markersize=marker_size, fillstyle='none', color='k', linewidth=line_width, markeredgewidth=markerwidth)



leg = ax.legend(prop={'size': 26})   # show legends

# label the x and y axes
plt.xlabel('Stream (in Thousand Points)', fontsize=27)
plt.ylabel('Time', fontsize=30)

plt.xlim(min(x_data), max(x_data)+0.4)
plt.xticks(np.arange(min(x_data), 11, step=2), fontsize=30)
plt.yticks([0,500,1000,1500,2000],fontsize=30)
plt.ylim(0, 2000+100)



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