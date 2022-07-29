
import transformer_functs
import numpy as np

##### The possible commands are:

#### 1st Create a class:
  # myclass_0 = IMG_Nump( coedir = ' ', dir= '' , transform_to_txt=True)
  # myclass_1 = Txt_Nump( coedir = ' ', dir= '' , transform_to_img=True, shape( int_y_row , int_x_col ))

#### 2nd use the methods:
  # --> myclass_0.build_coe()
  # --> myclass_1.build_array()
  # --> myclass_1.create_the_img()


# 1st Main Object -- Img_Nump --
  ### Object that takes two parameters which are 
      ##   1- dir -> image directory which is choosen to be transformed into .txt or .coe file
      ##   3- transform_to_txt -> Boolean indicator, true means the created object can be transformed into txt later
      ##   2- coedir -> directory for new .txt or .coe file which will be formed

  ### And have the attributes of 
      ## 1- Boolean value which shows if the image is grayscale or not
      ## 2- Numpy array of the grayscale image || To access it use Object.imgarray 

class IMG_Nump:
    def __init__(self, dir, coedir, transform_to_txt):
      self.dir = dir
      self.coedir = coedir
      self.transform_to_txt = transform_to_txt
      if(transform_to_txt):
        mylist = transformer_functs.imgadjust_isgray(dir)
        self.imgarray =  mylist[0]
        self.isnotgray = mylist[1]
    
    #To build the coe file use this method
    def build_coe(self):
      transformer_functs.create_coeFile(self.imgarray, self.isnotgray ,self.coedir)



# 2nd Main Object -- Txt_Nump --
  ### Object that takes two parameters which are 
    ##   1- dir ->  String of directory for new image which will be created from .txt or .coe file
    ##   2- coedir -> String of directory for source of the .txt or .coe file 
    ##   3- transform_to_img -> Boolean indicator, true means the created object can be transformed into image later
    ##   4- Shape -> !! List of integers which shows the number of bits along x and y axis or colums and rows. 
      # About the shape parameter:
      # Since this piece of code only deals with one dimensional txt file it is impossible to deduce rigth propotion that is why it should be entered manually
      # One possible thing to do you can start with an image and than turn that image to one dimensional txt file with the classes I defined above and then use that txt file. 


  ## And have the attributes of 
    # 1- Boolean value which shows if the image is grayscale or not
    # 2- Numpy array of the grayscale image || To access it use Object.imgarray 

class Txt_Nump:
    def __init__(self,dir, coedir, transform_to_img, shape):
        self.dir = dir
        self.coedir = coedir
        self.transform_to_img = transform_to_img
        assert( type(shape) == tuple) # The parameter shape must be tuple
        self.x_vec = shape[1]
        self.y_vec = shape[0]
        self.badchars = transformer_functs.bad_chars #You can add more chars with delete_unwanted_chars function or if there are small number you can manipulate by hand
        
        self.imgarray = np.zeros((self.y_vec,self.y_vec))

    def build_array(self):
        imgarray = transformer_functs.txttoarr(coedir =self.coedir,bad_chars_arr = self.badchars,img_y= self.y_vec,img_column=self.x_vec)
        self.imgarray = imgarray
        return imgarray

    def create_the_img(self):    
      transformer_functs.create_img(imgarray = self.imgarray, dir= self.dir)
