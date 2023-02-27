from tkinter import *
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os
from encrypt2 import *

class Stegno:

    art = 'by: Tanmay Kumar'
    output_image_size = 0
    global txt_font
    txt_font='arial'

    def main(self,root):
        root.title('Image Steganography')
        root.geometry('800x800')
        root.resizable(width =TRUE, height=TRUE)
        f = Frame(root)

        title = Label(f,text='Image Steganography')
        title.config(font=(txt_font,30))
        title.grid(pady=10)

        b_encode = Button(f,text="Encode Text", foreground="white",command= lambda :self.frame1_encode(f), padx=14,bg="grey")
        b_encode.config(font=(txt_font,14))
        b_decode = Button(f, text="Decode Text",padx=14,command=lambda :self.frame1_decode(f))
        b_decode.config(font=(txt_font,14))
        b_decode.grid(pady = 12)

        ascii_art = Label(f,text=self.art)
        ascii_art.config(font=(txt_font,12,'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=5,pady=5)

    def home(self,frame):
            frame.destroy()
            self.main(root)


    def frame1_decode(self,f):
        f.destroy()
        d_f2 = Frame(root)
        l2 = Label(d_f2, text='Enter the key(substitution cipher)')
        l2.config(font=(txt_font,18))
        l2.grid(pady=15)
        text_area = Text(d_f2, width=10, height=5)
        text_area.grid()
        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=(txt_font,18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda :self.frame2_decode(d_f2,text_area))
        bws_button.config(font=(txt_font,18))
        bws_button.grid()
        back_button = Button(d_f2, text='Cancel', command=lambda : Stegno.home(self,d_f2))
        back_button.config(font=(txt_font,18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_decode(self,d_f2,text_area):
        d_f3 = Frame(root)
        key=text_area.get("1.0", "end-1c")
        print(type(key))
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :')
            l4.config(font=(txt_font,18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg,key)
            print(hidden_data)
            l2 = Label(d_f3, text='Hidden data is :')
            l2.config(font=(txt_font,18))
            l2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel', command= lambda :self.page3(d_f3))
            back_button.config(font=(txt_font,11))
            back_button.grid(pady=15)
            back_button.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    def decode(self, image,key):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return (decryptMessage(data,key))

    def frame1_encode(self,f):
        f.destroy()
        f2 = Frame(root)
        l1= Label(f2,text='Select the Image in which \nyou want to hide text :')
        l1.config(font=(txt_font,18))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.frame2_encode(f2))
        bws_button.config(font=(txt_font,18))
        bws_button.grid()
        back_button = Button(f2, text='Cancel', command=lambda : Stegno.home(self,f2))
        back_button.config(font=(txt_font,18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()


    def frame2_encode(self,f2):
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)

            l3= Label(ep,text='Selected Image')
            l3.config(font=(txt_font,18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message')
            l2.config(font=(txt_font,18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            l3 = Label(ep, text='Enter the key(substitution cipher)')
            l3.config(font=(txt_font,18))
            l3.grid(pady=15)
            text_area_key = Text(ep, width=20, height=5)
            text_area_key.grid()
            encode_button = Button(ep, text='Cancel', command=lambda : Stegno.home(self,ep))
            encode_button.config(font=(txt_font,11))
            
            back_button = Button(ep, text='Encode', command=lambda : [self.enc_fun(text_area,myimg,text_area_key),Stegno.home(self,ep)])
            back_button.config(font=(txt_font,11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()


    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                '\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                    self.o_image_w,self.o_image_h,
                                    self.d_image_size/1000000,
                                    self.d_image_w,self.d_image_h)
            messagebox.showinfo('info',str)
        except:
            messagebox.showinfo('Info','Unable to get the information')
            
    def genData(self,data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_area,myimg,text_area_key):
        data = text_area.get("1.0", "end-1c")
        key=text_area_key.get("1.0", "end-1c")
        # print(data)
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            # change data
            newmsg=encryptMessage(data,key)
            print(newmsg)
            self.encode_enc(newimg, newmsg)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful")

    def page3(self,frame):
        frame.destroy()
        self.main(root)

root=Tk()
Stegno().main(root)
root.mainloop()
