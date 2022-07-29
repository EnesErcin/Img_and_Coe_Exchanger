import transform_img

willthiswork = transform_img.IMG_Nump(coedir = 'C:/Users/Enes/Desktop/myewtest.txt', dir= 'C:/Users/Enes/Desktop/NewishGardeb.jpg' , transform_to_txt=True)
willthiswork.build_coe()

willthiswork_2 = transform_img.Txt_Nump(coedir = 'C:/Users/Enes/Desktop/myewtest.txt', dir= 'C:/Users/Enes/Desktop/NewNewGardeb.jpg' , transform_to_img=True,shape=(331,501))
willthiswork_2.build_array()
willthiswork_2.create_the_img()

