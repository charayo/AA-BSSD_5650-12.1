from abc import ABCMeta, abstractmethod


class IImageViewer(metaclass=ABCMeta):
    # An interface implemented by both the Proxy and Real Subject

    @staticmethod
    @abstractmethod
    def display_image():
        raise NotImplementedError
