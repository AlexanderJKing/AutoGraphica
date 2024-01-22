"""root.plot_scatter_plot
Imports the ScatterPlot class for creating an instance of a scatter plot and plotting it.
Small demo on instantiating it as an object if this is run as a script.
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import warnings
warnings.filterwarnings("ignore")

import copy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the classes from the custom modules needed during instantiation of any Chart Class
from support_main_classes import ColumnAttributes, DataframeOverview
from support_plotting import Plotting
from support_rcParams import RCParams
pd.options.mode.chained_assignment = None  # default='warn'


class ScatterPlot:
    
    """
    A class for instantiating a 'scatter plot' object

    Attributes
    ----------
    pd_dataframe: pd.DataFrame
        The DataFrame from the file submitted by the user.
    color_code: str
        A valid Matplotlib color code.
    custom_title: str
        A valid title for the plot.
    xtick_rotation: int, float, str
        A valid rotation value for ticks along the 'x-axis'.
    legend_on: str
        A value specifying whether the legend of the plot is turned on.
    current_style: str
        A valid Matplotlib style.
    orientation: str
        A value specifying whether data on the 'x-axis' is flipped to display on the 'y-axis'.
    overview: support_main_classes.DataframeOverview
        An instance of the DataframeOverview class which will feature engineer additional information based on the DataFrame input.
    plot_funcs: support_plotting.Plotting
        An instance of the Plotting class which provides additional functions to support in the plotting of the DataFrame.
    rcparams: support_rcParams.RCParams
        An instance of the RCParams class which contains basic, universal characteristics for all plots generated.
    df: pd.DataFrame
        The original DataFrame inputted.
    chart_type: str
        The chart type that the user has selected on the app home page.
    """
    
    def __init__(self,
                 pd_dataframe: pd.DataFrame,
                 color_code: str=None,
                 custom_title: str=None,
                 xtick_rotation=None,
                 legend_on: str="on",
                 current_style: str=None,
                 orientation: str=None):
        
        self.overview = DataframeOverview(pd_dataframe)
        self.plot_funcs = Plotting()
        self.rcparams = RCParams()
        self.df = copy.copy(self.overview.dataframe)
        
        self.color_code = self.plot_funcs.check_valid_color(color_code)
        self.custom_title = custom_title
        self.xtick_rotation = xtick_rotation
        self.legend_on = legend_on
        self.current_style = current_style
        self.orientation = orientation
        self.chart_type = 'Scatter'
        
        self.chart_rules()   
        self.plot_funcs.set_plot_style(self.current_style)
        self.default_xtick_rotation()


    def default_xtick_rotation(self):

        "Sets the default position and type for all 'x-axis' ticks."

        try:
            self.xtick_rotation = float(self.xtick_rotation)
            self.xtick_rotation = int(self.xtick_rotation)
        except (ValueError, TypeError) as e:
            self.xtick_rotation = 0

        
    def chart_rules(self):

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Scatter Plot.
        if a column is of type 'Continuous', then it is valid for plotting along an 'x-axis'. 
        If a column is of type 'Continuous', then it is valid for plotting along a 'y-axis'.
        """
        
        self.x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous']
        
        self.y_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous']    
        
        
    def create_chart(self, x_axis_var, y_axis_var):

        """Creates a Scatter Plot
        
        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Date'/'Time'/'Continuous' column within the DataFrame
        y_axis_var: pd.Series
            A 'Continuous' column within the DataFrame
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, ax = plt.subplots(figsize=(4, 3))

        # 2) INSTANTIATE A 'PLOT' OBJECT FROM THE 'seaborn.objects' INTERFACE (so)    
        if self.orientation == 'horizontal':
            plot = sns.scatterplot(self.df,
                                   x=self.df[y_axis_var],
                                   y=self.df[x_axis_var],
                                   color=self.color_code,
                                   s=20,
                                   alpha=0.8,
                                   edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                   linewidth=0.5)
        else:
            plot = sns.scatterplot(self.df,
                                   x=self.df[x_axis_var],
                                   y=self.df[y_axis_var],
                                   color=self.color_code,
                                   s=20,
                                   alpha=0.8,
                                   edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                   linewidth=0.5)
        
        # 3) ADD THE LABELS FOR THE AXES
        if self.orientation == 'horizontal':
            ax.set_xlabel(y_axis_var, fontsize=8)
            ax.set_ylabel(x_axis_var, fontsize=8)
        else:
            ax.set_xlabel(x_axis_var, fontsize=8)
            ax.set_ylabel(y_axis_var, fontsize=8)
    
        # 4) CREATE THE TITLE FOR THE CHART
        self.plot_funcs.create_title(custom_title=self.custom_title,
                                     chart_type=self.chart_type,
                                     axis_variable1=y_axis_var,
                                     axis_variable2=x_axis_var,
                                     current_style=self.current_style)
        
        # 5) CREATE THE LEGEND FOR THE CHART        
        self.plot_funcs.create_legend(legend_on=self.legend_on,
                                      chart_type=self.chart_type,
                                      axis_variable1=y_axis_var,
                                      axis_variable2=x_axis_var,
                                      color_code=self.color_code,
                                      patches_=None,
                                      font_size=None,
                                      bbox_anchor=None,
                                      figure=None,
                                      legend_title='',
                                      current_style=self.current_style)
        
        # 6) ROTATE THE X-AXIS TICKS
        plt.xticks(rotation=self.plot_funcs.set_xaxis_rotation(user_xtick_rotation=self.xtick_rotation,
                                                               pd_series=self.df[x_axis_var],
                                                               orientation=self.orientation))
        
        # 7) TIGHTEN THE LAYOUT AND SET THE FONT SIZE OF TICKS AND LABELS
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        current_fig = plt.gcf()
        plt.close()
        
        return current_fig

    
    def plot_multiple_charts(self):

        """Creates a list of Matplotlib figures of all possible charts that can be made within the data,
        from the user-inputted chart-type.
        """
        
        chart_list = []  
        # Loop through each of the x-axis variables and for each variable, plot it with an y-axis variable
        for x_variable in self.x_list:
            for y_variable in self.y_list:
                
                # Check that the 'x' variable and 'y' variable aren't the same, since we are plotting 'continuous' categories on each axis. 
                if x_variable != y_variable:
                    chart_list.append(self.create_chart(y_variable, x_variable))
                    
        return chart_list
                    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# if __name__ == "__main__":
    
#     # Set the rcParams from the Python File
#     from rcParams import RCParams
#     params = RCParams()
#     style = 7
#     params.change_style(params.style_list[style])  #'dark_background'

#     file = r'###############################################/.csv'
#     dataframe = pd.read_csv(file)          

#     scatter_instance = ScatterPlot(pd_dataframe=dataframe,
#                                    color_code=None,
#                                    custom_title=None,
#                                    xtick_rotation=None,
#                                    legend_on="on",
#                                    current_style=style,
#                                    orientation=None)

#     scatter_instance.plot_multiple_charts()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

