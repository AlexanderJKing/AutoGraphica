"""app_get_attributes
This module is responsible for collecting all the attributes entered on page by the user.
"""

from matplotlib.colors import is_color_like


class AttributeContainer:

    """
    This is a Mixin class which contains a method for collecting each configurable attributes
    on the Chart configuration pages that the user can input to configure the plot.
    """
    
    @staticmethod
    def get_plot_style(page_id, screen_manager_instance):

        "Returns the plot style"
        
        style = screen_manager_instance.get_screen(page_id).ids.style_input.text
        if style == "":
            return None
        else:
            return style
        
    @staticmethod
    def get_title(page_id, screen_manager_instance):

        "Returns the title"
        
        title = screen_manager_instance.get_screen(page_id).ids.title_input.text
        if title == "":
            return None
        else:
            return title.strip()
    
    @staticmethod
    def get_color(page_id, screen_manager_instance):

        "Returns the color"
        
        color = screen_manager_instance.get_screen(page_id).ids.color_input.text
        if color == "":
            return None
        else:
            return color.strip()
    
    @staticmethod
    def get_legend(class_instance):

        "Returns the legend selection"
        
        if hasattr(class_instance, "legend"):
            return class_instance.legend
        else:
            return None
               
    @staticmethod
    def get_xtick_rotation(page_id, screen_manager_instance):

        "Returns the 'x-tick' rotation"
        
        xtick_rotation = screen_manager_instance.get_screen(page_id).ids.xtick_input.text
        if xtick_rotation == "":
            return None
        else:
            return xtick_rotation.strip()
    
    @staticmethod
    def get_orientation(class_instance):

        "Returns the orientation"
        
        if hasattr(class_instance, "orientation"):
            return class_instance.orientation
        else:
            return None
    
    @staticmethod
    def get_error_bar_type(class_instance):

        "Returns the error bar type"
        
        if hasattr(class_instance, "error_bar_type"):
            return class_instance.error_bar_type
        else:
            return None
    
    @staticmethod
    def get_error_bar_value(page_id, screen_manager_instance):

        "Returns the error bar value"
        
        error_value = screen_manager_instance.get_screen(page_id).ids.error_value_input.text
        
        if error_value == "":
            return None
        else:
            return error_value.strip()
        
    @staticmethod    
    def get_single_axes(class_instance):

        "Returns the single_axes option"

        if hasattr(class_instance, "single_axes"):
            return class_instance.single_axes
        else:
            return None
        
            z_axis_color = AttributeContainer.get_z_axis_color()
            palette = AttributeContainer.get_palette()
            space_legend_out = AttributeContainer.get_space_legend_out()
            
    @staticmethod
    def get_z_axis_color(class_instance):

        "Returns the 'z-axis-color' option"
        
        if hasattr(class_instance, "categorical_plot"):
            return class_instance.categorical_plot
        else:
            return None
    
    @staticmethod
    def get_palette(page_id, screen_manager_instance):

        "Returns the palette"
        
        palette = screen_manager_instance.get_screen(page_id).ids.palette_input.text
        if palette == "":
            return None
        else:
            return palette
    
    @staticmethod
    def get_space_legend_out(page_id, screen_manager_instance):

        "Returns the value by which to space the legend"
        
        legend_spacing = screen_manager_instance.get_screen(page_id).ids.legend_spacing.text
        
        if legend_spacing == "":
            return None
        else:
            return legend_spacing.strip()
        
        
    @staticmethod
    def get_pie_rotation(page_id, screen_manager_instance):  

        "Returns the value by which to rotate the pie chart"
        
        pie_rotation = screen_manager_instance.get_screen(page_id).ids.pie_rotation.text
        
        if pie_rotation == "":
            return None
        else:
            return pie_rotation.strip()
    
    @staticmethod
    def get_pie_slice(class_instance):

        "Returns the slice to explode in a pie chart"
        
        if hasattr(class_instance, "pie_slice"):
            return class_instance.pie_slice
        else:
            return None
    
    @staticmethod
    def get_pie_donut(class_instance):

        "Returns whether to create a donut chart"
        
        if hasattr(class_instance, "donut"):
            return class_instance.donut
        else:
            return None
        
    @staticmethod
    def get_hist_bins(page_id, screen_manager_instance):

        "Returns the number of bins in a histogram"
        
        hist_bins = screen_manager_instance.get_screen(page_id).ids.hist_bins.text
        
        if hist_bins == "":
            return None
        else:
            return hist_bins.strip()
        
    
    @staticmethod
    def get_hist_type(class_instance):

        "Returns the type of histogram"
        
        if hasattr(class_instance, "histogram_type"):
            return class_instance.histogram_type
        else:
            return None
        
    @staticmethod
    def get_bars_per_subplot(page_id, screen_manager_instance):

        "Returns the number of bars per subplot in a facet plot"
        
        bars = screen_manager_instance.get_screen(page_id).ids.n_bars_per_facet.text
        
        if bars == "":
            return None
        else:
            return bars.strip()
    
    @staticmethod
    def get_fig_height(page_id, screen_manager_instance):

        "Returns the figure height in a facet plot"
        
        fig_height = screen_manager_instance.get_screen(page_id).ids.fig_height.text
        
        if fig_height == "":
            return None
        else:
            return fig_height.strip()
    
    @staticmethod
    def get_fig_width(page_id, screen_manager_instance):

        "Returns the figure width in a facet plot"
        
        fig_width = screen_manager_instance.get_screen(page_id).ids.fig_width.text
        
        if fig_width == "":
            return None
        else:
            return fig_width.strip()
        
           
        
class AttributeChecker:

    """
    This is a Mixin class that is responsible for checking that each of the attributes submitted by the user
    in the chart configuration page is a valid attributes. There is a checker for each attribute available across all charts
    
    It will return a string that will be printed in an 'alert' dialog box that pops up, if any entries are invalid.
    """
    
    @staticmethod
    def get_color_checker(color):

        "Returns whether a color submitted is a valid color"
        
        if is_color_like(color) is True:
            return color
        elif color is None:
            return None
        else:
            return "Please input a correct color"
    
    @staticmethod
    def get_xtick_rotation_checker(xtick_rotation):

        "Returns whether the 'x-tick' rotation submitted is a valid number"
        
        if isinstance(xtick_rotation, (int, float, str)):            
            try:
                # Cast it into a float, can't convert directly to int if its a string of a float.
                xtick_rotation = float(xtick_rotation)
                return xtick_rotation         
            except ValueError:
                return "Please input a valid input for rotating the X-Axis Ticks"
            
        elif xtick_rotation is None:
            return None
        
        else:
            return "Please input a valid input for rotating the X-Axis Ticks"
        
        
         
    @staticmethod
    def get_error_bar_value_checker(error_bar_type, error_bar_value):

        "Returns whether the error bar value submitted is a valid number"
        
        if isinstance(error_bar_value, (int, float, str)):
            
            try:
                if error_bar_type in ('sd', 'se') and float(error_bar_value):
                    error_bar_value = float(error_bar_value)
                    return error_bar_value
                elif error_bar_type in ('ci', 'pi') and float(error_bar_value) in range(0, 100):
                    error_bar_value = float(error_bar_value)
                    return error_bar_value
                elif error_bar_type in ('ci', 'pi') and float(error_bar_value) not in range(0, 100):
                    return "Please enter a valid number between 0 - 100"
                else: 
                    raise ValueError
            
            except ValueError:
                return "Please enter a valid number"
            
        elif error_bar_value is None:
            return None
        
        else:
            return False
    
    @staticmethod
    def get_space_legend_out_checker(legend_spacing):

        "Returns whether the value entered to space the legend from the figure is valid"
        
        if legend_spacing is None:
            return None
        
        elif isinstance(legend_spacing, (int, float, str)):
            
            try:
                if float(legend_spacing):
                    if float(legend_spacing) >= 0.0 and float(legend_spacing) <= 1.0:
                        return None
                    else:
                        return "Please input a valid decimal number between 0.0 and 1.0"
                else: 
                    raise ValueError
            
            except ValueError:
                return "Please input a valid input for spacing the legend from the plot"

        else:
            return "Please input a valid input for spacing the legend from the plot"
        
        
    @staticmethod
    def get_pie_rotation_checker(pie_rotation):

        "Returns whether the value entered to rotate the pie chart is valid"
        
        if pie_rotation is None:
            return None
        
        if pie_rotation == "0" or pie_rotation == "0.0":
            return None
        
        elif isinstance(pie_rotation, (int, float, str)):
            try:
                if float(pie_rotation):
                    return None
                else: 
                    raise ValueError
            
            except ValueError:
                return "Please input a valid number for rotating the pie chart"

        else:
            return "Please input a valid number for rotating the pie chart"
        
        
    @staticmethod
    def get_hist_bins_checker(hist_bins):

        "Returns whether the value entered for the number of bins in a histogram is valid"
        
        if hist_bins is None:
            return None
        
        elif hist_bins == "0":
            return None
        
        elif isinstance(hist_bins, str):
            if hist_bins.isdigit():
                return None
            else:
                return "Please enter a valid number for the amount of Histogram Bins"
            
        elif isinstance(hist_bins, int):
            return None
        else:
            return "Please enter a valid number for the amount of Histogram Bins"

        
    @staticmethod
    def get_bars_per_subplot_checker(bars):

        "Returns whether the number of bars the user wishes to display on each facet of a Facet Plot, is valid"
        
        if bars is None:
            return None
        
        elif bars == "0":
            return None
        
        elif isinstance(bars, str):
            if bars.isdigit():
                return None
            else:
                return "Please enter a valid number for the number of bars per subplot"
        
        elif isinstance(bars, int):
            return None
        
        else:
            return "Please enter a valid number for the number of bars per subplot"
        
    @staticmethod
    def get_fig_height_checker(fig_height):

        "Returns whether the height of a figure in the Facet Plot is valid"
        
        if fig_height is None:
            return None
        
        elif fig_height == "0":
            return None
        
        elif isinstance(fig_height, str):
            if fig_height.isdigit():
                return None
            else:
                return "Please enter a valid number for the Height of the Figure"
        
        elif isinstance(fig_height, int):
            return None
        
        else:
            return "Please enter a valid number for the Height of the Figure"
    
    @staticmethod
    def get_fig_width_checker(fig_width):

        "Returns whether the width of a figure in the Facet Plot is valid"
        
        if fig_width is None:
            return None
        
        elif fig_width == "0":
            return None
        
        elif isinstance(fig_width, str):
            if fig_width.isdigit():
                return None
            else:
                return "Please enter a valid number for the Width of the Figure"
        
        elif isinstance(fig_width, int):
            return None
        
        else:
            return "Please enter a valid number for the Width of the Figure"
    

class CollectAttributes:

    """
    This is a Mixin class that is responsible for collecting all of the attributes from each chart page, provided they have been validated.
    They are then collated into a list that is returned at the end of each function.
    """
    
    @staticmethod
    def collect_attributes(chart_page: str, main_instance, screen_manager):

        "Collects the attributes for each chart" 
        
        if chart_page == "Line Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            error_bar_type = AttributeContainer.get_error_bar_type(main_instance)
            error_bar_value = AttributeContainer.get_error_bar_value(chart_page, screen_manager_instance=screen_manager)
            
            attributes = [color_code, custom_title, xtick_rotation, legend_on, current_style, orientation, error_bar_type, error_bar_value]
            return attributes
            
        elif chart_page == "Scatter Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            
            attributes = [color_code, custom_title, xtick_rotation, legend_on, current_style, orientation]
            return attributes
            
        elif chart_page == "Bar Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            single_axes = AttributeContainer.get_single_axes(main_instance)
            
            attributes = [color_code, custom_title, xtick_rotation, legend_on, current_style, orientation, single_axes]
            return attributes
            
        elif chart_page == "Box Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            # space_legend_out = AttributeContainer.get_space_legend_out(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            # palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            # z_axis_color = AttributeContainer.get_z_axis_color(main_instance)
            
            # attributes = [color_code, custom_title, xtick_rotation, legend_on, space_legend_out, current_style, orientation, palette, z_axis_color]
            attributes = [color_code, custom_title, xtick_rotation, legend_on, None, current_style, orientation, None, None]
            
            return attributes
            
        elif chart_page == "Pie Page":
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            space_legend_out = AttributeContainer.get_space_legend_out(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            pie_rotation = AttributeContainer.get_pie_rotation(chart_page, screen_manager_instance=screen_manager)
            pie_slice = AttributeContainer.get_pie_slice(main_instance)
            pie_donut = AttributeContainer.get_pie_donut(main_instance)
            
            attributes = [custom_title, legend_on, space_legend_out, current_style, palette, pie_rotation, pie_slice, pie_donut]
            return attributes
            
        elif chart_page == "Histogram Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            hist_bins = AttributeContainer.get_hist_bins(chart_page, screen_manager_instance=screen_manager)
            hist_type = AttributeContainer.get_hist_type(main_instance)
            
            attributes = [color_code, custom_title, xtick_rotation, legend_on, current_style, hist_bins, hist_type]
            return attributes
            
        elif chart_page == "MultiLine Page":
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            space_legend_out = AttributeContainer.get_space_legend_out(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            
            attributes = [custom_title, xtick_rotation, legend_on, space_legend_out, current_style, orientation, palette]
            return attributes
            
        elif chart_page == "MultiScatter Page":
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            space_legend_out = AttributeContainer.get_space_legend_out(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            
            attributes = [custom_title, xtick_rotation, legend_on, space_legend_out, current_style, orientation, palette]
            return attributes
            
            
        elif chart_page == "MultiBar Page":
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            legend_on = AttributeContainer.get_legend(main_instance)
            space_legend_out = AttributeContainer.get_space_legend_out(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            orientation = AttributeContainer.get_orientation(main_instance)
            palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            single_axes = AttributeContainer.get_single_axes(main_instance)
            
            attributes = [custom_title, xtick_rotation, legend_on, space_legend_out, current_style, orientation, palette, single_axes]
            return attributes
            
            
        elif chart_page == "Facet Page":
            color_code = AttributeContainer.get_color(chart_page, screen_manager_instance=screen_manager)
            custom_title = AttributeContainer.get_title(chart_page, screen_manager_instance=screen_manager)
            xtick_rotation = AttributeContainer.get_xtick_rotation(chart_page, screen_manager_instance=screen_manager)
            fig_width = AttributeContainer.get_fig_width(chart_page, screen_manager_instance=screen_manager)
            fig_height = AttributeContainer.get_fig_height(chart_page, screen_manager_instance=screen_manager)
            current_style = AttributeContainer.get_plot_style(chart_page, screen_manager_instance=screen_manager)
            palette = AttributeContainer.get_palette(chart_page, screen_manager_instance=screen_manager)
            bars = AttributeContainer.get_bars_per_subplot(chart_page, screen_manager_instance=screen_manager)
            
            attributes = [color_code, custom_title, xtick_rotation, fig_width, fig_height, current_style, palette, bars]
            return attributes
        
        
class DefineAttributes:

    """
    This is a Mixin class that is responsible for returning the error messages to 'alert' dialog boxes,
    for any incorrect submissions on the user's behalf when configuring the chart.
    """

    @staticmethod
    def define_line_attributes(alert_dialog_object, main_instance, screen_manager):

        "Defines the line attributes"
        
        attributes = CollectAttributes.collect_attributes("Line Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2]),
                                AttributeChecker.get_error_bar_value_checker(attributes[6], attributes[7])]
        
        for check in attribute_check_list:
            if check == "Please input a correct color":
                alert_dialog_object(check)
                return
            elif check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_object(check)
                return 
            elif check == "Please enter a valid number between 0 - 100":
                alert_dialog_object(check)
                return 
            elif check == "Please enter a valid number":
                alert_dialog_object(check)
                return
            else:
                pass
        return attributes
        
    @staticmethod
    def define_scatter_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the Scatter attributes"
        
        attributes = CollectAttributes.collect_attributes("Scatter Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2])]
        
        for check in attribute_check_list:
            if check == "Please input a correct color":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return 
            else:
                pass
        return attributes
        
    @staticmethod
    def define_bar_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the bar attributes"
        
        attributes = CollectAttributes.collect_attributes("Bar Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2])]
        
        for check in attribute_check_list:
            if check == "Please input a correct color":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return 
            else:
                pass
        return attributes
        
    @staticmethod
    def define_box_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the box attributes"
        
        attributes = CollectAttributes.collect_attributes("Box Page", main_instance, screen_manager)
        # attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
        #                         AttributeChecker.get_xtick_rotation_checker(attributes[2]),
        #                         AttributeChecker.get_space_legend_out_checker(attributes[4])]

        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2])]
                            
        
        for check in attribute_check_list:
            if check == "Please input a correct color":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return 
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return 
            elif check == "Please input a valid decimal number between 0.0 and 1.0":
                alert_dialog_box(check)
                return
            else:
                pass
        
        # 'space_legend_out'
        # if attributes[4] is not None:
            # attributes[4] = float(attributes[4])
        
        return attributes
            
    @staticmethod
    def define_pie_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the Pie attributes"
        
        attributes = CollectAttributes.collect_attributes("Pie Page", main_instance, screen_manager)

        attribute_check_list = [AttributeChecker.get_space_legend_out_checker(attributes[2]), 
                                AttributeChecker.get_pie_rotation_checker(attributes[5])]
        
        for check in attribute_check_list:
            if check == "Please input a valid decimal number between 0.0 and 1.0":
                alert_dialog_box(check)
                return 
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return 
            elif check == "Please input a valid number for rotating the pie chart":
                alert_dialog_box(check)
                return 
        
        # 'space_legend_out'
        if attributes[2] is not None:
            attributes[2] = float(attributes[2])
        # 'pie_rotation'
        if attributes[5] is not None:
            attributes[5] = float(attributes[5])
        # 'pie_slice'
        if attributes[6] == "none":
            attributes[6] = None
        return attributes
    
    @staticmethod
    def define_histogram_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the Histogram attributes"
        
        attributes = CollectAttributes.collect_attributes("Histogram Page", main_instance, screen_manager)
        
        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2]),
                                AttributeChecker.get_hist_bins_checker(attributes[5])]

        for check in attribute_check_list:
            if check == "Please input a correct color":
                self.show_alert_dialog(check)
                return
            elif check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return 
            elif check == "Please enter a valid number for the amount of Histogram Bins":
                alert_dialog_box(check)
                return 
        
        # 'hist_bins'
        if attributes[5] is not None and attributes[5].isdigit():
            attributes[5] = int(attributes[5])
        else:
            attributes[5] = 10

        return attributes
           
    @staticmethod
    def define_multiline_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the MultiLine attributes"
        
        attributes = CollectAttributes.collect_attributes("MultiLine Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_xtick_rotation_checker(attributes[1]),
                                AttributeChecker.get_space_legend_out_checker(attributes[3])]

        for check in attribute_check_list:
            if check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return
            
        # 'space_legend_out'
        if attributes[3] is not None:
            attributes[3] = float(attributes[3])
        return attributes

            
    @staticmethod
    def define_multiscatter_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the MultiScatter attributes"
        
        attributes = CollectAttributes.collect_attributes("MultiScatter Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_xtick_rotation_checker(attributes[1]),
                                AttributeChecker.get_space_legend_out_checker(attributes[3])]

        for check in attribute_check_list:
            if check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return
        
        # 'space_legend_out'
        if attributes[3] is not None:
            attributes[3] = float(attributes[3])
        return attributes

            
    @staticmethod
    def define_multibar_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the MultiBar attributes"
        
        attributes = CollectAttributes.collect_attributes("MultiBar Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_xtick_rotation_checker(attributes[1]),
                                AttributeChecker.get_space_legend_out_checker(attributes[3])]

        for check in attribute_check_list:
            if check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return
        
        # 'space_legend_out'
        if attributes[3] is not None:
            attributes[3] = float(attributes[3])
        return attributes

            
    @staticmethod
    def define_facet_attributes(alert_dialog_box, main_instance, screen_manager):

        "Defines the Facet attributes"
        
        attributes = CollectAttributes.collect_attributes("Facet Page", main_instance, screen_manager)
        attribute_check_list = [AttributeChecker.get_color_checker(attributes[0]),
                                AttributeChecker.get_xtick_rotation_checker(attributes[2]),
                                AttributeChecker.get_fig_width_checker(attributes[3]),
                                AttributeChecker.get_fig_height_checker(attributes[4]),
                                AttributeChecker.get_bars_per_subplot_checker(attributes[7])]

        for check in attribute_check_list:
            if check == "Please input a valid input for rotating the X-Axis Ticks":
                alert_dialog_box(check)
                return
            elif check == "Please input a valid input for spacing the legend from the plot":
                alert_dialog_box(check)
                return
            elif check == "Please enter a valid number for the number of bars per subplot":
                alert_dialog_box(check)
                return
            elif check == "Please enter a valid number for the Height of the Figure":
                alert_dialog_box(check)
                return
            elif check == "Please enter a valid number for the Width of the Figure":
                alert_dialog_box(check)
                return

        if attributes[3] is not None:
            attributes[3] = int(attributes[3])
        if attributes[4] is not None:
            attributes[4] = int(attributes[4])
        if attributes[7] is not None:
            attributes[7] = int(attributes[7])
        return attributes
    
    