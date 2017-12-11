


    from SimpleFilter import *

    sf = SimpleFilter()

    image_1 = sf.load('https://www.bluecross.org.uk/sites/default/files/assets/images/124044lpr.jpg',[200,200])
    image_2 = sf.load('https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg',[200,200])

    conv_1 = sf.cycle(image_1,simple_filters,flat=True)
    conv_2 = sf.cycle(image_2,simple_filters,flat=True)

    result = sf.euc(conv_1,conv_2)

    print(result)

    # Output >>> 10336.188050888552

    image = sf.load('https://uproxx.files.wordpress.com/2014/11/wlgrumpycat.jpg?quality=100&w=650',[200,200])

    sf.cycle(image,simple_filters5x5[0:2],3,plotall=True) # This will only use the first two filters in simple_filters

    # Output below
