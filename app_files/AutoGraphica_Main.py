"""AutoGraphica_Main
This is the main module, and is responsible forr building the foundations of the App.
"""

from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'resizable', True)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.write()
    

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kivy.resources import resource_add_path
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label.label import MDLabel
from kivymd.icon_definitions import md_icons

from root.instantiation_file_controller import FileController
from root.instantiation_create_chart_instance import CreateChartInstance
from app_get_attributes import DefineAttributes
from app_topbar import TopBarTools
from app_on_marked import OnMarked
from app_dialogs import Dialogs
from app_facet_page import FacetPageInitialization
from app_drop_down_menus import DropDownMenus
from app_create_display_page import CreateDisplayPage
from app_screens import FileModuleApp, HomePage, LinePage, ScatterPage, BarPage, BoxPage, PiePage, HistogramPage, MultiLinePage, MultiScatterPage, MultiBarPage, FacetPage, DisplayPage


Builder.load_file(os.path.join(os.path.dirname(__file__), "AutoGraphica_Main.kv"))

class AutoGraphicaApp(FileModuleApp, MDApp):

    """
    This is the main class that will run the app and contains the 'build()' function,
    which serves as a 'quasi' init function, responsible for initializing basic attributes about the class.
    """

    dialog = None
         
    def build(self): 

        """The build function establishes the platform, window size, and foundational attributes.

        Attributes
        ----------
        icon: str
            The path to the App icon
        theme_style: str
            The overall theme style
        primary_palette: str
            The primary palette of the app
        primary_hue: str
            The primary hue of the selected palette for the app.
        md_screen_manager: kivyMD.MDScreenManager
            The main screen manager instance, setup to manage the various screens (pages) added to the app.
        """
        
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (1300, 800)
        
        self.icon = self.resource_path("images/home_page_design.jpg")
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "100"
        
        self.md_screen_manager = MDScreenManager()
        self.md_screen_manager.add_widget(HomePage(name="Home Page"))
        self.md_screen_manager.add_widget(LinePage(name="Line Page"))
        self.md_screen_manager.add_widget(ScatterPage(name="Scatter Page"))
        self.md_screen_manager.add_widget(BarPage(name="Bar Page"))
        self.md_screen_manager.add_widget(BoxPage(name="Box Page"))
        self.md_screen_manager.add_widget(PiePage(name="Pie Page"))
        self.md_screen_manager.add_widget(HistogramPage(name="Histogram Page"))
        self.md_screen_manager.add_widget(MultiLinePage(name="MultiLine Page"))
        self.md_screen_manager.add_widget(MultiScatterPage(name="MultiScatter Page"))
        self.md_screen_manager.add_widget(MultiBarPage(name="MultiBar Page"))
        self.md_screen_manager.add_widget(FacetPage(name="Facet Page"))
        self.md_screen_manager.add_widget(DisplayPage(name="Display Page"))
        return self.md_screen_manager
    
    # === Add to create executable with PyInstaller ===
    # we need a function to make our script look in the correct folder for files
    # when pyinstaller has created the MEIPASS directory then we need to look in there. 
    # so this assumes all our files (.py, .kv, .png, etc.) are copied into a new folder for pyinstaller to look in. 
    # in the '.spec' file, we'll then need to do some extra work to make this work. 
    # if MEIPASS isn't there, then we want the relative path as per the code. 
    # we do this by creating the absolute path to the current directory, represented by a dot '.'
    # we then need to use this function everywhere we refer to a file, including file references
    # in the kv file, that's why we stick the function in the App class, so we can refer to it in the '.kv' file via 'app'. 
    
    @staticmethod
    def resource_path(relative_path):

        "This function returns an absolute path"
        
        try:
            base_path = sys._MEIPASS
        except Exception:
            # derive the absolute path of the relative_path
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)
    
        
    def validate_attributes(self, chart_type: str):

        """This function validates the attributes submitted by the user, and provided they are valid, constructs the DisplayPage
        and navigates to it based on the inputted chart type the user has selected.
        """
               
        if chart_type == "Line Config":
            self.chosen_page = "Line Page"
            attributes = DefineAttributes.define_line_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Line")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
            
        elif chart_type == "Scatter Config":
            self.chosen_page = "Scatter Page"
            attributes = DefineAttributes.define_scatter_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Scatter")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "Bar Config":
            self.chosen_page = "Bar Page"
            attributes = DefineAttributes.define_bar_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Bar")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "Box Config":
            self.chosen_page = "Box Page"
            attributes = DefineAttributes.define_box_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Box")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "Pie Config":
            self.chosen_page = "Pie Page"
            attributes = DefineAttributes.define_pie_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Pie")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "Histogram Config":
            self.chosen_page = "Histogram Page"
            attributes = DefineAttributes.define_histogram_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Histogram")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "MultiLine Config":
            self.chosen_page = "MultiLine Page"
            attributes = DefineAttributes.define_multiline_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="MultiLine")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "MultiScatter Config":
            self.chosen_page = "MultiScatter Page"
            attributes = DefineAttributes.define_multiscatter_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="MultiScatter")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "MultiBar Config":
            self.chosen_page = "MultiBar Page"
            attributes = DefineAttributes.define_multibar_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="MultiBar")
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        elif chart_type == "Facet Config":
            self.chosen_page = "Facet Page"
            attributes = DefineAttributes.define_facet_attributes(self.show_alert_dialog, self, self.md_screen_manager)
            
            if attributes is None:
                return
            else:
                self.create_display_page(dataframe=self.dataframe, chart_attributes=attributes, chart_type="Facet", facet_chart=True)
                # Now change the screen
                if self.dataframe is not None:
                    self.md_screen_manager.current = 'Display Page'
                    self.md_screen_manager.transition.direction = "left"
            
        return attributes

    ##############################################################################################################################################################################
    # Change Screens
    def change_nav_screen(self, id_):

        """This function changes screens to whatever screen the user has inputted through the '_id', which represents
        the chart type the user would have selected on the Home Page Nav Rail.
        """
        
        home_instance = HomePage()
        url_input = self.md_screen_manager.get_screen('Home Page').ids.name_input.text
        
        # Extract the dataframe, and any high-cardinal x, and y-axis variables for the 'Facet' Screen. 
        self.dataframe, facet_check = home_instance.call_change_nav_screen(id_, url_input, self.md_screen_manager)
        if facet_check == "is-facet":
            self.facet_high_cardinal_variables = home_instance.facet_high_cardinal_variables
            self.facet_y_variables = home_instance.facet_y_variables
        else:
            pass
        
        self.info_page = id_
        
    ##############################################################################################################################################################################
    # Dialog Boxes
    def info_dialog(self, *args):

        "Creates the 'info' dialog box"
        
        Dialogs.info_dialog(info_page=self.info_page)

    def show_alert_dialog(self, alert_text):

        "Creates the 'alert' dialog box"
        
        Dialogs.alert_dialog(alert_text, text_color=self.theme_cls.primary_color)

    ##############################################################################################################################################################################
    # Drop-Down Menus
    def dropdown_style_menu(self, chart_type):

        "Creates the drop-down menu for all 'styles'"
        
        DropDownMenus.dropdown_style_menu(chart_type, screen_manager=self.md_screen_manager)
 
    def dropdown_palette_menu(self, chart_type):

        "Creates the drop-down menu for all 'palettes'"
        
        DropDownMenus.dropdown_palette_menu(chart_type, screen_manager=self.md_screen_manager)

    ##############################################################################################################################################################################
    # On-Marked Methods
    def legend_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        "Creates the 'SegmentButton' for the legend option"
        
        self.legend = OnMarked.legend_on_marked(segment_button, segment_item, marked)
                               
    def orientation_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        "Creates the 'SegmentButton' for the orientation option"
        
        self.orientation = OnMarked.orientation_on_marked(segment_button, segment_item, marked)
        
    def single_axes_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):
        
        "Creates the 'SegmentButton' for the single_axes option"
        
        self.single_axes = OnMarked.single_axes_on_marked(segment_button, segment_item, marked)
        
    def categorical_plot_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool, chart_page):

        "Creates the 'SegmentButton' for the categorical_plot option"

        self.categorical_plot = OnMarked.categorical_plot_on_marked(segment_button, segment_item, marked, chart_page, screen_manager=self.md_screen_manager)
        
    def pie_slice_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        "Creates the 'SegmentButton' for the pie_slice option"
        
        self.pie_slice = OnMarked.pie_slice_on_marked(segment_button, segment_item, marked)
        
    def donut_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        "Creates the 'SegmentButton' for the donut option"
        
        self.donut = OnMarked.donut_on_marked(segment_button, segment_item, marked)

    def histogram_type_on_marked(self, segment_button: MDSegmentedButton, segment_item: MDSegmentedButtonItem, marked: bool):

        "Creates the 'SegmentButton' for the histogram_type option"
        
        self.histogram_type = OnMarked.histogram_type_on_marked(segment_button, segment_item, marked)
 
    # Checkboxes
    def sd_checkbox(self, checkbox, active):
        
        "Creates the Standard Deviation Checkbox"
        
        self.error_bar_type = OnMarked.sd_checkbox(checkbox, active, self.md_screen_manager)
            
    def se_checkbox(self, checkbox, active):
        
        "Creates the Standard Error Checkbox"
        
        self.error_bar_type = OnMarked.se_checkbox(checkbox, active, self.md_screen_manager)
            
    def pi_checkbox(self, checkbox, active):
        
        "Creates the Percentile Interval Checkbox"
        
        self.error_bar_type = OnMarked.pi_checkbox(checkbox, active, self.md_screen_manager)
            
    def ci_checkbox(self, checkbox, active):
        
        "Creates the Confidence Interval Checkbox"
        
        self.error_bar_type = OnMarked.ci_checkbox(checkbox, active, self.md_screen_manager)
    
    ##############################################################################################################################################################################
    # Top-App-Bar Methods
    def refresh_attributes(self, chart_type):

        "Refreshes the page of all buttons selected or text entered by the user when configuring a plot"
        
        facet_check = TopBarTools.refresh_attributes(chart_type, screen_manager=self.md_screen_manager)
        if facet_check == "is-facet":
            FacetPageInitialization.enable_facet_plot_attributes(screen_manager=self.md_screen_manager)
        else:
            pass
        
    def return_home(self, instance):

        "Returns to the Home Page, when the 'Home' button is clicked"
        
        TopBarTools.return_home(instance, self.md_screen_manager)
        
    def back_(self):

        "Returns to whatever the previous page the user was on"
        
        TopBarTools.back_(self, screen_manager=self.md_screen_manager, main_swiper=self.main_swiper)
        
    def previous(self):

        "Returns to the previous slide in the Swiper on the DisplayPage when displaying results"
        
        TopBarTools.previous(main_swiper=self.main_swiper)
    
    def next_(self):

        "Returns to the next slide in the Swiper on the DisplayPage when displaying results"
        
        TopBarTools.next_(main_swiper=self.main_swiper)
        
    def save_fig(self):

        "Saves the current figure the user is on in the DisplayPage"
        
        TopBarTools.save_fig(self)
            
    def save_all_fig(self):

        "Saves all figures generated on the DisplayPage"
        
        TopBarTools.save_all_fig(self)    
        
    ##############################################################################################################################################################################
    # Facet Methods 
    def dropdown_facet_x_menu(self, chart_type):

        "This function initializes the drop-down menu for all high-cardinal columns available to plot on the 'x-axis' of a facet plot"
        
        FacetPageInitialization.dropdown_facet_x_menu(chart_type,
                                                      screen_manager=self.md_screen_manager,
                                                      high_cardinal_variables=self.facet_high_cardinal_variables,
                                                      facet_y_variables=self.facet_y_variables)
        
    def dropdown_facet_y_menu(self, chart_type):

        "This function initializes the drop-down menu for all columns available to plot on the 'y-axis' of a facet plot"
        
        FacetPageInitialization.dropdown_facet_y_menu(chart_type,
                                                      screen_manager=self.md_screen_manager,
                                                      facet_y_variables=self.facet_y_variables)
            
    # ##############################################################################################################################################################################
    # Create the Charts
    def create_display_page(self, dataframe, chart_type: str, chart_attributes: list, facet_chart=False):

        """This function creates the DisplayPage of the app. Each time a chart is selected and generated, the DisplayPage is created all over again.
        
        Parameters
        ----------
        dataframe: pd.DataFrame
            The DataFrame created from the file inputted by the user.
        chart_type: str
            The chart type selected by the user.
        chart_attributes: list
            A list of all chart attributes selected by the user to configure the plot.
        facet_chart: bool
            A boolean value used to determine whether various facet plot configurations need to be initialized.
        """
        
        CreateDisplayPage.create_display_page(main_app_instance=self,
                                              dataframe=dataframe,
                                              chart_type=chart_type,
                                              chart_attributes=chart_attributes,
                                              facet_chart=facet_chart)
        
    
if __name__ == "__main__":
    
    # === Add to create an executable with PyInstaller ===
    if hasattr(sys, '_MEIPASS'):
        resource_add_path((os.path.join(sys._MEIPASS)))
        
    AutoGraphicaApp().run()


    
                       