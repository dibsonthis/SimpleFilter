<img src="https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/logo.png" width="700" height="150" align="middle">

#

# SimpleFilter v.1.3 Documentation

SimpleFilter is a <b>Python 3 module</b> that provides the tools necessary to build a convolutional classification network. It handles the convolutions or mutation of images and comes pre-packaged with SimpleClassifier, a k-nearest neighbor classifier that is optimized to work with the module

# Installation

	pip install SimpleFilter

# Example

![Alt text](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/test.PNG "test.py")

![H_Fig1](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/H_Fig1.png "H_Fig1")

![H_Fig2](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/H_Fig2.png "H_Fig2")

![H_Fig3](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/H_Fig3.png "H_Fig3")

![V_Fig1](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/V_Fig1.png "V_Fig1")

![V_Fig2](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/V_Fig2.png "V_Fig2")

![V_Fig3](https://github.com/dibsonthis/SimpleFilter/blob/master/SimpleFilter/Images/V_Fig3.png "V_Fig3")

# Dependencies

Installing through pip will also install all dependencies, however if for some reason they do not come through, you can install them manually as per below:

## matplotlib
	pip install matplotlib
## PIL
	pip install Pillow
## requests
	pip install requests

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
	
# SimpleFilter Functions

## <b>SimpleFilter.<i>create</b>(size, outer=-0.1, inner=1, rand=0)</i>

### Creates a size x size array, mainly used to create basic filters which can then be styled using the SimpleFilter.style function
-	Size: Size of the filter [size x size]
-	Outer: Value of all except the middle cell
-	Inner: Value of middle cell
-	Rand: Accepts list of integers to randomize cells

		f = sf.create(5) # creates a 5x5 kernel with outer cell value of -0.1 and inner cell value of 1
		
			>>> f
			
			>>> [[-0.1,-0.1,-0.1,-0.1,-0.1],
			     [-0.1,-0.1,-0.1,-0.1,-0.1],
			     [-0.1,-0.1, 1,  -0.1,-0.1],
			     [-0.1,-0.1,-0.1,-0.1,-0.1],
			     [-0.1,-0.1,-0.1,-0.1,-0.1]]
	
		f = sf.create(3,rand=[1,2,3,4]) # creates a 3x3 kernel with cells of random value taken from rand list
		
			>>> f
			
			>>> [[3,2,2],
			     [1,3,1],
			     [4,3,3]]

## <b>SimpleFilter.<i>load</b>(fpath, size=None, filter=False, convert=’L’)</i>
	
### Loads an image of any type using the PIL module and transforms it into an array that the SimpleFilter class can work with. Can also load images to be used as filters. Resizing images on load time will increase efficiency and speed of convolutions
-	Fpath: Image file path
-	Size: Accepts a list of width and height [w,h]. None loads image in actual size
-	Filter: When True replaces all cells of value 255 with 1 and all cells of value 0 with -1
-	Convert: Accepts PIL conversion type. ‘1’ loads image in black (255) and white (0)
		
		image = sf.load(path/to/image,[200,200]) # This loads an image at size 200x200 px
		
		filter = sf.load(path/to/image,[3,3],filter=True) # This loads a 3x3 image and converts
								   it to be used as a kernel

## <b>SimpleFilter<i>.randomize</b>(filter, rand=[-0.1,1])</i>

### Randomizes a filter using a list of integers. Rand lists are not limited to two numbers, however convolution with filters that have varying numbers may yield odd results
-	Filter: Filter to be randomized
-	Rand: Accepts list of ints or floats to randomize cells

		f = sf.create(3)
		
		sf.randomize(f,[1,3,6.3,0.7])
		
			>>> f
			
			>>> [[3,0.7,1],
			     [1,6.3,1],
			     [4,3,0.7]]

## <b>SimpleFilter.<i>prep</b>(array, filter, pad=0)</i>

### Prepares an image to be convoluted or mutated by padding all four sides of the array with any number provided. The padding is calculated based on each filter and thus larger filters will create a large amount of padding which will increase computation time
-	Array: Image array to be padded
-	Filter: Padding is created relative to the filter size
-	Pad: Integer that the padding is made of

		image = sf.load(path/to/image,[3,3])
		
			>>> image
			
			>>> [[1,1,1],
			     [1,1,1],
			     [1,1,1]]
			 
		filter = sf.create(3)
		
		sf.prep(image,filter)
		
			>>> image
			
			>>> [[0,0,0,0,0],
			     [0,1,1,1,0],
			     [0,1,1,1,0],
			     [0,1,1,1,0],
			     [0,0,0,0,0]]

## <b>SimpleFilter.<i>unprep</b>(array,filter)</i>

### Removes the padding from an image that has been fed through the SimpleFilter.prep function. Always make sure to unprep an image using the same filter that was used to prep it, otherwise the unprep function could distort or crop the image unintentionally
-	Array: Image array to be unpadded
-	Filter: Padding is removed relative to the filter size
		
			>>> image
			
			>>> [[0,0,0,0,0],
			     [0,1,1,1,0],
			     [0,1,1,1,0],
			     [0,1,1,1,0],
			     [0,0,0,0,0]]
			     
		sf.unprep(image,filter)
		
			>>> image
			
			>>> [[1,1,1],
			     [1,1,1],
			     [1,1,1]]
	

## <b>SimpleFilter.<i>conv</b>(array, filter)</i>

### Runs a single convolution on an image using a provided filter. This function is used as the basis of the mutations performed in the SimpleFilter.mut function. Important: Conv does NOT prep/unprep images automatically
-	Array: Image array to be convoluted
-	Filter: Filter to be used for convolution

		image = sf.load(path/to/image,[200,200])
		
		filter = sf.create(5)
		
		sf.prep(image,filter) # This is a crucial step as the conv function does not prep/unprep automatically

		conv = sf.conv(image,filter) # Performs a single convolution

## <b>SimpleFilter.<i>pool</b>(array)</i>

### Performs a max pooling function of size=2 and stride=2 on an image reducing it to half its original size
-	Array: Array to be pooled
	
		image = sf.load(path/to/image,[200,200])
		
			>>> len(image)
			>>> 400
			
		sf.pool(image)
		
			>>> len(image)
			>>> 200
		

## <b>SimpleFilter.<i>rectlin</b>(array)</i>

### Performs a rectilinear function on each cell in the image, changing all negative numbers into 0 whilst keeping any other number unchanged
-	Array: Array for which a rectilinear layer will be applied

		image = sf.load(path/to/image,[3,3])
		
			>>> image
			>>> [[1,234,50],
			     [-23,0,-133],
			     [54,21,7]]
		
		sf.reclin(image)
		
			>>> image
			>>> [[1,234,50],
			     [0,0,0],
			     [54,21,7]]

## <b>SimpleFilter.<i>mut</b>(array, filter, levels=1, plot=False, plotall=False, col=’Greys_r’, rand=[-0.1,1], r=False, pool=False, rectlin=False)</i>

### Mut stands for mutation and is a SimpleFilter vernacular for multilayered convolution. It uses the SimpleFilter.conv function to perform multiple convolutions or mutation on an image using a single provided filter. Important: Mut preps/unpreps images automatically
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

		image = sf.load(path/to/image,[200,200])
		filter = sf.create(3)
		
		mutation = sf.mut(image,filter,4,pool=True,reclin=True) # Performs 4 convolutions on image
									  using filter while also applying pooling
									  and rectlin on each convolution

## <b>SimpleFilter.<i>cycle</b>(array, filters, levels=1, pool=True, rectlin=True, col='Greys_r', plot=False, plotall=True, flat=False)</i>
	
### Cycles through a list of provided filters and performs multiple convolutions on or mutates an image using each filter and returns a list of arrays (images). Important: Cycle preps/unpreps images automatically
-	Array: Array to be cycled
-	Filters: Accepts a list of filters to cycle through
-	Levels: Number of mutations per filter
-	Pool: If True, applies a pooling layer after each convolution
-	Rectlin: If True, applies a rectilinear layer after each convolution
-	Col: Accepts matplotlib.pyplot.matshow color map
-	Plot: If True, plots final mutation
-	Plotall: If True, plots all mutations
-	Flat: If True, returns a flattened list that can be used in the SimpleFilter.euc function

		image = sf.load(path/to/image,[200,200])
		
		conv = sf.cycle(image, simple_filters, 4) 
		
		# This convolutes the image 4 times for each filter in simple_filters
		(simple_filters consists of four filters; horizontal line, vertical line, right
		diagonal line, left diagonal line) and plots all the images once complete
		

## <b>SimpleFilter.<i>style</b>(filter, front=1, back=-0.1, x=None, y=None, s=None, n= False)</i>
	
### Allows basic styling of a created filter or array. Mainly used to create basic filters such as horizontal lines, vertical lines and diagonal lines. A filter can go through the style function numerous times and if n is False, will append each style to the existing styled filter
-	Filter: Filter to be styled
-	Front: Integer to be applied to the styled areas
-	Back: Integer to be applied to the non-styled areas
-	X: Accepts a list containing the start and end indexes of the area to be filled in the Y direction [0,4] or [4, len(Filter)]
-	Y: Accepts a list containing the start and end indexes of the area to be filled in the X direction [0,4] or [4, len(Filter)]
-	S: Special function, allows the creation of diagonal filters using the keywords ‘rl’ for right to left diagonal or ‘lr’ for left to right diagonal
-	N: If True, replaces all the cells in the filter with the back variable before styling to ensure a blank slate

		filter = sf.create(3)
		
			>>> filter
		
			>>> [[-0.1,-0.1,-0.1],
			     [-0.1, 1,  -0.1],
			     [-0.1,-0.1,-0.1]]
			     
		sf.style(filter,x=[0,2],n=True) # Clears cell of any styling and fills the kernal horizontally from rows 0 to 1
		
			>>> filter
			
			>>> [[1, 1, 1],
			     [1, 1, 1],
			     [-0.1, -0.1, -0.1]]
			     
		sf.style(filter,y=[1,2],n=True) # Clears cell of any styling and fills the kernal vertically from rows 1 to 2
		
			>>> filter
			
			>>> [[-0.1, 1, -0.1],
			     [-0.1, 1, -0.1],
			     [-0.1, 1, -0.1]]
			     
		sf.style(filter,s="lr",n=True) # Clears cell of any styling and fills the kernal diagonally from left to right
		
			>>> filter
			
			>>> [[1, -0.1, -0.1],
			     [-0.1, 1, -0.1],
			     [-0.1, -0.1, 1]]
			     
		sf.style(filter,x=[0,1],y=[1,2],s="rl",n=True) # Multiple stylings can be done at once
		
			>>> filter
			
			>>> [[1, 1, 1],
			     [-0.1, 1, -0.1],
			     [1, 1, -0.1]]
		
## <b>SimpleFilter.<i>flat</b>(conv_layers)</i>

### Flattens a list of images into a single list of features to be used in the SimpleFilter.euc function
-	Conv_layers: A list of images (arrays) returned by the SimpleFilter.cycle function

		image1 = sf.create(5)
		image2 = sf.create(5)
		image3 = sf.create(5)
		
		images = [image1, image2, image3] # Flat function takes in a list of list of lists
		
			>>> images
			
			>>> [[[-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, 1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1]], 
			      
			     [[-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, 1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1]],
			      
			     [[-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, 1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1],
			      [-0.1, -0.1, -0.1, -0.1, -0.1]]]
			      
		flat = sf.flat(images)
		
			>>> flat
			
			>>> [-0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, 1, -0.1, -0.1,
			     -0.1,-0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, 1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1, 
			     -0.1, -0.1, 1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1,
			     -0.1, -0.1, -0.1, -0.1, -0.1]
		

## <b>SimpleFilter.<i>euc</b>(a, b)</i>
	
### Performs Euclidean distance calculation on two flattened arrays (lists) to determine the degree of closeness
-	A: List 1
-	B: List 2

		image1 = sf.create(3,rand=[4,5,6])
		image1 = sf.flat([image1]) # Flat function only takes in a list of list of lists
		
		image2 = sf.create(3,rand=[7,8,9])
		image2 = sf.flat([image2])
		
		result = sf.euc(image1, image2) # Performs Euclidean distance calculation
		
			>>> result
			
			>>> 9.848857801796104
			
## <b>simple_filters:</b> 

#### A list of four 3x3 kernels or filters (horizontal line, vertical line, right diagonal, left diagonal). To be used with sf.cycle()

## <b>simple_filters5x5:</b> 

#### A list of four 5x5 kernels or filters (horizontal line, vertical line, right diagonal, left diagonal). To be used with sf.cycle()

# SimpleClassifier Documentation

The SimpleClassifier is a k-nearest neighbor classifier that comes pre-packaged in the SimpleFilter module – It is optimized to be used with the SimpleFilter mutations, however any classifier of choice can be used instead with some modification

# SimpleClassifier Functions

<b>SimpleClassifier.<i>fit</b>(train_features, train_labels)</i>
	
Captures the training features and their corresponding labels
-	Train_features: The training data set
-	Train_Labels: The training labels

<b>SimpleClassifier<i>.predict</b>(test)</i>
	
Performs a prediction using the SimpleFilter.euc function to determine which label closest fits the test image
-	Test: Image to perform the prediction test on
