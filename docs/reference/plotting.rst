Plotting
========


mcoast
------

.. ['CoastPlotting', 'Coastlines', 'GridPlotting', 'LabelPlotting']

This action controls the plotting of coastlines, rivers, cities and country boundaries, as well as the latitude/longitude grid lines.

.. list-table::
   :header-rows: 1
   :widths: 70 20 10

   * - | Name
     - | Type
     - | Default
   * - | **map_coastline_resolution**
       | Select one of the pre-defined resolutions: automatic, low, medium, and high. When set to AUTOMATIC, a resolution appropriate to the scale of the map is chosen in order to balance quality with speed.
     - | 'automatic', 'low', 'medium', 'high'
     - | "automatic"
   * - | **map_coastline_land_shade**
       | Sets if land areas are shaded
     - | bool
     - | False
   * - | **map_coastline_land_shade_colour**
       | Colour of Shading of land areas
     - | Colour(string)
     - | "green"
   * - | **map_coastline_sea_shade**
       | Shade the sea areas
     - | bool
     - | False
   * - | **map_coastline_sea_shade_colour**
       | Colour of Shading of sea areas
     - | Colour(string)
     - | "blue"
   * - | **map_boundaries**
       | Add the political boundaries
     - | NoBoundaries(string)
     - | False
   * - | **map_cities**
       | Add the cities (capitals)
     - | NoCities(string)
     - | False
   * - | **map_preview**
       | OrderedDict([('for_docs', False), ('#text', 'Add a preview : only for metview')])
     - | bool
     - | False
   * - | **map_rivers**
       | Display rivers (on/off)
     - | True, False
     - | False
   * - | **map_rivers_style**
       | Line style for rivers
     - | LineStyle(string)
     - | "solid"
   * - | **map_rivers_colour**
       | Colour of the rivers
     - | Colour(string)
     - | "blue"
   * - | **map_rivers_thickness**
       | Line thickness of rivers
     - | int
     - | 1
   * - | **map_user_layer**
       | Display user shape file layer
     - | True, False
     - | False
   * - | **map_user_layer_name**
       | Path + name of the shape file to use
     - | string
     - | ""
   * - | **map_user_layer_projection**
       | Projection used in the shape file
     - | string
     - | ""
   * - | **map_user_layer_style**
       | Line style for User Layer
     - | LineStyle(string)
     - | "solid"
   * - | **map_user_layer_colour**
       | Colour of the User Layer
     - | Colour(string)
     - | "blue"
   * - | **map_user_layer_thickness**
       | Line thickness of User Layer
     - | int
     - | 1
   * - | **map_coastline_colour**
       | Colour of coastlines
     - | Colour(string)
     - | "black"
   * - | **map_coastline_style**
       | Line style of coastlines
     - | LineStyle(string)
     - | "solid"
   * - | **map_coastline_thickness**
       | Line thickness of coastlines
     - | int
     - | 1
   * - | **map_coastline_general_style**
       | Use a predefined style depending on the general theme
     - | string
     - | ""
   * - | **map_coastline**
       | Plot coastlines on map (ON/OFF)
     - | NoCoastPlotting(string)
     - | True
   * - | **map_grid**
       | Plot grid lines on map (On/OFF)
     - | NoGridPlotting(string)
     - | True
   * - | **map_label**
       | Plot label on map grid lines (On/OFF)
     - | NoLabelPlotting(string)
     - | True
   * - | **map_grid_latitude_reference**
       | Reference Latitude from which all latitude lines are drawn
     - | float
     - | 0
   * - | **map_grid_latitude_increment**
       | Interval between latitude grid lines
     - | float
     - | 10.0
   * - | **map_grid_longitude_reference**
       | Reference Longitude from which all longitude lines are drawn
     - | float
     - | 0
   * - | **map_grid_longitude_increment**
       | Interval between longitude grid lines
     - | float
     - | 20.0
   * - | **map_grid_line_style**
       | Line style of map grid lines
     - | LineStyle(string)
     - | "solid"
   * - | **map_grid_thickness**
       | Thickness of map grid lines
     - | int
     - | 1
   * - | **map_grid_colour**
       | Colour of map grid lines
     - | Colour(string)
     - | "black"
   * - | **map_grid_frame**
       | Add a frame around the projection
     - | bool
     - | False
   * - | **map_grid_frame_line_style**
       | Line style of map grid lines
     - | LineStyle(string)
     - | "solid"
   * - | **map_grid_frame_thickness**
       | Thickness of map grid lines
     - | int
     - | 1
   * - | **map_grid_frame_colour**
       | Colour of map grid lines
     - | Colour(string)
     - | "black"
   * - | **map_label_font**
       | Font of grid labels
     - | string
     - | "sansserif"
   * - | **map_label_font_style**
       | Font of grid labels
     - | string
     - | "normal"
   * - | **map_label_colour**
       | Colour of map labels
     - | Colour(string)
     - | "black"
   * - | **map_label_height**
       | Height og grid labels
     - | float
     - | 0.25
   * - | **map_label_blanking**
       | Blanking of the grid labels
     - | bool
     - | True
   * - | **map_label_latitude_frequency**
       | Evry Nth latitue grid is labelled
     - | int
     - | 1
   * - | **map_label_longitude_frequency**
       | Evry Nth longitude grid is labelled
     - | int
     - | 1
   * - | **map_label_left**
       | Enable the labels on the left of the map
     - | bool
     - | True
   * - | **map_label_right**
       | Enable the labels on the right of the map
     - | bool
     - | True
   * - | **map_label_top**
       | Enable the labels on the top of the map
     - | bool
     - | True
   * - | **map_label_bottom**
       | Enable the labels on the bottom of the map
     - | bool
     - | True


mcont
-----

.. ['Contour', 'Akima474Method', 'Akima760Method', 'AutomaticContourMethod', 'CountSelectionType', 'HighHiLo', 'IntervalSelectionType', 'IsoLabel', 'IsoShading', 'LevelListSelectionType', 'LowHiLo', 'NoIsoPlot', 'ValuePlot']

This action controls the plotting of isolines, contour bands and grid points.

.. list-table::
   :header-rows: 1
   :widths: 70 20 10

   * - | Name
     - | Type
     - | Default
   * - | **legend**
       | Turn legend on or off
     - | bool
     - | False
   * - | **contour**
       | Turn contouring on or off
     - | True, False
     - | True
   * - | **contour_method**
       | Contouring method
     - | 'automatic', 'linear', 'akima474', 'akima760'
     - | "automatic"
   * - | **contour_interpolation_floor**
       | Any value below this floor will be forced to the floor value. avoid the bubbles artificially created by the interpolation method
     - | float
     - | -2147483647
   * - | **contour_interpolation_ceiling**
       | any value above this ceiling will be forced to the ceiling value. avoid the bubbles artificially created by the interpolation method
     - | float
     - | 2147483647
   * - | **contour_automatic_setting**
       | Turn the automatic setting of contouring attributes
     - | False, 'style_name', 'ecmwf'
     - | False
   * - | **contour_style_name**
       | Use of a predeined setting
     - | string
     - | ""
   * - | **contour_metadata_only**
       | Only get the metadata
     - | bool
     - | False
   * - | **contour_hilo**
       | Plot local maxima/minima
     - | True, False
     - | False
   * - | **contour_grid_value_plot**
       | Plot Grid point values
     - | True, False
     - | False
   * - | **contour_akima_x_resolution**
       | X resolution of Akima interpolation.
     - | float
     - | 1.5
   * - | **contour_akima_y_resolution**
       | Y resolution of Akima interpolation.
     - | float
     - | 1.5
   * - | **contour_max_level**
       | Highest level for contours to be drawn
     - | float
     - | 1e+21
   * - | **contour_min_level**
       | Lowest level for contours to be drawn
     - | float
     - | -1e+21
   * - | **contour_shade_max_level**
       | Highest level for contours to be shaded
     - | float
     - | 1e+21
   * - | **contour_shade_min_level**
       | Lowest level for contours to be shaded
     - | float
     - | -1e+21
   * - | **contour_level_count**
       | Count or number of levels to be plotted. Magics will try to find "nice levels", this means that the number of levels could be slightly different from the asked number of levels
     - | int
     - | 10
   * - | **contour_level_tolerance**
       | Tolerance: Do not use nice levels if the number of levels is really to different [count +/- tolerance]
     - | int
     - | 2
   * - | **contour_reference_level**
       | Contour level from which contour interval is calculated
     - | float
     - | 0.0
   * - | **contour_hilo_type**
       | Type of high/low (TEXT/NUMBER/BOTH)
     - | 'text', 'number', 'both'
     - | "text"
   * - | **contour_hilo_window_size**
       | Size of the window used to calculate the Hi/Lo
     - | int
     - | 3
   * - | **contour_hilo_max_value**
       | Local HiLo above specified value are not drawn
     - | float
     - | 1e+21
   * - | **contour_hilo_min_value**
       | Local HiLo below specified value are not drawn
     - | float
     - | -1e+21
   * - | **contour_hi_max_value**
       | Local HI above specified value are not drawn
     - | float
     - | 1e+21
   * - | **contour_hi_min_value**
       | Local HI below specified value are not drawn
     - | float
     - | -1e+21
   * - | **contour_lo_max_value**
       | Local Lo above specified value are not drawn
     - | float
     - | 1e+21
   * - | **contour_lo_min_value**
       | Local Lo below specified value are not drawn
     - | float
     - | -1e+21
   * - | **contour_hilo_marker**
       | Plot hilo marker (ON/OFF)
     - | True, False
     - | False
   * - | **contour_interval**
       | Interval in data units between two contour lines
     - | float
     - | 8.0
   * - | **contour_label_type**
       | Type of label (text/number/both
     - | 'text', 'number', 'both'
     - | "number"
   * - | **contour_label_text**
       | Text for labels
     - | string
     - | ""
   * - | **contour_label_height**
       | Height of contour labels
     - | float
     - | 0.3
   * - | **contour_label_format**
       | Format of contour labels (MAGICS Format/(AUTOMATIC))
     - | string
     - | "(automatic)"
   * - | **contour_label_blanking**
       | Label Blanking
     - | bool
     - | True
   * - | **contour_label_font**
       | Name of the font
     - | string
     - | "sansserif"
   * - | **contour_label_font_style**
       | Style of the font normal/bold/italic
     - | 'normal', 'bold', 'italic'
     - | "normal"
   * - | **contour_label_colour**
       | Colour of contour labels
     - | string
     - | "contour_line_colour"
   * - | **contour_label_frequency**
       | Every Nth contour line is labelled
     - | int
     - | 2
   * - | **contour_shade_technique**
       | Technique used for shading (POLYGON_SHADING/ CELL_SHADING/ MARKER)
     - | 'polygon', 'grid_shading', 'cell_shading', 'marker'
     - | "polygon_shading"
   * - | **contour_shade_colour_method**
       | Method of generating the colours of the bands in contour shading (list/calculate/advanced)
     - | 'calculate', 'list', 'gradients', 'palette'
     - | "calculate"
   * - | **contour_level_list**
       | List of contour levels to be plotted
     - | floatarray
     - | []
   * - | **contour_line_style**
       | Style of contour line
     - | LineStyle(string)
     - | "solid"
   * - | **contour_line_thickness**
       | Thickness of contour line
     - | int
     - | 1
   * - | **contour_line_colour_rainbow**
       | if On, rainbow colouring method will be used.
     - | bool
     - | False
   * - | **contour_line_colour**
       | Colour of contour line
     - | Colour(string)
     - | "blue"
   * - | **contour_line_colour_rainbow_method**
       | Method of generating the colours for isoline
     - | 'calculate', 'list'
     - | "calculate"
   * - | **contour_line_colour_rainbow_max_level_colour**
       | Colour to be used for the max level
     - | Colour(string)
     - | "blue"
   * - | **contour_line_colour_rainbow_min_level_colour**
       | Colour to be used for the mainlevel
     - | Colour(string)
     - | "red"
   * - | **contour_line_colour_rainbow_direction**
       | Direction of colour sequencing for colouring
     - | 'clockwise', 'anti_clockwise'
     - | "anti_clockwise"
   * - | **contour_line_colour_rainbow_colour_list**
       | List of colours to be used in rainbow isolines
     - | stringarray
     - | []
   * - | **contour_line_colour_rainbow_colour_list_policy**
       | What to do if the list of colours is smaller that the list of contour: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **contour_line_thickness_rainbow_list**
       | List of thickness to used when rainbow method is on
     - | intarray
     - | []
   * - | **contour_line_thickness_rainbow_list_policy**
       | What to do if the list of thickness is smaller that the list of contour: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **contour_line_style_rainbow_list**
       | List of line style to used when rainbow method is on
     - | stringarray
     - | []
   * - | **contour_line_style_rainbow_list_policy**
       | What to do if the list of line styles is smaller that the list of contour: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **contour_highlight**
       | Plot contour highlights (ON/OFF)
     - | True, False
     - | True
   * - | **contour_level_selection_type**
       | count: calculate a reasonable contour interval taking into account the min/max and the requested number of isolines. interval: regularly spaced intervals using the reference_level as base. level_list: uses the given list of levels.
     - | 'count', 'interval', 'list'
     - | "count"
   * - | **contour_label**
       | Plot labels on contour lines
     - | True, False
     - | True
   * - | **contour_shade**
       | Turn shading on
     - | True, False
     - | False
   * - | **contour_legend_only**
       | Inform the contour object do generate only the legend and not the plot!
     - | bool
     - | False
   * - | **contour_grid_value_type**
       | For Gaussian fields, plot normal (regular) values or reduced grid values. (NORMAL/REDUCED/akima). If akima, the akima grid values will be plotted
     - | 'normal', 'reduced', 'akima'
     - | "normal"
   * - | **contour_grid_value_plot_type**
       | (VALUE/MARKER/BOTH)
     - | 'value', 'marker', 'both'
     - | "value"


msymb
-----

.. ['SymbolAdvancedTableMode', 'SymbolIndividualMode', 'SymbolPlotting', 'SymbolTableMode']



.. list-table::
   :header-rows: 1
   :widths: 70 20 10

   * - | Name
     - | Type
     - | Default
   * - | **symbol_advanced_table_selection_type**
       | Technique to use to calculate the shading band levels.
     - | 'count', 'interval', 'list'
     - | "count"
   * - | **symbol_advanced_table_min_value**
       | Min value to plot
     - | float
     - | -1e+21
   * - | **symbol_advanced_table_max_value**
       | Max value to plot
     - | float
     - | 1e+21
   * - | **symbol_advanced_table_level_count**
       | Count or number of levels to be plotted. Magics will try to find "nice levels", this means that the number of levels could be slightly different from the requested number of levels
     - | int
     - | 10
   * - | **symbol_advanced_table_level_tolerance**
       | Tolerance: Do not use "nice levels" if the number of levels is really to different [count +/- tolerance]
     - | int
     - | 2
   * - | **symbol_advanced_table_interval**
       | Interval in data units between different bands of shading
     - | float
     - | 8.0
   * - | **symbol_advanced_table_reference_level**
       | Level from which the level interval is calculated
     - | float
     - | 0.0
   * - | **symbol_advanced_table_level_list**
       | List of shading band levels to be plotted
     - | floatarray
     - | []
   * - | **symbol_advanced_table_colour_method**
       | Method of generating the colours of the bands in polygon shading
     - | ColourTechnique(string)
     - | "calculate"
   * - | **symbol_advanced_table_max_level_colour**
       | Highest shading band colour
     - | Colour(string)
     - | "blue"
   * - | **symbol_advanced_table_min_level_colour**
       | Lowest shading band colour
     - | Colour(string)
     - | "red"
   * - | **symbol_advanced_table_colour_direction**
       | Direction of colour sequencing for plotting (CLOCKWISE/ ANTI_CLOCKWISE)
     - | 'clockwise', 'anti-clockwise'
     - | "anti_clockwise"
   * - | **symbol_advanced_table_colour_list**
       | List of colours to be used in symbol plotting
     - | stringarray
     - | []
   * - | **symbol_advanced_table_colour_list_policy**
       | What to do if the list of colours is smaller than the list of intervals: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **symbol_advanced_table_marker_list**
       | List of markers to be used in symbol plotting
     - | intarray
     - | []
   * - | **symbol_advanced_table_marker_name_list**
       | List of markers to be used in symbol plotting symbol
     - | stringarray
     - | []
   * - | **symbol_advanced_table_marker_list_policy**
       | What to do if the list of markers is smaller than the list of intervals: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **symbol_advanced_table_height_method**
       | Method of generating the height
     - | HeightTechnique(string)
     - | "list"
   * - | **symbol_advanced_table_height_max_value**
       | Maximum height to use
     - | float
     - | 0.2
   * - | **symbol_advanced_table_height_min_value**
       | Mininimum height to use
     - | float
     - | 0.1
   * - | **symbol_advanced_table_height_list**
       | List of heights to be used
     - | floatarray
     - | []
   * - | **symbol_advanced_table_height_list_policy**
       | What to do if the list of heights is smaller than the list of intervals: lastone/cycle
     - | ListPolicy(string)
     - | "lastone"
   * - | **symbol_advanced_table_text_list**
       | Text to display
     - | stringarray
     - | []
   * - | **symbol_advanced_table_text_list_policy**
       | What to do if the list of text is smaller that the list of intervals lastone: reuse the last one, cycle: return to the fisrt one
     - | ListPolicy(string)
     - | "cycle"
   * - | **symbol_advanced_table_text_font**
       | Font to use for text plotting.
     - | string
     - | "sansserif"
   * - | **symbol_advanced_table_text_font_size**
       | Font size
     - | float
     - | 0.25
   * - | **symbol_advanced_table_text_font_style**
       | Font Style
     - | string
     - | "normal"
   * - | **symbol_advanced_table_text_font_colour**
       | Symbol Colour
     - | Colour(string)
     - | "automatic"
   * - | **symbol_advanced_table_text_display_type**
       | How to display text none:do not display it centre : display it instead of the symbol, right : attached it to the right of the symbol, top : attached it to the top of the symbol, bottom: attached it to the bottom of the symbol,
     - | 'centre', 'none', 'right', 'left', 'top', 'bottom'
     - | "none"
   * - | **symbol_advanced_table_outlayer_method**
       | outlayer method
     - | NoOutLayerTechnique(string)
     - | "none"
   * - | **symbol_advanced_table_outlayer_min_value**
       | outlayer min value
     - | float
     - | -1e+21
   * - | **symbol_advanced_table_outlayer_max_value**
       | outlayer max value
     - | float
     - | 1e+21
   * - | **legend_user_text**
       | if set, the text to be shown for the symbol group in the legend
     - | string
     - | ""
   * - | **symbol_colour**
       | Colour of symbols.
     - | Colour(string)
     - | "blue"
   * - | **symbol_height**
       | Height of symbols.
     - | float
     - | 0.2
   * - | **symbol_marker_mode**
       | Method to select a marker : by name, by index, by image : in that case, Magics will use an external image as marker.
     - | string
     - | "index"
   * - | **symbol_marker_index**
       | Marker indice: An integer between 1 and 28
     - | int
     - | 1
   * - | **symbol_marker_name**
       | Symbol name. Choose in a list of available markers dot/circle/ww_00 ...
     - | string
     - | "dot"
   * - | **symbol_image_path**
       | Path to the image
     - | string
     - | ""
   * - | **symbol_image_format**
       | Format of the image file. If set to AUTOMATIC, the file extension will be used to determine the file type.
     - | 'automatic', 'png', 'svg'
     - | "automatic"
   * - | **symbol_image_width**
       | width of the image
     - | float
     - | -1.0
   * - | **symbol_image_height**
       | height of the image
     - | float
     - | -1.0
   * - | **symbol_text_list**
       | list of texts to plot
     - | stringarray
     - | []
   * - | **symbol_text_position**
       | Position of the text
     - | 'right', 'left', 'bottom', 'top'
     - | "right"
   * - | **symbol_text_font**
       | Font to use
     - | string
     - | "sansserif"
   * - | **symbol_text_font_size**
       | Font size
     - | float
     - | 0.25
   * - | **symbol_text_font_style**
       | Font style
     - | string
     - | "normal"
   * - | **symbol_text_font_colour**
       | Font colour.
     - | Colour(string)
     - | "automatic"
   * - | **symbol_legend_height**
       | If set, the height will be used to plot the symbols in the legend
     - | float
     - | -1.0
   * - | **legend**
       | Turn legend on or off (ON/OFF) : New Parameter!
     - | bool
     - | False
   * - | **symbol_scaling_method**
       | Turn legend on or off (ON/OFF) : New Parameter!
     - | bool
     - | False
   * - | **symbol_scaling_level_0_height**
       | Turn legend on or off (ON/OFF) : New Parameter!
     - | float
     - | 0.1
   * - | **symbol_scaling_factor**
       | Turn legend on or off (ON/OFF) : New Parameter!
     - | float
     - | 4.0
   * - | **symbol_type**
       | Defines the type of symbol plotting required
     - | 'number', 'text', 'marker', 'wind'
     - | "number"
   * - | **symbol_table_mode**
       | Specifies if plotting is to be in advanced, table (on) or individual mode (off). Note: The simple table mode is not recommended anymore, try to use the advanced mode instead, this should give you easier control of the plot.
     - | SymbolMode(string)
     - | "OFF"
   * - | **symbol_format**
       | Format used to plot values (MAGICS Format/(AUTOMATIC))
     - | string
     - | "(automatic)"
   * - | **symbol_text_blanking**
       | blanking of the text
     - | bool
     - | False
   * - | **symbol_outline**
       | Add an outline to each symbol
     - | bool
     - | False
   * - | **symbol_outline_colour**
       | Colour of the outline
     - | Colour(string)
     - | "black"
   * - | **symbol_outline_thickness**
       | thickness of the outline
     - | int
     - | 1
   * - | **symbol_outline_style**
       | Line Style of outline
     - | LineStyle(string)
     - | "solid"
   * - | **symbol_connect_line**
       | Connect all the symbols with a line
     - | bool
     - | False
   * - | **symbol_connect_automatic_line_colour**
       | if on, will use the colour of the symbol
     - | bool
     - | True
   * - | **symbol_connect_line_colour**
       | Colour of the connecting line
     - | Colour(string)
     - | "black"
   * - | **symbol_connect_line_thickness**
       | thickness of the connecting line
     - | int
     - | 1
   * - | **symbol_connect_line_style**
       | Line Style of connecting line
     - | LineStyle(string)
     - | "solid"
   * - | **symbol_legend_only**
       | Inform the contour object do generate only the legend and not the plot .. [Web sdpecific]
     - | bool
     - | False
   * - | **symbol_min_table**
       | Table of minimum values. The table is used in conjunction with SYMBOL_MAX_TABLE
     - | floatarray
     - | []
   * - | **symbol_max_table**
       | Table of maximum values. The table is used in conjunction with SYMBOL_MIN_TABLE
     - | floatarray
     - | []
   * - | **symbol_marker_table**
       | Table of MARKER indices. The table is to be used in conjunction with SYMBOL_MIN_TABLE and SYMBOL_MAX_TABLE
     - | intarray
     - | []
   * - | **symbol_name_table**
       | Table of Symbol names. The table is to be used in conjunction with SYMBOL_MIN_TABLE and SYMBOL_MAX_TABLE
     - | stringarray
     - | []
   * - | **symbol_colour_table**
       | Table of SYMBOL colours. T The table is to be used in conjunction with SYMBOL_MIN_TABLE and SYMBOL_MAX_TABLE
     - | stringarray
     - | []
   * - | **symbol_height_table**
       | Table of SYMBOL heights. The table is to be used in conjunction with SYMBOL_MIN_TABLE and SYMBOL_MAX_TABLE
     - | floatarray
     - | []

