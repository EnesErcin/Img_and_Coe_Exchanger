# Img_and_Coe_Exchanger
**This repository includes methods that can create .txt files from an image also create an image form specific .txt files.**<br />

For some computer vision applications the image data should be represented as one dimensional format. Although the libaries such as __Image (Pillow)__  and __OpenCV__  offers functions that can transform the jpeg formatted files into numpy arrays, there is no specific function to make it one dimensional. At first, I found it to be very reasonable to not include such function as it seems useless but then I tried to build an image filtering application on **FPGA and hardware description languages**. To implement image processing unit on fpga it is neccesery to use built in **block rams** on fpga boards to store and export data. The neccesity is questionable as it may be possible to use registers all over the fpga. At the end of it all it is a very bad practice especially dealing with very large data in hardware scale. The __Vivado Software__ which is basically an fpga implementation programrequires users to input a .coe file which data is sperated with only commas and each data is placed in same order of their index. For example {1,2,3} the block ram of address 1 has the information of 2.<br />


This proccedure of going back and forth to analyse if my image process is really doing what it should do drove me crayz. I was tring the find each index on a .txt file plus I had to think about perfect addressing for filtering. So to apply image filtering you have to consider not only one index but all the indexes on choosen kernel which is truelly an impossible job. If you are not familer with computer vision basics I recomend __Victor Powells__ website which explained the positions of bits of an image perfectly [Link to resource 1*](https://setosa.io/ev/image-kernels/).


## How to use the Module:
- 1) Import the main by 
- 2) Define an object: <br />
&nbsp;   1. IMG_Nump(txtdir,imgdir,boolean)
&nbsp;   2. Txt_Nump(txtdir,imgdir,boolean,imgshape)
- 3) Call the methods of the specified objects:
&nbsp;  1. build_coe()<br />
&nbsp;  2. build_array()<br />
&nbsp;  3. create_the_img()<br />

Such as 
```
import libary transform_img
testimg = transform_img.IMG_nump()
testimg.build_coe()

```
Main methods are:
* 2nd use the methods:
&nbsp;  * --> myclass_0.build_coe()<br />
&nbsp;  * --> myclass_1.build_array()<br />
&nbsp;  * --> myclass_1.create_the_img()<br />



![Gif: description](https://github.com/EnesErcin/Img_and_Coe_Exchanger/blob/main/Module/ezgif.com-gif-maker.gif)
