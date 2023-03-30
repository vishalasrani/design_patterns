class WrittenText:

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class Wrapper():
    def __init__(self, wrapper):
        self.wrapper = wrapper


class UnderlineWrapper(Wrapper):

    """Wraps a tag in <u>"""

    def __init__(self, wrapper):
        super().__init__(wrapper)

    def render(self):
        return "<u>{}</u>".format(self.wrapper.render())


class ItalicWrapper(Wrapper):

    """Wraps a tag in <i>"""

    def render(self):
        return "<i>{}</i>".format(self.wrapper.render())


class BoldWrapper(Wrapper):

    """Wraps a tag in <b>"""

    def render(self):
        return "<b>{}</b>".format(self.wrapper.render())


if __name__ == '__main__':

    before_gfg = WrittenText("GeeksforGeeks")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print("before :", before_gfg.render())
    print("after :", after_gfg.render())
