"""
Class for reading and writing image to a certain location using np arrays.
"""
import numpy as np
import cv2 as cv

class ImageIO:
    """
    Class to read and write the image to a certain location.
    """
    pt: str
    
    def __init__(self, pat: str) -> None:
        """
        Initialize the reader under the certain folder.
        """
        self.pt = pat

    def read_image(self, name: str) -> np.ndarray:
        """
        Read the specific image under the folder.

        Parameters
        --------------
        name: str
            The name of the image to be read under the folder.
        """
        pat = self.pt + "\\" + name
        return cv.imread(pat)
    
    def update_dir(self, pat: str) -> None:
        """
        Update the path of the folder that this reader is initialized.
        """
        self.pt = pat


if __name__ == "__main__":
    reader = ImageIO("reference_images")
    print(reader.read_image("street_image.jpeg"))