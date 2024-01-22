"""root.instantiation_file_controller
A module dedicated towards checking and validating the file passed to it and returning a DataFrame based on a valid file extension.
"""


import os
import sys
import pandas as pd

class FileController:

    """
    The 'FileController' class is responsible for navigating the user's file directory.
    When they submit a path on the app, they will have the option to use the app's functionality to browse for the file.
    This class is also in charge of validating the file submitted and creating a DataFrame if so.

    Attributes
    ----------
    user_file_path: str
        This is the path to the file (csv/xlsx) that the user has submitted.
    dataframe: pd.DataFrame, None
        This is the DataFrame created from the user's file, providing that the file path was valid, and the file extension was valid.
    """
    
    def __init__(self, user_file_path):
        self.user_file_path = user_file_path
        self.pass_valid_file()
    
    def pass_valid_file(self):

        """This function checks to see whether the file path submitted was valid.
        If so, it creates a DataFrame from the file submitted.
        """
        
        if os.path.exists(self.user_file_path) is True:
            self.create_dataframe()
        else:
            self.dataframe = None
        
    def create_dataframe(self):

        """This function checks to see if the file in the file path has the extensions '.csv' or '.xlsx'
        If so, it creates a DataFrame from that file."""
        
        if self.user_file_path.endswith(".csv"):
            self.dataframe = pd.read_csv(self.user_file_path)
        elif self.user_file_path.endswith(".xlsx"):
            self.dataframe = pd.read_excel(self.user_file_path)
        else:
            self.dataframe = None
                
    def validate_dataframe(self):

        """This function determines whether the dataframe attribute got initialized with an actual DataFrame or returned a 'None' type."""
        
        if hasattr(self, 'dataframe'):
            if isinstance(self.dataframe, pd.core.frame.DataFrame):
                return True
        else:
            return False
        
    def input_chart_selection(self, chart_selection):

        """This function sets the attribute 'chart_input' based on the selection of the user"""
        
        if self.validate_dataframe() is True:
            chart_options = ['Line', 'Scatter', 'Bar', 'Box', 'Pie', 'Histogram', 'MultiLine', 'MultiScatter', 'MultiBar', 'Facet']

            if chart_selection in chart_options:
                self.chart_input = chart_selection
        else:
            pass

            