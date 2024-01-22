"""app_topbar
This module is responsible for defining the widgets displayed in the MDTopAppBar,
located in the various chart configuration pages and the Display Page.
"""

import os


class TopBarTools:

    """
    This class is a Mixin class designed to define the functionality behind the various widgets located in the Top App Bars of pages.
    """
    
    @staticmethod
    def refresh_attributes(chart_type: str, screen_manager):

        """This function clears all options that may have been configured at any stage within a chart configuration page.

        Parameters
        ----------
        chart_type: str
            The chart type the user has selected.
        screen_manager: kivyMD.MDScreenManager
            The Kivy Screen Manager object used to manage all screens defined in the app.
        """
        
        if chart_type == "Line Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.sd_check_input.active = False
            screen_manager.get_screen(chart_type).ids.se_check_input.active = False
            screen_manager.get_screen(chart_type).ids.pi_check_input.active = False
            screen_manager.get_screen(chart_type).ids.ci_check_input.active = False
            screen_manager.get_screen(chart_type).ids.error_value_input.text = ""
            screen_manager.get_screen(chart_type).ids.error_value_input.disabled = True
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "Scatter Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()

        elif chart_type == "Bar Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.single_axes_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "Box Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            # screen_manager.get_screen(chart_type).ids.third_axis_input.uncheck_item()
            # screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            # screen_manager.get_screen(chart_type).ids.legend_spacing.text = ""
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            # screen_manager.get_screen(chart_type).ids.palettes_button.disabled = True
            # screen_manager.get_screen(chart_type).ids.legend_spacing.disabled = True

            
        elif chart_type == "Pie Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.pie_slice.uncheck_item()
            screen_manager.get_screen(chart_type).ids.donut.uncheck_item()
            screen_manager.get_screen(chart_type).ids.pie_rotation.text = ""
            screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            screen_manager.get_screen(chart_type).ids.legend_spacing.text = ""
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "Histogram Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.hist_bins.text = ""
            screen_manager.get_screen(chart_type).ids.hist_type.uncheck_item()
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "MultiLine Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            screen_manager.get_screen(chart_type).ids.legend_spacing.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "MultiScatter Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            screen_manager.get_screen(chart_type).ids.legend_spacing.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
        elif chart_type == "MultiBar Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            screen_manager.get_screen(chart_type).ids.legend_spacing.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.orientation_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.single_axes_input.uncheck_item()
            screen_manager.get_screen(chart_type).ids.legend_input.uncheck_item()
            
            
        elif chart_type == "Facet Page":
            screen_manager.get_screen(chart_type).ids.style_input.text = ""
            screen_manager.get_screen(chart_type).ids.title_input.text = ""
            screen_manager.get_screen(chart_type).ids.xtick_input.text = ""
            screen_manager.get_screen(chart_type).ids.color_input.text = ""
            screen_manager.get_screen(chart_type).ids.palette_input.text = ""
            screen_manager.get_screen(chart_type).ids.n_bars_per_facet.text = ""
            screen_manager.get_screen(chart_type).ids.fig_height.text = ""
            screen_manager.get_screen(chart_type).ids.fig_width.text = ""
            screen_manager.get_screen(chart_type).ids.high_card_vars.text = ""
            screen_manager.get_screen(chart_type).ids.y_vars.text = ""
            screen_manager.get_screen(chart_type).ids.y_axis_button.disabled = True
            
            return "is-facet"
        
        return "not-facet"
    
    @staticmethod
    def return_home(instance, screen_manager):

        "This function returns the user to the Home screen, when the 'Home' button is selected."
        
        if screen_manager.current == "Display Page":
            TopBarTools.remove_display_page(screen_manager)
            
        screen_manager.current = 'Home Page'
        screen_manager.transition.direction = "right"
    
    @staticmethod
    def back_(main_app_instance, screen_manager, main_swiper):

        "This function goes back a previous page to either the chart configuration page the user was on, or the Home page."
        
        if hasattr(main_app_instance, "chosen_page"):
                  
            screen_manager.current = main_app_instance.chosen_page
            screen_manager.transition.direction = "right"
        
        # delete the 'MDSwiperItems' within the box layout, within the 'main_swiper'
        swiper_box_layout = main_swiper.children[0]
        swiper_box_layout.clear_widgets()
        TopBarTools.remove_display_page(screen_manager)
    
    @staticmethod
    def previous(main_swiper):

        "This function goes back a previous slide in the DisplayPage when displaying the output."
                
        if main_swiper.get_current_index() > 0:
            main_swiper.set_current(main_swiper.get_current_index() - 1)
    
    @staticmethod
    def next_(main_swiper):

        "This function goes forward a slide in the DisplayPage when displaying the output."
        
        if main_swiper.get_current_index() < len(main_swiper.get_items()) - 1:
            main_swiper.set_current(main_swiper.get_current_index() + 1)    
            
    @staticmethod
    def remove_display_page(screen_manager):

        "This function removes the DisplayPage (blanks it) from the ScreenManager, so it can be recreated when a new chart is selected"
        
        screen_manager.remove_widget(screen_manager.get_screen('Display Page'))
        
        
    @staticmethod
    def save_fig(main_app_instance):

        "This function saves a single figure when the 'Save' button is clicked"
        
        if hasattr(main_app_instance, "chart_list"):

            current_swiper_index = int(main_app_instance.main_swiper.get_current_index())
            current_chart = main_app_instance.chart_list[current_swiper_index]
            
            main_app_instance.open_file_manager(swiper_index=current_swiper_index,
                                                chart_figure=current_chart,
                                                chart_page=main_app_instance.chosen_page,
                                                single_chart=True)
    
    @staticmethod
    def save_all_fig(main_app_instance):

        "This function saves all figures when the 'Save All' button is clicked"
        
        if hasattr(main_app_instance, "chart_list"):

            main_app_instance.open_file_manager(full_chart_list=main_app_instance.chart_list,
                                                chart_page=main_app_instance.chosen_page,
                                                single_chart=False)



