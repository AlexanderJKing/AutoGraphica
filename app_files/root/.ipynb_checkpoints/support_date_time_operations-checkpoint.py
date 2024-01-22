"""root.chart_modules_support.date_time_operations
Module for handling date and time operations, particularly involved in checking whether a Pandas Series,
can constitute as a type of 'Date' or 'Time' and making any necessary, subsequent conversions afterwards.
"""

import copy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse
from dateutil.parser import ParserError

pd.options.mode.chained_assignment = None  # default='warn'


class DateTimeOperations:
    
    """ A class for instantiating an object to handle 'date' and 'time' operations.
    Intended to be a 'component' within the 'DataFrameOverview' class in the 'main_classes' module. """
    

    def return_date_format(self, pd_series):

        # 'date_time_separated' means wether the date and time are still in the same cell. 
        # if the time information is right next to the date information, we need to separate them and just return the date information

        # There are '10' characters in a valid date string (##/##/####)

        if all(pd_series.str.len() == 10) is True:
            new_series = copy.copy(pd_series)
            new_series = new_series.str.split("/")
            # gets the length of the list that is now in each value in the series
            date_list_len = new_series.str.len()

        else:
            return None
        
        # Checks that the length of the list is always 3. 
        if all(date_list_len == 3) is True:

            # Default format to be returned
            first = '%d'
            second = '%m'
            third = '%Y'

            # Figure out the days 
            # Apply a lambda function to check whether any of the values in the date list meet the requirements for day (i.e. greater than the maximum number of months).
            day_check_1 = new_series.apply(lambda date_list: True if int(date_list[0]) > 12 and int(date_list[0]) < 31 else False).astype(str)
            day_check_2 = new_series.apply(lambda date_list: True if int(date_list[1]) > 12 and int(date_list[1]) < 31 else False).astype(str)
            day_check_3 = new_series.apply(lambda date_list: True if int(date_list[2]) > 12 and int(date_list[2]) < 31 else False).astype(str)

            if day_check_1.str.contains('True').any():
                first = '%d'
            elif day_check_2.str.contains('True').any():
                second = '%d'
            else:
                third  = '%d'

            # Figure out the month
            month_check_1 = new_series.apply(lambda date_list: True if int(date_list[0]) <= 12 else False).astype(str)
            month_check_2 = new_series.apply(lambda date_list: True if int(date_list[1]) <= 12 else False).astype(str)
            month_check_3 = new_series.apply(lambda date_list: True if int(date_list[2]) <= 12 else False).astype(str)

            # must be all(), as all months are below or equal to 12, whereas not all days are below or equal to 12. 
            if month_check_1.str.contains('True').all():
                first = '%m'
            elif month_check_2.str.contains('True').all():
                second = '%m'
            else:
                third  = '%m'

            # Figure out the year
            year_check_1 = new_series.apply(lambda date_list: True if len(date_list[0]) == 4 else False).astype(str)
            year_check_2 = new_series.apply(lambda date_list: True if int(date_list[1]) == 4 else False).astype(str)
            year_check_3 = new_series.apply(lambda date_list: True if int(date_list[2]) == 4 else False).astype(str)

            if year_check_1.str.contains('True').all():
                first = '%Y'
            elif year_check_2.str.contains('True').all():
                second = '%Y'
            else:
                third  = '%Y'

            date_format = "/".join([first, second, third]) 
            return date_format

        else:
            return None
        
        
    def check_empty_time_data(self, pd_series):

        # Only for time data that is mixed in with date data. 
        new_series = copy.copy(pd_series)

        try:
            new_series = new_series.str.split(" ").apply(lambda x: x.pop(1)).str.split(":")

            timestamp_1 = new_series.apply(lambda time_list: "True" if time_list[0] == "00" else "False").astype(str)
            timestamp_2 = new_series.apply(lambda time_list: "True" if time_list[1] == "00" else "False").astype(str)
            timestamp_3 = new_series.apply(lambda time_list: "True" if time_list[2] == "00" or time_list[2] == "00+00" else "False").astype(str)

            if timestamp_1.str.contains("True").any() and timestamp_2.str.contains("True").any() and timestamp_3.str.contains("True").any():
                # Time Data is empty
                return True
            else:
                # Time Data is not empty
                return False

        except IndexError as pop_index:
            # Meaning that there is no second item in the list, as there was no spaces in this list, therefore it just contained 'date' data. 
            if str(pop_index) == "pop index out of range":
                return False

        

    def split_date_time(self, dataframe, col_name, count: int):

        # There is a High Probability that this is 'date & time' data.

        try: 
            temp_dataframe = copy.copy(dataframe)
            # Extract the 'date' and 'time' into two separated series
            date_series = pd.to_datetime(temp_dataframe[col_name]).dt.date
            time_series = pd.to_datetime(temp_dataframe[col_name]).dt.time

            # Create a new name for each new series that will be inserted back into the dataframe. 
            date_col_name = "Date_{}".format(str(count))
            time_col_name = "Time_{}".format(str(count))
            
            # Insert the two extracted series back into the dataframe and delete the old column
            temp_dataframe.insert(len(dataframe.columns), date_col_name, date_series)
            temp_dataframe.insert(len(dataframe.columns), time_col_name, time_series)
            temp_dataframe.drop(col_name, inplace=True, axis=1)
            
            # Convert the 'dtype' back to 'object', as we will need to assess if we can extract a 'format' from it. 
            temp_dataframe[date_col_name] = temp_dataframe[date_col_name].astype(str)
            temp_dataframe[time_col_name] = temp_dataframe[time_col_name].astype(str)

            # convert the new columns to datetime and timedelta respectively. 
            format_ = self.return_date_format(temp_dataframe[date_col_name])
            if format_ is not None:
                temp_dataframe[date_col_name] = pd.to_datetime(temp_dataframe[date_col_name], format=format_)
            else:
                temp_dataframe[date_col_name] = pd.to_datetime(temp_dataframe[date_col_name])
            
            # Convert to 'timedelta'
            temp_dataframe[time_col_name] = pd.to_timedelta(temp_dataframe[time_col_name].str.strip())
            
            return temp_dataframe

        except Exception as e:
            # We return the original dataframe in each alternative condition, as we don't want to return a 'None' object. 
            print("Error for 'split_date_time' function")
            print(str(e))
            return dataframe

        
        
    def is_date(self, string, fuzzy=False):
        """
        Return whether the string can be interpreted as a date.

        :param string: str, string to check for date
        :param fuzzy: bool, ignore unknown tokens in string if True
        """
        try: 
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False
        
    def acceptable_date_format(self, pd_series):
    
        dash_count = pd_series.str.count('/')
        colon_count = pd_series.str.count(':')
        if ((dash_count == 2).all()) and ((colon_count == 0).all()):
            return True
        else:
            return False
        
    def acceptable_time_format(self, pd_series):
        
        dash_count = pd_series.str.count('/')
        colon_count = pd_series.str.count(':')
        if ((dash_count == 0).all()) and ((colon_count >= 1).all()):
            return True
        else:
            return False
    
    def acceptable_date_time_format(self, pd_series):
    
        
        dash_count = pd_series.str.count('/')
        colon_count = pd_series.str.count(':')
        if ((dash_count >= 1).all()) and ((colon_count >= 1).all()):
            return True
        else:
            return False

    
    def determine_date(self, pd_series):
        
        """Checks whether;
            - dtype == 'object'
            - It is a valid 'date' format (i.e. there are 2 '/' and 0 ':')
            - Checks that each entry in the Series is a valid date
        """
        
        # Just because it is in the correct format for 'date' only, we still need to confirm.
        if self.acceptable_date_format(pd_series) is True:
            # Determine if the entire series is a valid 'date' series.
            # This will return a series of boolean values (True for 'is a date', and False for 'is not a date')
            date_check = pd_series.apply(self.is_date)
            # So the entire Series is only one value, and if that value is True, it is a valid date series
            if len(date_check.unique() == 1) and date_check[0] == True:
                return True
            else:
                # Not a valid date series
                return False
        else:
            return False
        
    def determine_time(self, pd_series):
        
        """Checks whether;
            - dtype = 'object'
            - It is a valid 'time' format (i.e. there is at least 1 ':' and 0 '/').
            - Checks whether each value outside the ':' can be converted into an integer. 
        """
        
        # Determine if the series is just time:
        if self.acceptable_time_format(pd_series) is True:
            valid_list = []
            check = pd_series.str.split(":")

            # value_list is a Tuple of 2 items
            # [0] is just the index
            # [1] is the actual list of split dates
            for value_list in check.iteritems():
                if all(value.isdigit() for value in value_list[1]):
                    valid_list.append(True)
                else:
                    valid_list.append(False)

            if all(value is True for value in valid_list) and len(valid_list) > 0:
                return True 
            else:
                return False
        else:
            return False
        
    
    def determine_date_and_time(self, pd_series):
        
        """Checks whether;
            - dtype = 'object'
            - It is not a valid date format (on its own)
            - It is not a valid time format (on its own)
            - It is a valid 'date' and 'time' format (contains 2 '/' and at least 1 ':'
        """
        
        
        # here we are determining that the datatype must be 'object' and that the data is not just 'date' and not just 'time'. 
        # For just 'date' data, there is only '/' and no ':'. - Should return False if number of ':' != 0
        # For just 'time' data, there is only ':' and no '/'. - Should return False if number of '/' != 0
        if self.acceptable_time_format(pd_series) is False and self.acceptable_date_format(pd_series) is False:
            
            # Now we need to check whether the data contains both 'date' and 'time' values. 
            # If there are 2 '/' and at least 1 ':' in the value. 
            if self.acceptable_date_time_format(pd_series) is True:
                return True
            else:
                return False
        else:
            return False
        


    def main_converter(self, pd_series):
       
        # We need to confirm that it is an 'object' dtype first. 
        if pd_series.dtype == 'object':
            
            try:
                # Determine if it is 'date' only
                if self.determine_date(pd_series) is True:
                    # If the Series is just 'date' data (i.e. no time) then we can just convert it to 'datetime64', after we find the appropriate 'strftime' format to pass through.
                    return 'Change_to_Date'
                    # pd_series = pd.to_datetime(pd_series, format=self.return_date_format(pd_series))
                
                # Determine if it is 'time' only
                elif self.determine_time(pd_series) is True:
                    return 'Change_to_Time'
                    # pd_series = pd.to_timedelta(pd_series.str.strip())
                
                # If it is not 'date' only, or 'time' only, then determine if it is 'date' AND 'time'. 
                elif self.determine_date_and_time(pd_series) is True:
                    return 'Split_&_Change_Date&Time'
                    
            except Exception as ex:
                print(str(ex))    
                        
        else:
            pass
                    

    def convert_timedelta(self, value):
    
        # Rounds a timedelta value to hour, with 2 decimal places (provided its originally in seconds - use 'dt.seconds')
        hour_value = round(((value / 60) / 60), 2)
        return hour_value
    