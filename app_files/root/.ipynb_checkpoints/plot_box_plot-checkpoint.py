"""root.plot_box_plot
Imports the BoxPlot class for creating an instance of a box plot and plotting it.
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


class BoxPlot:
    
    """
    A class for instantiating a 'box plot' object

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
    space_legend_out: int
        A value used to determine where the legend is placed in relation to the figure.
    current_style: str
        A valid Matplotlib style.
    orientation: str
        A value specifying whether data on the 'x-axis' is flipped to display on the 'y-axis'.
    palette: str
        A valid seaborn palette option.
    z_axis_color: str
        A value specifying whether to add a third variable along the 'z-axis' dimension, distinguished by color.
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
                 space_legend_out: int=None,
                 current_style: str=None,
                 orientation: str=None,
                 palette: str=None,
                 z_axis_color: str="off"):
        
        self.overview = DataframeOverview(pd_dataframe)
        self.plot_funcs = Plotting()
        self.rcparams = RCParams()
        self.df = copy.copy(self.overview.dataframe)
        
        self.color_code = self.plot_funcs.check_valid_color(color_code, palette)
        self.custom_title = custom_title
        self.xtick_rotation = xtick_rotation
        self.legend_on = legend_on
        self.space_legend_out = space_legend_out
        self.current_style = current_style
        self.orientation = orientation
        self.palette = palette
        self.z_axis_color = z_axis_color
        self.chart_type = 'Box'
        
        self.chart_rules()   
        self.plot_funcs.set_plot_style(self.current_style)
        self.outline_color = self.plot_funcs.define_edgecolor(self.current_style)
        self.default_xtick_rotation()
        

    def default_xtick_rotation(self):

        "Sets the default position and type for all 'x-axis' ticks."

        try:
            self.xtick_rotation = float(self.xtick_rotation)
            self.xtick_rotation = int(self.xtick_rotation)
        except (ValueError, TypeError) as e:
            self.xtick_rotation = 0

    def check_z_axis_var(self, z_axis_var):
        
        if self.z_axis_color == "off":
            return None
        else:
            # Since 'z_axis_color' is True, we shouldn't get any errors, as we are not passing 'None' this time, but whatever the 'z_axis_var' has been set to. 
            return self.df[z_axis_var]
        
    def chart_rules(self):

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Box Plot.
        if a column is of type 'Nominal', 'Nominal-Binary' or 'Ordinal', then it is valid for plotting along an 'x-axis'. 
        If a column is of type 'Continuous', then it is valid for plotting along a 'y-axis'.
        
        Variables deemed to have too high a cardinality, are filtered out.
        All columns within available to the 'x-axis' for plotting, are also available to an addition 'z-axis' dimension for plotting.
        """
        
        x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                  if column.data_category == 'Nominal'\
                  or column.data_category == 'Nominal-Binary'\
                  or column.data_category == 'Ordinal']
        
        self.x_list = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is True]
        self.high_cardinal_x_variables = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is False]
        
        for x_variable in self.x_list:
            self.plot_funcs.check_categorical_dtype(self.df, x_variable)
        
        self.y_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous']   
        
        self.z_list = copy.copy(self.x_list)
        
    def create_legend_handles_labels(self, axes):

        """This function takes a Matplotlib axes object and extracts the handles and lables from its legend.

        Parameters
        ----------
        axes: plt.axes
            A Matplotlib axes object
        """
        
        # if self.z_axis_color == "on":
        # Get the current handles and labels
        handles, labels = axes.get_legend_handles_labels()
        # get and remove the current legend
        axes.get_legend().remove()
        return [handles, labels]
    
    def create_chart(self, x_axis_var, y_axis_var, z_axis_var=None):

        """Creates a Box Plot 
        
        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame
        y_axis_var: pd.Series
            A 'Continuous' column within the DataFrame
        z_axis_var:
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, axes = plt.subplots(figsize=(4, 3))
        
        # 2) INSTANTIATE A 'BoxPlot' OBJECT FROM THE 'seaborn' INTERFACE (sns) 
        if self.orientation == 'horizontal':
            box = sns.boxplot(data=self.df,
                              x=self.df[y_axis_var],
                              y=self.df[x_axis_var],
                              color=self.color_code,
                              hue=self.check_z_axis_var(z_axis_var),
                              palette=None,  # self.palette
                              flierprops={"markeredgecolor": self.outline_color, "markeredgewidth": 0.5},
                              whiskerprops={"color": self.outline_color, "linewidth": 0.5},
                              boxprops={"edgecolor": self.outline_color, "linewidth": 0.5},
                              medianprops={"color": self.outline_color, "linewidth": 0.5},
                              capprops={"color": self.outline_color, "linewidth": 0.5})
            
        else:
            box = sns.boxplot(data=self.df,
                              x=self.df[x_axis_var],
                              y=self.df[y_axis_var],
                              color=self.color_code,
                              hue=self.check_z_axis_var(z_axis_var),
                              palette=None,  # self.palette
                              flierprops={"markeredgecolor": self.outline_color, "markeredgewidth": 0.5},
                              whiskerprops={"color": self.outline_color, "linewidth": 1},
                              boxprops={"edgecolor": self.outline_color, "linewidth": 1},
                              medianprops={"color": self.outline_color, "linewidth": 1},
                              capprops={"color": self.outline_color, "linewidth": 1})

        # 3) ADD THE LABELS FOR THE AXES
        if self.orientation == 'horizontal':
            box.set_ylabel(x_axis_var, fontsize=8)
            box.set_xlabel(y_axis_var, fontsize=8)
        else:
            box.set_ylabel(y_axis_var, fontsize=8)
            box.set_xlabel(x_axis_var, fontsize=8)
        
        # remove default legend
        # axes_legend = axes.get_legend()
        # if (self.z_axis_color is None or self.z_axis_color == "off") and self.legend_on == "on" and axes_legend is not None:
        #     handles_labels = self.create_legend_handles_labels(axes)
        # elif (self.z_axis_color is not None or self.z_axis_color == "on") and (self.legend_on == "off" or self.legend_on is None) and axes_legend is not None:
        #     handles_labels = self.create_legend_handles_labels(axes)
        #     handles_labels = [None, None]
        # else:
        #     handles_labels = [None, None]

        axes_legend = axes.get_legend()
        if axes_legend is not None:
            handles_labels = self.create_legend_handles_labels(axes)
        else:
            handles_labels = [None, None]
            
        # 4) CREATE THE TITLE FOR THE CHART 
        self.plot_funcs.create_title(custom_title=self.custom_title,
                                     chart_type=self.chart_type,
                                     axis_variable1=x_axis_var,
                                     axis_variable2=None,
                                     current_style=self.current_style)
        
        # 5) ROTATE THE X-AXIS TICKS
        plt.xticks(rotation=self.plot_funcs.set_xaxis_rotation(user_xtick_rotation=self.xtick_rotation,
                                                               pd_series=self.df[x_axis_var],
                                                               orientation=self.orientation))
        
        # 6) TIGHTEN THE LAYOUT AND SET THE FONT SIZE OF TICKS AND LABELS
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        
        # 7) CREATE THE LEGEND FOR THE CHART                 
        if (self.z_axis_color == "off" or self.z_axis_color is None) and self.legend_on == "on":
            self.plot_funcs.create_legend(legend_on=self.legend_on,
                                          chart_type=self.chart_type,
                                          axis_variable1=x_axis_var,
                                          axis_variable2=None,
                                          color_code=self.color_code,
                                          patches_=None,
                                          font_size=8,
                                          bbox_anchor=None,
                                          figure=None,
                                          legend_title='',
                                          current_style=self.current_style)
            # Make sure the legend tite is set to the same color as the labels (i.e. 'white' or 'black')
            axes.get_legend().get_title().set_color(self.plot_funcs.define_edgecolor(self.current_style))
            
        elif (self.z_axis_color == "on" or self.z_axis_color is not None) and self.legend_on == "on":
            # Extract all the legend parameters
            legend_params = self.plot_funcs.space_legend_out(self.df[z_axis_var], self.space_legend_out)
            legend_font, legend_bbox_anchor = legend_params[0], legend_params[1]
                        
            self.plot_funcs.create_legend(legend_on=self.legend_on,
                                          chart_type="MultiBox",
                                          axis_variable1=handles_labels[0],
                                          axis_variable2=handles_labels[1],
                                          color_code=self.color_code,
                                          patches_=None,
                                          font_size=legend_font,
                                          bbox_anchor=legend_bbox_anchor,
                                          figure=fig,
                                          legend_title=z_axis_var,
                                          current_style=self.current_style)
            # Make sure the legend tite is set to the same color as the labels (i.e. 'white' or 'black')
            axes.get_legend().get_title().set_color(self.plot_funcs.define_edgecolor(self.current_style))
        
        current_fig = plt.gcf()
        # plt.plot()
        plt.close()
        
        return current_fig
        
        
    def plot_multiple_charts(self):

        """Creates a list of Matplotlib figures of all possible charts that can be made within the data,
        from the user-inputted chart-type.
        """
        
        chart_list = []
        if len(self.x_list) > 0:                
            for x_variable in self.x_list:
                for y_variable in self.y_list:
                    
                    if self.z_axis_color is False:
                        chart_list.append(self.create_chart(x_variable, y_variable))
                    else:
                        for z_variable in self.z_list:
                            if x_variable != z_variable:
                                chart_list.append(self.create_chart(x_variable, y_variable, z_variable))
                                
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

#     box_instance = BoxPlot(pd_dataframe=dataframe,
#                            color_code=None,
#                            custom_title=None,
#                            xtick_rotation=None,
#                            legend_on="on",
#                            current_style=style,
#                            orientation=None,
#                            palette=None,
#                            z_axis_color=False)

#     box_instance.plot_multiple_charts()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

