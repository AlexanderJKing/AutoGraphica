"""root.support_main_classes
A module for containing the main classes dedicated towards categorising the different chart types,
that can be made with the available data passed into it as a DataFrame. 
The two classes are the 'ColumnAttributes' class and the 'DataFrameOverview' class, which work in tandem,
to determine which columns in the DataFrame get categorised as.
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import copy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from dateutil.parser import ParserError
from support_date_time_operations import DateTimeOperations
pd.options.mode.chained_assignment = None  # default='warn'


class ColumnAttributes:
    
    """
    A class for instantiating a 'column' object, based on a Series in a Pandas DataFrame.
    This object will contain a number of attributes, but most importantly a 'data category',
    which will define what charts it can make.
    
    Attributes
    ----------
    column_data: pd.Series
        The column of interest within the DataFrame.
    column_name: str
        The name of the column.
    column_dtype: str
        The data type of the column.
    unique_values: int
        The number of unique values within the column.
    null_values: int
        The number of null values within the column.
    """
    
    def __init__(self, pd_series):
        
        self.column_data = pd_series
        self.column_name = pd_series.name
        self.column_dtype = str(pd_series.dtype)
        self.unique_values = len(pd.unique(pd_series))
        self.null_values = len([null_value for null_value in pd_series.isnull() if null_value is True])
        self.create_data_category()
        
        
    def quantitative_type(self):

        "This function determines if a column is a quantitative type"
    
        if self.column_dtype == 'int64' and len(pd.unique(self.column_data)) > 2:
            self.data_category = 'Discrete'
            
        # First Check
        elif self.column_dtype == 'float64':
            series_check = pd.Series(dtype='bool')
            series_check = self.column_data.apply(lambda value: True if value.is_integer() else False)
            
            # Second Check - if column is 'Continuous' or 'Discrete', even though it's a 'float' datatype.
            if False in series_check.values:
                self.data_category = 'Continuous'
            else:
                self.data_category = 'Discrete'
                
        else:
            self.data_category = None
    
    
    def qualitative_type(self):

        "This function determines if a column is a qualitative type"
        
        # If there is 'x' or less unique values in the column, it will be labelled 'ordinal'
        threshold_value = 10  
    
        if self.column_dtype == 'object' and len(self.column_data) == len(pd.unique(self.column_data)) or\
        self.column_dtype == 'object' and len(pd.unique(self.column_data)) >= threshold_value:
            self.data_category = 'Nominal'

        # Check for any boolean representations
        elif self.column_dtype == 'int64' and len(pd.unique(self.column_data)) == 2:
            self.data_category = 'Nominal-Binary'
        
        # If the column is categorical and contains less than the threshold value. 
        elif self.column_dtype == 'object' and len(pd.unique(self.column_data)) <= threshold_value:
            self.data_category = 'Ordinal'
            
        elif self.column_dtype == 'datetime64[ns]' or  self.column_dtype == 'datetime64[ns, UTC]':
            self.data_category = 'Date'
            
        elif self.column_dtype == 'timedelta64[ns]':
            self.data_category = 'Time'
            
        else:
            self.data_category = None
    
    
    def create_data_category(self):

        "This function calls the above methods on the column to determine if it is quantitative or qualitative"
                
        self.quantitative_type()
        if not hasattr(self, 'data_category') or self.data_category is None:
            self.qualitative_type()
            
            
class DataframeOverview:
    
    """
    A class for providing an overview on the entire DataFrame.
    It initializes a dictionary of attributes which will then inform the various chart objects in the 
    'chart_modules' subpackage on what they can create.
    
    Attributes
    ----------
    dt: support_date_time_operations.DateTimeOperations
        An instance of the DateTimeOperations class.
    dataframe: pd.DataFrame
        The DataFrame created from the file inputted by the user.
    """
    
    def __init__(self, pd_dataframe):
        
        self.dt = DateTimeOperations()
        self.dataframe = pd_dataframe
        self.initialize_columns()
        
        
    def fill_null_values(self):

        "This function fills in null values in all columns."
        
        for column in list(self.dataframe.columns):
            if self.dataframe[column].dtype == 'object':
                self.dataframe[column].fillna("", inplace=True)
            elif self.dataframe[column].dtype == 'int64' or self.dataframe[column].dtype == 'float64':
                self.dataframe[column].fillna(0, inplace=True)
            else:
                pass
            
    def convert_date_time_columns(self):

        "This function converts any columns that are of type 'object' with a 'Datetime' format into type 'Datetime'."
        
        count = 0
        for column in list(self.dataframe.columns):
             
            # 1). Checking to see if we convert to 'date' only (format=##/##/####, or something similar).
            if self.dt.main_converter(self.dataframe[column]) == 'Change_to_Date':
                # If a 'format' can be found fill it in.
                if self.dt.return_date_format(self.dataframe[column]) is not None:
                    self.dataframe[column] = pd.to_datetime(self.dataframe[column], format=self.dt.return_date_format(self.dataframe[column]))
                # else if it can not be found, just convert without it. 
                else:
                    self.dataframe[column] = pd.to_datetime(self.dataframe[column])
            
            # 2). Checking to see if we convert to 'time' only (format=##:##:##, or something similar).
            elif self.dt.main_converter(self.dataframe[column]) == 'Change_to_Time':
                # Check to see if it is in a specific format. 
                try:
                    self.dataframe[column] = pd.to_timedelta(self.dataframe[column].str.strip())
                # If not, add in the extra two '00's at the end. 
                except ValueError as wrong_format: 
                    if str(wrong_format) == "expected hh:mm:ss format":
                        self.dataframe[column] = self.dataframe[column] + ':00'
                        self.dataframe[column] = pd.to_timedelta(self.dataframe[column].str.strip())
                except Exception as e:
                    print(str(e))
            
            # 3). Checking to see if we need to split 'date' and 'time' into two different columns. 
            elif self.dt.main_converter(self.dataframe[column]) == 'Split_&_Change_Date&Time':
                self.dataframe = self.dt.split_date_time(self.dataframe, column, count)
                count += 1
                
            else:
                pass
        
        
    def initialize_columns(self): 

        """This function initializes all columns in the DataFrame by:
            - filling in all null values
            - converting any datetime columns.
        """
        
        count = 0
        self.column_attributes = {}
        # Check for null values:
        self.fill_null_values()
        # Convert any date/time objects
        self.convert_date_time_columns()
        # Strip any leading or trailing spaces in the column names
        self.dataframe.columns = self.dataframe.columns.str.strip() 

        
        for column in list(self.dataframe.columns):  
            col_id = 'col_' + str(count)
            self.column_attributes[col_id] = ColumnAttributes(self.dataframe[column])
            count += 1
            
            
    def print_attributes(self):

        "This function prints out all attributes of interest about the class"
        
        if hasattr(self, "column_attributes"):
            
            for column in list(self.column_attributes.keys()):
                column_instance = self.column_attributes.get(column)

                # print each attribute from that instance
                # print(column_instance.column_data)
                print(f"Column Name is: '{column_instance.column_name}'")
                print(f"Column dtype is: '{column_instance.column_dtype}'")
                print(f"Column data category is: '{column_instance.data_category}'")
                print(f"Column Unique Value Count is: '{column_instance.unique_values}'")
                print(f"Column Null Value Count is: '{column_instance.null_values}'")
                print("\n")
                
        else:
            print("Class attribute 'column_attributes' has not been initialized")


