import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
from PIL import Image
import math
import requests
from io import BytesIO

class SimpleFilter():

    def __init__(self):
        pass

    def create(self,size=3,outer=-0.1,inner=1,rand=0):
        filt = []
        if rand == 0:
            for row in range(0,size):
                    filt.append([outer]*size)
        else:
            for row in range(0,size):
                filt.append([[0]*size]*size)
            for index, line in enumerate(filt):
                for ind, cell in enumerate(line):
                    filt[index][ind] = random.choice(rand)
        if rand == 0:
            filt[int(size/2)][int(size/2)] = inner
        else:
            filt[int(size/2)][int(size/2)] = random.choice(rand)

        return filt

    @staticmethod
    def load(fpath,size=None,filter=False,convert='L',comp=True):

        if 'http://' in fpath or 'https://' in fpath or 'www.' in fpath:
            response = requests.get(fpath)
            test_img = Image.open(BytesIO(response.content)).convert(convert)
        else:
            test_img = Image.open(fpath, 'r').convert(convert)

        if size !=None:
            test_img = test_img.resize((size[0], size[1]), Image.ANTIALIAS)
        test = list(test_img.getdata())
        image = []

        for i in test:
            image.append(i)

        if filter == True:
            for index,cell in enumerate(image):
                if cell == 0:
                    image[index] = -0.1
                elif cell == 255:
                    image[index] = 1

        if comp == True:

            image = [image[i:i + test_img.size[0]] for i in range(0, len(image), test_img.size[0])]

        return image

    def randomize(self,filter,rand=[-0.1,1]):
        for index,value in enumerate(filter):
            for ind,val in enumerate(value):
                filter[index][ind] = random.choice(rand)

    def prep(self,array,filter,pad=0):

        size = int(len(filter)/2)

        for times in range(0,size):
            array.append([pad]*len(array[0]))
            array.insert(0,[pad]*len(array[0]))

            for row in array:
                row.append(pad)
                row.insert(0,pad)

    def unprep(self,array,filter):

        size = int(len(filter)/2)

        for times in range(0,size):
            array.pop()
            array.pop(0)

            for row in array:
                row.pop()
                row.pop(0)

    def conv(self,array,filter):

        newarray = []
        size = len(filter)//2
        chunk = len(array[0])-size*2


        for index, row in enumerate(array[size:]):
            for indx,cell in enumerate(row[size:]):
                result = []
                for line in array[index-size:index+size+1]:
                    result.append(line[indx-size:indx+size+1])
                for section in result:
                    if not section:
                        result.clear()
                if result:
                    for i,v in enumerate(result):
                        for ii,vv in enumerate(v):
                            result[i][ii] = result[i][ii]*filter[i][ii]
                if result:
                    for i,section in enumerate(result):
                        result[i] = sum(result[i])
                    result = sum(result)/len(result)
                    newarray.append(result)

        newarray = [newarray[x:x+chunk] for x in range(0, len(newarray), chunk)]

        return newarray

    def mut(self,array,filter,levels=1,plot=False,plotall=False,col='Greys_r',
            r=False,rand=[-0.1,1],pool=False,rectlin=False):
        result = array
        for level in range(0,levels):
             if r == True:
                self.randomize(filter,rand=rand)

             self.prep(result,filter)
             result = self.conv(result,filter)
             if pool == True:
                 result = self.pool(result)
             if rectlin == True:
                 self.rectlin(result)
             if plotall == True:
                 plt.matshow(result,cmap=col)
                 plt.title(level)
        plt.show()
        if plot == True:
            plt.matshow(result,cmap=col)
            plt.show()
        self.unprep(array,filter)
        return result


    def cycle(self,array,filters,levels=1,pool=True,rectlin=True,col='Greys_r',
                plot=False,plotall=True,flat=False):

        conv_layers = []
        for index,filt in enumerate(filters):
            self.prep(array,filt)
            result = self.mut(array,filt,levels,pool=pool,rectlin=rectlin,plotall=plotall,plot=plot,col=col)
            conv_layers.append(result)
            self.unprep(array,filt)
        if flat == False:
            return conv_layers
        elif flat == True:
            flattened = self.flat(conv_layers)
            return flattened

    def pool(self,array):

        result = []

        for index in range(0,len(array)-1,2):
            for indx in range(0,len(array[0])-1,2):

                temp = []

                temp.append(array[index][indx])
                temp.append(array[index][indx+1])
                temp.append(array[index-1][indx])
                temp.append(array[index-1][indx+1])

                result.append(max(temp))

        result = [result[i:i + int(len(array[0])/2)] for i in range(0, len(result), int(len(array[0])/2))]

        return result

    def rectlin(self,array):
        for index,row in enumerate(array):
            for indx,cell in enumerate(row):
                if cell < 0:
                    array[index][indx] = 0
        return array

    def cull(self,array,factor=-1,length=10):
        count = []
        index = 0
        for i,v in enumerate(array):
                count.append(array.count(v))
        for i,v in enumerate(count):
                if v == max(count):
                        index = i
                        break
        array = [x if x not in range(array[index]-length,array[index]+length) else factor for x in array]
        return array

    def cull_all(self,array,factor=-1,length=10):
        array_cull = array[:]
        for i,v in enumerate(array_cull):
            array_cull[i] = sf.cull(array_cull[i],factor,length)
        return array_cull

    def style(self,filter,front=1,back=-0.1,x=None,y=None,s=None,n=False):
        if n==True:
            for index, row in enumerate(filter):
                for indx, cell in enumerate(row):
                    filter[index][indx] = back

        if x != None and y == None:
            for i in range(x[0],x[1]):
                for indx, cell in enumerate(filter[i]):
                    filter[i][indx] = front

        if y != None and x == None:
            for i in range(y[0],y[1]):
                for index, row in enumerate(filter):
                    for indx, cell in enumerate(row):
                        filter[index][i] = front

        if x != None and y != None:
            for i in range(x[0],x[1]):
                for indx, cell in enumerate(filter[i]):
                    filter[i][indx] = front
            for i in range(y[0],y[1]):
                for index, row in enumerate(filter):
                    for indx, cell in enumerate(row):
                        filter[index][i] = front

        if s == 'lr':
            for index, row in enumerate(filter):
                filter[index][index] = front

        if s == 'rl':
            i = 1
            for index, row in enumerate(filter):
                filter[index][-i] = front
                i+=1

        return filter

    def flat(self, conv_layers):
        layers = []
        for row1 in conv_layers:
            for row2 in row1:
                for cell in row2:
                    layers.append(cell)
        return layers

    def euc(self,a,b):
      arr = []
      if isinstance(a, list) and isinstance(b, list) or isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) == len(b):
          for indx,val in enumerate(a):
            arr.append( ((a[indx] - b[indx])**2) )
          return math.sqrt(sum(arr))
        else:
          return 'Error: Lists must be of same lengths'
      elif isinstance(a, int) and isinstance(b, int):
        return abs(a-b)
      else:
        return 'Error: Must be either int or list objects'

class SimpleClassifier():

  def fit(self,train_features,train_labels):
    self.train_features = train_features
    self.train_labels = train_labels

  def predict(self,test):
    test = [test]
    result = []
    for i,v in enumerate(test):
      predictions = []
      for index,value in enumerate(self.train_features):
          label = SimpleFilter().euc(test[i],value)
          predictions.append(label)
      for index,val in enumerate(predictions):
          if val == min(predictions):
              result.append(self.train_labels[index])
    return result


lrdiag = SimpleFilter().create(3,-0.1)
SimpleFilter().style(lrdiag,s='lr')
rldiag = SimpleFilter().create(3,-0.1)
SimpleFilter().style(rldiag,s='rl')
hline = SimpleFilter().create(3)
SimpleFilter().style(hline,x=[1,2])
vline = SimpleFilter().create(3)
SimpleFilter().style(vline,y=[1,2])

lrdiag5 = SimpleFilter().create(5,-0.1)
SimpleFilter().style(lrdiag5,s='lr')
rldiag5 = SimpleFilter().create(5,-0.1)
SimpleFilter().style(rldiag5,s='rl')
hline5 = SimpleFilter().create(5)
SimpleFilter().style(hline5,x=[2,3])
vline5 = SimpleFilter().create(5)
SimpleFilter().style(vline5,y=[2,3])

# Default lists of basic filters to be accessed when using the cycle function

simple_filters = [vline,hline,lrdiag,rldiag]
simple_filters5x5 = [vline5,hline5,lrdiag5,rldiag5]

default_filters = {'simple_filters':simple_filters,'simple_filters5x5':simple_filters5x5}
