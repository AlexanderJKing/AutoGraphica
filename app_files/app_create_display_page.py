"""app_create_display_page
This module is responsible for creating the Display page of the app (i.e. where all plots generated will be displayed).
"""

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.swiper.swiper import MDSwiper
from kivymd.uix.swiper.swiper import MDSwiperItem
from app_screens import DisplayPage
from root.instantiation_create_chart_instance import CreateChartInstance
from libs.garden.garden_matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from libs.garden.garden_matplotlib import backend_kivy


class CreateDisplayPage:

    """
    This class is a Mixin class responsible for creating the 'Display' page within the app.
    """
    
    @staticmethod  
    def create_display_page(main_app_instance, dataframe, chart_type: str, chart_attributes: list, facet_chart=False):

        """This function is used to create the display page. It uses a Kivy Swiper widget to display a gallery of plots automatically generated from 
        the file inputted by the user at the home page.

        Parameters
        ----------
        main_app_instance: kivy.MDApp
            The main app instance should be passed into this function.
        dataframe: pd.DataFrame
            The DataFrame created by the user's inputted file.
        chart_type: str
            The chart type of interest selected by the user.
        chart_attributes: list
            A list of all the chart attributes the user wishes to configure the plot with.
        facet_chart: bool
            A boolean value dictating whether any facet operations need to be performed on the plot.
        """
        
        main_app_instance.md_screen_manager.add_widget(DisplayPage(name="Display Page"))                           
        main_app_instance.display_instance = main_app_instance.md_screen_manager.get_screen('Display Page')
                                   
        # Access the main swiper 
        main_app_instance.main_swiper = main_app_instance.md_screen_manager.get_screen('Display Page').ids.swiper
        
        if facet_chart is False:
            main_app_instance.chart_list = CreateDisplayPage.return_chart_instance(main_app_instance, dataframe, chart_type, chart_attributes, facet_chart=False)
        else:
            main_app_instance.chart_list = CreateDisplayPage.return_chart_instance(main_app_instance, dataframe, chart_type, chart_attributes, facet_chart=True)

        print(main_app_instance.chart_list)
                    
        if main_app_instance.chart_list is not None:
            for chart in main_app_instance.chart_list:
                box = MDBoxLayout()
                box.add_widget(FigureCanvasKivyAgg(chart))
                
                # create the swiper object
                swiper = MDSwiperItem()
                swiper.add_widget(box)
                
                main_app_instance.main_swiper.add_widget(swiper)

        print('finding the children')
        for child in main_app_instance.main_swiper.children:
            print(child)

    
    @staticmethod
    def return_chart_instance(main_app_instance, dataframe, chart_type, chart_attributes: list, facet_chart=False):

        """This function generates a list of all possible plots for a given chart type.

        Parameters
        ----------
        main_app_instance: kivy.MDApp
            The main app instance should be passed into this function.
        dataframe: pd.DataFrame
            The DataFrame created by the user's inputted file.
        chart_type: str
            The chart type of interest selected by the user.
        chart_attributes: list
            A list of all the chart attributes the user wishes to configure the plot with.
        facet_chart: bool
            A boolean value dictating whether any facet operations need to be performed on the plot.
        """
    
        # So now we have a DataFrame 
        chart_creator_instance = CreateChartInstance(pd_dataframe=dataframe,
                                                     chart_type=chart_type,
                                                     chart_parameters=chart_attributes)
        chart_instance = chart_creator_instance.validate_chart_attributes()
        
        if chart_instance is not None:
            
            if facet_chart is False:
                chart_list = chart_instance.plot_multiple_charts()
                return chart_list
            
            else:
                x_var = main_app_instance.md_screen_manager.get_screen("Facet Page").ids.high_card_vars.text
                y_var = main_app_instance.md_screen_manager.get_screen("Facet Page").ids.y_vars.text
                if x_var != "" and y_var != "":
                    chart_list = chart_instance.plot_facet_chart(x_var, y_var)
                    return chart_list
        else:
            return None
               
