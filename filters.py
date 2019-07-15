from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im


def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)

# def obamicon(im):
#   # Load the pixel data from im.
#   pixels = im.getdata()
#   # Create a list to hold the new image pixel data.
#   new_pixels = []
#
#   # Define color constants to use for recoloring.
#   darkBlue = (0, 51, 76)
#   red = (217, 26, 33)
#   lightBlue = (112, 150, 158)
#   yellow = (252, 227, 166)
#
#   # Process the pixels in the image.
#   for p in pixels:
#     # Pixel intensity = R value + G value + B value
#     intensity = p[0] + p[1] + p[2]
#
#     if intensity < 182:
#       new_pixels.append(darkBlue)
#
#     elif intensity >= 182 and intensity < 364:
#       new_pixels.append(red)
#
#     elif intensity >= 364 and intensity < 546:
#       new_pixels.append(lightBlue)
#
#     elif intensity >=546:
#       new_pixels.append(yellow)
#
#   # Save the filtered pixels as a new image
#   newim = Image.new("RGB", im.size)
#   newim.putdata(new_pixels)
#   return newim
#
#   def fun(im):
#     # Load the pixel data from im.
#     pixels = im.getdata()
#     # Create a list to hold the new image pixel data.
#     new_pixels = []
#
#     # Define color constants to use for recoloring.
#     lightBlue = (204,255,255)
#     yellow = (252, 227, 166)
#     aqua = (0, 255, 255)
#     pink = (255,182,193)
#
#
#
#     # Process the pixels  in the image.
#     for p in pixels:
#       # Pixel intensity = R value + G value + B value
#       intensity = p[0] + p[1] + p[2]
#
#       if intensity < 50:
#         new_pixels.append(lightBlue)
#
#       elif intensity >= 50 and intensity < 300:
#         new_pixels.append(pink)
#
#       elif intensity >= 300 and intensity < 500:
#         new_pixels.append(aqua)
#
#       elif intensity >= 500:
#         new_pixels.append(yellow)
#
#     # Save the filtered pixels as a new image
#     newim = Image.new("RGB", im.size)
#     newim.putdata(new_pixels)
#     return newim

    def black_white(im):
      # Load the pixel data from im.
      pixels = im.getdata()
      # Create a list to hold the new image pixel data.
      new_pixels = []

      # Define color constants to use for recoloring.
      grey1 = (224,224,224)
      grey2 = (192,192,192)
      grey3 = (160,160,160)
      grey4 = (130,130,130)

      # Process the pixels in the image.
      for p in pixels:
        # Pixel intensity = R value + G value + B value
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
          new_pixels.append(grey1)

        elif intensity >= 182 and intensity < 364:
          new_pixels.append(grey2)

        elif intensity >= 364 and intensity < 546:
          new_pixels.append(grey3)

        elif intensity >=546:
          new_pixels.append(grey4)

      # Save the filtered pixels as a new image
      newim = Image.new("RGB", im.size)
      newim.putdata(new_pixels)
      return newim
