
import filters

def main():

    filename = input ("Enter the name of the image file to edit ==> ")

    img = filters.load_img(filename)

    # newimg = filters.obamicon(img)
    #
    # newimg = filters.fun(img)
    
    newimg = filters.black_white(img)

    filters.save_img(newimg, "recolored.jpg")

if __name__== '__main__':
    main()
