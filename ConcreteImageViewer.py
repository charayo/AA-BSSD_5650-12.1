from PIL import Image

from IImageViewer import IImageViewer


class ConcreteImageViewer(IImageViewer):
    # The actual real object that the proxy is representing

    def __init__(self, file_name):
        # hypothetically enormous amounts of data
        self.image = Image.open(file_name)

    def display_image(self):
        return self.image
