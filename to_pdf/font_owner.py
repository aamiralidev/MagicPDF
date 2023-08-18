import abc

from fonts.font import Font


class FontOwner(abc.ABC):
    def __init__(self, font=None):
        self.font = font if font is not None else Font()

    @abc.abstractmethod
    def update_font(self):
        pass

    def set_font_family(self, family):
        self.font.family = family
        self.update_font()

    def set_font_size(self, size):
        self.font.size = size
        self.update_font()

    def set_font_style(self, style):
        self.font.style = style
        self.update_font()
