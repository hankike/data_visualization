from pybaseball import team_pitching
from pybaseball import statcast_pitcher
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")
sns.set_style("white")

# First we want to pick a pitcher that we will run our graphs with. As an LSU grad, I picked Paul Skenes and will be using his 2025 stats.
skenes_stats = statcast_pitcher('2025-03-18', '2025-09-28', 694973)

# After getting his data I will find the average velocity of his pitches in order to know what pitches we are working with for the color palette. In the future I am to include these averages in the graph.
skenes_stats.groupby("pitch_type").release_speed.agg("mean") 

# First we will pick color palette. My palette is from TJStats as I like the colors he picked. The colors listed here are what he corresponds to each pitch.
pitch_colors = ['#FF007D', '#F79E70', '#FE6100',
                '#67E18D', '#1BB999', '#98165D', '#3025CE']

# First we make our facetgrid with Seaborn
g = sns.FacetGrid(skenes_stats, row="pitch_type",
                  hue="pitch_type", aspect=15, height=.5, palette=pitch_colors)

# Then our individual kdeplots
g.map(sns.kdeplot, "release_speed",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "release_speed", clip_on=False, color="w", lw=2, bw_adjust=.5)

g.refline(y=0, linewidth=1, linestyle="-", color=None, clip_on=False)

# x labels
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "release_speed")

# The spacing of the different graphs
g.figure.subplots_adjust(hspace=.25)

# get rid of clunky titles
g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

pitch_colors = ['#FF007D', '#F79E70', '#FE6100',
                '#67E18D', '#1BB999', '#98165D', '#3025CE']

g = sns.FacetGrid(skenes_stats, row="pitch_type",
                  hue="pitch_type", aspect=15, height=.5, palette=pitch_colors)

g.map(sns.kdeplot, "release_speed",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "release_speed", clip_on=False, color="w", lw=2, bw_adjust=.5)

g.refline(y=0, linewidth=1, linestyle="-", color=None, clip_on=False)


def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "release_speed")

g.figure.subplots_adjust(hspace=.25)

g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

plt.title("Paul Skenes Velocity Distribution", y=8)

# plot!
plt.show()

# My goal is to expand on this graph and to create more, but this is my second draft and I am proud of it!
