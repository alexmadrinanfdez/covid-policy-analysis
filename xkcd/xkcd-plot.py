import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # https://xkcd.com/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines.right.set_color('none')
    ax.spines.top.set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-50, 50])

    line_straight = np.ones(100)
    line_down = np.zeros(100) - range(-50, 50)
    line_up = range(-30, 70)

    ax.annotate(
        'different policies',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(20, -40))
    ax.annotate(
        '',
        xy=(20, 30), arrowprops=dict(arrowstyle='->'), xytext=(30, -35))
    ax.annotate(
        '',
        xy=(5, -25), arrowprops=dict(arrowstyle='->'), xytext=(20, -40))

    ax.plot(line_straight)
    ax.plot(line_down)
    ax.plot(line_up)

    ax.set_xlabel('Policy stringency')
    ax.set_ylabel('Effect on the curve of cases')
    fig.text(
        0.5, 0.05,
        'Marginal effect of policies on COVID-19 cases',
        ha='center')
    fig.savefig('xkcd-img.png', format='png')