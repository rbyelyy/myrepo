import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool

# set tools
TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave,hover"


# source file
csv_file = pd.read_csv('times.csv')

# releases
get_unique_releases = np.unique(np.array(csv_file['Release']))


# output to static HTML file
output_file("perfromance.html", title="Performance")

# create a new plot with a a datetime axis type
p = figure(width=800, height=350, x_axis_type="datetime", tools=TOOLS)

# add figure
for i in get_unique_releases:
   release_data = csv_file.ix[csv_file['Release'] == i].reset_index(drop=True)
   dates = np.array(release_data['Date'], dtype=np.datetime64)

   source = ColumnDataSource(
      data=dict(
         revision=release_data['Revision'].tolist(),
      )
   )


   p.circle(dates, release_data['Duration'], size=40, color='green', alpha=0.2, source=source, legend=i)
   p.line(dates, release_data['Duration'], legend=i)

   hover = p.select(dict(type=HoverTool))

   hover.tooltips = [
      ("revision", "@revision"),
   ]






# NEW: customize by setting attributes
p.title = "Performance"
p.legend.orientation = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Duration'
p.ygrid.band_fill_color = "red"
p.ygrid.band_fill_alpha = 0.1





# show the results
show(p)

