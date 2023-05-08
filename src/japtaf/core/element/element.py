import abc
from selenium.webdriver.remote.webelement import WebElement


class Element:
    """Base class for all element subtypes"""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def click(self):
        pass

    @abc.abstractmethod
    def type(self, text: str = ""):
        pass
