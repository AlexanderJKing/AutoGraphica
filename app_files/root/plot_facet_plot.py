"""root.plot_facet_plot
Imports the FacetPlot class for creating an instance of a facet plot and plotting it.
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

# import the classes from the custom modules needed during instantiation of any Chart Class
from support_main_classes import ColumnAttributes, DataframeOverview
from support_plotting import Plotting
from support_rcParams import RCParams
from support_facets import Facets
pd.options.mode.chained_assignment = None  # default='warn'


class FacetPlot(Facets):
    
    """
    A class for instantiating a 'facet plot' object.
    This object is for splitting high cardinal categorical values into subplots.
    
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
    figure_width: int
        The width of the figure.
    figure_height: int
        The height of the figure.
    current_style: str
        A valid Matplotlib style.
    palette: str
        A valid seaborn palette option.
    n_bars_per_facet: int
        A value specifying the number of bars within each facet (subplot).
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
                 figure_width: int=15,
                 figure_height: int=15,
                 current_style: str=None,
                 palette: str=None,
                 n_bars_per_facet: int=10):
        
        self.overview = DataframeOverview(pd_dataframe)
        self.plot_funcs = Plotting()
        self.rcparams = RCParams()
        self.df = copy.copy(self.overview.dataframe)
        
        self.color_code = color_code
        self.custom_title = custom_title
        self.xtick_rotation = xtick_rotation
        self.figure_width = figure_width
        self.figure_height = figure_height
        self.current_style = current_style
        self.palette = palette
        self.n_bars_per_facet = n_bars_per_facet
        self.chart_type = 'Facet'
        
        self.chart_rules() 
        self.return_default_n_bars_per_facet()
        self.return_minimum_width_per_facet()
        self.return_minimum_height_per_facet()
        self.plot_funcs.set_plot_style(self.current_style)
        self.default_xtick_rotation()


    def default_xtick_rotation(self):

        "Sets the default position and type for all 'x-axis' ticks."

        try:
            self.xtick_rotation = float(self.xtick_rotation)
            self.xtick_rotation = int(self.xtick_rotation)
        except (ValueError, TypeError) as e:
            self.xtick_rotation = 0
        
        
    def return_default_n_bars_per_facet(self):

        "This function sets the default number of bars per facet (subplot) if the user did not specify."
        
        # Need to make sure that we aren't plotting '0' and that the user accepts the default if they don't want to change anything, which is '10'. 
        if self.n_bars_per_facet is None:
            self.n_bars_per_facet = 10

    
    def return_minimum_width_per_facet(self):

        "This function sets the default width of the figure, if the user did not specify."
        
        if self.figure_width is None:
            self.figure_width = 15

    
    def return_minimum_height_per_facet(self):

        "This function sets the default height of the figure, if the user did not specify."
        
        if self.figure_height is None:
            self.figure_height = 15
            
        
    def chart_rules(self):

        """This function determines which columns in a DataFrame are suitable for the 'x' and 'y' columns in a Facet Plot.
        if a column is of type 'Nominal', 'Nominal-Binary' or 'Ordinal', then it is valid for plotting along an 'x-axis'. 
        If a column is of type 'Continuous' or 'Discrete', then it is valid for plotting along a 'y-axis'.
        """
        
        # A bar chart will deal with categorical data on the 'x-axis'. 
        x_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Nominal'\
                       or column.data_category == 'Nominal-Binary'\
                       or column.data_category == 'Ordinal']
        
        # We will need to display the data differently if the number of bars gets too many. 
        # Therefore we will create a separate list, limited to variables with bars that can actually fit on the 'a-axis'.
        self.high_cardinal_x_variables = [x_variable for x_variable in x_list if self.plot_funcs.unique_threshold(self.df[x_variable]) is False]
        
        for high_x_variable in self.high_cardinal_x_variables:
            self.plot_funcs.check_categorical_dtype(self.df, high_x_variable)
        
        self.y_list = [column.column_name for column in list(self.overview.column_attributes.values())\
                       if column.data_category == 'Continuous'\
                       or column.data_category == 'Discrete']   
                
        
    def create_chart(self, high_card_var, y_axis_var):

        """Creates a Facet Plot

        Parameters
        ----------
        high_card_var: pd.Series
            A 'Nominal'/'Nominal-Binary'/'Ordinal' column within the DataFrame that has been evaluated to have too high a cardinality 
        y_axis_var:
            A 'Continuous'/'Discrete' column within the DataFrame
        """
        
        df_index = 0
        # 1) CALCULATE THE NUMBER OF ROWS, AND THE NUMBER OF COLUMNS
        rows, cols = Facets.calculate_nrows_ncols(pd_dataframe=self.df,
                                                  high_cardinal_variable=high_card_var,
                                                  n_bars=self.n_bars_per_facet,
                                                  number_of_columns=4)
        
        # 2) SPLIT THE DATAFRAME INTO A LIST OF SUB-DATAFRAMES (BASED ON USER DEFINED NUMBER OF BARS PER PLOT)         
        df_list = Facets.create_faceted_dataframes(pd_dataframe=self.df,
                                                   high_cardinal_variable=high_card_var,
                                                   n_bars=self.n_bars_per_facet)
        
        # 3) DEFINE THE MATPLOTLIB FIGURE AND AXES 
        fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(self.figure_width, self.figure_height), constrained_layout=True)
        
        # 4) LOOP THORUGH ALL THE ROWS, LOOP THROUGH ALL THE COLUMNS
        for row_ind in range(0, rows):
            for col_ind in range(0, cols):
        
                if df_index != len(df_list):
                    
                    # 5) FOR EACH ITERATION OF THE LOOP, ADD A 'BAR' CHART THROUGH THE AXES, TO THE FACET.
                    # Add in a bar chart with the 'labels' (unique values of the x-axis) and the values (some 'continuous' variable on the 'y-axis') at the specified 'axes' location. 
                    axes[row_ind, col_ind].bar(x=df_list[df_index][high_card_var].unique(),
                                               height=df_list[df_index][y_axis_var],
                                               color=self.plot_funcs.check_valid_color(self.color_code, self.palette),
                                               width=0.6, 
                                               edgecolor=self.plot_funcs.define_edgecolor(self.current_style),
                                               linewidth=0.5)                    
                    
                    # 6) ROTATE THE X-AXIS TICKS
                    axes[row_ind, col_ind].tick_params("x", labelrotation=float(self.plot_funcs.set_xaxis_rotation(user_xtick_rotation=self.xtick_rotation,
                                                                                                                   pd_series=df_list[df_index][high_card_var],
                                                                                                                   orientation=None)))
                    axes[row_ind, col_ind].tick_params("x", labelsize=5.0)
                    axes[row_ind, col_ind].tick_params("y", labelsize=5.0)
                    
                    # 7) ADD THE LABELS FOR THE 'Y' AXES WHEN THE COLUMN POSITION IS AT 0
                    # Set the y-label for the left-side axes. 
                    if col_ind == 0:
                        axes[row_ind, col_ind].set_ylabel(y_axis_var, fontsize=6)
                    
                    df_index += 1

                else:
                    # if we reach the end of the list of DataFrames, then 'break'. 
                    break
                    
        # 8) DELETE ANY SPARE AXES 
        Facets.delete_spare_axes(figure=fig,
                                 axes_objects=axes,
                                 list_of_dataframes=df_list,
                                 n_rows=rows,
                                 n_cols=cols)
        
        # 9) CREATE THE TITLE FOR THE CHART
        if self.custom_title is None:
            facet_title = f"'{y_axis_var}' / '{high_card_var}' {self.chart_type} Chart"
        else:
            facet_title = self.custom_title
        
        if self.figure_height >= 18 and self.figure_height < 20:
            y_ = 1.0
        elif self.figure_height >= 20 and self.figure_height < 23:
            y_ = 1.02
        elif self.figure_height >= 23 and self.figure_height < 25:
            y_ = 1.035
        elif self.figure_height >= 25 and self.figure_height < 30:
            y_ = 1.05
        elif self.figure_height > 30:
            y_ = 1.08
        else:
            y_ = 0.98 
        plt.suptitle(facet_title, y=y_, fontsize='small', fontweight='normal', color=self.plot_funcs.define_edgecolor(self.current_style))
  
        # 10) TIGHTEN THE LAYOUT AND PLOT THE FIGURE
        plt.tight_layout()
        current_fig = plt.gcf()
        plt.close() 
        return current_fig 
        
    def plot_facet_chart(self, high_cardinal_var, y_axis_var):

        """Creates a list of Matplotlib figures of all possible charts that can be made within the data,
        from the user-inputted chart-type.
        """
        
        chart_list = []
        if len(self.high_cardinal_x_variables) > 0:
            chart_list.append(self.create_chart(high_cardinal_var, y_axis_var))
            
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

#     facetplot_instance = FacetPlot(pd_dataframe=dataframe,
#                                    color_code=None,
#                                    custom_title=None,
#                                    xtick_rotation=None,
#                                    current_style=style,
#                                    orientation=None,
#                                    palette=None,
#                                    single_axes=True,
#                                    n_bars_per_facet=10)


#     facetplot_instance.plot_facet_chart(high_cardinal_var='Generator_Reference', y_axis_var='MEC_MW')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#


