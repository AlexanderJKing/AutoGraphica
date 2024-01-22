"""root.chart_modules_support.plotting
A module dedicated towards buffering or supporting different plotting operations for each of the charts in the 'chart_modules' subpackage.
"""
import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import warnings
warnings.filterwarnings("ignore")

import copy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like
from matplotlib.lines import Line2D
from matplotlib import patches
import seaborn as sns

from support_rcParams import RCParams

pd.options.mode.chained_assignment = None  # default='warn'


class Plotting:
    
    """A class for instantiating an object intended to be a 'component' in a 'chart objects' initialization, 
    it will add additional methods and operations for plotting the actual charts."""
    
    def set_plot_style(self, plot_style):
        
        if plot_style is not None:
            plt.style.use(plot_style)
        else:
            pass
    
    
    def check_categorical_dtype(self, dataframe, column):
        
        """Need this method to avoid a 'TypeError' when using str accessors. 
        We need to use a str accessor when checking the character length of a value for the x-axis rotation (str.len())
        To fully convert a column to an 'object' dtype, we actually need to convert it to 'str'."""
        
        if dataframe[column].dtype != 'object':
            # We need to convert to 'str' for it to fully convert the values in the series to 'object'. 
            dataframe[column] = dataframe[column].astype('str')
        

        
    def unique_threshold(self, pd_series, thresh_val=30):
        
        """Need to determine that the number of values in the series, will actually fit as columns,
        If its more than the arbitrary 'thresh_val' then a different plot (like a facet plot, etc). should be recommended. 
        """
        
        if len(pd_series.unique()) <= thresh_val:
            return True
        else:
            return False
        
        
        
    def create_title(self, custom_title: str, chart_type: str, axis_variable1, axis_variable2=None, current_style=None):
                
        if custom_title is not None:
             plt.suptitle(custom_title, y=0.98, fontsize='large', fontweight='normal', color=self.define_edgecolor(current_style))
        else:
            if chart_type == 'Line':
                default_title = f"'{axis_variable1}'  {chart_type} Chart"
                
            elif chart_type == 'Scatter':
                default_title = f"'{axis_variable1}' / '{axis_variable2}'  {chart_type} Plot"
                
            elif chart_type == 'Histogram':
                default_title = f"'{axis_variable1}'  {chart_type}"
                
            elif chart_type == 'Bar':
                default_title = f"'{axis_variable1}' {chart_type} Chart"
            
            elif chart_type == 'Pie':
                default_title = f"'{axis_variable1}' {chart_type} Chart"
                
            elif chart_type == 'Box':
                default_title = f"'{axis_variable1}' {chart_type} Plot"
            
            elif chart_type == 'MultiLine':
                default_title = f"'{axis_variable1}' / '{axis_variable2}'  {chart_type} Chart"
                
            elif chart_type == 'MultiScatter':
                default_title = f"'{axis_variable1}' / '{axis_variable2}' {chart_type} Plot"
                
            elif chart_type == 'MultiBar':
                default_title = f"'{axis_variable1}' {chart_type} Chart"
                
            plt.suptitle(default_title, y=0.98, fontsize='large', fontweight='normal', color=self.define_edgecolor(current_style))
        
        
    
    def create_legend(self, legend_on: str, chart_type: str, axis_variable1, axis_variable2=None,
                      color_code=None, patches_=None, font_size=None, bbox_anchor=None, figure=None, legend_title='', current_style=None):
                
        # We need to split up a column that has too many unique categorical values, as defined by the threshold.
        if chart_type == "Line" and legend_on == "on":
            handle = Line2D([0], [0], color=color_code, alpha=0.5)
            return plt.legend(handles=[handle], labels=[axis_variable1], loc='upper right', title=legend_title, labelcolor=self.define_edgecolor(current_style), fontsize="8")
        
        elif chart_type == "Scatter" and legend_on =="on":
            handle = Line2D([0], [0], linestyle='None', color=color_code, marker='o', markerfacecolor=color_code, alpha=0.5)
            return plt.legend(handles=[handle], labels=[axis_variable1], loc='upper right', title=legend_title, labelcolor=self.define_edgecolor(current_style), fontsize="8")
            
        elif chart_type == "Bar" and legend_on == "on":
            handle = patches.Patch(color=color_code, alpha=0.5)
            return plt.legend(handles=[handle], labels=[axis_variable1], loc='upper right', title=legend_title, labelcolor=self.define_edgecolor(current_style), fontsize="8")
        
        elif chart_type == "Box" and legend_on == "on":
            handle = patches.Patch(color=color_code, alpha=0.5)
            return plt.legend(handles=[handle], labels=[axis_variable1], loc='upper right', title=legend_title, labelcolor=self.define_edgecolor(current_style), fontsize="8")
        
        elif chart_type == "Pie" and legend_on == "on":
            return plt.legend(handles=patches_, labels=axis_variable1, loc='upper right', fontsize=font_size, bbox_to_anchor=bbox_anchor, title=legend_title, labelcolor=self.define_edgecolor(current_style))
        
        elif chart_type == "Histogram" and legend_on == "on":
            handle = patches.Patch(color=color_code, alpha=0.5)
            plt.legend(handles=[handle], labels=[axis_variable1], loc='upper right', title=legend_title, labelcolor=self.define_edgecolor(current_style), fontsize="8")
                          
        elif chart_type == "MultiLine" and legend_on == "on":
            plt.legend(handles=axis_variable1, labels=axis_variable2, loc='upper right', fontsize=font_size, bbox_to_anchor=bbox_anchor, title=legend_title, labelcolor=self.define_edgecolor(current_style))
            
        elif chart_type == "MultiScatter" and legend_on == "on":
            plt.legend(handles=axis_variable1, labels=axis_variable2, loc='upper right', fontsize=font_size, bbox_to_anchor=bbox_anchor, title=legend_title, labelcolor=self.define_edgecolor(current_style))
            
        elif chart_type == "MultiBar" and legend_on == "on":
            plt.legend(handles=axis_variable1, labels=axis_variable2, loc='upper right', fontsize=font_size, bbox_to_anchor=bbox_anchor, title=legend_title, labelcolor=self.define_edgecolor(current_style))
            
        elif chart_type == "MultiBox" and legend_on == "on":
            return plt.legend(handles=axis_variable1, labels=list(axis_variable2), loc='upper right', fontsize=font_size, bbox_to_anchor=bbox_anchor, title=legend_title, labelcolor=self.define_edgecolor(current_style))

        
        
    def set_xaxis_rotation(self, user_xtick_rotation, pd_series, orientation=None):
        
        """Check the character length of each string, in this case, column values that are categorical:
        Strings >= 12 should be rotated 90 degress. 
        Strings <= 4 should not be rotated at all. 
        Strings <=4 and >= 12 should be rotated 45 degrees
        
        x_tick_rotation that is not 'None' (i.e. the user entered something) should be adjusted to whatever the user entered.
        """
        
        len_check_series = pd_series.astype(str).str.len()
        char_count_dict = {pd_series[i]: len_check_series[i] for i in range(len(pd_series))}
        char_len_list = list(char_count_dict.values())
        
        if orientation == 'horizontal':
            if user_xtick_rotation is None and any(char_len >= 8 for char_len in char_len_list):
                rotation = '-90'
            # Characters less than 4 can be kept at 0 for rotation
            elif user_xtick_rotation is None and any(char_len <= 4 for char_len in char_len_list):
                rotation = '0'
            # Characters between 4 and 12 items should be rotated to 45 degrees. 
            elif user_xtick_rotation is None and all(char_len >= 4 and char_len < 8 for char_len in char_len_list):
                rotation = '-45'
            elif user_xtick_rotation is None and all(char_len >= 2 and char_len < 8 for char_len in char_len_list):
                rotation = '-45'
            elif user_xtick_rotation is None and all(char_len >= 1 and char_len < 8 for char_len in char_len_list):
                rotation = '-35'
            else:
                rotation = user_xtick_rotation
                        
        else:
            # Characters greater than 12 means we shoud switch the rotation to 90 degrees
            if user_xtick_rotation is None and any(char_len >= 8 for char_len in char_len_list):
                rotation = '90'
            # Characters less than 4 can be kept at 0 for rotation
            elif user_xtick_rotation is None and all(char_len <= 4 for char_len in char_len_list):
                rotation = '0'
            # Characters between 4 and 12 items should be rotated to 45 degrees. 
            elif user_xtick_rotation is None and all(char_len >= 4 and char_len < 8 for char_len in char_len_list):
                rotation = '45'
            elif user_xtick_rotation is None and all(char_len >= 2 and char_len < 8 for char_len in char_len_list):
                rotation = '45'
            elif user_xtick_rotation is None and all(char_len >= 1 and char_len < 8 for char_len in char_len_list):
                rotation = '35'
            else:
                rotation = user_xtick_rotation
        
        return rotation
    
    
    
    def check_valid_color(self, custom_color, palette=None):
        
        # default color = '#1E53A2'
        if custom_color is not None and is_color_like(custom_color) is True:
            color_object = custom_color
        elif custom_color is not None and is_color_like(custom_color) is False:
            color_object = '#1E53A2'
        elif custom_color is None and palette is None:
            color_object = '#1E53A2'
        elif custom_color is None and palette is not None:
            color_object = sns.color_palette(palette)
        else:
            color_object = None
            
        return color_object
    
    
    
    def define_edgecolor(self, current_style):
        
        # Check if style sheet is 'dark-mode'
        if current_style == 'dark_background':
            return 'white'
        else:
            return 'black'
        
        
        
    def check_palette_type(self, chosen_palette):
        
        dark_palettes = ['dark', 'tab20b', 'Dark2', 'rocket', 'mako', 'inferno', 'magma', 'icefire']
        
        if chosen_palette in dark_palettes:
            return 'white'
        else:
            return 'black'
        
        
        
    def prioritise_color(self, color_code, palette):
        
        # Will either be '#1E53A2' or 'None'
        valid_color_code = self.check_valid_color(color_code)
                
        # If user entered a 'color' that isn't the default, and 'palette' has been entered, return the user defined 'color'
        if valid_color_code != '#1E53A2' and valid_color_code is not None and palette is not None:
            return valid_color_code
        
        # If the 'color' is the default color, and a palette has been entered, return the 'palette'
        elif valid_color_code == '#1E53A2' and palette is not None:
            return sns.color_palette(palette)
                
        # return the default color_code, which should be '#1E53A2'.
        else:
            return '#1E53A2'

    
    
    def space_legend_out(self, pd_series, space_legend_out_):
        
        if pd_series.dtype != 'object':
            pd_series_copy = copy.copy(pd_series)
            pd_series_copy = pd_series_copy.astype('str')
        else:
            pd_series_copy = copy.copy(pd_series)
            
            
        max_length = max(pd_series_copy.str.len())
                
        if space_legend_out_ is not None and space_legend_out_ <= 1.0:
            
            if max_length <= 5:
                legend_font_size = 8.5
                bbox_anchor = (space_legend_out_ + 1.0, 1.0)
            elif max_length > 5 and max_length <= 20:
                legend_font_size = 7.2
                bbox_anchor = (space_legend_out_ + 1.0, 1.0)
            elif max_length > 20 and max_length <= 30:
                legend_font_size = 4.0
                bbox_anchor = (space_legend_out_ + 1.0, 1.0)
            elif max_length > 30:
                legend_font_size = 3.5
                bbox_anchor = (space_legend_out_ + 1.0, 1.0)
        
        else:
            if max_length <= 5:
                legend_font_size = 10
                bbox_anchor = (1.2, 0.95)

            elif max_length > 5 and max_length <= 10:
                legend_font_size = 8.5
                bbox_anchor = (1.3, 1.0)

            elif max_length > 10 and max_length <= 20:
                legend_font_size = 7.5
                bbox_anchor = (1.4, 1.0)

            elif max_length > 20 and max_length <= 30:
                legend_font_size = 6.5
                bbox_anchor = (1.4, 1.0)

            elif max_length > 30 and max_length <= 40:
                legend_font_size = 4.0
                bbox_anchor = (1.45, 1.0)

            else:
                legend_font_size = 3.5
                bbox_anchor = (1.55, 1.0)

        return [legend_font_size, bbox_anchor]
    
    
    
    def pie_chart_size_parameters(self, pd_series, donut=False):

        unique_len = len(pd_series.unique())
        
        if donut is False:

            if unique_len <= 5:
                pct_distance = 0.6
                font_size = 8

            elif unique_len > 5 and unique_len <= 10:
                pct_distance = 0.7
                font_size = 7

            elif unique_len > 10 and unique_len <= 15:
                pct_distance = 0.8
                font_size = 6.5

            elif unique_len > 15 and unique_len <= 20:
                pct_distance = 0.85
                font_size = 6

            elif unique_len > 20 and unique_len <= 25:
                pct_distance = 0.90
                font_size = 5.5

            elif unique_len > 25 and unique_len <= 30:
                pct_distance = 0.92
                font_size = 5.0
        
        else:
            
            if unique_len <= 5:
                pct_distance = 0.80
                font_size = 8

            elif unique_len > 5 and unique_len <= 10:
                pct_distance = 0.80
                font_size = 7

            elif unique_len > 10 and unique_len <= 15:
                pct_distance = 0.82
                font_size = 6.5

            elif unique_len > 15 and unique_len <= 20:
                pct_distance = 0.85
                font_size = 6

            elif unique_len > 20 and unique_len <= 25:
                pct_distance = 0.90
                font_size = 5.5

            elif unique_len > 25 and unique_len <= 30:
                pct_distance = 0.90
                font_size = 5.2
                
        return [pct_distance, font_size]
    
    
    
    def create_percentage_data(self, pd_series):
        
        # Create a dicitonary containing every unique value and how many times it occurs throughout the series. 
        series_unique_dict = {key: val for (key, val) in zip(list(pd_series.value_counts().index), list(pd_series.value_counts()))}

        percents = []
        for part in series_unique_dict.values():
            percents.append(100 * (float(part)/float(sum(series_unique_dict.values()))))

        if int(sum(percents)) == 100:
            return [percents, list(series_unique_dict.keys())]
        else:
            return None
    
    
    def explode_slice(self, pd_series, chosen_slice):
        
        if chosen_slice == "none" or chosen_slice is None:
            return None

        data = self.create_percentage_data(pd_series)[0]
        data.sort(reverse=True)
        explode_list = [0] * len(data)

        if chosen_slice == 'smallest':
            explode_list[-1] = 0.15
        elif chosen_slice == 'largest':
            explode_list[0] = 0.15
        else:
            pass

        return explode_list
    
      
    def apply_donut(self, donut, current_style):
        
        if donut == "on" and self.define_edgecolor(current_style) == 'white':
            wedgeprops = {'width': 0.4,'edgecolor': 'black', 'linewidth': 1.2}
        elif donut == "on" and self.define_edgecolor(current_style) == 'black':
            wedgeprops = {'width': 0.4,'edgecolor': 'white', 'linewidth': 1.2}
        else:
            wedgeprops = None
        
        return wedgeprops
 
        
    def apply_rotation(self, rotation):
        
        if rotation is None:
            return 0
        else:
            return rotation