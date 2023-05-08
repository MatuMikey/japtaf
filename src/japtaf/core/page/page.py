import abc


class Page:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass

    def get_current_url(self) -> str:
        pass
