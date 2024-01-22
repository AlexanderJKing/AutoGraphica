"""app_facet_page
A module responsible for initializing the Facet Page in the app. This page stands out given the complexity involved,
and as a result there are multiple drop-down menus that are not located in the 'app_drop_down_menus' module.
"""

from kivymd.uix.menu import MDDropdownMenu


class FacetPageInitialization:

    """
    This is a Mixin class responsible for initializing the Facet Page with the various options available to the user to configure the Facet Plot. 
    """
    
    @staticmethod  
    def dropdown_facet_x_menu(chart_type, screen_manager, high_cardinal_variables, facet_y_variables):

        """This function creates the drop-down menu for all columns in the file considered to be of high enough cardinality to plot in a Facet Plot
        If there are fields in the file that can be plotted along the x-axis and y-axis together, then the function will enable them for configuration. 

        Parameters
        ----------
        chart_type: str
            The chart type selected by the user.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        high_cardinal_variables: list
            A list of all high cardinal variables available to plot along the 'x-axis'.
        facet_y_variables: list
            A list of all variables available to plot along the 'y-axis'.
        """
        
        facet_x_menu_items = [{"text": f"{variable}", "on_release": lambda x=f"{variable}": FacetPageInitialization.facet_x_menu_callback(x, chart_type, screen_manager)} for variable in high_cardinal_variables]
        facet_y_menu_items = [{"text": f"{variable}", "on_release": lambda x=f"{variable}": FacetPageInitialization.facet_y_menu_callback(x, chart_type, screen_manager)} for variable in facet_y_variables]
        
        if len(facet_x_menu_items) > 0 and len(facet_y_menu_items) > 0:
            facet_variable_menu = MDDropdownMenu(caller=screen_manager.get_screen(chart_type).ids.high_cards_button, items=facet_x_menu_items)
            facet_variable_menu.open()
    
    @staticmethod
    def facet_x_menu_callback(text_item, chart_type, screen_manager):

        "A callback method that gets triggered when the user clicks the drop-down menu"
        
        screen_manager.get_screen(chart_type).ids.high_card_vars.text = text_item
        FacetPageInitialization.enable_facet_y_attribute(screen_manager)
    
    @staticmethod
    def enable_facet_y_attribute(screen_manager):

        "A function to enable the 'y-axis' variables drop-down menu to be displayed."
        
        high_card_check = screen_manager.get_screen("Facet Page").ids.high_card_vars.text
        if high_card_check == "" or high_card_check is None:
            screen_manager.get_screen("Facet Page").ids.y_axis_button.disabled = True
        else:
            screen_manager.get_screen("Facet Page").ids.y_axis_button.disabled = False
      
    @staticmethod 
    def dropdown_facet_y_menu(chart_type, screen_manager, facet_y_variables):

        """This function creates the drop-down menu for all columns in the file that can be plotted along the 'y-axis' in a Facet Plot.

        Parameters
        ----------
        chart_type: str
            The chart type selected by the user.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        facet_y_variables: list
            A list of all variables available to plot along the 'y-axis'.
        """
        
        facet_y_menu_items = [{"text": f"{variable}", "on_release": lambda x=f"{variable}": FacetPageInitialization.facet_y_menu_callback(x, chart_type, screen_manager)} for variable in facet_y_variables]
        
        if len(facet_y_menu_items) > 0:
            facet_variable_menu = MDDropdownMenu(caller=screen_manager.get_screen(chart_type).ids.y_axis_button, items=facet_y_menu_items)
            facet_variable_menu.open()
            
    @staticmethod        
    def facet_y_menu_callback(text_item, chart_type, screen_manager):

        "A callback method that gets triggered when the user clicks the drop-down menu"
        
        screen_manager.get_screen(chart_type).ids.y_vars.text = text_item
        FacetPageInitialization.enable_facet_plot_attributes(screen_manager)
    
              
    @staticmethod            
    def enable_facet_plot_attributes(screen_manager):

        "A function that enables all widgets on the Facet page, or disables them."
        
        y_axis_check = screen_manager.get_screen("Facet Page").ids.y_vars.text
        high_card_check = screen_manager.get_screen("Facet Page").ids.high_card_vars.text
        
        if (y_axis_check == "" and high_card_check == "") or (y_axis_check is None and high_card_check is None)\
        or (y_axis_check is None and high_card_check == "") or (y_axis_check == "" and high_card_check is None):
            
            screen_manager.get_screen("Facet Page").ids.styles_button.disabled = True
            screen_manager.get_screen("Facet Page").ids.title_input.disabled = True
            screen_manager.get_screen("Facet Page").ids.xtick_input.disabled = True
            screen_manager.get_screen("Facet Page").ids.color_input.disabled = True
            screen_manager.get_screen("Facet Page").ids.palettes_button.disabled = True
            screen_manager.get_screen("Facet Page").ids.n_bars_per_facet.disabled = True
            screen_manager.get_screen("Facet Page").ids.fig_height.disabled = True
            screen_manager.get_screen("Facet Page").ids.fig_width.disabled = True
            screen_manager.get_screen("Facet Page").ids.fig_width.disabled = True
            screen_manager.get_screen("Facet Page").ids.validate_button.disabled = True
        else:
            screen_manager.get_screen("Facet Page").ids.styles_button.disabled = False
            screen_manager.get_screen("Facet Page").ids.title_input.disabled = False
            screen_manager.get_screen("Facet Page").ids.xtick_input.disabled = False
            screen_manager.get_screen("Facet Page").ids.color_input.disabled = False
            screen_manager.get_screen("Facet Page").ids.palettes_button.disabled = False
            screen_manager.get_screen("Facet Page").ids.n_bars_per_facet.disabled = False
            screen_manager.get_screen("Facet Page").ids.fig_height.disabled = False
            screen_manager.get_screen("Facet Page").ids.fig_width.disabled = False
            screen_manager.get_screen("Facet Page").ids.fig_width.disabled = False
            screen_manager.get_screen("Facet Page").ids.validate_button.disabled = False

