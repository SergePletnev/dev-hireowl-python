from framework.elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def input_text(self, txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
