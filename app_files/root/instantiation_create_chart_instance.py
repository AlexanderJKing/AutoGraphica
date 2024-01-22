"""root.instantiation_create_chart_instance
A module that checks and validates user-submitted chart attribtues and returns an instance of that chart.
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import pandas as pd
from instantiation_chart_rules import ChartRules
from plot_line_graph import LineGraph
from plot_scatter_plot import ScatterPlot
from plot_bar_chart import BarChart
from plot_box_plot import BoxPlot
from plot_pie_chart import PieChart
from plot_histogram import Histogram
from plot_multi_line_graph import MultiLineGraph
from plot_multi_scatter_plot import MultiScatterPlot
from plot_multi_bar_chart import MultiBarChart
from plot_facet_plot import FacetPlot


class CreateChartInstance(ChartRules):

    """
    The class 'CreateChartInstance' composes an instance of the selected graph that the user wishes to generate.
    It first carefully evaluates all of the parameters submitted by the user to configure the plot, and once this has
    been validated, proceeds to create and return an instance of that plot.

    Attributes
    ----------
    pd_dataframe: pd.DataFrame
        This is a DataFrame object of the csv/xlsx input originally submitted by the user
    chart_type: str
        This is the chart type that they selected (Line, Scatter, Bar, etc.)
    chart_parameters: list
        This is a list of parameters which will configure the specified chart type submitted by the user prior.
    """
    
    def __init__(self, pd_dataframe, chart_type, chart_parameters):
        self.dataframe = pd_dataframe
        self.chart_type = chart_type
        self.chart_parameters = chart_parameters
 
    def validate_chart_attributes(self):

        """This function determines which chart type was selected by the user,
        evaluates all if any, parameters selected to configure that chart,
        then creates an instance of that chart and returns it.

        Parameters
        ----------
        No parameters used other than attributes instantiated upon instance creation.

        Returns
        -------
        Object
            An instance of a graph object, determined by the user upon selection (LineGraph, ScatterPlot, BarChart, etc.)
        """
        
        if self.chart_type == 'Line':
            self.chart_dict = self.collect_line_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.line_config_check(*self.chart_dict.values()) is True:
                    return LineGraph(**self.chart_dict)
                
        elif self.chart_type == 'Scatter':
            self.chart_dict = self.collect_scatter_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.scatter_config_check(*self.chart_dict.values()) is True:
                    return ScatterPlot(**self.chart_dict)
 
        elif self.chart_type == "Bar":
            self.chart_dict = self.collect_bar_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.bar_config_check(*self.chart_dict.values()) is True:
                    return BarChart(**self.chart_dict)
            
        elif self.chart_type == "Box":
            self.chart_dict = self.collect_box_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.box_config_check(*self.chart_dict.values()) is True:
                    return BoxPlot(**self.chart_dict)
                    
        elif self.chart_type == "Pie":
            self.chart_dict = self.collect_pie_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.pie_config_check(*self.chart_dict.values()) is True:
                    return PieChart(**self.chart_dict)

        elif self.chart_type == "Histogram":
            self.chart_dict = self.collect_histogram_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.histogram_config_check(*self.chart_dict.values()) is True:
                    return Histogram(**self.chart_dict)

        elif self.chart_type == "MultiLine":
            self.chart_dict = self.collect_multiline_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.multiline_config_check(*self.chart_dict.values()) is True:
                    return MultiLineGraph(**self.chart_dict)

        elif self.chart_type == "MultiScatter":
            self.chart_dict = self.collect_multiscatter_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.multiscatter_config_check(*self.chart_dict.values()) is True:
                    return MultiScatterPlot(**self.chart_dict)

        elif self.chart_type == "MultiBar":
            self.chart_dict = self.collect_multibar_attributes(self.chart_parameters)
            
            if self.chart_dict is not None:
                if ChartRules.multibar_config_check(*self.chart_dict.values()) is True:
                    return MultiBarChart(**self.chart_dict)
            
        elif self.chart_type == "Facet":
            self.chart_dict = self.collect_facet_attributes(self.chart_parameters)
                        
            if self.chart_dict is not None:
                if ChartRules.facet_config_check(*self.chart_dict.values()) is True:
                    return FacetPlot(**self.chart_dict)

    
    def collect_line_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """
        
        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "legend_on", "current_style", "orientation", "error_bar_type", "error_bar_value"]
        
        if len(list_of_attributes)  == len(attr_keys):
            # Have to make sure that what was entered was exact
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                   
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_scatter_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "legend_on", "current_style", "orientation"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_bar_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "legend_on", "current_style", "orientation", "single_axes"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_box_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "legend_on", "space_legend_out",  "current_style", "orientation", "palette", "z_axis_color"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_pie_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["custom_title", "legend_on", "space_legend_out", "current_style", "palette", "rotation", "chosen_slice", "donut"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_histogram_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "legend_on", "current_style", "n_bins", "histogram_type"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_multiline_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["custom_title", "xtick_rotation", "legend_on", "space_legend_out", "current_style", "orientation", "palette"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict


    def collect_multiscatter_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["custom_title", "xtick_rotation", "legend_on", "space_legend_out", "current_style", "orientation", "palette"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_multibar_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["custom_title", "xtick_rotation", "legend_on", "space_legend_out", "current_style", "orientation", "palette", "single_axes"]
        
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

    def collect_facet_attributes(self, list_of_attributes: list) -> dict:

        """This function takes a list of attributes, checks to see whether it is the correct length,
        then constructs a dictionary of all attributes submitted by the user to configure the plot
        
        Parameters
        ----------
        list_of_attributes: list
            This is a list of all the attributes the user would've clicked on or submitted from the app.
            
        Returns
        -------
        dict
            This dictionary contains all the attributes that can be used to configure the plot. 
        """

        chart_dict = {"pd_dataframe": self.dataframe}
        attr_keys = ["color_code", "custom_title", "xtick_rotation", "figure_width", "figure_height", "current_style", "palette", "n_bars_per_facet"]
                
        if len(list_of_attributes)  == len(attr_keys):
            attr_dict = {attr_keys[i]: list_of_attributes[i] for i in range(len(attr_keys))}
        else:
            attr_dict = None
            
                    
        if attr_dict is not None:
            chart_dict.update(attr_dict)
            return chart_dict

