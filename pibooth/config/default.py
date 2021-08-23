# -*- coding: utf-8 -*-

"""Pibooth default configuration.
"""

import itertools
from collections import OrderedDict as odict
from pibooth import language


def values_list_repr(values):
    """Concatenate a list of values to a readable string.
    """
    return "'{}' or '{}'".format("', '".join([str(i) for i in values[:-1]]), values[-1])


DEFAULT = odict((
    ("GENERAL",
        odict((
            ("language",
                ("en",
                 "User interface language: {}".format(values_list_repr(language.get_supported_languages())),
                 "UI language", language.get_supported_languages())),
            ("directory",
                ("~/Pictures/pibooth",
                 "Path to save pictures (list of quoted paths accepted)",
                 None, None)),
            ("autostart",
                (False,
                 "Start pibooth at Raspberry Pi startup",
                 "Auto-start", ['True', 'False'])),
            ("debug",
                (False,
                 "In debug mode, exceptions are not caught, logs are more verbose, pictures are cleared at startup",
                 "Debug mode", ['True', 'False'])),
            ("plugins",
                ('',
                 "Path to custom plugin(s) not installed with pip (list of quoted paths accepted)",
                 None, None)),
            ("plugins_disabled",
                ('',
                 "Plugin names to be disabled after startup (list of quoted names accepted)",
                 None, None)),
            ("vkeyboard",
                (False,
                 "Enable a virtual keyboard in the settings interface",
                 "Virtual keyboard", ['True', 'False'])),
        ))
     ),
    ("WINDOW",
        odict((
            ("size",
                ((800, 480),
                 "The (width, height) of the display window or 'fullscreen'",
                 'Startup size', ['(800, 480)', 'fullscreen'])),
            ("background",
                ((0, 0, 0),
                 "Background RGB color or image path",
                 None, None)),
            ("text_color",
                ((255, 255, 255),
                 "Text RGB color",
                 "Text RGB color", (255, 255, 255))),
            ("flash",
                (True,
                 "Blinking background when a capture is taken",
                 "Flash on capture", ['True', 'False'])),
            ("animate",
                (False,
                 "Animate the last taken picture by displaying captures one by one",
                 "Animated picture", ['True', 'False'])),
            ("animate_delay",
                (0.2,
                 "How long is displayed the capture in seconds before switching to the next one",
                 None, None)),
            ("finish_picture_delay",
                (0,
                 "On 'finish' state: how long is displayed the final picture in seconds (0 if never shown)",
                 "Finish picture display time", [str(i) for i in range(0, 121, 5)])),
            ("wait_picture_delay",
                (-1,
                 "On 'wait' state: how long is displayed the final picture in seconds before being hidden (-1 if never hidden)",
                 "Wait picture display time", ['-1'] + [str(i) for i in range(0, 121, 5)])),
            ("chosen_delay",
                (4,
                 "How long is displayed the 'chosen' state:  (0 if never shown)",
                 "Chosen layout display time", [str(i) for i in range(0, 10)])),
            ("arrows",
                ('bottom',
                 "Show arrows to indicate physical buttons: 'bottom', 'top', 'hidden' or 'touchscreen'",
                 "Show button arrows", ['bottom', 'top', 'hidden', 'touchscreen'])),
            ("arrows_x_offset",
                (0,
                 "Apply horizontal offset to arrows position",
                 None, None)),
            ("preview_delay",
                (3,
                 "How long is the preview in seconds",
                 "Preview delay", [str(i) for i in range(1, 21)])),
            ("preview_countdown",
                (True,
                 "Show a countdown timer during the preview",
                 "Preview countdown", ['True', 'False'])),
            ("preview_stop_on_capture",
                (False,
                 "Stop the preview before taking the capture",
                 None, None)),
        ))
     ),
    ("PICTURE",
        odict((
            ("orientation",
                ("auto",
                 "Orientation of the final picture: 'auto', 'portrait' or 'landscape'",
                 "Orientation", ['auto', 'portrait', 'landscape'])),
            ("captures",
                ((4, 1),
                 "Possible choice(s) of captures numbers (numbers between 1 to 4)",
                 "Number of captures", ['1', '2', '3', '4'] + [str(val) for val in itertools.permutations(range(1, 5), 2)])),
            ("captures_effects",
                ("none",
                 "Effect applied to the captures (list of quoted names accepted)",
                 None, None)),
            ("captures_cropping",
                (False,
                 "Crop each capture border in order to fit the paper size",
                 "Crop captures",  ['True', 'False'])),
            ("margin_thick",
                (100,
                 "Thick (in pixels) between captures and picture borders/texts",
                 "Borders width", [str(i) for i in range(0, 210, 10)])),
            ("footer_text1",
                ("Footer 1",
                 "Main text displayed",
                 "Title", "")),
            ("footer_text2",
                ("Footer 2",
                 "Secondary text displayed",
                 "Sub-title", "")),
            ("text_colors",
                ((0, 0, 0),
                 "RGB colors used for footer texts (list of tuples accepted)",
                 None, None)),
            ("text_fonts",
                (('Amatic-Bold', 'AmaticSC-Regular'),
                 "Fonts name or file path used for footer texts (list of quoted names accepted)",
                 None, None)),
            ("text_alignments",
                ('center',
                 "Alignments used for footer texts: 'left', 'center' or 'right' (list of quoted names accepted)",
                 None, None)),
            ("overlays",
                ('',
                 "Overlay path (PNG file) with same aspect ratio than final picture (list of quoted paths accepted)",
                 None, None)),
            ("backgrounds",
                ((255, 255, 255),
                 "Background RGB color or image path (list of tuples or quoted paths accepted)",
                 None, None)),
        ))
     ),
    ("CAMERA",
        odict((
            ("iso",
                (100,
                 "Adjust ISO for lighting issues, can be different for preview and capture (list of integers accepted)",
                 None, None)),
            ("flip",
                (False,
                 "Flip horizontally the capture",
                 None, None)),
            ("rotation",
                (0,
                 "Rotation of the camera: 0, 90, 180 or 270, can be different for preview and capture (list of integers accepted)",
                 None, None)),
            ("resolution",
                ((1934, 2464),
                 "Resolution for camera captures (preview will have same aspect ratio)",
                 None, None)),
            ("delete_internal_memory",
                (False,
                 "Delete captures from camera internal memory (when applicable)",
                 None, None)),
        ))
     ),
    ("PRINTER",
        odict((
            ("printer_name",
                ("default",
                 "Name of the printer defined in CUPS (or use the 'default' one)",
                 None, None)),
            ("printer_options",
                ({},
                 "Print options passed to the printer, shall be a valid Python dictionary",
                 None, None)),
            ("printer_delay",
                (10,
                 "How long is the print view in seconds (0 to skip it)",
                 "Time to show print screen", [str(i) for i in range(0, 21)])),
            ("auto_print",
                (0,
                 "Number of pages automatically sent to the printer (or use 'max' to reach max duplicate)",
                 "Automatically printed pages", [str(i) for i in range(0, 11)] + ['max'])),
            ("max_pages",
                (-1,
                 "Maximum number of printed pages before warning on paper/ink levels (-1 = infinite)",
                 'Maximum of printed pages', [str(i) for i in range(-1, 1000)])),
            ("max_duplicates",
                (3,
                 "Maximum number of duplicate pages sent to the printer (avoid paper waste)",
                 'Maximum of printed duplicates', [str(i) for i in range(0, 10)])),
            ("pictures_per_page",
                (1,
                 "Print 1, 2, 3 or 4 picture copies per page",
                 'Number of copies per page', [str(i) for i in range(1, 5)])),
        ))
     ),
    ("CONTROLS",
        odict((
            ("debounce_delay",
                (0.3,
                 "How long to press a single hardware button in seconds",
                 None, None)),
            ("multi_press_delay",
                (0.5,
                 "How long to press multiple hardware buttons in seconds",
                 None, None)),
            ("picture_btn_pin",
                (11,
                 "Physical GPIO IN pin to take a picture",
                 None, None)),
            ("picture_led_pin",
                (7,
                 "Physical GPIO OUT pin to light a LED when picture button is pressed",
                 None, None)),
            ("print_btn_pin",
                (13,
                 "Physical GPIO IN pin to print a picture",
                 None, None)),
            ("print_led_pin",
                (15,
                 "Physical GPIO OUT pin to light a LED when print button is pressed",
                 None, None)),
        ))
     ),
))
