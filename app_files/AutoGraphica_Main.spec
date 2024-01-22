# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

block_cipher = None

a = Analysis(
    ['AutoGraphica_Main.py'],
    pathex=["C:\\################################################\\AutoGraphica_v8\\exe"],
    binaries=[],
    datas=[('AutoGraphica_Main.kv', '.'), ("app_create_display_page.py", "."), ("app_dialogs.py", "."), ("app_drop_down_menus.py", "."), ("app_facet_page.py", "."), ("app_get_attributes.py", "."), ("app_information.py", "."), ("app_on_marked.py", "."), ("app_screens.py", "."), ("app_topbar.py", "."), ("./root/instantiation_create_chart_instance.py", "root"), ("./root/instantiation_chart_rules.py", "root"), ("./root/instantiation_file_controller.py", "root"), ("./root/support_date_time_operations.py", "root"), ("./root/support_plotting.py", "root"), ("./root/support_facets.py", "root"), ("./root/support_rcParams.py", "root"),("./root/support_main_classes.py", "root"), ("./root/plot_bar_chart.py", "root"), ("./root/plot_box_plot.py", "root"), ("./root/plot_facet_plot.py", "root"), ("./root/plot_histogram.py", "root"), ("./root/plot_line_graph.py", "root"), ("./root/plot_multi_bar_chart.py", "root"), ("./root/plot_multi_line_graph.py", "root"), ("./root/plot_multi_scatter_plot.py", "root"),("./root/plot_pie_chart.py", ".root"), ("./root/plot_scatter_plot.py", "root"),("./images/bar_chart.png", "images"), ("./images/box_plot.png", "images"), ("./images/facet_plot.png", "images"), ("./images/histogram_chart.png", "images"), ("./images/line_chart.png", "images"), ("./images/multi_bar_chart.png", "images"), ("./images/multi_line_graph.png", "images"), ("./images/multi_scatter_plot.png", "images"), ("./images/pie_chart.png", "images"), ("./images/scatter_plot.png", "images"), ("./images/home_page_design.jpg", "images"), ("./images/page_design.png", "images"), ("./libs/garden/garden_matplotlib/backend_kivyagg.py", "garden_matplotlib")],
    hiddenimports=["seaborn"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='AutoGraphica_Main',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    Tree("C:\\################################################\\AutoGraphica_v8\\exe\\"),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AutoGraphica_Main',
)