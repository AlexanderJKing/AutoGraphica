"""app_information
This module is responsible for containing all the text that can be displayed in the various info-dialog alerts that can pop up, dependent on the chart type selected.
"""

line_graph_info = """Outlined below are the various different options available for configuring the Line Graphs to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n

Error Bar Type: The error bars available for generating an estimate of central tendency can show one of two general things;\n
    - the range of uncertainty about the estimate\n
    - the spread of the underlying data around it.\n

Error Bar Value: The value pertaining to the 'Error Bar Type'. It must be noted that this value for the Percentile Interval ('pi') and the Confidence Interval ('ci') must be between 0 - 100."""


scatter_plot_info = """Outlined below are the various different options available for configuring the Scatter Plots to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n
"""


bar_chart_info = """Outlined below are the various different options available for configuring the Bar Charts to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n

Single Axis: This switch decides whether to plot an adjacent 'Continuous' variable along the 'y-axis'.
"""


box_plot_info = """Outlined below are the various different options available for configuring the Box Plots to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n
"""

# Third Axis Active: This switch decides whether to plot a 'categorical' variable in the data along the 3rd axis by way of color.\n

# Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn./n

# Legend Spacing: This entry takes a floating number between 0.0 and 1.0 and is used to determine how far to space the legend from the axes in the plot. If no number is inputted a default spacing option will be determines, which may overlap with the plot itself.


pie_chart_info = """Outlined below are the various different options available for configuring the Pie Charts to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Donut: This switch determines whether the plot will be a regular Pie Chart or if it will be a Donut Chart.

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn./n

Pie Chart Rotation: This input rotates the Pie Chart itself by the set amount inputted. There is no limit on the degrees to which it can be rotated, even minus values are permitted.\n

Explode Slice: This switch will determine whether to extract, or 'explode' a slice from the Pie Chart, with the 'smallest' and 'largest' slices of the Pie Chart available.\n 

Legend Spacing: This entry takes a floating number between 0.0 and 1.0 and is used to determine how far to space the legend from the axes in the plot. If no number is inputted a default spacing option will be determines, which may overlap with the plot itself.
"""

histogram_plot_info = """Outlined below are the various different options available for configuring the Histogram Plots to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Number of Bins: This is the number of bins used when grouping the frequency of numerical data.\n

Type: This switch determines the 'type' of histogram that will be displayed, whether it will be traditional 'bars' or with an 'area' plot (Default is 'bars').
"""

multiline_plot_info = """Outlined below are the various different options available for configuring the MultiLine Graphs to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Legend Spacing: This entry takes a floating number between 0.0 and 1.0 and is used to determine how far to space the legend from the axes in the plot. If no number is inputted a default spacing option will be determines, which may overlap with the plot itself.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n

Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn.
"""

multiscatter_plot_info = """Outlined below are the various different options available for configuring the MultiScatter Plots to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Legend Spacing: This entry takes a floating number between 0.0 and 1.0 and is used to determine how far to space the legend from the axes in the plot. If no number is inputted a default spacing option will be determines, which may overlap with the plot itself.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n

Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn.
"""


multibar_plot_info = """Outlined below are the various different options available for configuring the MultiBar Charts to be generated.\n 

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Legend: This switch turns the legend 'on' or 'off' when the plot is generated.\n

Legend Spacing: This entry takes a floating number between 0.0 and 1.0 and is used to determine how far to space the legend from the axes in the plot. If no number is inputted a default spacing option will be determines, which may overlap with the plot itself.\n

Orientation: This switch either keeps the 'x' and 'y' axes on their original axes ('vertical') or switches them to be on the opposite axes ('horizontal').\n

Single Axis: This switch decides whether to plot an adjacent 'Continuous' variable along the 'y-axis'.\n

Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn.
"""

facet_plot_info = """Outlined below are the various different options available for configuring the Facet Plot to be generated.\n 

High Cardinal Variables: These are variables considered to be of high cardinality, i.e. above 30 unique values within a categorical variable. As such they are divided into subplots (facets) to more easily analyze them. Available high cardinality variables will be displayed in the drop-down menu, and once an appropriate variable has been selected, this will unlock the 'Y-Acis Variables' input for selection.\n

Y-Axis Variables: These are 'Continuous' variables available that will be plotted on the 'y-axis' alongside the High Cardinal Variable selected. Once this has been inputted, all other configuration options will be unlocked.\n

Plot Style: The Plot Styles available are responsible for cutomising the overall look of the Figure and Axes in the Plot. There are 26 currently available, that originate from the plotting libraries Matplotlib and Seaborn.\n

Custom Title: This can be any title you prefer, but if left blank, a default title will be generted for the plot, composing the names of the variables in the axes of the plot.\n

Custom Color: The color entry can be defined in a number of ways which are listed below;\n
    - RGB/RGBA values in brackets (0, 0, 0)/(0, 0, 0, 0),\n
    - Hex codes like #FFFFFF,\n
    - single word color entries such as 'red'.\n
    
Rotate X-Axis Ticks: This entry allows the x-axis ticks to be rotated by a number of degrees. This can be any number, even a minus number to rotate in the opposite direction.\n 

Palettes: The Palette options available are responsible for highlighting the differences in the data drawn when a third dimensions is added to the plot. There are 76 different palettes available that originate from the plotting libraries Matplotlib and Seaborn.\n

No. of Bars per Subplot: This is the number of values within the High Cardinal Variable selected that will be placed in each subplot (facet), represented as bars.\n 

Figure Height: The height of the figure.\n

Figure Width: The width of the figure.\n
"""