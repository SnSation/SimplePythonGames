import math

class Display:
    def __init__(self, name):
        self.name = name
        self.height = 0
        self.width = 0

        self.title = ""
        self.subtitle = ""

        # Border_Pattern: What Series of Symbols denotes a border
        self.border_pattern = ["#"]

        # Padding: Whitespace Characters between border and content
        self.padding = 0

        # Lines hold the content to be printed
        self.content = []

        # Perspectives are a dictionary of other display objects
        # These display objects are used for sub-windows
        # {
        #     Name : Display Object
        # }
        self.perspectives = {}

        # The Current Perspective in its formatted state
        # {
        #     Perspective Name : Formatted Lines
        # }
        self.current_perspective = None

    def __repr__(self):
        return f'< Display | Name: {self.name} >'

    # Getters and Setters
    def set_name(self, name_str):
        self.name = name_str

    def get_name(self):
        return self.name

    def set_height(self, height_int):
        self.height = height_int
    
    def get_height(self):
        return self.height

    def set_width(self, width_int):
        self.width = width_int

    def get_width(self):
        return self.width

    def set_border_pattern(self, pattern_list):
        self.border_pattern = pattern_list

    def get_border_pattern(self):
        return self.border_pattern

    def set_padding(self, padding_int):
        self.padding = padding_int

    def get_padding(self):
        return self.padding

    def set_title(self, title_string):
        self.title = title_string

    def get_title(self):
        return self.title

    def set_subtitle(self, subtitle_string):
        self.subtitle = subtitle_string

    def get_subtitle(self):
        return self.subtitle

    def set_content(self, content_list):
        self.content = content_list

    def get_content(self):
        return self.content

    def set_perspectives(self, perspectives_dict):
        self.perspectives = perspectives_dict

    def get_perspectives(self):
        return self.perspectives

    def set_perspective(self, name_str, display_obj):
        self.perspectives[name_str] = display_obj

    def get_perspective(self, name_str):
        return self.perspectives[name_str]

    def set_current_perspective(self, name_str):
        self.current_perspective = {
            name_str:self.format_perspective(name_str)
        }

    def get_current_perspective(self):
        return self.current_perspective

    # Format Methods
    def no_max(self, dimension_str):
        if dimension_str == "height":
            self.set_height(0)
        elif dimension_str == "width":
            self.set_width(0)

    def create_horizontal_border(self):
        horizontal_border = []
        border_pattern = self.get_border_pattern()
        max_width = self.get_width()

        # Get Border Thickness
        thickness = 0
        for string in border_pattern:
            if len(string) > thickness:
                thickness = len(string)

        # Create a row for each line of thickness
        current_row = 0
        while current_row < thickness:
            this_row = []
            current_column = 0
            border_index = 0
            while current_column < max_width:
                if border_index == len(border_pattern):
                    border_index = 0
                if current_row >= len(border_pattern[border_index]):
                    this_row.append(" ")
                else:
                    this_row.append(border_pattern[border_index][current_row])
                border_index += 1
                current_column += 1
            horizontal_border.append("".join(this_row))
            current_row += 1

        return horizontal_border

    def get_vertical_border(self, line_index):
        border_pattern =self.get_border_pattern()

        border_index = line_index
        if border_index >= (len(border_pattern) - 1):
            border_index = (border_index + 1) % len(border_pattern)
        
        vertical_border = border_pattern[border_index]
        

        return vertical_border

    def get_horizontal_padding(self):
        padding_string = " " * self.get_padding()
        return padding_string

    def get_vertical_padding(self, line_index):
        max_width = self.get_width()
        border_thickness = len(self.get_vertical_border(line_index))
        padding_thickness = len(self.get_horizontal_padding())

        space_count = self.get_width() - (border_thickness * 2) - (padding_thickness * 2)

        whitespace = " " * space_count

        return whitespace

    def format_perspective(self, perspective_name):
        this_perspective = self.get_perspective(perspective_name)
        formatted_content = []
        max_width = self.get_width()
        padding = self.get_padding()
        max_characters = max_width - (padding * 2)

        current_line = 0
        

        current_index = 0
        last_index = current_index + max_characters
        splitting = True

        while splitting:
            # If the last line does not meet the max width, set the last index to last character of the line
            # and stop the loop
            if last_index >= len(text):
                last_index = len(text)
                splitting = False

            # Break the line in to lines the size of the max width
            new_line = text[current_index:last_index]

            # Add the new line to the lines we will display
            formatted_lines.append(new_line)

            # Update the indices from which to create new lines
            current_index = last_index + 1
            last_index = current_index + max_characters


        return formatted_lines

    # Data Manipulation Functions
    def update_perspective(self, name, display_object):
        self.perspectives[name] = display_object

    def update_display(self):
        pass
    
    # Getting Display Data
    def get_display(self):
        pass

    # The Actual Print Function
    def show(self):
        current_line = 0
        window_dimensions = [self.get_width(), self.get_height()]
        content_start = self.get_padding() + 1
        content_end = self.get_height() - self.get_padding() - 1

        while current_line <= self.get_height():
            current_line += 1
            if (current_line == 1) or (current_line == self.get_height()):
                print(self.get_horizontal_border())
            else:
                vertical_borders = self.get_vertical_border(current_line)
            elif (current_line < content_start) or (current_line > content_end):
                print("\n")
