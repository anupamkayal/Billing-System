from tkinter  import *
from tkinter import messagebox
import time
from datetime import date,datetime
import keyboard
import random
from tkinter import filedialog
from fpdf import FPDF
import os
import errno
import unicodedata
import os.path
from plyer import notification

class Bill:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry('1400x1200+0+0')
		self.root.wm_iconbitmap('bill_icon.ico')	
		self.root.overrideredirect(0)
		keyboard.add_hotkey('esc', lambda : self.root.destroy())
		self.root.title("Billing software")
		self.root.configure(bg="black")
		heading=Label(self.root,text='Billing system',bg="#074463",fg='yellow',font=("times new roman", 35 ,"bold"),bd=4,relief=GROOVE,pady=2)
		heading.pack(side=TOP,fill=X)
		self.date=Label(self.root,font=("arial",30),justify=LEFT,fg="red",bg="#074463")
		self.date.place(x=15,y=7,width=300,height=52)
		self.datefunc()
		self.clock=Label(self.root,font=("Arial" ,30),justify=RIGHT,fg="red",bg="#074463")
		self.clock.place(x=1000,y=5,width=300,height=52)
		self.clockfunc()
		#lable frame
		userfrom=LabelFrame(self.root,text='Customer Details',font=("times new roman", 15, "bold"),bd=5,relief=GROOVE,bg="#074463",fg="yellow")
		userfrom.place(x=0,y=65,height=100,width=1376)
		cosmetics=LabelFrame(self.root,text="Cosmetics",font=("times new roman", 15, "bold"),bd=5,relief=GROOVE,bg="#074463",fg="yellow")
		cosmetics.place(x=0,y=165,height=380,width=325)
		grocery=LabelFrame(self.root,text="Grocery",font=("times new roman", 15, "bold"),bd=5,relief=GROOVE,bg="#074463",fg="yellow")
		grocery.place(x=330,y=165,height=380,width=325)
		cold_drinks=LabelFrame(self.root,text="Cold Drinks",font=("times new roman", 15, "bold"),bd=5,relief=GROOVE,bg="#074463",fg="yellow")
		cold_drinks.place(x=660,y=165,height=380,width=325)
		billing_menu=LabelFrame(self.root,text="Billing Menu",font=("times new roman", 15, "bold"),bd=5,relief=GROOVE,bg="#074463",fg="yellow")
		billing_menu.place(x=0,y=550,height=200,width=1376)
		
		#frame
		billframe=Frame(self.root,bd=5,relief=GROOVE)
		billframe.place(x=990,y=165,height=380,width=375)
		buttonframe=Frame(billing_menu,bd=7,relief=GROOVE,bg='#074463')
		buttonframe.place(x=680,y=0,height=130,width=640)
	
		#variable
		self.custdata=StringVar()
		self.custphone=StringVar()
		self.billdata=StringVar()

		self.soapdata=IntVar()
		self.sanitizer=IntVar()
		self.facecreamvar=IntVar()
		self.facewashvar=IntVar()
		self.hairsprayvar=IntVar()
		self.hairgelvar=IntVar()
		self.bodysprayvar=IntVar()

		self.ricevar=IntVar()
		self.oilvar=IntVar()
		self.wheatvar=IntVar()
		self.dalvar=IntVar()
		self.sugarvar=IntVar()
		self.saltvar=IntVar()
		self.teavar=IntVar()

		self.mazavar=IntVar()
		self.cocacolavar=IntVar()
		self.spritevar=IntVar()
		self.railneervar=IntVar()
		self.frootivar=IntVar()
		self.limcavar=IntVar()
		self.thansupvar=IntVar()

		self.totalcosmetics_pricevar=StringVar()
		self.totalgrocery_pricevar=StringVar()
		self.totalcolddrinks_pricevar=StringVar()

		self.cosmetics_gstvar=StringVar()
		self.grocery_gstvar=StringVar()
		self.colddrinks_gstvar=StringVar()
		self.cosmetics_gstvar.set(value="5%")
		self.grocery_gstvar.set(value="5%")
		self.colddrinks_gstvar.set(value="18%")
		
		self.soapprice=StringVar()
		self.soapprice.set(value="30")
		self.sanitizerprice=StringVar()
		self.sanitizerprice.set(value="60")
		self.facecreamprice=StringVar()
		self.facecreamprice.set(value="40")
		self.facewashprice=StringVar()
		self.facewashprice.set(value='30')
		self.hairsprayprice=StringVar()
		self.hairsprayprice.set(value='30')
		self.hairgelprice=StringVar()
		self.hairgelprice.set(value='20')
		self.bodysprayprice=StringVar()
		self.bodysprayprice.set(value='150')

		self.riceprice=StringVar()
		self.riceprice.set(value='46')
		self.oilprice=StringVar()
		self.oilprice.set(value='62')
		self.wheatprice=StringVar()
		self.wheatprice.set(value='30')
		self.dalprice=StringVar()
		self.dalprice.set(value='42')
		self.sugarprice=StringVar()
		self.sugarprice.set(value='40')
		self.saltprice=StringVar()
		self.saltprice.set(value='15')
		self.teaprice=StringVar()
		self.teaprice.set(value='10')

		self.mazaprice=StringVar()
		self.mazaprice.set(value='35')
		self.cocacolaprice=StringVar()
		self.cocacolaprice.set(value='40')
		self.spriteprice=StringVar()
		self.spriteprice.set(value='45')
		self.railneerprice=StringVar()
		self.railneerprice.set(value='15')
		self.frootiprice=StringVar()
		self.frootiprice.set(value='30')
		self.limcaprice=StringVar()
		self.limcaprice.set(value='35')
		self.thansupprice=StringVar()
		self.thansupprice.set(value='45')

		#lable
		Customer_name=Label(userfrom,text="Customer Name :",font="Helvetica 15 italic",fg="lightgreen",bg="#074463")
		Customer_name.place(x=20,y=20)
		Custome_ph=Label(userfrom,text="Customer phone No.",font="Helvetica 15 italic",fg="lightgreen",bg="#074463")
		Custome_ph.place(x=450,y=20)
		Billing_no=Label(userfrom,text="Billing No:",font="Helvetica 15 italic",fg="lightgreen",bg="#074463")
		Billing_no.place(x=900,y=20)
		#cosmetics
		soap=Label(cosmetics,text="Bath Soap:",font="Helvetica 13 bold",fg="light green",bg="#074463")
		soap.place(x=0,y=20)
		sanitizer=Label(cosmetics,text="Hand sanitizers :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		sanitizer.place(x=0,y=70)
		facecream=Label(cosmetics,text="Face Cream :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		facecream.place(x=0,y=120)
		facewash=Label(cosmetics,text="Face Wash :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		facewash.place(x=0,y=170)
		hairspray=Label(cosmetics,text="Hair Spray :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		hairspray.place(x=0,y=220)
		hairgel=Label(cosmetics,text="Hair Gel :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		hairgel.place(x=0,y=270)
		bodyspray=Label(cosmetics,text="Body Spray :",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		bodyspray.place(x=0,y=320)
		#grocery
		rice=Label(grocery,text="Rice:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		rice.place(x=0,y=20)
		oil=Label(grocery,text="Oil:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		oil.place(x=0,y=70)
		wheat=Label(grocery,text="wheat:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		wheat.place(x=0,y=120)
		Dal=Label(grocery,text="Dal:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		Dal.place(x=0,y=170)
		sugar=Label(grocery,text="Sugar:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		sugar.place(x=0,y=220)
		salt=Label(grocery,text="Salt:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		salt.place(x=0,y=270)
		tea=Label(grocery,text="Tea:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		tea.place(x=0,y=320)
		#cold drinks
		maza=Label(cold_drinks,text="Maza:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		maza.place(x=0,y=20)
		cocacola=Label(cold_drinks,text="Cocacola:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		cocacola.place(x=0,y=70)
		sprite=Label(cold_drinks,text="Sprite:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		sprite.place(x=0,y=120)
		railneer=Label(cold_drinks,text="RailNeer:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		railneer.place(x=0,y=170)
		frooti=Label(cold_drinks,text="Frooti:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		frooti.place(x=0,y=220)
		limca=Label(cold_drinks,text="Limca:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		limca.place(x=0,y=270)
		thansup=Label(cold_drinks,text="Thans Up:",font="Helvetica 13 bold",fg="lightgreen",bg="#074463")
		thansup.place(x=0,y=320)
		#frame heading
		bill_heading=Label(billframe,text="Bill Area",font=("arial",13,"bold"),bd=7,relief=GROOVE)
		bill_heading.pack(fill=X)

		#scrollbar & textarea
		scrollbar=Scrollbar(billframe,orient=VERTICAL)
		self.textarea=Text(billframe,yscrollcommand=scrollbar.set)
		scrollbar.config(command=self.textarea.yview)
		scrollbar.pack(side=RIGHT,fill=Y)
		self.textarea.pack(fill=BOTH,expand=True)

		#billmenu label
		cosmetics_price=Label(billing_menu,text="Total Cosmetics Price:",font="arial 13 bold",bg="#074463",fg='white')
		cosmetics_price.place(x=20,y=15)		
		grocery_price=Label(billing_menu,text="Total Grocery Price:",font="arial 13 bold",bg="#074463",fg='white')
		grocery_price.place(x=20,y=55)
		cold_drinks_price=Label(billing_menu,text="Total Cold Drinks Price:",font="arial 13 bold",bg="#074463",fg='white')
		cold_drinks_price.place(x=20,y=95)
		cosmetics_gst=Label(billing_menu,text="Cosmetics G.S.T",font="arial 13 bold",bg='#074463',fg="white")
		cosmetics_gst.place(x=400,y=15)
		cosmetics_gst=Label(billing_menu,text="Grocery G.S.T",font="arial 13 bold",bg='#074463',fg="white")
		cosmetics_gst.place(x=400,y=55)
		cosmetics_gst=Label(billing_menu,text="Cold Drinks G.S.T",font="arial 13 bold",bg='#074463',fg="white")
		cosmetics_gst.place(x=400,y=95)

		#qnt
		item=Label(cosmetics,text="Qty:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item.place(x=150,y=-10)
		item=Label(grocery,text="Qty:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item.place(x=100,y=-10)
		item=Label(cold_drinks,text="Qty:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item.place(x=100,y=-5)

		
		#PER PRICE LABEL
		item_price=Label(cosmetics,text="Item Price:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item_price.place(x=220,y=-10)
		item_price=Label(grocery,text="Item Price:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item_price.place(x=200,y=-10)
		item_price=Label(cold_drinks,text="Item Price:",font="arial 13 bold",bg="#074463",fg="lightgreen")
		item_price.place(x=200,y=-10)


		
		#entry
		Customer_entry=Entry(userfrom,textvariable=self.custdata,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		Customer_entry.place(x=200,y=20,height=28,width=209)
		Customer_entry.bind('<KeyRelease>',self.upper)
		Customerphone_entry=Entry(userfrom,textvariable=self.custphone,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		Customerphone_entry.place(x=650,y=20,height=28,width=205)
		bill_entry=Entry(userfrom,textvariable=self.billdata,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		bill_entry.place(x=1000,y=20,height=28,width=205)
		#cosmetics
		soap_entry=Entry(cosmetics,textvariable=self.soapdata,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		soap_entry.place(x=150,y=20,height=28,width=50)
		sanitizer_entry=Entry(cosmetics,textvariable=self.sanitizer,font=("arial",13,"bold"),bd=3,relief=SUNKEN,)
		sanitizer_entry.place(x=150,y=70,height=28,width=50)
		facecream_entry=Entry(cosmetics,textvariable=self.facecreamvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		facecream_entry.place(x=150,y=120,height=28,width=50)
		facewash_entry=Entry(cosmetics,textvariable=self.facewashvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		facewash_entry.place(x=150,y=170,height=28,width=50)
		hairspray_entry=Entry(cosmetics,textvariable=self.hairsprayvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		hairspray_entry.place(x=150,y=220,height=28,width=50)
		hairgel_entry=Entry(cosmetics,textvariable=self.hairgelvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		hairgel_entry.place(x=150,y=270,height=28,width=50)
		bodyspray_entry=Entry(cosmetics,textvariable=self.bodysprayvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		bodyspray_entry.place(x=150,y=320,height=28,width=50)

		#grocery
		rice_entry=Entry(grocery,textvariable=self.ricevar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		rice_entry.place(x=100,y=20,height=28,width=50)
		oil_entry=Entry(grocery,textvariable=self.oilvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		oil_entry.place(x=100,y=70,height=28,width=50)
		wheat_entry=Entry(grocery,textvariable=self.wheatvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		wheat_entry.place(x=100,y=120,height=28,width=50)
		dal_entry=Entry(grocery,textvariable=self.dalvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		dal_entry.place(x=100,y=170,height=28,width=50)
		sugar_entry=Entry(grocery,textvariable=self.sugarvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		sugar_entry.place(x=100,y=220,height=28,width=50)
		salt_entry=Entry(grocery,textvariable=self.saltvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		salt_entry.place(x=100,y=270,height=28,width=50)
		tea_entry=Entry(grocery,textvariable=self.teavar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		tea_entry.place(x=100,y=320,height=28,width=50)
		
		#cold drinks
		maza_entry=Entry(cold_drinks,textvariable=self.mazavar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		maza_entry.place(x=100,y=20,height=28,width=50)
		cocacola_entry=Entry(cold_drinks,textvariable=self.cocacolavar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		cocacola_entry.place(x=100,y=70,height=28,width=50)
		sprite_entry=Entry(cold_drinks,textvariable=self.spritevar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		sprite_entry.place(x=100,y=120,height=28,width=50)
		railneer_entry=Entry(cold_drinks,textvariable=self.railneervar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		railneer_entry.place(x=100,y=170,height=28,width=50)
		frooti_entry=Entry(cold_drinks,textvariable=self.frootivar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		frooti_entry.place(x=100,y=220,height=28,width=50)
		limca_entry=Entry(cold_drinks,textvariable=self.limcavar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		limca_entry.place(x=100,y=270,height=28,width=50)
		thansup_entry=Entry(cold_drinks,textvariable=self.thansupvar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		thansup_entry.place(x=100,y=320,height=28,width=50)

		#bill menu entry
		
		cosmetics_price_entry=Entry(billing_menu,textvariable=self.totalcosmetics_pricevar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		cosmetics_price_entry.place(x=250,y=15,height=28,width=120)
		grocery_price_entry=Entry(billing_menu,textvariable=self.totalgrocery_pricevar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		grocery_price_entry.place(x=250,y=55,height=28,width=120)
		colddrinks_price_entry=Entry(billing_menu,textvariable=self.totalcolddrinks_pricevar,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		colddrinks_price_entry.place(x=250,y=95,height=28,width=120)

		cosmetics_gst_entry=Entry(billing_menu,textvariable=self.cosmetics_gstvar,font=("arial",13,"bold"),state="readonly",cursor="no",bd=3,relief=SUNKEN)
		cosmetics_gst_entry.place(x=550,y=15,height=28,width=120)
		grocery_gst_entry=Entry(billing_menu,textvariable=self.grocery_gstvar,font=("arial",13,"bold"),state="readonly",cursor="no",bd=3,relief=SUNKEN)
		grocery_gst_entry.place(x=550,y=55,height=28,width=120)
		colddrinks_gst_entry=Entry(billing_menu,textvariable=self.colddrinks_gstvar,state="readonly",cursor="no",font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		colddrinks_gst_entry.place(x=550,y=95,height=28,width=120)

		#
		self.soap_price=Entry(cosmetics,textvariable=self.soapprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.soap_price.place(x=235,y=18,height=28,width=50)
		self.soap_price.bind("<Button-1>",self.warning)
		self.sanitizer_price=Entry(cosmetics,textvariable=self.sanitizerprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.sanitizer_price.place(x=235,y=70,height=28,width=50)
		self.sanitizer_price.bind("<Button-1>",self.warning)
		self.facecream_price=Entry(cosmetics,textvariable=self.facecreamprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.facecream_price.place(x=235,y=120,height=28,width=50)
		self.facecream_price.bind("<Button-1>",self.warning)
		self.facewash_price=Entry(cosmetics,textvariable=self.facewashprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.facewash_price.place(x=235,y=170,height=28,width=50)
		self.facewash_price.bind("<Button-1>",self.warning)
		self.hairspray_price=Entry(cosmetics,textvariable=self.hairsprayprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.hairspray_price.place(x=235,y=220,height=28,width=50)
		self.hairspray_price.bind("<Button-1>",self.warning)
		self.hairgel_price=Entry(cosmetics,textvariable=self.hairgelprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.hairgel_price.place(x=235,y=270,height=28,width=50)
		self.hairgel_price.bind("<Button-1>",self.warning)
		self.bodyspray_price=Entry(cosmetics,textvariable=self.bodysprayprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.bodyspray_price.place(x=235,y=320,height=28,width=50)
		self.bodyspray_price.bind("<Button-1>",self.warning)

		self.rice_price=Entry(grocery,textvariable=self.riceprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.rice_price.place(x=215,y=20,height=28,width=50)
		self.rice_price.bind("<Button-1>",self.warning)
		self.oil_price=Entry(grocery,textvariable=self.oilprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.oil_price.place(x=215,y=70,height=28,width=50)
		self.oil_price.bind("<Button-1>",self.warning)
		self.wheat_price=Entry(grocery,textvariable=self.wheatprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.wheat_price.place(x=215,y=120,height=28,width=50)
		self.wheat_price.bind("<Button-1>",self.warning)		
		self.dal_price=Entry(grocery,textvariable=self.dalprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.dal_price.place(x=215,y=170,height=28,width=50)
		self.dal_price.bind("<Button-1>",self.warning)		
		self.sugar_price=Entry(grocery,textvariable=self.sugarprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.sugar_price.place(x=215,y=220,height=28,width=50)
		self.sugar_price.bind("<Button-1>",self.warning)		
		self.salt_price=Entry(grocery,textvariable=self.saltprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.salt_price.place(x=215,y=270,height=28,width=50)
		self.salt_price.bind("<Button-1>",self.warning)		
		self.tea_price=Entry(grocery,textvariable=self.teaprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.tea_price.place(x=215,y=320,height=28,width=50)
		self.tea_price.bind("<Button-1>",self.warning)
		self.maza_price=Entry(cold_drinks,textvariable=self.mazaprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.maza_price.place(x=215,y=20,height=28,width=50)
		self.maza_price.bind("<Button-1>",self.warning)
		self.cocacola_price=Entry(cold_drinks,textvariable=self.cocacolaprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.cocacola_price.place(x=215,y=70,height=28,width=50)
		self.cocacola_price.bind("<Button-1>",self.warning)
		self.sprite_price=Entry(cold_drinks,textvariable=self.spriteprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.sprite_price.place(x=215,y=120,height=28,width=50)
		self.sprite_price.bind("<Button-1>",self.warning)
		self.railneer_price=Entry(cold_drinks,textvariable=self.railneerprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.railneer_price.place(x=215,y=170,height=28,width=50)
		self.railneer_price.bind("<Button-1>",self.warning)	
		self.frooti_price=Entry(cold_drinks,textvariable=self.frootiprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.frooti_price.place(x=215,y=220,height=28,width=50)
		self.frooti_price.bind("<Button-1>",self.warning)
		self.limca_price=Entry(cold_drinks,textvariable=self.limcaprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.limca_price.place(x=215,y=270,height=28,width=50)
		self.limca_price.bind("<Button-1>",self.warning)
		self.thansup_price=Entry(cold_drinks,textvariable=self.thansupprice,font=("arial",13,"bold"),bd=3,relief=SUNKEN)
		self.thansup_price.place(x=215,y=320,height=28,width=50)
		self.thansup_price.bind("<Button-1>",self.warning)
		
		
		
		
		
		
		




		#button
		search=Button(userfrom,text="Search",command=self.find,font=("Helvetica",13,"italic"),cursor="hand2")
		search.place(x=1230,y=20,height=28,width=64)
		total=Button(buttonframe,text="Total",command=self.totalfunc,font=('arial',13,"bold"),cursor="hand2")
		total.place(x=10,y=30,height=55,width=140)
		genarate_btn=Button(buttonframe,text="Genarate Bill",command=self.billtotal,font=('arial',13,"bold"),cursor="hand2")
		genarate_btn.place(x=160,y=30,height=55,width=140)
		clear=Button(buttonframe,text="Clear",command=self.clearfunc,font=('arial',13,"bold"),cursor="hand2")
		clear.place(x=320,y=30,height=55,width=140)
		exit=Button(buttonframe,text="Exit",command=self.exitfunc,font=('arial',13,"bold"),cursor="hand2")
		exit.place(x=477,y=30,height=55,width=140)
		self.file_create()
		self.billdisplay()
		url=''
		self.ran=random.randint(1000,9999)

		
	
	

	def file_create(self):
		folder=os.path.isdir('D:\\Customer Bill\\txt')
		if folder==True:
			return
		else:
			try:
				os.makedirs('D:\\Customer Bill\\txt')
			except OSError as error:
				if error.errno !=errno.EEXIST:
					raise	
		
  
	def upper(self,event):
		self.custdata.set(self.custdata.get().upper())

	def warning(self,event):
		messagebox.showwarning("warning"," only admin can change the Price value")
		obj=messagebox.askyesno("warning","Do you want to change the Price value")
		if obj==1:
					
			self.soap_price.focus_set()
			self.soap_price.configure(state="normal")
			self.soapprice.set(value=self.soapprice.get())
			self.sanitizer_price.focus_set()
			self.sanitizer_price.configure(state="normal")
			self.sanitizerprice.set(self.sanitizerprice.get())
			self.facecream_price.focus_set()
			self.facecream_price.configure(state="normal")
			self.facecreamprice.set(self.facecreamprice.get())		
			self.facewash_price.focus_set()	
			self.facewash_price.configure(state="normal")
			self.facewashprice.set(self.facewashprice.get())			
			self.hairspray_price.focus_set()
			self.hairspray_price.configure(state="normal")
			self.hairsprayprice.set(self.hairsprayprice.get())		
			self.hairgel_price.focus_set()
			self.hairgel_price.configure(state="normal")
			self.hairgelprice.set(self.hairgelprice.get())			
			self.bodyspray_price.focus_set()
			self.bodyspray_price.configure(state="normal")
			self.bodysprayprice.set(self.bodysprayprice.get())
			self.rice_price.focus_set()
			self.rice_price.configure(state="normal")
			self.riceprice.set(self.riceprice.get())			
			self.oil_price.focus_set()
			self.oil_price.configure(state="normal")
			self.oilprice.set(self.oilprice.get())			
			self.wheat_price.focus_set()
			self.wheat_price.configure(state="normal")
			self.wheatprice.set(self.wheatprice.get())			
			self.dal_price.focus_set()
			self.dal_price.configure(state="normal")
			self.dalprice.set(self.dalprice.get())			
			self.sugar_price.focus_set()
			self.sugar_price.configure(state="normal")
			self.sugarprice.set(value=self.sugarprice.get())
			self.salt_price.focus_set()
			self.salt_price.configure(state="normal")
			self.saltprice.set(value=self.saltprice.get())
			self.tea_price.focus_set()
			self.tea_price.configure(state="normal")
			self.teaprice.set(value=self.teaprice.get())
			self.maza_price.focus_set()
			self.maza_price.configure(state="normal")
			self.mazaprice.set(value=self.mazaprice.get())
			self.cocacola_price.focus_set()
			self.cocacola_price.configure(state="normal")
			self.cocacolaprice.set(value=self.cocacolaprice.get())
			self.sprite_price.focus_set()
			self.sprite_price.configure(state="normal")
			self.spriteprice.set(value=self.spriteprice.get())
			self.railneer_price.focus_set()
			self.railneer_price.configure(state="normal")
			self.railneerprice.set(value=self.railneerprice.get())
			self.frooti_price.focus_set()
			self.frooti_price.configure(state="normal")
			self.frootiprice.set(value=self.frootiprice.get())
			self.limca_price.focus_set()
			self.limca_price.configure(state="normal")
			self.limcaprice.set(value=self.limcaprice.get())
			self.thansup_price.focus_set()
			self.thansup_price.configure(state="normal")
			self.thansupprice.set(value=self.thansupprice.get())



		else:
			self.soap_price.configure(state="readonly",cursor="no")
			self.sanitizer_price.configure(state="readonly",cursor="no")		
			self.facecream_price.configure(state="readonly",cursor="no")
			self.facewash_price.configure(state="readonly",cursor="no")
			self.hairspray_price.configure(state="readonly",cursor="no")
			self.hairgel_price.configure(state="readonly",cursor="no")
			self.bodyspray_price.configure(state="readonly",cursor="no")
			self.rice_price.configure(state="readonly",cursor="no")
			self.oil_price.configure(state="readonly",cursor="no")
			self.wheat_price.configure(state="readonly",cursor="no")
			self.dal_price.configure(state="readonly",cursor="no")
			self.sugar_price.configure(state="readonly",cursor="no")
			self.salt_price.configure(state="readonly",cursor="no")
			self.tea_price.configure(state="readonly",cursor="no")
			self.maza_price.configure(state="readonly",cursor="no")
			self.cocacola_price.configure(state="readonly",cursor="no")
			self.sprite_price.configure(state="readonly",cursor="no")
			self.railneer_price.configure(state="readonly",cursor="no")
			self.frooti_price.configure(state="readonly",cursor="no")
			self.limca_price.configure(state="readonly",cursor="no")
			self.thansup_price.configure(state="readonly",cursor="no")

	def clockfunc(self):
		self.current_time=time.strftime("%I:%M:%S")
		self.clock["text"]=self.current_time
		self.clock.after(1000,self.clockfunc)

	def datefunc(self):
		current_date=date.today().strftime("%d/%m/%y")
		self.date["text"]=current_date
	def totalfunc(self):

		
		soap=(round((105/100)*self.soapdata.get()*int(self.soapprice.get())))
		sanitizer=(round((105/100)*self.sanitizer.get()*int(self.sanitizerprice.get())))
		facecream=(round((105/100)*self.facecreamvar.get()*int(self.facecreamprice.get())))
		facewash=round((105/100)*self.facewashvar.get()*int(self.facewashprice.get()))
		hairspray=round((105/100)*self.hairsprayvar.get()*int(self.hairsprayprice.get()))
		hairgel=round((105/100)*self.hairgelvar.get()*int(self.hairgelprice.get()))
		bodyspray=round((105/100)*self.bodysprayvar.get()*int(self.bodysprayprice.get()))


		cosmetics=(soap+sanitizer+facecream+facewash+hairspray+hairgel+bodyspray)
		
		cosmetics_total=str(round(cosmetics))
		self.totalcosmetics_pricevar.set(cosmetics_total)

		#grocery
		

		rice=round((105/100)*self.ricevar.get()*int(self.riceprice.get()))
		oil=round((105/100)*self.oilvar.get()*int(self.oilprice.get()))
		wheat=round((105/100)*self.wheatvar.get()*int(self.wheatprice.get()))
		dal=round((105/100)*self.dalvar.get()*int(self.dalprice.get()))
		sugar=round((105/100)*self.sugarvar.get()*int(self.sugarprice.get()))
		salt=round((105/100)*self.saltvar.get()*int(self.saltprice.get()))
		tea=round((105/100)*self.teavar.get()*int(self.teaprice.get()))

		grocery=(rice+oil+wheat+dal+sugar+salt+tea)
		
		grocery_total=str(round(grocery))
		self.totalgrocery_pricevar.set(grocery_total)

		#cold drinks
		
	
		maza=round((118/100)*self.mazavar.get()*int(self.mazaprice.get()))
		cocacola=round((118/100)*self.cocacolavar.get()*int(self.cocacolaprice.get()))
		sprite=round((118/100)*self.spritevar.get()*int(self.spriteprice.get()))
		railneer=round((118/100)*self.railneervar.get()*int(self.railneerprice.get()))
		froti=round((118/100)*self.frootivar.get()*int(self.frootiprice.get()))
		limca=round((118/100)*self.limcavar.get()*int(self.limcaprice.get()))
		thansup=round((118/100)*self.thansupvar.get()*int(self.thansupprice.get()))

		colddrinks=(maza+cocacola+sprite+railneer+froti+limca+thansup)
		colddrinks_total=str(round(colddrinks))
		self.totalcolddrinks_pricevar.set(colddrinks_total)

		

		all_total=(cosmetics+grocery+colddrinks)
		display_alltotal=str(round(all_total))
		messagebox.showinfo("Total",f"Total cost: {display_alltotal}")

	
		
	def billdisplay(self):	
		self.textarea.delete(1.0,END)		
		self.textarea.insert(index=END, chars="\t     Kayal private Ltd.")
		self.textarea.insert(index=END, chars="\n\t     110 Roking Avenue")
		self.textarea.insert(index=END, chars="\n\t     Kolkata-700144")
		self.textarea.insert(index=END, chars="\n\t      West Bengal ")
		self.textarea.insert(index=END, chars="\n\t   Phone No. +919851447523")
		self.textarea.insert(index=END, chars="\n\t   G.S.T No. : Gst542143")
		self.textarea.insert(index=END, chars="\n\t\tTAX INVOICE")
		self.textarea.insert(index=END, chars="\n----------------------------------------")
		self.textarea.insert(index=END, chars=f"\nBill No:  ")		
		self.textarea.insert(index=END, chars=f"\nCustomer Name. :{self.custdata.get()}")
		self.textarea.insert(index=END, chars=f"\nCustomer Ph. :{self.custphone.get()}")	
		self.textarea.insert(index=END, chars="\n----------------------------------------")		
		self.textarea.insert(index=END, chars="\nProduct \t\tQtn\tG.S.T\tPrice")
		self.textarea.insert(index=END, chars="\n----------------------------------------")
	def billtime(self):
		self.textarea.delete(1.0,END)
		current_date=date.today().strftime("%d-%b-%Y")
		now=datetime.now()
		current_time=now.strftime("%I:%M %p")
		
		
		self.textarea.insert(index=END, chars="\t     Kayal private Ltd.")
		self.textarea.insert(index=END, chars="\n\t     110 Roking Avenue")
		self.textarea.insert(index=END, chars="\n\t     Kolkata-700144")
		self.textarea.insert(index=END, chars="\n\t      West Bengal ")
		self.textarea.insert(index=END, chars="\n\t   Phone No. +919851447523")
		self.textarea.insert(index=END, chars="\n\t   G.S.T No. : Gst542143")
		self.textarea.insert(index=END, chars="\n\t\tTAX INVOICE")
		self.textarea.insert(index=END, chars="\n----------------------------------------")
		self.textarea.insert(index=END, chars=f"\nBill No: {self.ran}\t\t  {current_date}  {current_time} ")		
		self.textarea.insert(index=END, chars=f"\nCustomer Name.: {self.custdata.get()}")
		self.textarea.insert(index=END, chars=f"\nCustomer Ph.: {self.custphone.get()}")	
		self.textarea.insert(index=END, chars="\n----------------------------------------")		
		self.textarea.insert(index=END, chars="\nProduct\t\tQtn\tG.S.T\tPrice")
		
	

	
	def billfunc(self):
		self.billtime()
		self.textarea.insert(index=END, chars="\n----------------------------------------")
		if self.soapdata.get()!=0:
			self.textarea.insert(index=END, chars=f'\nsoap\t\t{self.soapdata.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.soapdata.get()*int(self.soapprice.get()))}')
		if self.sanitizer.get()!=0:
			self.textarea.insert(index=END, chars=f'\nHand Sanitizer\t\t{self.sanitizer.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.sanitizer.get()*int(self.sanitizerprice.get()))}')
		if self.facecreamvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nFace Cream\t\t{self.facecreamvar.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.facecreamvar.get()*int(self.facecreamprice.get()))}')
		if self.facewashvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nFace Wash\t\t{self.facewashvar.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.facewashvar.get()*int(self.facewashprice.get()))}')
		if self.hairsprayvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nHair Spray\t\t{self.hairsprayvar.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.hairsprayvar.get()*int(self.hairsprayprice.get()))}')
		if self.hairgelvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nHair Gel\t\t{self.hairgelvar.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.hairgelvar.get()*int(self.hairgelprice.get()))}')			
		if self.bodysprayvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nBody Spray\t\t{self.bodysprayvar.get()}\t{self.cosmetics_gstvar.get()}\t{round((105/100)*self.bodysprayvar.get()*int(self.bodysprayprice.get()))}')		
		if self.ricevar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nRice\t\t{self.ricevar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.ricevar.get()*int(self.riceprice.get()))}')
		if self.oilvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nOil\t\t{self.oilvar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.oilvar.get()*int(self.oilprice.get()))}')
		if self.wheatvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nWheat\t\t{self.wheatvar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.wheatvar.get()*int(self.wheatprice.get()))}')
		if self.dalvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nDal\t\t{self.dalvar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.dalvar.get()*int(self.dalprice.get()))}')
		if self.sugarvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nSugar\t\t{self.sugarvar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.sugarvar.get()*int(self.sugarprice.get()))}')
		if self.saltvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nSalt\t\t{self.saltvar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.saltvar.get()*int(self.saltprice.get()))}')
		if self.teavar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nTea\t\t{self.teavar.get()}\t{self.grocery_gstvar.get()}\t{round((105/100)*self.teavar.get()*int(self.teaprice.get()))}')
		if self.mazavar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nMaza\t\t{self.mazavar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.mazavar.get()*int(self.mazaprice.get()))}')
		if self.cocacolavar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nCocacola\t\t{self.cocacolavar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.cocacolavar.get()*int(self.cocacolaprice.get()))}')
		if self.spritevar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nSprite\t\t{self.spritevar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.spritevar.get()*int(self.spriteprice.get()))}')
		if self.railneervar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nRailneer\t\t{self.railneervar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.railneervar.get()*int(self.railneerprice.get()))}')
		if self.frootivar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nFrooti\t\t{self.frootivar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.frootivar.get()*int(self.frootiprice.get()))}')
		if self.limcavar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nLimca\t\t{self.limcavar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.limcavar.get()*int(self.limcaprice.get()))}')
		if self.thansupvar.get()!=0:
			self.textarea.insert(index=END, chars=f'\nThansup\t\t{self.thansupvar.get()}\t{self.colddrinks_gstvar.get()}\t{round((118/100)*self.thansupvar.get()*int(self.thansupprice.get()))}')
		
	def billtotal(self):
		custname=self.custdata.get()
		custph=self.custphone.get()
		soapdata=self.soapdata.get()
		sanitizerdata=self.sanitizer.get()
		facecreamdata=self.facecreamvar.get()
		facewashdata=self.facewashvar.get()
		hairspraydata=self.hairsprayvar.get()		
		hairgeldata=self.hairgelvar.get()
		bodyspraydata=self.bodysprayvar.get()
		ricedata=self.ricevar.get()
		oildata=self.oilvar.get()
		wheatdata=self.wheatvar.get()
		daldata=self.dalvar.get()
		sugardata=self.sugarvar.get()
		saltdata=self.saltvar.get()
		teadata=self.teavar.get()
		mazadata=self.mazavar.get()
		cocacoladata=self.cocacolavar.get()
		spritedata=self.spritevar.get()
		railneerdata=self.railneervar.get()
		frootidata=self.frootivar.get()
		limcadata=self.limcavar.get()
		thansupdata=self.thansupvar.get()

		if 	custname=="" and custph=="":
			messagebox.showerror("Error","Enter Customer Name & Phone No.")
		else:	
			if soapdata==0 and sanitizerdata==0 and facecreamdata==0 and facewashdata==0 and hairspraydata==0 and hairgeldata==0 and bodyspraydata==0 and ricedata==0 and oildata==0 and wheatdata==0 and daldata==0 and sugardata==0 and saltdata==0 and teadata==0 and mazadata==0 and cocacoladata==0 and spritedata==0 and railneerdata==0 and frootidata==0 and limcadata==0 and thansupdata==0:
				messagebox.showerror('Error',"Fill atlast one box")
			else:
			
				self.billfunc()
				
				#cosmetics
				subsoap=self.soapdata.get()*int(self.soapprice.get())
				subsanitizer=self.sanitizer.get()*int(self.sanitizerprice.get())
				subfacecream=self.facecreamvar.get()*int(self.facecreamprice.get())
				subfacewash=self.facewashvar.get()*int(self.facewashprice.get())
				subhairspray=self.hairsprayvar.get()*int(self.hairsprayprice.get())
				subhairgel=self.hairgelvar.get()*int(self.hairgelprice.get())
				subbodyspray=self.bodysprayvar.get()*int(self.bodysprayprice.get())

				subtotal_cosmetic=(subsoap+subsanitizer+subfacecream+subfacewash+subhairgel+subbodyspray)

				#grocery
				subrice=self.ricevar.get()*int(self.riceprice.get())
				suboil=self.oilvar.get()*int(self.oilprice.get())
				subwheat=self.wheatvar.get()*int(self.wheatprice.get())
				subdal=self.dalvar.get()*int(self.dalprice.get())
				subsugar=self.sugarvar.get()*int(self.sugarprice.get())
				subsalt=self.saltvar.get()*int(self.saltprice.get())
				subtea=self.teavar.get()*int(self.teaprice.get())

				subtotal_grocery=(subrice+suboil+subwheat+subdal+subsugar+subsalt+subtea)

				#cold drinks
				submaza=self.mazavar.get()*int(self.mazaprice.get())
				subcocacola=self.cocacolavar.get()*int(self.cocacolaprice.get())
				subsprite=self.spritevar.get()*int(self.spriteprice.get())
				subrailneer=self.railneervar.get()*int(self.railneerprice.get())
				subfrooti=self.frootivar.get()*int(self.frootiprice.get())
				sublimca=self.limcavar.get()*int(self.limcaprice.get())
				subthansup=self.limcavar.get()*int(self.limcaprice.get())

				subtotal_colddrinks=(submaza+subcocacola+subsprite+subrailneer+subfrooti+sublimca+subthansup)

				#sub total
				sub_total=(float(subtotal_cosmetic+subtotal_grocery+subtotal_colddrinks))


				#Grand Total	
				soap=(round((105/100)*self.soapdata.get()*int(self.soapprice.get())))
				sanitizer=(round((105/100)*self.sanitizer.get()*int(self.sanitizerprice.get())))
				facecream=(round((105/100)*self.facecreamvar.get()*int(self.facecreamprice.get())))
				facewash=round((105/100)*self.facewashvar.get()*int(self.facewashprice.get()))
				hairspray=round((105/100)*self.hairsprayvar.get()*int(self.hairsprayprice.get()))
				hairgel=round((105/100)*self.hairgelvar.get()*int(self.hairgelprice.get()))
				bodyspray=round((105/100)*self.bodysprayvar.get()*int(self.bodysprayprice.get()))


				cosmetics=(soap+sanitizer+facecream+facewash+hairspray+hairgel+bodyspray)
		
				cosmetics_total=str(round(cosmetics))
				self.totalcosmetics_pricevar.set(cosmetics_total)

				#grocery
		

				rice=round((105/100)*self.ricevar.get()*int(self.riceprice.get()))
				oil=round((105/100)*self.oilvar.get()*int(self.oilprice.get()))
				wheat=round((105/100)*self.wheatvar.get()*int(self.wheatprice.get()))
				dal=round((105/100)*self.dalvar.get()*int(self.dalprice.get()))
				sugar=round((105/100)*self.sugarvar.get()*int(self.sugarprice.get()))
				salt=round((105/100)*self.saltvar.get()*int(self.saltprice.get()))
				tea=round((105/100)*self.teavar.get()*int(self.teaprice.get()))

				grocery=(rice+oil+wheat+dal+sugar+salt+tea)
		
				grocery_total=str(round(grocery))
				self.totalgrocery_pricevar.set(grocery_total)

				#cold drinks
		
	
				maza=round((118/100)*self.mazavar.get()*int(self.mazaprice.get()))
				cocacola=round((118/100)*self.cocacolavar.get()*int(self.cocacolaprice.get()))
				sprite=round((118/100)*self.spritevar.get()*int(self.spriteprice.get()))
				railneer=round((118/100)*self.railneervar.get()*int(self.railneerprice.get()))
				froti=round((118/100)*self.frootivar.get()*int(self.frootiprice.get()))
				limca=round((118/100)*self.limcavar.get()*int(self.limcaprice.get()))
				thansup=round((118/100)*self.thansupvar.get()*int(self.thansupprice.get()))

				colddrinks=(maza+cocacola+sprite+railneer+froti+limca+thansup)
				colddrinks_total=str(round(colddrinks))
				self.totalcolddrinks_pricevar.set(colddrinks_total)

		

				all_total=(cosmetics+grocery+colddrinks)
				display_alltotal=(round(all_total))


				self.textarea.insert(index=END, chars="\n----------------------------------------")
				self.textarea.insert(index=END, chars=f"\n\t\tSub Total :{sub_total}")
				self.textarea.insert(index=END, chars=f"\n\t\tS.G.S.T :\t 7.00")
				self.textarea.insert(index=END, chars=f"\n\t\tC.G.S.T :\t 21.00")
				self.textarea.insert(index=END, chars="\n----------------------------------------")
				self.textarea.insert(index=END, chars=f"\n\t\tTotal :\t {display_alltotal}")
				self.textarea.insert(index=END, chars="\n----------------------------------------")
				self.textarea.insert(index=END, chars="\n\t\tThank You \t Visit Again")

				data=messagebox.askyesno('Print',"Do You Want To Print")
				if data==1:
					bill_data=str((self.textarea.get(1.0,END)))
					global url
					url=open('D:\\Customer Bill\\txt\\'+str(self.ran)+'.txt','a+')
					url.write(bill_data)
					url.close()
					pdf=FPDF()
					pdf = FPDF('P', 'mm', 'A4')
					pdf.add_page()
					pdf.set_font('Arial','',15)		
					with open('D:\\Customer Bill\\txt\\'+str(self.ran)+'.txt','r')	as files:
						for i in files:
							unicodedata.normalize('NFKD',i).encode('ascii','ignore')
							pdf.cell(90,5,txt=i,ln=1,align="C")		
					pdf.output('D:\\Customer Bill\\'+str(self.ran)+'.pdf')
					files.close()
					messagebox.showinfo('info',f'Bill NO. {self.ran} save successfully')
					
				else:
					return
					

				


	def find(self):
		billlist=self.billdata.get()
		if billlist!='':
			present="no"
			for i in os.listdir('D:\\Customer Bill\\txt\\'):
				if i.split('.')[0] == self.billdata.get():
					f1=open(f'D:\\Customer Bill\\txt\\{i}','r')
					self.textarea.delete(1.0,END)
					for d in f1:
						self.textarea.insert(END,d)
					f1.close()	
					present='yes'
			if present=="no":
				messagebox.showerror('Error','Bill No. not found')
		else:
			messagebox.showerror('Error','Please! Enter Your Bill No. ')
				
	def clearfunc(self):
		self.soapdata.set(value=0)
		self.sanitizer.set(value=0)
		self.facecreamvar.set(value=0)
		self.facewashvar.set(value=0)
		self.hairsprayvar.set(value=0)
		self.hairgelvar.set(value=0)
		self.bodysprayvar.set(value=0)
		self.ricevar.set(value=0)
		self.oilvar.set(value=0)
		self.wheatvar.set(value=0)
		self.dalvar.set(value=0)
		self.sugarvar.set(value=0)
		self.saltvar.set(value=0)
		self.teavar.set(value=0)
		self.mazavar.set(value=0)
		self.cocacolavar.set(value=0)
		self.spritevar.set(value=0)
		self.railneervar.set(value=0)
		self.frootivar.set(value=0)
		self.limcavar.set(value=0)
		self.thansupvar.set(value=0)
		self.totalcosmetics_pricevar.set('')
		self.totalgrocery_pricevar.set('')
		self.totalcolddrinks_pricevar.set('')
		self.custdata.set('')
		self.custphone.set('')
		self.ran=random.randint(1000, 9999)


	def exitfunc(self):
		yes_no=messagebox.askyesno('Exit','Do You Want To Close The Application')
		if yes_no==1:
			self.root.destroy()
		else:
			return


root=Tk()
Bill(root)
root.mainloop()
