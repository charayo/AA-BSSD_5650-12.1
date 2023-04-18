"""
A Proxy Concept Example
https://sbcode.net/python/proxy/#proxyproxy_conceptpy
"""
from ConcreteImageViewer import ConcreteImageViewer
from IImageViewer import IImageViewer


class Proxy(IImageViewer):
    """
    The proxy. In this case the proxy will act as a cache for
    `enormous_data` and only populate the enormous_data when it
    is actually necessary
    """

    def __init__(self, file_name):
        self.image = None
        self.real_subject = ConcreteImageViewer(file_name)

    def display_image(self):
        """
        Using the proxy as a cache, and loading data into it only if
        it is needed
        """
        if self.image is None:
            print("pulling data from RealSubject")
            self.image = self.real_subject.display_image()
            print(self.image.format)
            print(self.image.size)
            self.image.show()
        else:
            print("pulling data from Proxy cache")
            self.image.show()

# end class Proxy(IImageViewer):


if __name__ == "__main__":
    images = ["img.png", "yellow_balloons.jpeg"]
    for image in images:
        image_viewer = Proxy(image)

        print(id(image_viewer))

        image_viewer.display_image()
        # image loaded from cache, but also no new real would be made
        image_viewer.display_image()
