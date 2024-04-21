import random

class ImageSelector:
    def __init__(self):
        self.images = ["image1.png", "image2.png", "image3.png", "image4.png"]
    
    def choose_image(self):
        return random.choice(self.images)
    

# Use for main file

image_selector = ImageSelector()
random_image = image_selector.choose_image()

