"""root.plot_pie_chart
Imports the PieChart class for creating an instance of a pie chart and plotting it.
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


class PieChart:
    
    """
    A class for instantiating a 'pie chart' object

    Attributes
    ----------
    pd_dataframe: pd.DataFrame
        The DataFrame from the file submitted by the user.
    color_code: str
        A valid Matplotlib color code.
    custom_title: str
        A valid title for the plot.
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
    rotation: int
        A value specifying to what degree the user wishes to rotate the pie chart.
    chosen_slice: str
        A string input indicating if the user wishes to explode the smallest or largest slice in the pie chart.
    donut: str
        A string input indicating if the user wishes to display the pie chart as a donut chart.
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
                 legend_on: str="on",
                 space_legend_out: float=None,
                 current_style: str=None,
                 orientation: str=None,
                 palette: str=None,
                 rotation: int=None,
                 chosen_slice: str=None,
                 donut: str="off"):
        
        self.overview = DataframeOverview(pd_dataframe)
        self.plot_funcs = Plotting()
        self.rcparams = RCParams()
        self.df = copy.copy(self.overview.dataframe)
        
        self.color_code = color_code
        self.custom_title = custom_title
        self.legend_on = legend_on
        self.space_legend_out = space_legend_out
        self.current_style = current_style
        self.orientation = orientation
        self.palette = palette
        self.rotation = rotation
        self.chosen_slice = chosen_slice
        self.donut = donut
        self.chart_type = 'Pie'
        
        self.chart_rules()
        self.plot_funcs.set_plot_style(self.current_style)

    
    def chart_rules(self):

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Pie Chart.
        if a column is of type 'Nominal', 'Nominal-Binary' or 'Ordinal', then it is valid for plotting along an 'x-axis'. 
        Variables deemed to have too high a cardinality, are filtered out.
        """
        
        # A bar chart will deal with categorical data on the 'x-axis'. 
        x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Nominal'\
                       or column.data_category == 'Nominal-Binary'\
                       or column.data_category == 'Ordinal']
        
        # We will need to display the data differently if the number of slices gets too many. 
        # Therefore we will create a separate list, limited to variables with bars that can actually fit on the 'x-axis'.
        self.x_list = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is True]
        
        for x_variable in self.x_list:
            self.plot_funcs.check_categorical_dtype(self.df, x_variable)            
        
        
    def create_chart(self, x_axis_var):

        """Creates a Pie Chart
        
        Parameters
        ----------
        x_axis_var: pd.Series
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame.
        """
        
        # 1) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, ax = plt.subplots(figsize=(4, 3))
    
        # 2) APPLY ANY WEDGES OR EXPLODED SLICES AS SPECIFIED (IF ANY)
        # Get the wedges, returns 'None', if 'donut' is 'False'
        wedge_props = self.plot_funcs.apply_donut(self.donut, self.current_style)
        # explode_slice (Can either be 'None' - 'Largest' - 'Smallest')
        explode_ = self.plot_funcs.explode_slice(self.df[x_axis_var], self.chosen_slice)
        
        # 3) GET THE DATA AS A PERCENTAGE OF 100%
        data = self.plot_funcs.create_percentage_data(self.df[x_axis_var])[0]
        # Basically, if the 'legend' is turned on, we're going to migrate all the labels onto that, instead of on the plot. 
        if self.legend_on == "on":
            labels = None
            legend_labels = self.plot_funcs.create_percentage_data(self.df[x_axis_var])[1]
        else:
            labels = self.plot_funcs.create_percentage_data(self.df[x_axis_var])[1]
            legend_labels = None
        
        # 4) RETURN THE TEXT PARAMETERS FOR BOTH INSIDE THE PIE CHART AND ON THE LEGEND
        # Return the parameters as they are in proportion to the number of variables in the Pi Chart. 
        size_params = self.plot_funcs.pie_chart_size_parameters(self.df[x_axis_var], self.donut)
        pct, font = size_params[0], size_params[1]
        
        legend_params = self.plot_funcs.space_legend_out(self.df[x_axis_var], self.space_legend_out)
        legend_font, legend_bbox_anchor = legend_params[0], legend_params[1]
        
        # 5) CREATE THE PIE CHART
        patches, texts, autotexts = plt.pie(data,
                                            labels=labels,
                                            colors=sns.color_palette(self.palette),
                                            explode=explode_,
                                            startangle=self.plot_funcs.apply_rotation(self.rotation),
                                            autopct="%1.1f%%",
                                            pctdistance=pct,
                                            textprops={'fontsize': font, 'weight': 'bold'},
                                            wedgeprops=wedge_props)
        
        # 6) SET THE COLOR OF THE TEXT AND AUTOTEXT ACCORDINGLY, BASED ON THE STYLE AND PALETTE BEING USED. 
        # Sets the color of the text (labels) based on whether the style is darkmode or not, AND.....
        # Sets the color of the autotext (percentages) based on whether the palette is 'dark' or 'light'. 
        [text.set_color(self.plot_funcs.define_edgecolor(self.current_style)) for text in texts]
        [autotext.set_color(self.color_code) if self.color_code is not None else autotext.set_color(self.plot_funcs.check_palette_type(self.palette)) for autotext in autotexts]
        
        # 7) CREATE THE TITLE FOR THE CHART
        self.plot_funcs.create_title(custom_title=self.custom_title,
                                     chart_type=self.chart_type,
                                     axis_variable1=x_axis_var,
                                     axis_variable2=None,
                                     current_style=self.current_style)
        
        # 8) CREATE THE LEGEND FOR THE CHART                
        self.plot_funcs.create_legend(legend_on=self.legend_on,
                                      chart_type=self.chart_type,
                                      axis_variable1=legend_labels,
                                      axis_variable2=None,
                                      color_code=self.color_code,
                                      patches_=patches,
                                      font_size=legend_font,
                                      bbox_anchor=legend_bbox_anchor,
                                      figure=None,
                                      legend_title=x_axis_var,
                                      current_style=self.current_style)
        # Make sure the legend tite is set to the same color as the labels (i.e. 'white' or 'black')
        if self.legend_on == "on":
            ax.get_legend().get_title().set_color(self.plot_funcs.define_edgecolor(self.current_style))
        
        # 9) TIGHTEN THE LAYOUT AND PLOT THE FIGURE
        plt.tight_layout()        
        current_fig = plt.gcf()
        plt.close()
        
        return current_fig
        
        
    def plot_multiple_charts(self):

        """Creates a list of Matplotlib figures of all possible charts that can be made within the data,
        from the user-inputted chart-type.
        """
        
        chart_list = []
        if len(self.x_list) > 0:
        
            for x_variable in self.x_list:
                chart_list.append(self.create_chart(x_variable))
                
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

#     pie = PieChart(pd_dataframe=dataframe,
#                  color_code=None,
#                  custom_title=None,
#                  legend_on="on",
#                  current_style=style,
#                  orientation=None,
#                  palette=None,
#                  rotation=None,
#                  chosen_slice=None,
#                  donut=False)

#     pie.plot_multiple_charts()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

