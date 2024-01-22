"""app_drop_down_menus
This module is responsible for creating all dropdown menus to dispaly multiple options to the user during certain chart configurations.
"""

from kivymd.uix.menu import MDDropdownMenu


class DropDownMenus:

    """
    This class is a Mixin class that creates drop-down menus for all 'pallete' options available to the user,
    and all 'styles' available to the user during chart configuration.
    """
    
    @staticmethod
    def dropdown_style_menu(chart_type, screen_manager):

        """This function creates a drop-down menu for all Matplotlib styles that the user can configure their plots with.

        Parameters
        ----------
        chart_type: str
            The chart type specified by the user.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        """

        style_options = ['ggplot', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
                         'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
                         'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'dark_background', 'grayscale',
                         'tableau-colorblind10', 'Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'fast', 'fivethirtyeight']

        
        # style_options = ['ggplot', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
        #                  'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid','seaborn-v0_8-deep', 'seaborn-v0_8-muted',
        #                  'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster',
        #                  'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid',
        #                  'dark_background', 'grayscale', 'tableau-colorblind10', 'Solarize_Light2', '_classic_test_patch',
        #                  'bmh', 'classic', 'fast', 'fivethirtyeight', '_mpl-gallery', '_mpl-gallery-nogrid']
                         

        style_menu_items = [{"text": f"{style}", "on_release": lambda x=f"{style}": DropDownMenus.style_menu_callback(x, chart_type, screen_manager)} for style in style_options]

        style_menu = MDDropdownMenu(caller=screen_manager.get_screen(chart_type).ids.styles_button, items=style_menu_items)
        style_menu.open()
    
    @staticmethod
    def style_menu_callback(text_item, chart_type, screen_manager):

        "A callback method that gets triggered when the user clicks the drop-down menu"
        
        screen_manager.get_screen(chart_type).ids.style_input.text = text_item    
        
    
    @staticmethod
    def dropdown_palette_menu(chart_type, screen_manager):

        """This function creates a drop-down menu for all Seaborn palettes that the user can configure their plots with.

        Parameters
        ----------
        chart_type: str
            The chart type specified by the user.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        """
        
        palette_options = ['pastel', 'deep', 'muted', 'bright', 'dark', 'colorblind','tab10', 'tab20', 'tab20b', 'tab20c', 'hls', 'husl', 'Set1', 'Set2', 'Set3',
                           'Paired', 'Accent', 'Pastel1', 'Pastel2', 'Dark2', 'Greys', 'Reds', 'Greens', 'Blues', 'Oranges', 'Purples', 'BuGn', 'BuPu', 'GnBu',
                           'OrRd', 'PuBu', 'RdPu', 'YlGn', 'PuBuGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'RdBu', 'RdGy', 'PRGn', 'PiYG', 'BrBG', 'RdYlBu', 'RdYlGn', 'Spectral',
                           'rocket', 'mako', 'flare', 'crest', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'vlag', 'icefire', 'coolwarm', 'bwr', 'seismic', 'flag',
                           'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                           'turbo', 'nipy_spectral', 'gist_ncar']
        
        palette_menu_items = [{"text": f"{palette}", "on_release": lambda x=f"{palette}": DropDownMenus.palette_menu_callback(x, chart_type, screen_manager)} for palette in palette_options]
        palette_menu = MDDropdownMenu(caller=screen_manager.get_screen(chart_type).ids.palettes_button, items=palette_menu_items)
        palette_menu.open()
    
    @staticmethod
    def palette_menu_callback(text_item, chart_type, screen_manager):

        "A callback method that gets triggered when the user clicks the drop-down menu"
        
        screen_manager.get_screen(chart_type).ids.palette_input.text = text_item





