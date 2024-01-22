"""app_dialogs
This module is responsible for generating all dialog boxes that appear to the user when certain actions are committed.
"""

from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRoundFlatButton, MDFillRoundFlatButton


class Dialogs:

    """
    This class is a Mixin class created to define each of the separate dialog boxes that appear given certain scenarios.
    """
    
    @staticmethod
    def read_info_options(chart_type):

        "This function determines the content of the info dialog button, based on the selected chart input." 

        info_text = ""

        if chart_type == "Line":
            from app_information import line_graph_info
            info_text = line_graph_info
        elif chart_type == "Scatter":
            from app_information import scatter_plot_info
            info_text = scatter_plot_info
        elif chart_type == "Bar":
            from app_information import bar_chart_info
            info_text = bar_chart_info
        elif chart_type == "Box":
            from app_information import box_plot_info
            info_text = box_plot_info
        elif chart_type == "Pie":
            from app_information import pie_chart_info
            info_text = pie_chart_info
        elif chart_type == "Histogram":
            from app_information import histogram_plot_info
            info_text = histogram_plot_info
        elif chart_type == "MultiLine":
            from app_information import multiline_plot_info
            info_text = multiline_plot_info
        elif chart_type == "MultiScatter":
            from app_information import multiscatter_plot_info
            info_text = multiscatter_plot_info
        elif chart_type == "MultiBar":
            from app_information import multibar_plot_info
            info_text = multibar_plot_info
        elif chart_type == "Facet":
            from app_information import facet_plot_info
            info_text = facet_plot_info

        return chart_type, info_text

    
    @staticmethod
    def info_dialog(info_page, *args):

        """This function is responsible for creating the 'info' dialog that pops up when a user wishes to see information about the chart they can configure.

        Parameters
        ----------
        info_page: str
            The name of the page the user is currently on (i.e. the chart type).
        *args: 
            A number of arguments that get passed to the function upon action from the user when clicking buttons or entering text.
        """

        chart_type, info_text = Dialogs.read_info_options(info_page)

        layout = MDBoxLayout(orientation='vertical', adaptive_height=True)  # set orientation and use adaptive_height
        label = MDLabel(text=info_text, halign="left", valign="top", adaptive_height=True)
        layout.add_widget(label)

        dialog = MDDialog(
            title=f"{chart_type} Configuration Information",
            type="custom",
            content_cls=MDScrollView(size=(Window.width / 2, Window.height / 2)),  # set content of dialog to a ScrollView
            buttons=[
                MDFillRoundFlatButton(text="Close",
                                      text_color='black',
                                      on_release=lambda *args: dialog.dismiss()
                                     )
            ])

        dialog.content_cls.add_widget(layout)  # add the BoxLayout to the ScrollView
        dialog.update_height()  # update the dialog
        dialog.open()
        
    
    @staticmethod
    def alert_dialog(alert_text, text_color):

        """This function is responsible for creating the 'alert' dialog that pops up when a user has inputted incorrect values in the chart configuration.

        Parameters
        ----------
        alert_text: str
            The text that pops up in the alert dialog box.
        text_color: str
            The string representation of the color the text will be in.
        """
        
        dialog = MDDialog(text=alert_text,
                          buttons=[
                              MDFillRoundFlatButton(text="Close",
                                                    theme_text_color="Custom",
                                                    text_color='black',
                                                    on_release=lambda *args: dialog.dismiss()
                                                   )
                          ])
        dialog.open()



