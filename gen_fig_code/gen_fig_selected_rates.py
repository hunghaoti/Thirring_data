import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


Delta_1, Delta_2, m1, m2 = 0.1, -0.9, 0.6, 0.1

dt = 0.01
param = 'Delta' + str(Delta_1) + 'to' + str(Delta_2) + 'm' + str(m1) + 'to' + str(m2)
data_path = '../data_submit/Fig2/' + param + '/'
data = pd.read_csv(data_path + 'return_rates.csv')
save_fig_name = '../figs/selected_quenches_fig'

def strToComplex(c_str):
    c_str = c_str.replace(" ", "")
    c_str = c_str.replace(",", "+")
    c_str = c_str.replace(")", "j")
    c_str = c_str.replace("(", "")
    c_str = c_str.replace("+-", "-")
    return complex(c_str)


def GetComplexDataFromFile(file_str, every_n_line):
    file1 = open(file_str, 'r')
    Lines = file1.readlines()
    allList = []
    for subline in range(0, every_n_line):
        allList.append([])

    cnt = 0
    for line in Lines:
        c = strToComplex(line)
        list_idx = cnt % every_n_line
        allList[list_idx].append(c)
        cnt += 1

    return allList


def plot_eigval(inset_ax, t, t_posx = 0.6, t_posy=-1.15):
    file_name = data_path + 't' + str(t) + "_spec"
    ys = GetComplexDataFromFile(file_name, 1)
    c_list = ys[0]
    n_list = []
    r_list = []
    i_list = []
    for i in range(len(c_list)):
        n_list.append(abs(c_list[i]))
        r_list.append(c_list[i].real)
        i_list.append(c_list[i].imag)
    #inset_ax.set_frame_on(False)
    max_idx = n_list.index(max(n_list))
    unitcir = plt.Circle((0, 0), 1.0, fill = False)
    inset_ax.add_patch(unitcir)
    inset_ax.axis('off')
    inset_ax.scatter(r_list, i_list, s = 0.2, color = 'b')
    inset_ax.scatter(r_list[max_idx], i_list[max_idx], s = 10, color = 'r', marker = 'x')
    inset_ax.scatter(0, 0, s = 3, color = 'black') ## circle O point
    inset_ax.text(t_posx, t_posy, "$t$="+str(t),fontsize=10)

def plot_eigval_0(inset_ax, t, t_posx = 1.2, t_posy = -1.15):
    file_name = data_path + 't' + str(t) + "_spec"
    ys = GetComplexDataFromFile(file_name, 1)
    c_list = ys[0]
    n_list = []
    r_list = []
    i_list = []
    for i in range(len(c_list)):
        n_list.append(abs(c_list[i]))
        r_list.append(c_list[i].real)
        i_list.append(c_list[i].imag)
    #inset_ax.set_frame_on(False)
    max_idx = n_list.index(max(n_list))
    unitcir = plt.Circle((0, 0), 1.0, fill = False)
    inset_ax.add_patch(unitcir)
    inset_ax.axis('on')
    inset_ax.set_xlabel('$\operatorname{Re}(\lambda_i)$',fontsize=8,labelpad=-1)
    inset_ax.set_ylabel('$\operatorname{Im}(\lambda_i)$',fontsize=8,labelpad=-6)
    inset_ax.scatter(r_list, i_list, s = 0.2, color = 'b')
    inset_ax.scatter(r_list[max_idx], i_list[max_idx], s = 10, color = 'r', marker = 'x')
    inset_ax.scatter(0, 0, s = 3, color = 'black') ## circle O point
    inset_ax.text(t_posx, t_posy, "$t$="+str(t),fontsize=10)

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(12)

# fig a
ax = axes.T.flatten()[0]
ax.plot(data.t, data.r0, linestyle = '-', label = '$r_0(t)$')
ax.plot(data.t, data.r1, linestyle = '--', label = '$r_1(t)$')
ax.set_xlim([-0.5, 10.5])
ax.set_ylim([-0.01, 2.])

ax.legend(loc = 'upper right')

ax.set_xlabel('$t$', fontsize = 12)
ax.set_ylabel('$r_i(t)$', fontsize = 12)
title_str = '$(ma, \Delta):($' + str(m1) + ', ' + str(Delta_1) + ')$\\rightarrow($' + str(m2) + ', ' + str(Delta_2) + ')'
ax.set_title(title_str, fontsize = 14)

ran = 0.22
wrate = "85%"
hrate = "100%"

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.08, 0.26, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
axins1.patch.set_alpha(0.5)
plot_eigval_0(axins1, 0)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.25, 0.75, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 4)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.25, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 6)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.5, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 7.7)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.77, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 7.8)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.77, 0.28, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 9)

# fig b
ax = axes.T.flatten()[1]
Delta_1, Delta_2, m1, m2 = 0.1, -0.9, 0.7, 0.1

dt = 0.01
param = 'Delta' + str(Delta_1) + 'to' + str(Delta_2) + 'm' + str(m1) + 'to' + str(m2)
data_path = '../data_submit/Fig2/' + param + '/'
data = pd.read_csv(data_path + 'return_rates.csv')
t_star = 7.78
ax.plot(data.t, data.r0, linestyle = '-', label = '$r_0(t)$')
ax.plot(data.t, data.r1, linestyle = '--', label = '$r_1(t)$')
ax.axvline(x = t_star, color = 'black',linestyle = '-.', alpha = 0.5, label = '$t^*=$' + str(t_star))
ax.set_xlim([-0.5, 10.5])
ax.set_ylim([-0.01, 2.])

ax.legend(loc = 'upper right')

ax.set_xlabel('$t$', fontsize = 12)
ax.set_ylabel('$r_i(t)$', fontsize = 12)
title_str = '$(ma, \Delta):($' + str(m1) + ', ' + str(Delta_1) + ')$\\rightarrow($' + str(m2) + ', ' + str(Delta_2) + ')'
ax.set_title(title_str, fontsize = 14)

ran = 0.22
wrate = "85%"
hrate = "100%"

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.08, 0.28, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
axins1.patch.set_alpha(0.5)
plot_eigval_0(axins1, 0)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.25, 0.73, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 4)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.25, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 6)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.5, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 7.7)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.77, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 7.8)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.77, 0.28, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 9)

ax.arrow(6.97, 1.22, 7.65-6.97, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(7.65, 1.22, 0, -1.2, head_width=0.15, head_length=0.025, fc='k', ec='k', alpha = 0.8)
ax.arrow(8.05, 1.22, 7.88-8.05, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(7.88, 1.22, 0, -1.2, head_width=0.15, head_length=0.025, fc='k', ec='k', alpha = 0.8)

# fig c
ax = axes.T.flatten()[2]
Delta_1, Delta_2, m1, m2 = -0.9, 0.9, 0.1, 0.1

dt = 0.01
param = 'Delta' + str(Delta_1) + 'to' + str(Delta_2) + 'm' + str(m1) + 'to' + str(m2)
data_path = '../data_submit/Fig2/' + param + '/'
data = pd.read_csv(data_path + 'return_rates.csv')
t_star = 3.62
ax.plot(data.t, data.r0, linestyle = '-', label = '$r_0(t)$')
ax.plot(data.t, data.r1, linestyle = '--', label = '$r_1(t)$')
ax.axvline(x = t_star, color = 'black',linestyle = '-.', alpha = 0.5, label = '$t^*=$' + str(t_star))
ax.set_xlim([-0.5, 10.5])
ax.set_ylim([-0.01, 0.25])
ax.legend(loc = 'upper right')

ax.set_xlabel('$t$', fontsize = 12)
ax.set_ylabel('$r_i(t)$', fontsize = 12)
title_str = '$(ma, \Delta):($' + str(m1) + ', ' + str(Delta_1) + ')$\\rightarrow($' + str(m2) + ', ' + str(Delta_2) + ')'
ax.set_title(title_str, fontsize = 14)

ran = 0.22
wrate = "85%"
hrate = "100%"

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.17, 0.12, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
axins1.patch.set_alpha(0.5)

t_posx, t_posy = 0, 0.2
plot_eigval_0(axins1, 0, t_posx, t_posy)

t_posx, t_posy = -0.1, 0.2
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.17, 0.34, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 1, t_posx, t_posy)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.17, 0.56, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 3.6, t_posx, t_posy)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.42, 0.2, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 3.7, t_posx, t_posy)

t_posx, t_posy = 0.2, 0.2
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.61, 0.2, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 6, t_posx, t_posy)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.80, 0.2, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 9, t_posx, t_posy)

#ax.arrow(0.7, 0.04, -0.7, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
#ax.arrow(0, 0.04, 0, -0.044, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)
ax.arrow(3.31, 0.162, 3.5 - 3.31, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(3.5, 0.162, 0, -0.166, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)
ax.arrow(4.2, 0.07, 3.75-4.2, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(3.75, 0.07, 0, -0.074, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)

# fig d
ax = axes.T.flatten()[3]
Delta_1, Delta_2, m1, m2 = 0.9, 0.9, 1000, 0.1

dt = 0.01
param = 'Delta' + str(Delta_1) + 'to' + str(Delta_2) + 'm' + str(m1) + 'to' + str(m2)
data_path = '../data_submit/Fig2/' + param + '/'
data = pd.read_csv(data_path + 'return_rates.csv')

t_star = 9.53
ax.plot(data.t, data.r0, linestyle = '-', label = '$r_0(t)$')
ax.plot(data.t, data.r1, linestyle = '--', label = '$r_1(t)$')
ax.axvline(x = t_star, color = 'black',linestyle = '-.', alpha = 0.5, label = '$t^*=$' + str(t_star))
#plt.axvline(x = t_star, color = 'black', alpha = 0.3)
ax.set_xlim([-0.5, 10.5])
ax.set_ylim([-0.01, 0.75])

ax.legend(loc = 'upper right')

ax.set_xlabel('$t$', fontsize =12)
ax.set_ylabel('$r_i(t)$', fontsize = 12)
title_str = '$(ma, \Delta):($' + str(m1) + ', ' + str(Delta_1) + ')$\\rightarrow($' + str(m2) + ', ' + str(Delta_2) + ')'
ax.set_title(title_str, fontsize = 14)

ran = 0.22
wrate = "85%"
hrate = "100%"

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.08, 0.65, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
axins1.patch.set_alpha(0.5)
plot_eigval_0(axins1, 0)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.15, 0.05, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 2)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.37, 0.05, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 5)
axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.42, 0.65, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 8)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.65, 0.05, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 9.5)

axins1 = inset_axes(ax, width=wrate, height=hrate,
                    bbox_to_anchor=(0.65, 0.5, ran, ran),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
plot_eigval(axins1, 9.6)


#ax.arrow(1.2, 0.15, -1.2, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
#ax.arrow(0, 0.15, 0, -0.15, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)
ax.arrow(8.6, 0.1, 9.4-8.6, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(9.4, 0.1, 0, -0.1, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)
ax.arrow(8.6, 0.45, 9.65-8.6, 0, head_width=0.0, head_length=0.0, fc='k', ec='k', width = 0.0005, alpha = 0.8)
ax.arrow(9.65, 0.45, 0, -0.45, head_width=0.15, head_length=0.005, fc='k', ec='k', alpha = 0.8)

for n, ax in enumerate(axes.T.flatten()):
    ax.text(-0.14, 1.1, '(' + string.ascii_lowercase[n] + ')', transform=ax.transAxes,
            size=14)

fig.tight_layout()
plt.subplots_adjust(hspace=0.35, wspace=0.27, left=0.08, right = 0.97)

plt.savefig(save_fig_name + '.pdf')
#plt.savefig(save_fig_name + '.png')
#plt.show()
plt.close()

