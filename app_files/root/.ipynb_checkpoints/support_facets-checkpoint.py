"""root.support_facets
A module built to support the 'FacetPlot' class. 
Mainly involving the creation of the individual facets (sub-plots), 
i.e. the number of rows and columns and deletion of any spare axes created.
"""

import copy
import math
import pandas as pd

class Facets:
    
    """
    A Mixin class for instantiating an object to support operations when creating the facet plot
    """
    
    @staticmethod
    def facet_cardinal_series(pd_series, n_bars_per_facet):

        """A function that takes a column in the DataFrame of high cardinality,
        and determines the optimal number of facets (subplots) to generate for it,
        by partitioning the column with a brand new column, that groups values by that optimal number.
        
        Parameters
        ----------
        pd_series: pd.Series
            The column in the DataFrame of high cardinality.
        n_bars_per_facet: int
            The number of bars plotted ber facet (subplot).
        """

        count = 0
        series_list = []
        pd_series_len = len(pd_series)

        if n_bars_per_facet != 0:
            # The divisor is how many times we loop by
            divisor = math.floor(pd_series_len / n_bars_per_facet)
            for i in range(0, divisor):
                facet_list = ["Facet_{}".format(count)] * n_bars_per_facet
                series_list.extend(facet_list)
                count += 1

            # Need to calculate the remainder, as we have deliberately rounded down the divisor. 
            # So now we calculate what's left for the last few values, as we need an even series to reinsert into the dataframe. 
            facet_string = "Facet_{}".format(count)
            len_of_series_list = len(series_list)
            remainder = pd_series_len - len_of_series_list
            
            if remainder > 0:
                facet_list = [facet_string] * remainder
                series_list.extend(facet_list)
            else:
                pass
        else:
            series_list.extend([0] * len(pd_series))

        facet_series = pd.Series(series_list)
        return facet_series
    
    
    @staticmethod
    def calculate_nrows_ncols(pd_dataframe, high_cardinal_variable, n_bars, number_of_columns=4):

        """This function calculates the number of rows and columns best suited to plot the subplots in
        
        Parameters
        ----------
        pd_dataframe: pd.DataFrame
            The DataFrame created when the user submitted a file csv/xlsx.
        high_cardinal_variable: str
            The name of the high cardinal column within the DataFrame.
        n_bars: int
            The number of bars per facet (subplot).
        number_of_columns: int
            The number of columns within the facet plot (default is 4)."""
        
        facet_series = Facets.facet_cardinal_series(pd_series=pd_dataframe[high_cardinal_variable],
                                                    n_bars_per_facet=n_bars)
        n_facets = len(facet_series.unique())
        # We choose to round up, as even though only one plot might be for an entire row, we can always delete any spare axes. 
        number_of_rows = math.ceil(n_facets / number_of_columns)
        
        return [number_of_rows, number_of_columns]

    
    @staticmethod
    def create_faceted_dataframes(pd_dataframe, high_cardinal_variable, n_bars):

        """This function creates a list of DataFrames, that have been partitioned from the original DataFrame,
        into this list, the length of which has been determined to be the optimal number subplots to plot individual DataFrames.

        Parameters
        ----------
        pd_dataframe: pd.DataFrame
            The DataFrame created when the user submitted a file csv/xlsx.
        high_cardinal_variable: str
            The name of the high cardinal column within the DataFrame.
        n_bars: int
            The number of bars per facet (subplot).
        """
    
        dataframe_copy = copy.copy(pd_dataframe)
        
        # Create a Facet Series
        facet_series = Facets.facet_cardinal_series(pd_series=dataframe_copy[high_cardinal_variable],
                                                  n_bars_per_facet=n_bars)
        
        # Insert the 'new' Facet Series (named 'Facet_Groups') into the attribute dataframe
        dataframe_copy.insert(len(dataframe_copy.columns), 'Facet_Groups', facet_series)
        
        # Create a List of DataFrames that have been partitioned from that added series 'Facet_Groups'
        dataframes_list = [dataframe_copy.loc[dataframe_copy['Facet_Groups'] == facet] for facet in dataframe_copy['Facet_Groups'].unique()]
        
        # Reset all the indexes back to 0
        [dataframe.reset_index(inplace=True) for dataframe in dataframes_list]

        return dataframes_list
    
    
    @staticmethod
    def delete_spare_axes(figure,
                          axes_objects,
                          list_of_dataframes,
                          n_rows,
                          n_cols):

        """This function deletes any spare axes found at the tail of the facet,
        (i.e. any empty frames/figures)
        
        Parameters
        ----------
        figure: plt.Figure
            A Matplotlib figure object.
        axes_objects: plt.axes
            A Matplotlib axes object.
        list_of_dataframes: list
            A list of partitioned DataFrames, built from the original DataFrame inputted.
        n_rows: int
            The number of rows in the facet plot.
        n_cols: int
            The number of columns in the facet plot.
        """

        total_axes = n_rows * n_cols
        remainder_axes = total_axes -  len(list_of_dataframes)

        counter = 0
        counter_bool = False
        # We need to keep track of what the original number of columns entered was. 
        original_ncols = copy.copy(n_cols) 

        # If the total number of axes is greater than the number of DataFrames plotted inside them.
        if total_axes > len(list_of_dataframes):

            # Loop Through every row entry
            for row_ind_ in range(0, n_rows):

                # Lower the index, since it started at 0, in reverse, it should start at 3 (since it only goes up to 4, but does not include 4)
                # This will decrease after every row iteration. 
                n_rows -= 1

                # Loop throuhg every column entry
                for col_ind_ in range(0, n_cols):

                    # Lower the column index, since it started at 0, in reverse it should also start at 3. This will decrease after every column iteration. 
                    n_cols -= 1
                    # Delete the axes at the specified point. 
                    figure.delaxes(axes_objects[n_rows][n_cols])

                    # Increase the counter
                    counter += 1

                    # If the counter is the same as the number of original remaining axes to be deleted, then break. 
                    if counter == remainder_axes:
                        # need to break out of the outer loop manually too. 
                        counter_bool = True
                        break

                # breaking out of outer loop manually. 
                if counter_bool is True:
                    break

                # Since we have gone through a full iteration of the columns, we need to set 
                n_cols += original_ncols




    