from tkinter import *
from math import *
from tkinter import messagebox
import random,smtplib
import os,tempfile
#fuctionality part
        
def total():
    global soapprice,facecreamprice,hairgelprice,hairsprayprice,bodylotionprice,facewashprice,totalcosmeticsprice,totalcosmeticstax,ricebagprice,oilprice
    global Daalprice,wheatprice,sugarprice,Teaprice,mazaprice,Spriteprice,thumpsupprice,pepsiprice,Frootiprice,Cocacolaprice,totalcooldrinktax,totalgrocerytax
    global totalcooldrinkprice,totalgroceryprice
    soapprice=int(bathSoapEntry.get())*30
    facecreamprice=int(FacecreamEntry.get())*70
    hairsprayprice=int(hairsprayEntry.get())*100
    hairgelprice=int(hairgelEntry.get())*50
    bodylotionprice=int(bodylotionEntry.get())*150
    facewashprice=int(FacewashEntry.get())*100
    
    totalcosmeticsprice=sum([soapprice,facecreamprice,hairsprayprice,hairgelprice,bodylotionprice,facewashprice])
    totalcosmeticstax=totalcosmeticsprice*0.1
    
    CosmeticpriceEntry.delete(0,END)
    CosmeticpriceEntry.insert(1,totalcosmeticsprice)
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(1,totalcosmeticstax)
    
    ricebagprice= int(riceEntry.get())*1200
    oilprice=int(oilEntry.get())*100
    Daalprice=int(DaalEntry.get())*80
    wheatprice=int(wheatEntry.get())*56
    sugarprice=int(sugarEntry.get())*25
    Teaprice=int(TeaEntry.get())*45
    
    totalgroceryprice=sum([ricebagprice,oilprice,Daalprice,wheatprice,sugarprice,Teaprice])
    totalgrocerytax=totalgroceryprice*0.025

    GrocerypriceEntry.delete(0,END)
    GrocerypriceEntry.insert(0,totalgroceryprice)
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,totalgrocerytax)
    
    mazaprice=int(MaazaEntry.get())*80
    pepsiprice=int(pepsiEntry.get())*75
    Spriteprice=int(SpriteEntry.get())*60
    thumpsupprice=int(ThumsupEntry.get())*80
    Frootiprice=int(FrootiEntry.get())*80
    Cocacolaprice=int(CocacolaEntry.get())*90
    
    totalcooldrinkprice=sum([mazaprice,pepsiprice,Spriteprice, thumpsupprice,Frootiprice,Cocacolaprice])
    totalcooldrinktax=totalcooldrinkprice*0.1
    
    cooldrinkpriceEntry.delete(0,END)
    cooldrinkpriceEntry.insert(0, totalcooldrinkprice)
    cooldrinktaxEntry.delete(0,END)
    cooldrinktaxEntry.insert(0,totalcooldrinktax)
def search_bill():
    if billEntry.get()=='':
        messagebox.showerror('Error',"please enter billno")
    else:
        for i in os.listdir('bills/'):
            l=i.split('.')
            l.remove('txt')
            a=int(l[0])
            if int(billEntry.get()) == a:
                #print(billEntry.get())
                fp=open(f'bills/{i}','r')
                textarea.delete(1.0,END)
                for data in fp:
                    textarea.insert(END,data)
                fp.close()
                break

        else:
            messagebox.showerror('Error','invalid bill number')   
if not os.path.exists('bills'):
    os.mkdir('bills')    

def save_bill():
    result = messagebox.askyesno('SaveBill','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'{billnumber} is saved successfully')
        #billnumber=random.randint(1000,9999)
global billnumber
billnumber=random.randint(1000,9999)    
def bill_area():
    #billnumber=random.randint(1000,9999) 
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details are required')
    elif CosmeticpriceEntry.get()=='' and GrocerypriceEntry.get()=='' and cooldrinkpriceEntry.get()=='':
        messagebox.showerror('Error',"please select any one of the items to generate bill")    
    elif cosmetictaxEntry.get()==0 and GrocerypriceEntry.get() and cooldrinkpriceEntry.get():
        messagebox.showerror('Error',"please select any one of the items to generate bill")
    else    :
        textarea.delete(1.0,END)    
        textarea.insert(END,'***Welcome Customers***\n')  
        textarea.insert(END,f'Customer Name : {nameEntry.get()}\n')
        textarea.insert(END,f'Bill Number : {billnumber}\n')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n') 
        textarea.insert(END,f'========================================================================================\n')   
        textarea.insert(END,'Product\t\t\t\t\tQuantity\t\t\t\t\tPrice\n')
        textarea.insert(END,f'========================================================================================\n')
        if bathSoapEntry.get()!='0':
            textarea.insert(END,f" BathSoap \t\t\t\t\t{bathSoapEntry.get()}\t\t\t\t\t{soapprice}\n")
        if FacecreamEntry.get()!='0':
            textarea.insert(END,f' FaceCream \t\t\t\t\t {FacecreamEntry.get()}\t\t\t\t\t{facecreamprice}\n') 
        if hairgelEntry.get()!='0':
            textarea.insert(END,f" Hairgel \t\t\t\t\t{hairgelEntry.get()}\t\t\t\t\t{hairgelprice}\n")  
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f' HairSpray \t\t\t\t \t{hairsprayEntry.get()}\t\t\t\t\t{hairsprayprice}\n')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f' BodyLotion \t\t\t\t\t{bodylotionEntry.get()}\t\t\t\t\t{bodylotionprice}\n')
        if FacewashEntry.get()!='0':
            textarea.insert(END,f' FaceWash \t\t\t\t\t{FacecreamEntry.get()} \t\t\t\t\t{facewashprice}\n')
        if riceEntry.get()!='0':
            textarea.insert(END,f' RiceBags \t\t\t\t\t{riceEntry.get()}\t\t\t\t\t{ricebagprice}\n')
        if oilEntry.get()!='0':
            textarea.insert(END,f' OilPackets \t\t\t\t\t{oilEntry.get()}\t\t\t\t\t{oilprice}\n')
        if DaalEntry.get()!='0':
            textarea.insert(END,f' Daal \t\t\t\t\t{DaalEntry.get()}\t\t\t\t\t{Daalprice}\n')
        if wheatEntry.get()!='0':
            textarea.insert(END,f' Wheat \t\t\t\t\t{wheatEntry.get()}\t\t\t\t\t{wheatprice}\n')
        if sugarEntry.get()!='0':
            textarea.insert(END,f' Sugar \t\t\t\t\t{sugarEntry.get()}\t\t\t\t\t{sugarprice}\n')
        if TeaEntry.get()!='0':
            textarea.insert(END,f' Tea \t\t\t\t\t{TeaEntry.get()}\t\t\t\t\t{Teaprice}\n')
        if MaazaEntry.get()!='0':
            textarea.insert(END,f' Maaza \t\t\t\t\t{MaazaEntry.get()}\t\t\t\t\t{mazaprice}\n') 
        if pepsiEntry.get()!='0':
            textarea.insert(END,f' Pepsi \t\t\t\t\t{pepsiEntry.get()}\t\t\t\t\t{pepsiprice}\n')
        if SpriteEntry.get()!='0':
            textarea.insert(END,f' Sprite \t\t\t\t\t{SpriteEntry.get()}\t\t\t\t\t{Spriteprice}\n')
        if ThumsupEntry.get()!='0':
            textarea.insert(END,f' Thumsup \t\t\t\t\t{ThumsupEntry.get()}\t\t\t\t\t{thumpsupprice}\n') 
        if FrootiEntry.get()!='0':
            textarea.insert(END,f' Frooti \t\t\t\t\t{FrootiEntry.get()}\t\t\t\t\t{Frootiprice}\n')
        if CocacolaEntry.get()!='0':
            textarea.insert(END,f' Coca Cola \t\t\t\t\t{CocacolaEntry.get()} \t\t\t\t\t{Cocacolaprice}\n')      
        textarea.insert(END,f'========================================================================================')
        if cosmetictaxEntry.get()!='0.0':
            textarea.insert(END,f'Cosmetic tax \t\t\t\t\t{totalcosmeticstax}\n')
        if grocerytaxEntry.get()!='0.0':
            textarea.insert(END,f'Grocery tax \t\t\t\t\t{totalgrocerytax}\n')
        if cooldrinktaxEntry.get()!='0.0':
            textarea.insert(END,f'Cool drink tax \t\t\t\t\t {totalcooldrinktax}\n')
            textarea.insert(END,f'========================================================================================')
        totalcost=sum([totalcosmeticsprice,totalgroceryprice,totalcooldrinkprice,totalcooldrinktax,totalcosmeticstax,totalgrocerytax])
        textarea.insert(END,f'GrandTotal \t\t\t\t\t {totalcost}\n')
        textarea.insert(END,f"\n\n\t**********THANK YOU FOR SHOPPING!! VISIT AGAIN !!! HAVE A GREAT DAY**********\n")
        save_bill()
        
def printbilling():
    if textarea.get(1.0,END) =='\n':
        messagebox.showerror("Error","Bill is Empty")
    else:
       file = tempfile.mktemp('.txt')
       open(file,'w').write(textarea.get(1.0,END))
       os.startfile(file,'print')   
def sendmail():
    def sendgmail():
        try :
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(gmailidlabelEntry.get(),gmailpasswordlabelEntry.get())
            message=email_textarea.get(1.0,END)
            reciever=recieverlabelEntry.get()
            ob.sendmail(gmailidlabelEntry.get(),recieverlabelEntry.get(),message)
            ob.quit()
            messagebox.showinfo('SUCCESS','Bill is successfully sent',parent=root1)
        except:
            messagebox.showerror("Eroor",'Something went wrong',parent=root1)
    if textarea.get(1.0,END) =='\n':
       messagebox.showerror("Error","Bill is Empty") 
    else:
        root1=Toplevel()
        root1.title("Send Email")
        root1.config(bg="gray20")
        root1.resizable(0,0)
        root1.config(bg='light sea green')
        senderFrame=LabelFrame(root1,text="Sender Frame",font=("times new roman",15,'bold'),bg='Hotpink4',fg="yellow")
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
    
        gmailidlabel=Label(senderFrame,text="Senders Email",font=("times new roman",15,'bold'),bg='Hotpink4',fg="white")
        gmailidlabel.grid(row=0,column=0)
    
        gmailidlabelEntry=Entry(senderFrame,font=("times new roman",15,'bold'),bd=3,width=25,relief=GROOVE)
        gmailidlabelEntry.grid(row=0,column=1,padx=30,pady=10) 
    
        gmailpasswordlabel=Label(senderFrame,text="Sender's Password",font=("times new roman",15,'bold'),bg='Hotpink4',fg="white")
        gmailpasswordlabel.grid(row=1,column=0)
    
        gmailpasswordlabelEntry=Entry(senderFrame,font=("times new roman",15,'bold'),bd=3,width=25,relief=GROOVE,show='*')
        gmailpasswordlabelEntry.grid(row=1,column=1,padx=30,pady=10)
    
        recieverFrame=LabelFrame(root1,text="Reciever Frame",font=("times new roman",15,'bold'),bg='Hotpink4',fg="yellow")
        recieverFrame.grid(row=1,column=0,padx=40,pady=20)
    
        recieverlabel=Label(recieverFrame,text="Reciever's Email",font=("times new roman",15,'bold'),bg='Hotpink4',fg="white")
        recieverlabel.grid(row=0,column=0)
    
        recieverlabelEntry=Entry(recieverFrame,font=("times new roman",15,'bold'),bd=3,width=25,relief=GROOVE)
        recieverlabelEntry.grid(row=0,column=1,padx=30,pady=10) 
    
        messagelabel=Label(recieverFrame,text="Message",font=("times new roman",15,'bold'),bg='Hotpink4',fg="white")
        messagelabel.grid(row=1,column=0,padx=10,pady=8)
    
        email_textarea=Text(recieverFrame,font=("times new roman",15,'bold'),bd=2,relief=GROOVE,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('\t\t\t\t\t','\t\t'))
    
        sendButton=Button(root1,text='SEND',font=("times new roman",15,'bold'),width=15,command=sendgmail,bd=7,relief=GROOVE,bg='Hotpink4',fg='yellow')
        sendButton.grid(row=2,column=0,pady=20)
    root1.mainloop() 
def clearall():
    bathSoapEntry.delete(0,END)
    bathSoapEntry.insert(0,0)
    FacecreamEntry.delete(0,END)
    FacecreamEntry.insert(0,0)
    FacewashEntry.delete(0,END)
    FacewashEntry.insert(0,0)
    hairgelEntry.delete(0,END)
    hairgelEntry.insert(0,0)
    bodylotionEntry.delete(0,END)
    bodylotionEntry.insert(0,0)
    
    riceEntry.delete(0,END)
    riceEntry.insert(0,0)
    oilEntry.delete(0,END)
    oilEntry.insert(0,0)
    DaalEntry.delete(0,END)
    DaalEntry.insert(0,0)
    wheatEntry.delete(0,END)
    wheatEntry.insert(0,0)
    sugarEntry.delete(0,END)
    sugarEntry.insert(0,0)
    TeaEntry.delete(0,END)
    TeaEntry.insert(0,0)
    
    MaazaEntry.delete(0,END)
    MaazaEntry.insert(0,0)
    pepsiEntry.delete(0,END)
    pepsiEntry.insert(0,0)
    SpriteEntry.delete(0,END)
    SpriteEntry.insert(0,0)
    ThumsupEntry.delete(0,END)
    ThumsupEntry.insert(0,0)
    FrootiEntry.delete(0,END)
    FrootiEntry.insert(0,0)
    CocacolaEntry.delete(0,END)
    CocacolaEntry.insert(0,0)
    
    CosmeticpriceEntry.delete(0,END)  
    GrocerypriceEntry.delete(0,END)
    cooldrinkpriceEntry.delete(0,END)
    
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    cooldrinktaxEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)
    textarea.delete(1.0,END) 
     
                               

#gui part
root=Tk()


root.title("Retail Billing System")
#root.geometry(widthxheight)
root.geometry("1270x685")
root.iconbitmap('icons.ico')
root.config(bg='light sea green')
headinglabel=Label(root,text="Retail Billing System",font=('times new roman',25,'bold'),bg='Hotpink4',fg='yellow',border='9',relief=GROOVE)
headinglabel.pack(fill=X,pady=10)

customer_details_frame=LabelFrame(root,text='Customer details',font=('times new roman',15,'bold'),bg='Hotpink4',fg='yellow',border='4',relief=GROOVE)
customer_details_frame.pack(fill=X)

namelabel=Label(customer_details_frame,text="Name of customer",bg='Hotpink4',fg='white',font=('times new roman',15,'bold'))
namelabel.grid(row=0,column=0,padx=20,pady=5)

nameEntry=Entry(customer_details_frame,font=('arial',12),border=7,width=20)
nameEntry.grid(row=0,column=1,padx=20,pady=5)

phonelabel=Label(customer_details_frame,text="Phone Number",bg='Hotpink4',fg='white',font=('times new roman',15,'bold'))
phonelabel.grid(row=0,column=2,padx=20,pady=5)

phoneEntry=Entry(customer_details_frame,font=('arial',15),border=7,width=18)
phoneEntry.grid(row=0,column=3,padx=20,pady=5)

billlabel=Label(customer_details_frame,text="Bill Number",bg='Hotpink4',fg='white',font=('times new roman',15,'bold'))
billlabel.grid(row=0,column=4,padx=20,pady=5)

billEntry=Entry(customer_details_frame,font=('arial',15),border=7,width=18)
billEntry.grid(row=0,column=5,padx=20,pady=15)

searchbutton=Button(customer_details_frame,text="SEARCH",font=('arial',15,'bold'),bd=7,padx=60,pady=1,fg='yellow',bg='Hotpink4',command=search_bill)
searchbutton.grid(row=0,column=7,columnspan=4)

productsFrame=Frame(root)
productsFrame.pack(fill=X,pady=10)

cosmeticsFrame=LabelFrame(productsFrame,text="Cosmetics Frame",font=("times new roman",15,'bold'),fg='yellow',bg='Hotpink4',relief=GROOVE,bd=6)
cosmeticsFrame.grid(row=0,column=0)

bathSoap=Label(cosmeticsFrame,text="Bath Soap",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
bathSoap.grid(row=0,column=0,padx=10,pady=9,sticky='w')


bathSoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
bathSoapEntry.grid(row=0,column=1,padx=10,pady=9)
bathSoapEntry.insert(0,0)

Facecream=Label(cosmeticsFrame,text="Face Cream",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Facecream.grid(row=1,column=0,pady=9,padx=10,sticky='w')

FacecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
FacecreamEntry.grid(row=1,column=1,padx=10,pady=9)
FacecreamEntry.insert(0,0)


Facewash=Label(cosmeticsFrame,text="Face Wash",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Facewash.grid(row=2,column=0,pady=9,padx=10,sticky='w')

FacewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
FacewashEntry.grid(row=2,column=1,padx=10,pady=9)
FacewashEntry.insert(0,0)

hairspray=Label(cosmeticsFrame,text="Hair Spray",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
hairspray.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
hairsprayEntry.grid(row=3,column=1,padx=10,pady=9)
hairsprayEntry.insert(0,0)

hairgel=Label(cosmeticsFrame,text="Hair gel",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
hairgel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
hairgelEntry.grid(row=4,column=1,padx=10,pady=9)
hairgelEntry.insert(0,0)

bodylotion=Label(cosmeticsFrame,text="Body Lotion",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
bodylotion.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,border=7)
bodylotionEntry.grid(row=5,column=1,padx=10,pady=9)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text="Groceries Frame",font=("times new roman",15,'bold'),fg='yellow',bg='Hotpink4',relief=GROOVE,bd=6)
groceryFrame.grid(row=0,column=1)

rice=Label(groceryFrame,text="Rice Bags",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
rice.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
riceEntry.grid(row=0,column=1,padx=10,pady=9)
riceEntry.insert(0,0)

Oil=Label(groceryFrame,text="Oil packets",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Oil.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
oilEntry.grid(row=1,column=1,padx=10,pady=9)
oilEntry.insert(0,0)

Daal=Label(groceryFrame,text="Daal",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Daal.grid(row=2,column=0,pady=9,padx=10,sticky='w')

DaalEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
DaalEntry.grid(row=2,column=1,padx=10,pady=9)
DaalEntry.insert(0,0)

wheat=Label(groceryFrame,text="Wheat ",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
wheat.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
wheatEntry.grid(row=3,column=1,padx=10,pady=9)
wheatEntry.insert(0,0)

sugar=Label(groceryFrame,text="Sugar",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
sugar.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
sugarEntry.grid(row=4,column=1,padx=10,pady=9)
sugarEntry.insert(0,0)

Tea=Label(groceryFrame,text="Tea",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Tea.grid(row=5,column=0,pady=9,padx=10,sticky='w')

TeaEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,border=7)
TeaEntry.grid(row=5,column=1,padx=10,pady=9)
TeaEntry.insert(0,0)

cooldrinksFrame=LabelFrame(productsFrame,text="Cold Drinks",font=("times new roman",15,'bold'),fg='yellow',bg='Hotpink4',relief=GROOVE,bd=6)
cooldrinksFrame.grid(row=0,column=2)
 
Maaza=Label(cooldrinksFrame,text="Maaza",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Maaza.grid(row=0,column=0,pady=9,padx=10,sticky='w')

MaazaEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
MaazaEntry.grid(row=0,column=1,padx=10,pady=9)
MaazaEntry.insert(0,0)

pepsi=Label(cooldrinksFrame,text="Pepsi",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
pepsi.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
pepsiEntry.grid(row=1,column=1,padx=10,pady=9)
pepsiEntry.insert(0,0)

Sprite=Label(cooldrinksFrame,text="Sprite",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Sprite.grid(row=2,column=0,pady=9,padx=10,sticky='w')


SpriteEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
SpriteEntry.grid(row=2,column=1,padx=10,pady=9)
SpriteEntry.insert(0,0)

Thumsup=Label(cooldrinksFrame,text="Thumsup",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Thumsup.grid(row=3,column=0,pady=9,padx=10,sticky='w')

ThumsupEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
ThumsupEntry.grid(row=3,column=1,padx=10,pady=9)
ThumsupEntry.insert(0,0)

Frooti=Label(cooldrinksFrame,text="Frooti",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Frooti.grid(row=4,column=0,pady=9,padx=10,sticky='w')

FrootiEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
FrootiEntry.grid(row=4,column=1,padx=10,pady=9)
FrootiEntry.insert(0,0)

Cocacola=Label(cooldrinksFrame,text="Coca cola",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Cocacola.grid(row=5,column=0,pady=9,padx=10,sticky='w')

CocacolaEntry=Entry(cooldrinksFrame,font=("times new roman",15,'bold'),width=10,border=7)
CocacolaEntry.grid(row=5,column=1,padx=10,pady=9)
CocacolaEntry.insert(0,0)

billarea=Frame(productsFrame,bd=7,relief=GROOVE)
billarea.grid(row=0,column=3)

billarealabel=Label(billarea,text="Bill Area",font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billarea,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billarea,height=20,width=88,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

BillmenuFrame=LabelFrame(root,text="Cold Drinks",font=("times new roman",15,'bold'),fg='yellow',bg='Hotpink4',relief=GROOVE,bd=6)
BillmenuFrame.pack(pady=10,fill=X)

Cosmeticprice=Label(BillmenuFrame,text="Cosmetic Price",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
Cosmeticprice.grid(row=0,column=0,pady=9,padx=20,sticky='w')

CosmeticpriceEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
CosmeticpriceEntry.grid(row=0,column=1,padx=20,pady=9)
#CosmeticpriceEntry.insert(0,0)

groceryprice=Label(BillmenuFrame,text="Grocery Price",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
groceryprice.grid(row=1,column=0,pady=9,padx=20,sticky='w')

GrocerypriceEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
GrocerypriceEntry.grid(row=1,column=1,padx=20,pady=9)
#GrocerypriceEntry.insert(0,0)

cooldrinkprice=Label(BillmenuFrame,text="cooldrink Price",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
cooldrinkprice.grid(row=2,column=0,pady=9,padx=20,sticky='w')

cooldrinkpriceEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
cooldrinkpriceEntry.grid(row=2,column=1,padx=20,pady=9)
#cooldrinkpriceEntry.insert(0,0)

cosmetictax=Label(BillmenuFrame,text="Cosmetic Tax",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
cosmetictax.grid(row=0,column=2,pady=9,padx=20,sticky='w')

cosmetictaxEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
cosmetictaxEntry.grid(row=0,column=3,padx=20,pady=9)
#cosmetictaxEntry.insert(0,0)

grocerytax=Label(BillmenuFrame,text="Grocery Tax",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
grocerytax.grid(row=1,column=2,pady=9,padx=20,sticky='w')

grocerytaxEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
grocerytaxEntry.grid(row=1,column=3,padx=20,pady=9)
#grocerytaxEntry.insert(0,0)

cooldrinktax=Label(BillmenuFrame,text="Cooldrink Tax",font=('arial',13,'bold'),fg='white',bg='Hotpink4')
cooldrinktax.grid(row=2,column=2,pady=9,padx=20,sticky='w')

cooldrinktaxEntry=Entry(BillmenuFrame,font=("times new roman",15,'bold'),width=10,border=7)
cooldrinktaxEntry.grid(row=2,column=3,padx=20,pady=9)
#cooldrinktaxEntry.insert(0,0)

buttonFrame=Frame(BillmenuFrame,bd=7,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text="Total",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text="Bill",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text="Email",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=sendmail)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text="Print",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=printbilling)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text="Clear",font=("arial",15,'bold'),bg='Hotpink4',fg='white',bd=5,width=8,padx=27,pady=10,command=clearall)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()
