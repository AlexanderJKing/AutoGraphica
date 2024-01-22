"""root.instantiation_chart_rules
Two Mixin Classes with static methods that are designed to authorize and validate the user-submitted parameters for the selected chart.
"""

import os
import sys
import itertools
import pandas as pd
from matplotlib.colors import is_color_like


class ChartAttributeRules:

    """
    The 'ChartAttributeRules' class checks and sees whether certain rules
    for each available parameter on the user interface, is being adhered to.
    Each input provided by the user is assessed using these rules. 
    There are 20 different parameters available for user configuration across all graph options.
    """

    
    @staticmethod
    def color_code_check(color_code_: str) -> bool:  # 1
        """This function checks that the color entered by the user is a valid color option, as accepted by Matplotlib.
        
        Parameters
        ----------
        color_code_: str
            This is the color option, as string, entered by the user to be evaluated.
            
        Returns
        -------
        bool
            Returns True if a valid color option. False if otherwise.
        """

        if is_color_like(color_code_) is True:
            return True
        elif color_code_ is None:
            return True
        else:
            return False
    
    @staticmethod
    def xtick_rotation_check(xtick_rotation_: int) -> bool:  # 2
        """This function checks to see whether the entry for rotating the ticks on the 'x-axis' is valid.
        It expects an integer input, but also accepts float and string values, if those strings can be cast as numeric.
        
        Parameters
        ----------
        xtick_rotation_: int, float, str
            This is the xtick_rotation option, as either an integer, float or string, entered by the user to be evaluated.
        
        Returns
        -------
        bool
            Returns True if a valid xtick rotation option. False if otherwise.
        """

        if isinstance(xtick_rotation_, (int, float, str)):
            return True
        elif xtick_rotation_ is None:
            return True
        else:
            return False
    
    @staticmethod
    def custom_title_check(custom_title_: str) -> bool:  # 3
        """This function checks to see whether the entry for the title of the plot is valid.
        
        Parameters
        ----------
        custom_title_: str
            This is the custom title option, as string, entered by the user to be evaluated.
        
        Returns
        -------
        bool
            Returns True if a valid title option. False if otherwise.
        """

        if isinstance(custom_title_, str):
            return True
        elif custom_title_ is None:
            return True
        else:
            return False
    
    @staticmethod
    def legend_on_check(legend_on_: str) -> bool:  # 4
        """This function checks to see whether the entry for the legend of the plot is valid.
        
        Parameters
        ----------
        legend_on_: str
            This is the legend option, as a str, entered by the user as either 'on/off', to be evaluated.
        
        Returns
        -------
        bool
            Returns True if a valid legend option. False if otherwise.
        """

        if legend_on_ == 'on':
            return True
        elif legend_on_ == 'off':
            return True
        elif legend_on_ is None:
            return True
        else:
            return False
    
    @staticmethod
    def space_legend_out_check(space_legend_out_: int) -> bool:  # 5
        """This function checks to see whether the entry for spacing the legend of the plot is valid.
        
        Parameters
        ----------
        space_legend_out_: int, float, str
            This is the option for spacing the legend out from the figure of the plot.
            It expects an 'int' argument, but will accept 'float' and 'str'.
        
        Returns
        -------
        bool
            Returns True if a valid option for spacing the legend from the plot. False if otherwise.
        """
        
        if isinstance(space_legend_out_, (int, float, str)):
            
            if float(space_legend_out_) >= 0 and float(space_legend_out_) <= 1.0:
                return True
            else:
                return False
        
        elif space_legend_out_ is None:
            return True
        
        else:
            return False

    @staticmethod
    def current_style_check(current_style_: str) -> bool:  # 6
        """This function checks to see whether the current style for the plot, inputted by the user, is valid.
        
        Parameters
        ----------
        current_style_: str
            This is the option for setting the style of the plot. It must be an accepted Matplotlib style.
        
        Returns
        -------
        bool
            Returns True if a valid style option. False if otherwise.
        """

        available_styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
                            'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
                            'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster',
                            'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

        # available_styles = ['ggplot', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
        #                  'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid','seaborn-v0_8-deep', 'seaborn-v0_8-muted',
        #                  'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster',
        #                  'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid',
        #                  'dark_background', 'grayscale', 'tableau-colorblind10', 'Solarize_Light2', '_classic_test_patch',
        #                  'bmh', 'classic', 'fast', 'fivethirtyeight', '_mpl-gallery', '_mpl-gallery-nogrid']

        if current_style_ in available_styles:
            return True
        elif current_style_ is None:
            return True
        else:
            return False

    @staticmethod
    def orientation_check(orientation_: str) -> bool:  # 7
        """This function checks to see whether the orientation of the axes is 'vertical' or 'horizontal', as inputted by the user.
        
        Parameters
        ----------
        orientation_: str
            This is the option for setting the orientation of the plot. It can either flip the data from the 'x' to the 'y' axis, or vice versa.
        
        Returns
        -------
        bool
            Returns True if a valid orientation option. False if otherwise.
        """

        if orientation_ == 'vertical':
            return True
        elif orientation_ == 'horizontal':
            return True
        elif orientation_ is None:
            return True
        else:
            return False

    @staticmethod
    def palette_check(palette_: str) -> bool:  # 8
        """This function checks whether the current 'palette' of the plot is valid. It must be an accepted Seaborn palette option.
        
        Parameters
        ----------
        palette_: str
            This is the option for setting the palette of the plot. It must be a valid Seaborn palette option.
        
        Returns
        -------
        bool
            Returns True if a valid palette option. False if otherwise.
        """

        matplotlib_palettes = ['tab10', 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind', 'tab20', 'tab20b', 'tab20c']
        
        circular_palettes = ['hls', 'husl']
        
        qualitative_color_brewer_palettes = ['Set1', 'Set2', 'Set3', 'Paired', 'Accent', 'Pastel1', 'Pastel2', 'Dark2']
        
        sequential_color_brewer_palettes = ['Greys', 'Reds', 'Greens', 'Blues', 'Oranges', 'Purples', 'BuGn', 'BuPu',
                                            'GnBu', 'OrRd', 'PuBu', 'RdPu', 'YlGn', 'PuBuGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']
        
        diverging_color_brewer_palettes = ['RdBu', 'RdGy', 'PRGn', 'PiYG', 'BrBG', 'RdYlBu', 'RdYlGn', 'Spectral']
        
        sequential_palettes = ['rocket', 'mako', 'flare', 'crest', 'viridis', 'plasma', 'inferno', 'magma', 'cividis']
        
        diverging_color_palettes = ['vlag', 'icefire', 'coolwarm', 'bwr', 'seismic']
        
        miscellaneous_color_maps = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2',
                                    'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar']

        all_palettes = list(itertools.chain(matplotlib_palettes, circular_palettes, qualitative_color_brewer_palettes,
                                            sequential_color_brewer_palettes, diverging_color_brewer_palettes, sequential_palettes,
                                            diverging_color_palettes, miscellaneous_color_maps))

        if palette_ in all_palettes:
            return True
        elif palette_ is None:
            return True
        else:
            return False

    @staticmethod
    def single_axes_check(single_axes_: str) -> bool:  # 9
        """This function checks whether the user has selected for the data to be displayed via a single axis, or multiple axes. 
        Primarily for plots that can plot a single variable or an additional second variable on the 'y-axis'.
        
        Parameters
        ----------
        single_axes_: str
            This is the option for setting the number of axes on the plot.
        
        Returns
        -------
        bool
            Returns True if a valid axes option. False if otherwise.
        """

        if single_axes_ == "on":
            return True
        elif single_axes_ == "off":
            return True
        elif single_axes_ is None:
            return True
        else:
            return False

    @staticmethod
    def error_bar_type_check(error_bar_type_: str) -> bool:  # 10
        """This function checks the submission for the type of error bar submitted by the user for a 'line' plot.
        
        Parameters
        ----------
        error_bar_type_: str
            This is the option for setting the type of error bar available for line plots.
        
        Returns
        -------
        bool
            Returns True if a valid error bar type. False if otherwise.
        """

        if error_bar_type_ == "sd":
            return True
        elif error_bar_type_ == "se":
            return True
        elif error_bar_type_ == "pi":
            return True
        elif error_bar_type_ == "ci":
            return True
        elif error_bar_type_ == None:
            return True
        else:
            return False

    @staticmethod
    def error_bar_value_check(error_bar_type_: str, error_bar_value_: int) -> bool:  # 11
        """This function checks to see whether the value entered when an error bar type has already been selected, is valid.
        
        Parameters
        ----------
        error_bar_type_: str
            This is the option for setting the type of error bar available for line plots.
        error_bar_value_: int, float, str
            This is the option for determining the magnitude of the specific error bar type already selected. 
        
        Returns
        -------
        bool
            Returns True if a valid error bar value submitted. False if otherwise.
        """
    
        if isinstance(error_bar_value_, (int, float, str)):            
            try:
                if error_bar_type_ in ('sd', 'se') and float(error_bar_value_):
                    return True
                elif error_bar_type_ in ('ci', 'pi') and float(error_bar_value_) in range(0, 100):
                    return True
                else: 
                    raise ValueError
            
            except ValueError:
                return False
            
        elif error_bar_value_ is None:
            return True
        
        else:
            return False

    @staticmethod
    def z_axis_color_check(z_axis_color_: str) -> bool:  # 12
        """This function checks to see whether to apply a color palette when an additional dimension (z-axis) has been added to the plot.
        
        Parameters
        ----------
        z_axis_color_: str
            This is the option for determining whether to apply a color palette along a third dimension (z-axis).
        
        Returns
        -------
        bool
            Returns True if a z_axis specified. False if otherwise.
        """

        if z_axis_color_ == "on":
            return True
        elif z_axis_color_ == "off":
            return True
        elif z_axis_color_ is None:
            return True
        else:
            return False

    @staticmethod
    def rotation_check(rotation_: int) -> bool:  # 13
        """This function checks to see whether a valid rotation value has been entered for rotating pie charts. 
        
        Parameters
        ----------
        rotation_: str
            This is the option for determining to what degree to rotate a pie chart.
        
        Returns
        -------
        bool
            Returns True if a valid rotation specified. False if otherwise.
        """
        
        if rotation_ is None:
            return True
        
        elif isinstance(rotation_, (int, float, str)):
            
            try:
                rotation_new = float(rotation_)
                print("This should convert")
                return True            
            except ValueError:
                return False
        else:
            return False

    @staticmethod
    def chosen_slice_check(chosen_slice_: str) -> bool:  # 14
        """This function checks to see whether the user would like to explode one of the slices in the pie chart. 
        They can either choose to explode the 'largest', 'smallest', or none.
        
        Parameters
        ----------
        chosen_slice_: str
            This is the option for selecting a slice within a pie chart to explode.
        
        Returns
        -------
        bool
            Returns True if a valid slice option specified. False if otherwise.
        """

        if chosen_slice_ == None:
            return True
        elif chosen_slice_ == "largest":
            return True
        elif chosen_slice_ == "smallest":
            return True
        else:
            return False
        
    @staticmethod
    def donut_check(donut_: str) -> bool:  # 15
        """This function checks to see whether the user would like to display their pie chart, as a donut chart.
        
        Parameters
        ----------
        donut_: str
            This is the option for selecting whether to turn a pie chart into a donut chart.
        
        Returns
        -------
        bool
            Returns True if a valid donut option specified. False if otherwise.
        """

        if donut_ == "on":
            return True
        elif donut_ == "off":
            return True
        elif donut_ == None:
            return True
        else:
            return False

    @staticmethod
    def n_bins_check(n_bins_: int) -> bool:  # 16
        """This function checks to see whether the value entered for the number of bins to include in a histogram is valid.
        
        Parameters
        ----------
        n_bins_: str, int
            This is the number of bins the user would like their histogram to display.
        
        Returns
        -------
        bool
            Returns True if a valid number is specified. False if otherwise.
        """

        if isinstance(n_bins_, str):
            if n_bins_.isdigit():
                return True
            else:
                return False
        elif isinstance(n_bins_, int):
            return True      
        elif n_bins_ is None:
            return True
        else:
            return False

    @staticmethod
    def histogram_type_check(histogram_type_: str) -> bool:  # 17
        """This function checks to see which type of histogram the user wishes to display, can either be a traditional bar display, or an area display. 
        
        Parameters
        ----------
        histogram_type_: str
            This is the type of histogram to display, either a bar plot, or area plot.
        
        Returns
        -------
        bool
            Returns True if a valid histogram type specified. False if otherwise.
        """

        if histogram_type_ == "bars":
            return True
        elif histogram_type_ == "area":
            return True
        elif histogram_type_ is None:
            return True
        else:
            return False

    @staticmethod
    def n_bars_per_facet_check(n_bars_per_facet_: int) -> bool:  # 18
        """This function

        Parameters
        ----------
        n_bars_per_facet_: int
            This is the number of pars that appears in each subplot of the facet plot.
        
        Returns
        -------
        bool
            Returns True if a valid number of bars specified. False if otherwise.
        """

        if isinstance(n_bars_per_facet_, int):
            if n_bars_per_facet_ > 0:
                return True
            else:
                return False
        elif n_bars_per_facet_ is None:
            return True
        else:
            return False
        
    @staticmethod
    def figure_width_check(figure_width_: int) -> bool:  # 19
        """This function checks to see if the width specified for the facet plot is valid.
        
        Parameters
        ----------
        figure_width_: int
            This is the number used to specify the width of the facet plot.
        
        Returns
        -------
        bool
            Returns True if a valid width specified. False if otherwise.
        """
        
        if isinstance(figure_width_, int):
            if figure_width_ > 0:
                return True
            else:
                return False
        elif figure_width_ is None:
            return True
        else:
            return False
        

    @staticmethod
    def figure_height_check(figure_height_: int) -> bool:  # 20
        """This function checks to see if the height specified for the facet plot is valid.
        
        Parameters
        ----------
        figure_height_: int
            This is the number used to specify the height of the facet plot.
        
        Returns
        -------
        bool
            Returns True if a valid width specified. False if otherwise.
        """
        
        if isinstance(figure_height_, int):
            if figure_height_ > 0:
                return True
            else:
                return False
        elif figure_height_ is None:
            return True
        else:
            return False
        
        
class ChartRules(ChartAttributeRules):

    """
    The 'ChartRules' class is the final test required before configuring the plot. 
    It checks each entry submitted by the user, as to how they wish to configure their plot.
    If all options return valid for the configuration of the plot, then a boolean value of 'True' is returned.
    """
    
    @staticmethod
    def line_config_check(pd_dataframe: pd.DataFrame,
                          color_code: bool,
                          custom_title: bool,
                          xtick_rotation: bool,
                          legend_on: bool,
                          current_style: bool,
                          orientation: bool,
                          error_bar_type: bool,
                          error_bar_value: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a line graph are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """

        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.error_bar_type_check(error_bar_type))
        bool_list.append(ChartAttributeRules.error_bar_value_check(error_bar_type, error_bar_value))
                
        if all(bool_list) is True:
            return True
        else:
            return False
        
    @staticmethod
    def scatter_config_check(pd_dataframe: pd.DataFrame, 
                             color_code: bool,
                             custom_title: bool,
                             xtick_rotation: bool,
                             legend_on: bool,
                             current_style: bool,
                             orientation: bool) -> bool:
        
        """This function evaluates whether each of the parameters configured for a scatter plot are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def bar_config_check(pd_dataframe: pd.DataFrame,
                         color_code: bool,
                         custom_title: bool,
                         xtick_rotation: bool,
                         legend_on: bool,
                         current_style: bool,
                         orientation: bool,
                         single_axes: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a bar plot are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.single_axes_check(single_axes))
        
        print(bool_list)
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def box_config_check(pd_dataframe: pd.DataFrame,
                         color_code: bool,
                         custom_title: bool,
                         xtick_rotation: bool,
                         legend_on: bool,
                         space_legend_out: bool,
                         current_style: bool,
                         orientation: bool,
                         palette: bool,
                         z_axis_color: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a box plot are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.space_legend_out_check(space_legend_out))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        bool_list.append(ChartAttributeRules.z_axis_color_check(z_axis_color))
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def pie_config_check(pd_dataframe: pd.DataFrame,
                         custom_title: bool,
                         legend_on: bool,
                         space_legend_out: bool,
                         current_style: bool,
                         palette: bool,
                         rotation: bool,
                         chosen_slice: bool,
                         donut: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a pie chart are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.space_legend_out_check(space_legend_out))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        bool_list.append(ChartAttributeRules.rotation_check(rotation))
        bool_list.append(ChartAttributeRules.chosen_slice_check(chosen_slice))
        bool_list.append(ChartAttributeRules.donut_check(donut))
                
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def histogram_config_check(pd_dataframe: pd.DataFrame,
                               color_code: bool,
                               custom_title: bool,
                               xtick_rotation: bool,
                               legend_on: bool,
                               current_style: bool,
                               n_bins: bool,
                               histogram_type: bool) -> bool:
        
        """This function evaluates whether each of the parameters configured for a histogram are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.n_bins_check(n_bins))
        bool_list.append(ChartAttributeRules.histogram_type_check(histogram_type))
        
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def multiline_config_check(pd_dataframe: pd.DataFrame,
                               custom_title: bool,
                               xtick_rotation: bool,
                               legend_on: bool,
                               space_legend_out: bool,
                               current_style: bool,
                               orientation: bool,
                               palette: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a multiline graph are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.space_legend_out_check(space_legend_out))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def multiscatter_config_check(pd_dataframe: pd.DataFrame,
                                  custom_title: bool,
                                  xtick_rotation: bool,
                                  legend_on: bool,
                                  space_legend_out: bool,
                                  current_style: bool,
                                  orientation: bool,
                                  palette: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a multiscatter plot are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.space_legend_out_check(space_legend_out))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def multibar_config_check(pd_dataframe: pd.DataFrame,
                              custom_title: bool,
                              xtick_rotation: bool,
                              legend_on: bool,
                              space_legend_out: bool,
                              current_style: bool,
                              orientation: bool,
                              palette: bool,
                              single_axes: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a multibar chart are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.legend_on_check(legend_on))
        bool_list.append(ChartAttributeRules.space_legend_out_check(space_legend_out))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.orientation_check(orientation))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        bool_list.append(ChartAttributeRules.single_axes_check(single_axes))
        
                
        if all(bool_list) is True:
            return True
        else:
            return False

    @staticmethod
    def facet_config_check(pd_dataframe: pd.DataFrame,
                           color_code: bool,
                           custom_title: bool,
                           xtick_rotation: bool,
                           figure_width: bool,
                           figure_height: bool,
                           current_style: bool,
                           palette: bool,
                           n_bars_per_facet: bool) -> bool:

        """This function evaluates whether each of the parameters configured for a facet plot are valid. 
        If so, a boolean value of True is returned and the plot is configured. If False, no plot is generated.
        """
        
        bool_list = []
        bool_list.append(ChartAttributeRules.color_code_check(color_code))
        bool_list.append(ChartAttributeRules.custom_title_check(custom_title))
        bool_list.append(ChartAttributeRules.xtick_rotation_check(xtick_rotation))
        bool_list.append(ChartAttributeRules.figure_width_check(figure_width))
        bool_list.append(ChartAttributeRules.figure_height_check(figure_height))
        bool_list.append(ChartAttributeRules.current_style_check(current_style))
        bool_list.append(ChartAttributeRules.palette_check(palette))
        bool_list.append(ChartAttributeRules.n_bars_per_facet_check(n_bars_per_facet))
                    
        if all(bool_list) is True:
            return True
        else:
            return False

