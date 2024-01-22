"""root.support_rcParams
A module containing the default pre-set rcparams when plotting the different charts.
"""

import matplotlib.pyplot as plt

class RCParams:

    """
    A class establishing some basic rcParams universal to all plots.
    
    Attributes
    ----------
    style_list: list
        A list of all matplotlib styles applicable to the plots.
    """
    
    def __init__(self):
        self.initialize_rcParams()
        self.style_list = ['Solarize_Light2',
                           '_classic_test_patch',
                           'bmh',
                           'classic',
                           'dark_background',
                           'fast',
                           'fivethirtyeight',
                           'ggplot',
                           'grayscale',
                           'seaborn',
                           'seaborn-bright',
                           'seaborn-colorblind',
                           'seaborn-dark',
                           'seaborn-dark-palette',
                           'seaborn-darkgrid',
                           'seaborn-deep',
                           'seaborn-muted',
                           'seaborn-notebook',
                           'seaborn-paper',
                           'seaborn-pastel',
                           'seaborn-poster',
                           'seaborn-talk',
                           'seaborn-ticks',
                           'seaborn-white',
                           'seaborn-whitegrid',
                           'tableau-colorblind10']

        
    def initialize_rcParams(self):

        plt.rcParams['axes.labelpad'] = 15.0
        plt.rcParams['axes.labelsize'] = 'large'
        plt.rcParams['axes.labelweight'] = 'heavy'  # light, normal, regular, semibold, demibold, demi, bold, heavy, extra bold, etc.

        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.alpha'] = 0.4
        plt.rcParams['grid.linewidth'] = 0.5
        
        plt.rcParams['figure.dpi'] = 170


        
    def change_style(self, current_style):
        plt.style.use(current_style)
