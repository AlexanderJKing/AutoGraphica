"""root.plot_bar_chart
Imports the BarChart class for creating an instance of a bar chart and plotting it.
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


class BarChart:
    
    """
    A class for instantiating a 'bar chart' object
    
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
    single_axes: str
        A value specifying whether to display on a single axis or an additional axis.
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
                 xtick_rotation: int=None,
                 legend_on: str="on",
                 current_style: str=None,
                 orientation: str=None,
                 single_axes: str="on"):
        
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
        self.single_axes = single_axes
        self.chart_type = 'Bar'
        
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

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Bar Chart.
        if a column is of type 'Nominal', 'Nominal-Binary' or 'Ordinal', then it is valid for plotting along an 'x-axis'. 
        If a column is of type 'Continuous' or 'Discrete', then it is valid for plotting along a 'y-axis'.
        Variables deemed to have too high a cardinality, are filtered out.
        """
        
        # A bar chart will deal with categorical data on the 'x-axis'. 
        x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Nominal'\
                       or column.data_category == 'Nominal-Binary'\
                       or column.data_category == 'Ordinal']
        
        # We will need to display the data differently if the number of bars gets too many. 
        # Therefore we will create a separate list, limited to variables with bars that can actually fit on the 'a-axis'.
        self.x_list = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is True]
        self.high_cardinal_x_variables = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is False]
        
        # Make sure that all data is of type 'object' ('Nominal-Binary' mighn't be for example). 
        for x_variable in self.x_list:
            self.plot_funcs.check_categorical_dtype(self.df, x_variable)
        
        # Numerical data on the 'y-axis'
        self.y_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous'\
                       or column.data_category == 'Discrete']   
        
        
    def create_single_axes_chart(self, x_axis_var): 

        """Creates a Bar Chart along a single axis
        
        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, ax = plt.subplots(figsize=(4, 3))
        
        # 2) INSTANTIATE A 'PLOT' OBJECT FROM THE 'seaborn.objects' INTERFACE (so) 
        if self.orientation == 'horizontal':
            plot = sns.countplot(self.df,
                                 y=self.df[x_axis_var],
                                 color=self.color_code,
                                 edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                 linewidth=0.6)
        else:
            plot = sns.countplot(self.df,
                                 x=self.df[x_axis_var],
                                 color=self.color_code,
                                 edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                 linewidth=0.6)
        
        # 3) ADD THE LABELS FOR THE AXES
        if self.orientation == 'horizontal':
            ax.set_ylabel(x_axis_var, fontsize=6)
            ax.set_xlabel("Count", fontsize=6)
        else:
            ax.set_xlabel(x_axis_var, fontsize=6)
            ax.set_ylabel("Count", fontsize=6)

        # 4) CREATE THE TITLE FOR THE CHART
        self.plot_funcs.create_title(custom_title=self.custom_title,
                                     chart_type=self.chart_type,
                                     axis_variable1=x_axis_var,
                                     axis_variable2=None,
                                     current_style=self.current_style)
        
        # 5) CREATE THE LEGEND FOR THE CHART   
        self.plot_funcs.create_legend(legend_on=self.legend_on,
                                      chart_type=self.chart_type,
                                      axis_variable1=x_axis_var,
                                      axis_variable2=None,
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
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)
        plt.tight_layout()
        current_fig = plt.gcf()
        plt.close()
        
        return current_fig
        
        
    def create_double_axes_chart(self, x_axis_var, y_axis_var):

        """Creates a Bar Chart along a dual axes
        
        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame
        y_axis_var: pd.Series
            A 'Continuous'/'Discrete' column within the DataFrame
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, ax = plt.subplots(figsize=(4, 3))
        
        # 2) INSTANTIATE A 'PLOT' OBJECT FROM THE 'seaborn.objects' INTERFACE (so) 
        if self.orientation == 'horizontal':
            double_plot = sns.barplot(self.df,
                                      x=self.df[y_axis_var],
                                      y=self.df[x_axis_var],
                                      color=self.color_code,
                                      edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                      linewidth=0.6,
                                      errorbar=None)
        else:
            double_plot = sns.barplot(self.df,
                                      x=self.df[x_axis_var],
                                      y=self.df[y_axis_var],
                                      color=self.color_code,
                                      edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                      linewidth=0.6,
                                      errorbar=None)
        
        # 3) ADD THE LABELS FOR THE AXES
        if self.orientation == 'horizontal':
            ax.set_xlabel(y_axis_var, fontsize=6)
            ax.set_ylabel(x_axis_var, fontsize=6)
        else:
            ax.set_xlabel(x_axis_var, fontsize=6)
            ax.set_ylabel(y_axis_var, fontsize=6)
        
        # 4) CREATE THE TITLE FOR THE CHART
        self.plot_funcs.create_title(custom_title=self.custom_title,
                                     chart_type=self.chart_type,
                                     axis_variable1=y_axis_var,
                                     axis_variable2=None,
                                     current_style=self.current_style)
        
        # 5) CREATE THE LEGEND FOR THE CHART 
        self.plot_funcs.create_legend(legend_on=self.legend_on,
                              chart_type=self.chart_type,
                              axis_variable1=y_axis_var,
                              axis_variable2=None,
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
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)
        plt.tight_layout()
        current_fig = plt.gcf()
        plt.close()
        
        return current_fig
        
        
    def plot_multiple_charts(self):

        """Creates a list of Matplotlib figures of all possible charts that can be made within the data,
        from the user-inputted chart-type.
        """
        
        chart_list = []
        # Loop through each of the y-axis variables and for each variable, plot it with an x-axis variable
        if (self.single_axes == 'on' or self.single_axes is None) and len(self.x_list) > 0:            
            for x_variable in self.x_list:
                chart_list.append(self.create_single_axes_chart(x_variable))
                
        elif self.single_axes == 'off' and len(self.x_list) > 0: 
            for x_variable in self.x_list:
                for y_variable in self.y_list:
                    chart_list.append(self.create_double_axes_chart(x_variable, y_variable))
                    
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

#     bar_instance = BarChart(pd_dataframe=dataframe,
#                             color_code=None,
#                             custom_title=None,
#                             xtick_rotation=None,
#                             legend_on="on",
#                             current_style=style,
#                             orientation=None,
#                             single_axes="on")

#     bar_instance.plot_multiple_charts()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

