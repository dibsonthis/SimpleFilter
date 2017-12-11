# Example

![Alt text](https://github.com/dibsonthis/SimpleFilter/blob/master/test.PNG "test.py")

![H_Fig1](https://github.com/dibsonthis/SimpleFilter/blob/master/H_Fig1.png "H_Fig1")

![H_Fig2](https://github.com/dibsonthis/SimpleFilter/blob/master/H_Fig2.png "H_Fig2")

![H_Fig3](https://github.com/dibsonthis/SimpleFilter/blob/master/H_Fig3.png "H_Fig3")

![V_Fig1](https://github.com/dibsonthis/SimpleFilter/blob/master/V_Fig1.png "V_Fig1")

![V_Fig2](https://github.com/dibsonthis/SimpleFilter/blob/master/V_Fig2.png "V_Fig2")

![V_Fig3](https://github.com/dibsonthis/SimpleFilter/blob/master/V_Fig3.png "V_Fig3")

# Dependencies

* matplotlib (pip install matplotlib)
* PIL (pip install Pillow)
* requests (pip install requests)

<h1> How to use SimpleFilter: </h1>

	Every function is listed below with a description of its parameters, however here's a quick demonstration:

	from SimpleFilter import *

	sf = SimpleFilter()

	image = sf.load(path/to/image,[200,200]) # This loads an image at size 200x200 px
	image2 = sf.load(path/to/image,[200,200])

	conv = sf.cycle(image, simple_filters, 4) # This convolutes the image 4 times for each filter in simple_filters (simple_filters consists of four filters; horizontal line, vertical line, right diagonal line, left diagonal line) and plots all the images once complete
	conv2 = sf.cycle(image2, simple_filters, 4)

	flat = sf.flat(conv) # Thus flattens the images into a single list
	flat2 = sf.flat(conv2)

	result = sf.euc(flat1,flat2) # This performs an Euclidean distance calculation on the flattened convolutions to determine how close they are to one another, the smaller the number the closer they are and the higher chance that they are similar



SimpleFilter v.1.0 Documentation

SimpleFilter is a module that provides the tools necessary to build a convolutional classification network. It handles the convolutions or mutation of images and comes pre-packaged with SimpleClassifier, a k-nearest neighbor classifier that is optimized to work with the module

SimpleFilter.create(size, outer=-0.1, inner=1, rand=0)
	Creates a size x size array, mainly used to create basic filters which can then be styled using the SimpleFilter.style function
-	Size: Size of the filter [size x size]
-	Outer: Integer of all except the middle cell
-	Inner: Integer of middle cell
-	Rand: Accepts list of integers to randomize cells

SimpleFilter.load(fpath, size=None, filter=False, convert=’L’)
	Loads an image of any type using the PIL module and transforms it into an array that the SimpleFilter class can work with. Can also load images to be used as filters. Resizing images on load time will increase efficiency and speed of convolutions
-	Fpath: Image file path
-	Size: Accepts a list of width and height [w,h]. None loads image in actual size
-	Filter: When True replaces all cells of value 255 with 1 and all cells of value 0 with -1
-	Convert: Accepts PIL conversion type. ‘1’ loads image in black (255) and white (0)

SimpleFilter.randomize(filter, rand=[-0.1,1])
	Randomizes a filter using a list of integers. Rand lists are not limited to two numbers, however convolution with filters that have varying numbers may yield odd results
-	Filter: Filter to be randomized
-	Rand: Accepts list of integers to randomize cells

SimpleFilter.prep(array, filter, pad=0)
	Prepares an image to be convoluted or mutated by padding all four sides of the array with any number provided. The padding is calculated based on each filter and thus larger filters will create a large amount of padding which will increase computation time
-	Array: Image array to be padded
-	Filter: Padding is created relative to the filter size
-	Pad: Integer that the padding is made of

SimpleFilter.unprep(array,filter)
	Removes the padding from an image that has been fed through the SimpleFilter.prep function. Always make sure to unprep an image using the same filter that was used to prep it, otherwise the unprep function could distort or crop the image unintentionally
-	Array: Image array to be unpadded
-	Filter: Padding is removed relative to the filter size

SimpleFilter.conv(array, filter)
	Runs a single convolution on an image using a provided filter. This function is used as the basis of the mutations performed in the SimpleFilter.mut function
-	Array: Image array to be convoluted
-	Filter: Filter to be used for convolution

SimpleFilter.pool(array)
	Performs a max pooling function of size=2 and stride=2 on an image reducing it to half its original size
-	Array: Array to be pooled

SimpleFilter.rectlin(array)
	Performs a rectilinear function on each cell in the image, changing all negative numbers into 0 whilst keeping any other number unchanged
-	Array: Array for which a rectilinear layer will be applied

SimpleFilter.mut(array, filter, levels=1, plot=False, plotall=False, col=’Greys_r’, rand=[-0.1,1], r=False, pool=False, rectlin=False)
	Mut stands for mutation and is a SimpleFilter vernacular for multilayered convolution. It uses the SimpleFilter.conv function to perform multiple convolutions or mutation on an image using a single provided filter
-	Array: Array to be mutated
-	Filter: Filter to be used for mutation
-	Levels: Levels of mutation
-	Plot: If True, plots final mutation
-	Plotall: If True, plots all mutations
-	Col: Accepts matplotlib.pyplot.matshow color map
-	R: If True, randomizes filter before every convolution
-	Rand: Accepts list of integers to randomize filter when r is True
-	Pool: Applies a pooling layer after every convolution
-	Rectlin: Applies a Rectilinear layer after every convolution

SimpleFilter.cycle(array, filters, levels=1, pool=True, rectlin=True, col='Greys_r', plot=False, plotall=True, flat=False)
	Cycles through a list of provided filters and performs multiple convolutions on or mutates an image using each filter and returns a list of arrays (images)
-	Array: Array to be cycled
-	Filters: Accepts a list of filters to cycle through
-	Levels: Number of mutations per filter
-	Pool: If True, applies a pooling layer after each convolution
-	Rectlin: If True, applies a rectilinear layer after each convolution
-	Col: Accepts matplotlib.pyplot.matshow color map
-	Plot: If True, plots final mutation
-	Plotall: If True, plots all mutations
-	Flat: If True, returns a flattened list that can be used in the SimpleFilter.euc function

SimpleFilter.style(filter, front=1, back=-0.1, x=None, y=None, s=None, n= False)
	Allows basic styling of a created filter or array. Mainly used to create basic filters such as horizontal lines, vertical lines and diagonal lines. A filter can go through the style function numerous times and if n is False, will append each style to the existing styled filter
-	Filter: Filter to be styled
-	Front: Integer to be applied to the styled areas
-	Back: Integer to be applied to the non-styled areas
-	X: Accepts a list containing the start and end indexes of the area to be filled in the Y direction [0,4] or [4, len(Filter)]
-	Y: Accepts a list containing the start and end indexes of the area to be filled in the X direction [0,4] or [4, len(Filter)]
-	S: Special function, allows the creation of diagonal filters using the keywords ‘rl’ for right to left diagonal or ‘lr’ for left to right diagonal
-	N: If True, replaces all the cells in the filter with the back variable before styling to ensure a blank slate

SimpleFilter.flat(conv_layers):
	Flattens a list of images into a single list of features to be used in the SimpleFilter.euc function
-	Conv_layers: A list of images (arrays) returned by the SimpleFilter.cycle function
SimpleFilter.euc(a, b)
	Performs Euclidean distance calculation on two flattened arrays (lists) to determine the degree of closeness
-	A: List 1
-	B: List 2

SimpleClassifier documentation
	The SimpleClassifier is a k-nearest neighbor classifier that comes pre-packaged in the SimpleFilter module – It is optimized to be used with the SimpleFilter mutations, however any classifier of choice can be used instead with some modification

SimpleClassifier.fit(train_features, train_labels)
	Captures the training features and their corresponding labels
-	Train_features: The training data set
-	Train_Labels: The training labels

SimpleClassifier.predict(test)
	Performs a prediction using the SimpleFilter.euc function to determine which label closest fits the test image
-	Test: Image to perform the prediction test on

simple_filters: A list of four 3x3 kernels or filters (horizontal line, vertical line, right diagonal, left diagonal). To be used with sf.cycle()

simple_filters5x5: A list of four 5x5 kernels or filters (horizontal line, vertical line, right diagonal, left diagonal). To be used with sf.cycle()