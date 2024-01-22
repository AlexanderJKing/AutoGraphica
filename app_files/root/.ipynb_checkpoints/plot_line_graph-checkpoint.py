"""root.plot_line_graph
Imports the LineGraph class for creating an instance of a line chart and plotting it.
Small demo on instantiating it as an object if this is run as a script.
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import warnings
warnings.filterwarnings("ignore")

import copy
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the ticker and DayLocator for specifying how ticks for date and time are managed. 
import matplotlib.ticker as ticker
from matplotlib.dates import DayLocator

# import the classes from the custom modules needed during instantiation of any Chart Class
from support_main_classes import ColumnAttributes, DataframeOverview
from support_plotting import Plotting
from support_rcParams import RCParams
pd.options.mode.chained_assignment = None  # default='warn'


class LineGraph:

    """
    A class for instantiating a 'line graph' object
    
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
    error_bar_type: str
        The type of error bar to display in the plot.
    error_bar_value: int
        The value for the respective error bar type chosen prior.
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
                 error_bar_type: str=None,
                 error_bar_value: int=None):
        
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
        self.error_bar_type = error_bar_type
        self.error_bar_value = error_bar_value
        self.chart_type = 'Line'
        
        self.chart_rules()
        self.plot_funcs.set_plot_style(self.current_style)
        self.default_xtick_rotation()

    def default_xtick_rotation(self):

        "Sets the default position and type for all 'x-axis' ticks."

        try:
            self.xtick_rotation = int(self.xtick_rotation)
        except (ValueError, TypeError) as e:
            self.xtick_rotation = 0
        
    def locator_interval(self, date_series, optimal_tick_no=20):

        """This function smoothes the interval between ticks when plotting date figures

        Parameters
        ----------
        date_series: pd.Series
            The column within the DataFrame that is of type 'Datetime'.
        optimal_tick_no: int
            The optimal number of ticks to fit along the axis.
        """

        # Calculates the optimum interval between dates, to fit around 20 major ticks on the Figure
        date_difference = max(date_series) - min(date_series)
        
        # If the difference in days is actually smaller than the optimal ticks, then ideally we just want 1 tick per day. 
        if int(date_difference.days) >= optimal_tick_no: 
            locator_result = math.ceil(date_difference.days / optimal_tick_no)
        else:
            locator_result = date_difference.days

        return locator_result
    
        
    def chart_rules(self):

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Line Graph.
        if a column is of type 'Date', 'Time' or 'Continuous', then it is valid for plotting along an 'x-axis'. 
        If a column is of type 'Continuous', then it is valid for plotting along a 'y-axis'.
        """
                 
        self.x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Date'\
                       or column.data_category == 'Time'\
                       or column.data_category == 'Continuous']
        
        # Continuous variables
        self.y_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous']      
    
    
    def create_chart(self, x_axis_var, y_axis_var, time_var=False):

        """Creates a Line Graph

        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Date'/'Time'/'Continuous' column within the DataFrame
        y_axis_var: pd.Series
            A 'Continuous' column within the DataFrame
        time_var: bool
            A boolean value indicating whether a variable representing just time is present.
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, ax = plt.subplots(figsize=(4, 3))
        
        # 2) DEFINE THE ERRORBAR - IF ANY
        if self.error_bar_type is None:
            self.errorbar_tuple = ("ci", int(0))
        else:
            print(type(self.error_bar_value))
            self.errorbar_tuple = (self.error_bar_type, int(self.error_bar_value))
                
        # 2) INSTANTIATE A 'PLOT' OBJECT FROM THE 'seaborn.objects' INTERFACE (so)    
        if self.orientation == 'horizontal':
            if time_var is True:
                # We need to serialize the TimeDelta range to hours
                converted_time_series = self.df[x_axis_var].dt.seconds.apply(self.overview.dt.convert_timedelta)
                plot = sns.lineplot(self.df,
                                    x=self.df[y_axis_var],
                                    y=converted_time_series,
                                    color=self.color_code,
                                    errorbar=self.errorbar_tuple)
                ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
            elif time_var is False:
                plot = sns.lineplot(self.df,
                                    x=self.df[y_axis_var],
                                    y=self.df[x_axis_var],
                                    color=self.color_code,
                                    errorbar=self.errorbar_tuple)
                ax.yaxis.set_major_locator(DayLocator(interval=self.locator_interval(self.df[x_axis_var])))
            else:
                plot = sns.lineplot(self.df,
                                    x=self.df[y_axis_var],
                                    y=self.df[x_axis_var],
                                    color=self.color_code, 
                                    errorbar=self.errorbar_tuple)
                
        else:
            if time_var is True:
                converted_time_series = self.df[x_axis_var].dt.seconds.apply(self.overview.dt.convert_timedelta)
                plot = sns.lineplot(self.df,
                                    x=converted_time_series,
                                    y=self.df[y_axis_var],
                                    color=self.color_code,
                                    errorbar=self.errorbar_tuple)
                ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
            elif time_var is False:
                plot = sns.lineplot(self.df,
                                    x=self.df[x_axis_var],
                                    y=self.df[y_axis_var],
                                    color=self.color_code,
                                    errorbar=self.errorbar_tuple)
                ax.xaxis.set_major_locator(DayLocator(interval=self.locator_interval(self.df[x_axis_var])))
            else:
                plot = sns.lineplot(self.df,
                                    x=self.df[x_axis_var],
                                    y=self.df[y_axis_var],
                                    color=self.color_code,
                                    errorbar=self.errorbar_tuple)
        
        # 3) ADD THE LABELS FOR THE AXES
        if self.orientation == 'horizontal':
            ax.set_xlabel(y_axis_var, fontsize=10)
            ax.set_ylabel(x_axis_var, fontsize=10)
        else:
            ax.set_xlabel(x_axis_var, fontsize=10)
            ax.set_ylabel(y_axis_var, fontsize=10)
            
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
        if time_var is True:
            plt.xticks(rotation=self.plot_funcs.set_xaxis_rotation(user_xtick_rotation=self.xtick_rotation,
                                                                   pd_series=converted_time_series,
                                                                   orientation=self.orientation))    
        else:
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
        # Loop through each of the x-axis variables and for each variable, plot it with a y-axis variable
        for x_variable in self.x_list:
            for y_variable in self.y_list:
                
                # Check that the 'x' variable and 'y' variable aren't the same, since we are plotting 'continuous' categories on each axis. 
                if x_variable != y_variable:
                    if self.df[x_variable].dtype == 'datetime64[ns]':
                        chart_list.append(self.create_chart(x_variable, y_variable, time_var=False))

                    elif self.df[x_variable].dtype == 'timedelta64[ns]':
                        chart_list.append(self.create_chart(x_variable, y_variable, time_var=True))
                        
                    elif self.df[x_variable].dtype == 'float64':
                        chart_list.append(self.create_chart(x_variable, y_variable, time_var=None))
                        
        return chart_list

       
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# if __name__ == "__main__":
    
#     # Set the rcParams from the Python File
#     from rcParams import RCParams
#     params = RCParams()
#     style = 4
#     params.change_style(params.style_list[style])  #'dark_background'

#     file = r'###############################################/.csv'
#     dataframe = pd.read_csv(file)

#     line_instance = LineGraph(pd_dataframe=dataframe,
#                               color_code=None,
#                               custom_title=None,
#                               xtick_rotation=None,
#                               legend_on="on",
#                               current_style=style,
#                               orientation=None,
#                               error_bar_type=None,
#                               error_bar_value=None)

#     line_instance.plot_multiple_charts()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

