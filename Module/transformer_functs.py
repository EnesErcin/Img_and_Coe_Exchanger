import numpy as np
import cv2
import pandas as pd
from PIL import Image as im




# Function that takes the inputs of 
    ## a directory of an any image 
    ## If the image is coloured than it asks you if you want to work with grayscale
# Returns a boolean value for grayscale and the grayscale image array as numpy array

def imgadjust_isgray(dir):
    # Returns a tupple (newimgarray(numpyarray), isnotgray(boolean) )

    myimg = (cv2.imread(dir))

    initial_dimensions = len(myimg.shape) 

    if (initial_dimensions > 3 ):
        print("This image has more then 3 dimensions")

    elif(initial_dimensions == 3 ):
        print("This Image Is Coloured Should I Fix it")
        Togray = (input("Press 1 for Yes"))

        if(Togray != "1"):
            assert(type(myimg) == np.ndarray) # It did not returned np array
            print("Your img shape: " , myimg.shape)
            return myimg,True
            
        else:
            myimg = (cv2.imread(dir,0))
            print("Your img shape: " , myimg.shape)

            assert(len(myimg.shape) == 2) # It didnot become grayscale
            assert(type(myimg) == np.ndarray) # It did not returned np array
            return myimg, False

    elif(initial_dimensions == 2):
        print("This Image is Grayscale, Thats Good")

        assert(type(myimg) == np.ndarray)  # It did not returned np array
        return myimg,False








# This Function that takes the inputs of 
    ## a np.array that represent the img, 
    ## boolean value true if colored,
    ## the new directory to dump the new txt file which will be formed
# and creates one dimensional .txt file from a img array

def create_coeFile(imgarray,isnotgray,CoeDir):
        if not(isnotgray):
          defualtmaxaddr = 499550
          maxramsize = int(input("What is the maximum number of address in bram ? || note: there is a default value") or defualtmaxaddr)
          

          # Adjust the magnitude
          # Block Ram Maximum Size !!
          assert(imgarray.size < maxramsize) # Image Too Big
          print("This is the choosen number of address",imgarray.size)
          print("Checkinking if same as images row*column= ", imgarray.shape[1]*imgarray.shape[0] ,"\nChecking if same:" ,bool(int(imgarray.shape[1]*imgarray.shape[0]) == imgarray.size ))
          assert(int(imgarray.shape[1]*imgarray.shape[0]) == imgarray.size) #They should have been equal

          NumofColums = int(imgarray.shape[1])
          NumofRows = int(imgarray.shape[0])
          print(imgarray.shape)

          # Create .Coe File
          with open(CoeDir,"w") as mycoe:
            mycoe.write("memory_initialization_radix=10: \n")
            mycoe.write("memory_initialization_vector= \n")

            for row in range (0, NumofRows):
              for column in range (0,NumofColums):

                try:
                    mycoe.write(str(imgarray[row][column]))
                                     
                except:
                    print("myrow", row)
                    print("mycolum", column)

                if(row == NumofRows-1 and column == NumofColums -1):  
                    mycoe.write(";")
                    print("Coe File is created at this location: ", CoeDir)
                    assert(NumofColums*NumofRows ==((row +1)* (column +1 ))) # Coe is not approprate size
                else:
                      mycoe.write(",") 
                      mycoe.write("\n")

                
        else:
          print("You Dont Want Colored Img to be converted as coe")







#   The function updates the bad chars array which will be filtered out while reading the txt file. 
#   !! Be catious to enter numbers that will cause problems 
#   Function returns updated bad chars.

bad_chars = [ "'" , ',',';']

def delete_unwanted_chars(bad_chars):
    print(" Chars Such as : \n-- Space , /n , comma(,) ,semicolon(;)    \n-- memory_initialization_radix=10; \n-- memory_initialization_vector=' \n  are already ommitted \n")

    more_char = (input("Want to add new char  \n   Press c if no "))
    isrepeated = False

    #Input loop that takes as many inputs as long as _morechar_ stays as "c" 
    while(more_char == "c"):
        newbadchar = input("Any other unwanted chars")
        more_char = (input("Want to add more char   \n   Press c if no "))

        ## Checks if the user try to add same chars 
        for items in bad_chars:
            if(newbadchar ==  items):
                print("You have already added this")
                isrepeated = True
            else:
                isrepeated = False

        ## If not the same char then added to badchars list
        if not (isrepeated):
            bad_chars.append(newbadchar)
        else:
            isrepeated = False

    else:
        print("Loop Ended")
        return bad_chars








# This Function that takes the inputs of 
    ## Directory of a one dimensional .txt file which represents an image, 
        #   I assume one line represents one bit and there is inital two lines of certain indicators
        #   The source of my assumptions come from the inital purpose of this project which is creating  .coe files for vivado design suit for FPGA design.    
    ## Boolean value true if colored,
    ## New directory to dump the new txt file which will be formed
# and creates one dimensional .txt file from a img array

def txttoarr(coedir,bad_chars_arr,img_y,img_column):
    img_arr = np.zeros((img_y,img_column))
    x = 0
    y = -1      # y + 1 in the loop occurs before numpy insertation
    
    print(img_arr.shape)
    with open(coedir,"r") as fp:

        for count, line in enumerate(fp):
            # I assume the file has no comment lines and there are two initlising lines for coe file
                # 1- memory_initialization_radix=10: 
                # 2- memory_initialization_vector=
            # Filtering every line for comments is possible solution

            if count > 1 :

                x = (count-2) % (img_column) # Lnegth of column is +1

                line_wo_comma = ''.join(filter(lambda i: i not in bad_chars_arr, line))   

                if x == 0:
                        y = y + 1

                try:
                        img_arr[y][x] = int(line_wo_comma)
                except:
                    print("This rows and Columns are problem: \n")
                    print("My_Y:", y)
                    print("My_X:", x) 
                    print(line_wo_comma)   

    return img_arr     



def create_img(imgarray,dir):
    newimgarray = im.fromarray(np.uint8(imgarray*255), 'L')
    newimgarray.save(dir)

    print("Img is saved on specified location: -> " , dir)