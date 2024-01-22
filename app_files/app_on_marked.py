"""app_on_marked
This module is responsible for all the SegmentedButton widget options displayed on various Chart configuration pages.
"""

from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem


class OnMarked:

    """
    This is a Mixin class that is responsible for creating all the SegmentedButtons for the:
        - legend
        - orientation
        - single axes
        - categorical plot
        - pie_slice
        - donut
        - histogram type
    It also contains the checkboxes available to tick for the Error Bar Types on the Line Graph Page. 
    """
    
    @staticmethod
    def legend_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the legend option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text 
        if on_marked_value == "on":
            return "on"
        elif on_marked_value == "off":
            return "off"
        else:
            return None
    
    @staticmethod
    def orientation_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the orientation option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text 
        if on_marked_value == "vertical":
            return "vertical"
        elif on_marked_value == "horizontal":
            return "horizontal"
        else:
            return None         
    
    @staticmethod
    def single_axes_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the single_axes option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text 
        if on_marked_value == "on":
            return "on"
        elif on_marked_value == "off":
            return "off"
        else:
            return None
    
    @staticmethod
    def categorical_plot_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool, chart_page, screen_manager):

        """Creates the MDSegmentedButton for the categorical_plot option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        chart_page:
            The name of the page the user is currently on (i.e. the chart type selected).
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        """
        
        on_marked_value = segment_item.text 
        if on_marked_value == "on":
            screen_manager.get_screen(chart_page).ids.legend_spacing.disabled = False
            screen_manager.get_screen(chart_page).ids.palettes_button.disabled = False
            return "on"
        elif on_marked_value == "off":
            screen_manager.get_screen(chart_page).ids.legend_spacing.disabled = True
            screen_manager.get_screen(chart_page).ids.palettes_button.disabled = True
            return "off"
        else:
            return None
    
    @staticmethod
    def pie_slice_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the pie_slice option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text
        if on_marked_value == "smallest":
            return "smallest"
        elif on_marked_value == "largest":
            return "largest"
        elif on_marked_value == "none":
            return "none"
        else:
            return None
    
    @staticmethod
    def donut_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the donut option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text
        if on_marked_value == "on":
            return "on"
        elif on_marked_value == "off":
            return "off"
        else:
            return None
    
    @staticmethod
    def histogram_type_on_marked(segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        """Creates the MDSegmentedButton for the histogram_type option.

        Parameters
        ----------
        segment_button: MDSegmentedButton
            A KivyMD SegmentButton object.
        segment_item: MDSegmentedButtonItem
            A KivyMD SegmentButtonItem object.
        marked: bool
            The value to indicate whether the user has marked the button or not. 
        """
        
        on_marked_value = segment_item.text
        if on_marked_value == "bars":
            return "bars"
        elif on_marked_value == "area":
            return "area"
        else:
            return None
        
        
    @staticmethod
    def sd_checkbox(checkbox, active, screen_manager):

        "The Standard Deviation Checkbox"
        
        if active is True:
            screen_manager.get_screen('Line Page').ids.error_value_input.disabled = False
            return "sd"
        else: 
            screen_manager.get_screen('Line Page').ids.sd_check_input.active = False
            return None
    
    @staticmethod
    def se_checkbox(checkbox, active, screen_manager):

        "The Standard Error Checkbox"
        
        if active is True:
            screen_manager.get_screen('Line Page').ids.error_value_input.disabled = False
            return "se"
        else: 
            screen_manager.get_screen('Line Page').ids.se_check_input.active = False
            return None
    
    @staticmethod
    def pi_checkbox(checkbox, active, screen_manager):

        "The Percentile Interval Checkbox"
        
        if active is True:
            screen_manager.get_screen('Line Page').ids.error_value_input.disabled = False
            return "pi"
        else: 
            screen_manager.get_screen('Line Page').ids.pi_check_input.active = False
            return None
    
    @staticmethod
    def ci_checkbox(checkbox, active, screen_manager):

        "The Confidence Interval Checkbox"
        if active is True:
            screen_manager.get_screen('Line Page').ids.error_value_input.disabled = False
            return "ci"
        else: 
            screen_manager.get_screen('Line Page').ids.ci_check_input.active = False
            return None


