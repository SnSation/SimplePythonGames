import math

class Display:
    def __init__(self):
        self.name = None
        self.height = 0
        self.width = 0

        self.title = None
        self.subtitle = None

        # Border_Pattern: What Series of Symbols denotes a border
        self.border_pattern = ["#"]

        # Padding: Whitespace Characters between border and content
        self.padding = 0

        # Content holds data to be printed
        # {
        #     Section Name : Section Content (List)
        # }
        self.content = {}

        # Order is the order in which content sections are displayed
        self.order = []

        # Perspectives are a dictionary of other display objects
        # These display objects are used for sub-windows
        # {
        #     Object.name : Object.display
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
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

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

    def set_subtitle(self, subtitle_str):
        self.subtitle = subtitle_str

    def get_subtitle(self):
        return self.subtitle

    def set_content(self, content_dict):
        self.content = content_dict

    def get_content(self):
        return self.content
    
    def set_section(self, section_name, content_list):
        current_content = self.get_content()
        current_content[section_name] = content_list
        self.set_content(current_content)

    def get_section(self, section_name):
        current_content = self.get_content()
        return current_content[section_name]

    def remove_section(self, section_name):
        current_content = self.get_content()
        del current_content[section_name]

    def add_section(self, section_name, section_content):
        current_content = self.get_content()
        current_content[section_name] = section_content
        self.set_content(current_content)

    def add_to_section(self, section_name, text):
        section_content = self.get_section(section_name)
        section_content.append(text)
        self.set_section(section_name, section_content)

    def remove_from_section(self, section_name, text):
        section_content = self.get_section(section_name)
        section_content.remove(text)
        self.set_section(section_name, section_content)

    def set_order(self, section_list):
        self.content_order = section_list

    def get_order(self):
        return self.content_order

    def add_to_order(self, section_name):
        current_order = self.get_order()
        current_order.append(section_name)
        self.set_order(current_order)

    def insert_in_order(self, position, section_name):
        position_index = position - 1
        current_order = self.get_order()
        current_order.insert(position_index, section_name)
        self.set_order(current_order)

    def remove_from_order(self, section_name):
        current_order = self.get_order()
        current_order.remove(section_name)
        self.set_order(current_order)

    def set_perspectives(self, perspectives_dict):
        self.perspectives = perspectives_dict

    def get_perspectives(self):
        return self.perspectives

    def set_perspective(self, name_str, display_obj):
        self.perspectives[name_str] = display_obj

    def get_perspective(self, name_str):
        return self.perspectives[name_str]

    def set_current_perspective(self, name_str):
        self.current_perspective = self.get_perspective(name_str)
        self.set_subtitle(name_str)

    def get_current_perspective(self):
        return self.current_perspective

    def clear_perspective(self):
        self.current_perspective = None

    # Format Methods
    def no_max(self, dimension_str):
        if dimension_str == "height":
            self.set_height(0)
        elif dimension_str == "width":
            self.set_width(0)

    def format_line(self, line_str, max_width):
        formatted_lines = []
        new_line_count = int(math.ceil(len(line_str) / max_width))
        
        current_index = 0
        last_index = max_width

        while len(formatted_lines) < new_line_count:
            if last_index >= len(line_str):
                last_index = len(line_str)
            new_line = line_str[current_index:last_index]
            formatted_lines.append(new_line)
            current_index = last_index
            last_index = last_index + max_width

        return formatted_lines

    def get_horizontal_border(self):
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

    def get_horizontal_padding(self, line_index):
        base_space = self.get_padding()
        border_space = len(self.get_vertical_border(line_index))
        padding_string = " " * (base_space + border_space - 1)

        return padding_string

    def get_vertical_padding(self, line_index):
        line_width = self.get_width()
        border_thickness = len(self.get_vertical_border(line_index))
        padding_thickness = len(self.get_horizontal_padding(line_index))

        space_count = line_width - (border_thickness * 2) - (padding_thickness * 2)

        whitespace = " " * space_count

        return whitespace

    # Data Manipulation Functions
    def update_perspective(self, obj):
        self.set_perspective(obj.get_name(), obj.get_display())
        self.set_current_perspective(obj.get_name())

    # The Actual Print Function
    def show(self):
        max_width = self.get_width()
        max_height =self.get_height()

        horizontal_border = self.get_horizontal_border()
        border_thickness = len(horizontal_border)
        padding = self.get_padding()

        window_line = 0
        vertical_line = 0
        content_line = 0

        content_start = border_thickness + padding
        content_end = max_height - (content_start * 2)
        content_width = max_width - (content_start * 2)
        

        content = self.get_content()
        order = self.get_order()

        formatted_lines = []
        
        if self.get_title() != None:
            formatted_lines.append(self.get_title())
        if self.get_subtitle() != None:
            formatted_lines.append(self.get_subtitle())
        for section in order:
            for line in content[section]:
                formatted_content = formatted_content + self.format_line(line, content_width)

        center = None

        while window_line <= max_height:
            if window_line <= border_thickness:
                print(horizontal_border[window_line])
            elif window_line >= (max_height - border_thickness):
                print(horizontal_border[(max_height - window_line)])
            else:
                left = self.get_vertical_border(vertical_line)
                right = left[::-1]
                line_padding = self.get_horizontal_padding(vertical_line)
                if (window_line < content_start) or (window_line > content_end):
                    center = self.get_vertical_padding(vertical_line)
                else:
                    if content_line >= len(formatted_content):
                        center = self.get_vertical_padding(vertical_line)
                    else:
                        center = formatted_content[content_line]
                        content_line += 1
                print(f'{left}{line_padding}{center}{line_padding}{right}')
                vertical_line += 1
            window_line += 1