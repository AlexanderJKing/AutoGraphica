"""app_screens
This module is responsible for creating all Screens (Pages) in the app, with the exception of the DisplayPage, which has its own module.
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import pandas as pd
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.navigationrail import MDNavigationRail
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from root.instantiation_create_chart_instance import CreateChartInstance


class FileModuleApp(Widget):

    """
    This class is responsible for navigating the user's file system. This occurs when the user is 
    prompted to either select a file to input, or save the output of the charts generated.
    
    Attributes
    ----------
    file_manager_obj_browse: kivyMD.MDFileManager
        A file manager instance to navigate the user's file system when looking for a csv/xlsx file.
    file_manager_obj_save: kivyMD.MDFileManager
        A file manager instance to navigate the user's file system when to save a single chart.
    file_manager_obj_save_all: kivyMD.MDFileManager
        A file manager instance to navigate the user's file system when to save all charts.
    """
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.file_manager_obj_browse = MDFileManager(
            # Selection path = where this starts
            select_path=self.select_path_browse,
            # exit_path, what should be the method when the user wants to close the file manager
            exit_manager=self.exit_manager_browse,
            preview=False,
            sort_by_desc=False)
        
        self.file_manager_obj_save = MDFileManager(
            select_path=self.select_path_save,
            exit_manager=self.exit_manager_save,
            preview=False,
            sort_by_desc=False)
        
        self.file_manager_obj_save_all = MDFileManager(
            select_path=self.select_path_save_all,
            exit_manager=self.exit_manager_save_all,
            preview=False,
            sort_by_desc=False)

    
    def select_path_browse(self, path):

        "The input the user selects when choosing a path to a file csv/xlsx"
        
        self.exit_manager_browse()
        self.ids.name_input.text = path

    
    def select_path_save(self, path):

        "The path the user selects when choosing a path to save a single chart to."
        
        self.exit_manager_save()
        if os.path.isdir(path) is True:
            count = 0
            save_name = self.chart_page.split(" ")[0] + "_chart" + f"({count})" + ".png"
            save_path = os.path.join(path, save_name)

            # Now we need to check the path again, in case we already saved a chart there with the same name.
            x = False
            while x is False:    
                if os.path.exists(save_path):
                    count += 1
                    save_name = self.chart_page.split(" ")[0] + "_chart" + f"({count})" + ".png"
                    save_path = os.path.join(path, save_name)
                else:
                    x = True
            
            self.chart_figure.tight_layout()
            self.chart_figure.savefig(save_path, dpi=199, bbox_inches='tight')

        self.swiper_index = 0
        self.chart_figure = None
        self.chart_page = ''
    

    
    def select_path_save_all(self, path):

        "The path the user selects when choosing a directory to save all charts to."
        
        self.exit_manager_save_all()
        if os.path.isdir(path) is True:
    
            count = 0
            for chart in self.full_chart_list:
                chart.tight_layout()
                save_name = self.chart_page.split(" ")[0] + "_chart" + f"({count})" + ".png"
                save_path = os.path.join(path, save_name)
                
                chart.savefig(save_path, dpi=199, bbox_inches='tight')
                count += 1

        self.full_chart_list = []
        self.chart_page = ''

    
    def open_file_manager(self,
                          swiper_index=None,
                          chart_figure=None,
                          chart_page=None,
                          single_chart=None,
                          full_chart_list=[]):

        """This function opens the file manager object at the root directory on the user's computer.
        It determines whether just browse the file system, to save a single output, or to save all outputs.

        Parameters
        ----------
        swiper_index: int
            The position of the swiper on the Display Page. 
        chart_figure:
            The figure of the chart.
        chart_page: str
            The current page the user is on (i.e. the chart type selected).
        single_chart: bool
            Boolean value indicating whether the user intends to save a single output, all outputs, or browse the file system.
        full_chart_list: list
            A list of all chart objects/
        """

        if single_chart is None:
            # Without this method, we cannot say where the mnaager can start from. 
            self.file_manager_obj_browse.show('/')
        elif single_chart is True:
            self.file_manager_obj_save.show('/')
            # We are only saving a single chart
            self.swiper_index = swiper_index
            self.chart_figure = chart_figure
            self.chart_page = chart_page
        elif single_chart is False:
            self.file_manager_obj_save_all.show('/')
            self.full_chart_list = full_chart_list
            self.chart_page = chart_page

    
    def exit_manager_browse(self, *args):
        # Make sure to add *args to the parameters, otherwise it will throw an error. 
        self.file_manager_obj_browse.close()
        
    def exit_manager_save(self, *args):
        self.file_manager_obj_save.close()
        
    def exit_manager_save_all(self, *args):
        self.file_manager_obj_save_all.close()
            
        
        
        
class HomePage(FileModuleApp, MDScreen, MDFloatLayout):

    """
    This class is responsible for creating the Home Page of the app.
    it is from here, that the file inputted by the user will be validated and the options to navigate to different charts will be displayed.
    """
    
    
    def validate_dataframe(self, file_path: str):

        "This function validates the file inputted by the user, and if valid, creates a DataFrame from it."
        
        file_path = file_path.strip()
        
        if os.path.exists(file_path) is True:   
            if file_path.endswith(".csv"):
                dataframe = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                dataframe = pd.read_excel(file_path)
            else:
                dataframe = None    
        else:
            dataframe = None
            
        return dataframe
                    
                     
    def disable_navrail(self):

        "This function enables/disables the nav rail depending on whether a valid file path has been inputted by the user."
        
        input_text = self.ids.name_input.text.strip()
        # if the textfield is empty, leave navrail disabled. 
        if input_text == "":
            self.ids.nav_rail.disabled = True
            
        else:
            if os.path.isfile(input_text) is True:
                dataframe = self.validate_dataframe(input_text)
                # So now if a DataFrame is not created, the NavRail won't activate. 
                if dataframe is not None:
                    self.ids.nav_rail.disabled = False
                else:
                    self.ids.nav_rail.disabled = True
            else:
                self.ids.nav_rail.disabled = True
                
                
    def clear_url_textbox(self):
        
        "This function clears the URL textbox displayed on the Home Page of any text."
        
        self.ids.name_input.text = ""
        self.disable_navrail()
        
        
    def call_change_nav_screen(self, id_, home_url_path, screen_manager):

        """This function changes the screen to the desired chart page the user has clicked on from the Nav Rail on the left-hand side of the Home Page of the app.

        Parameters
        ----------
        id_: str
            The Chart Option the user selected on the Nav Rail.
        home_url_path: str
            The path to the file inputted by the user.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        """

        # dataframe = self.validate_dataframe(self.md_screen_manager.get_screen('Home Page').ids.name_input.text)
        dataframe = self.validate_dataframe(home_url_path)
        
        if dataframe is not None:
            if id_ == 'Line':
                screen_manager.current = 'Line Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Scatter':
                screen_manager.current = 'Scatter Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Bar':
                screen_manager.current = 'Bar Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Box':
                screen_manager.current = 'Box Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Pie':
                screen_manager.current = 'Pie Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Histogram':
                screen_manager.current = 'Histogram Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'MultiLine':
                screen_manager.current = 'MultiLine Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'MultiScatter':
                screen_manager.current = 'MultiScatter Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'MultiBar':
                screen_manager.current = 'MultiBar Page'
                screen_manager.transition.direction = "left"

            elif id_ == 'Facet':
                # Need to initialize the dataframe as a class attribute for the 'initialize_facet_variables()' method
                self.dataframe = dataframe
                self.initialize_facet_variables()
                screen_manager.current = 'Facet Page'
                screen_manager.transition.direction = "left"
                return dataframe, "is-facet"
            
            return dataframe, "not-facet"
        
        
    # Facet Methods
    def initialize_facet_variables(self):

        "This function initializes any facet variables found within the file inputted by the user."
        
        chart_creator_instance = CreateChartInstance(pd_dataframe=self.dataframe,
                                                     chart_type="Facet",
                                                     chart_parameters=[None, None, None, None, None, None, None, None])
        chart_instance = chart_creator_instance.validate_chart_attributes()
        self.facet_high_cardinal_variables = chart_instance.high_cardinal_x_variables
        self.facet_y_variables = chart_instance.y_list
        

class LinePage(MDScreen):

    "A blank LinePage instance, which is configured in the '.kv' file."
    
    pass


class ScatterPage(MDScreen):

    "A blank ScatterPage instance, which is configured in the '.kv' file."
    
    pass


class BarPage(MDScreen):

    "A blank BarPage instance, which is configured in the '.kv' file."
    
    pass


class BoxPage(MDScreen):

    "A blank BoxPage instance, which is configured in the '.kv' file."
    
    pass


class PiePage(MDScreen):

    "A blank PiePage instance, which is configured in the '.kv' file."
    
    pass


class HistogramPage(MDScreen):

    "A blank HistogramPage instance, which is configured in the '.kv' file."
    
    pass


class MultiLinePage(MDScreen):

    "A blank MultiLinePage instance, which is configured in the '.kv' file."
    
    pass


class MultiScatterPage(MDScreen):

    "A blank MultiScatterPage instance, which is configured in the '.kv' file."
    
    pass


class MultiBarPage(MDScreen):

    "A blank MultiBarPage instance, which is configured in the '.kv' file."
    
    pass


class FacetPage(MDScreen):

    "A blank FacetPage instance, which is configured in the '.kv' file."

    pass


class DisplayPage(MDScreen):

    "A blank DisplayPage instance, which is configured in the '.kv' file."
    
    pass


