import numpy as np
import matplotlib.pyplot as plt

def multiple_plot(items, dfs:list, /, xa=None, xb=None, ylabel='', legend=None):
    ncols = 2
    xa = xa if xa else [None] * len(items)
    xb = xb if xb else [None] * len(items)

    fig, axs = plt.subplots(nrows=len(items)//ncols, ncols=ncols, sharex=True, figsize=(20, 30))

    for i, item in enumerate(items):
        ax = axs[i // ncols, i % ncols]
        for df in dfs:
            df.loc[xa[i]:xb[i], item].plot(ax=ax)
        ax.set_title(item)
        ax.set_ylabel(ylabel)
        if legend:
            ax.legend(legend)
    
    return fig, axs

def heatmap(mat, *, xticks, yticks, cmap="Reds"):
    mat = mat if type(mat) == np.ndarray else mat.to_numpy()

    fig, ax = plt.subplots(figsize=(7, 7))
    # heatmap
    im = ax.imshow(X=mat, cmap=cmap)
    # colorbar
    ax.figure.colorbar(im, ax=ax, shrink=0.75)
    # show all ticks...
    ax.set_xticks(range(len(xticks)))
    ax.set_yticks(range(len(yticks)))
    # ...and label them
    ax.set_xticklabels(xticks)
    ax.set_yticklabels(yticks)
    # loop over data dimensions and create text annotations
    for i in range(len(xticks)):
        for j in range(len(yticks)):
            text = ax.text(j, i, round(mat[i, j], ndigits=3), ha="center", va="center")
    
    return fig, ax