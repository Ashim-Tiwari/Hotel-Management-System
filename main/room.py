from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Room_Booking:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #=======================variables=================\
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_no_of_day=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        # ======================title=====================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ======================logo=====================
        img2=Image.open(r"D:\hotel management system\hotel images\hotel logo.webp")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=5,y=2,width=100,height=40)

        # ======================label_frame=====================
        label_frame_left=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
        label_frame_left.place(x=5,y=50,width=425,height=490)

        # ======================labels and entries=====================
        #customer contact
        lbl_cust_contact=Label(label_frame_left,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(label_frame_left,width=17,textvariable=self.var_contact,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        ## fetch data button
        btn_fetch_data=Button(label_frame_left,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8,command=self.fetch_contact)
        btn_fetch_data.place(x=310,y=4)

        #check in date
        check_in_date=Label(label_frame_left,text="Chect In Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        text_check_in_date=ttk.Entry(label_frame_left,textvariable=self.var_checkin,width=22,font=("arial",13,"bold"))
        text_check_in_date.grid(row=1,column=1)

        #check out date
        check_out_date=Label(label_frame_left,text="Check Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        text_check_out_date=ttk.Entry(label_frame_left,width=22,textvariable=self.var_checkout,font=("arial",13,"bold"))
        text_check_out_date.grid(row=2,column=1)

        #room type
        lbl_room_type=Label(label_frame_left,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_room_type.grid(row=3,column=0,sticky=W)

        connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
        my_cursor=connection.cursor()
        my_cursor.execute("select `Room Type` from details")
        ide=my_cursor.fetchall()

        combo_room_type=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=20,state="readonly")
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1,padx=2)

        #available room
        lbl_available_room=Label(label_frame_left,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_available_room.grid(row=4,column=0,sticky=W)

        # entry_room_available=ttk.Entry(label_frame_left,width=22,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
        # entry_room_available.grid(row=4,column=1)

        connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
        my_cursor=connection.cursor()
        my_cursor.execute("select `Room No.` from details")
        rows=my_cursor.fetchall()


        combo_room_no=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_roomavailable,width=20,state="readonly")
        combo_room_no["value"]=rows
        combo_room_no.current(0)
        combo_room_no.grid(row=4,column=1,padx=2)

        #meal
        lbl_meal=Label(label_frame_left,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)

        combo_meal=ttk.Combobox(label_frame_left,font=("arial",12,"bold"),textvariable=self.var_meal,width=20,state="readonly")
        combo_meal["value"]=("Breakfast","Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1,padx=2)

        #no of days
        lbl_no_of_days=Label(label_frame_left,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_no_of_days.grid(row=6,column=0,sticky=W)

        entry_no_of_days=ttk.Entry(label_frame_left,width=22,textvariable=self.var_no_of_day,font=("arial",13,"bold"))
        entry_no_of_days.grid(row=6,column=1)

        #sub total
        lbl_sub_total=Label(label_frame_left,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_sub_total.grid(row=7,column=0,sticky=W)

        entry_sub_total=ttk.Entry(label_frame_left,width=22,textvariable=self.var_actualtotal,font=("arial",13,"bold"))
        entry_sub_total.grid(row=7,column=1)

        #paid tax
        lbl_paid_tax=Label(label_frame_left,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=8,column=0,sticky=W)

        entry_paid_tax=ttk.Entry(label_frame_left,width=22,textvariable=self.var_paidtax,font=("arial",13,"bold"))
        entry_paid_tax.grid(row=8,column=1)


        #total cost
        lbl_total_cost=Label(label_frame_left,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_total_cost.grid(row=9,column=0,sticky=W)

        entry_total_cost=ttk.Entry(label_frame_left,width=22,textvariable=self.var_total,font=("arial",13,"bold"))
        entry_total_cost.grid(row=9,column=1)

        # bill button
        btn_bill=Button(label_frame_left,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.total)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)

        #===============Buttons==================
        btn_frame=Frame(label_frame_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.add_button)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.deleted)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.reset)
        btn_reset.grid(row=0,column=3,padx=1)

        #==============right side image===========================
        imgs=Image.open(r"D:\hotel management system\hotel images\bedroom.jpg")
        imgs=imgs.resize((400,300),Image.Resampling.LANCZOS)
        self.photoimgs=ImageTk.PhotoImage(imgs)

        lblimgs=Label(self.root,image=self.photoimgs,bd=0,relief=RIDGE)
        lblimgs.place(x=580,y=55,width=880,height=300)

        #===============table frame search system==================

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=280,width=860,height=260)

        lbl_searchby=Label(table_frame,text="Search By:",font=("arial",12,"bold"),bg="pink",fg="green")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar() 

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["value"]=("Customer Contact","Room No")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar() 

        txt_search=ttk.Entry(table_frame,width=22,text=self.txt_search,font=("arial",13,"bold"))
        txt_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.search)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show_all=Button(table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9,command=self.fetch_data)
        btn_show_all.grid(row=0,column=4,padx=1)

#===============Show data table==================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("Customer Contact","Checkin date","Checkout date","Room Type","Room No","Meal","No of Days"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_x.config(command=self.room_table.xview)
        scrollbar_y.config(command=self.room_table.yview)
        self.room_table.heading("Customer Contact",text="Customer Contact")
        self.room_table.heading("Checkin date",text="Checkin date")
        self.room_table.heading("Checkout date",text="Checkout date")
        self.room_table.heading("Room Type",text="Room Type")
        self.room_table.heading("Room No",text="Room No")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("No of Days",text="No of Days")

        self.room_table["show"]="headings"

        self.room_table.column("Customer Contact",width=100)
        self.room_table.column("Checkin date",width=100)
        self.room_table.column("Checkout date",width=100)
        self.room_table.column("Room Type",width=100)
        self.room_table.column("Room No",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("No of Days",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)  
        self.fetch_data()

    def add_button(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Check in date and customer contact must be filled.",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_no_of_day.get()
                                                                                                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success","Room has been booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                my_cursor.execute("select * from room")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    # Clear any existing rows in the treeview widget
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("",END,values=i)
                    connection.commit()
                connection.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_no_of_day.set(row[6])
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.error("Error","Please enter contact number.",parent=self.root)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
            my_cursor=connection.cursor()
            my_cursor.execute("update room set `Checkin date`=%s,`Checkout date`=%s,`Room Type`=%s,`Room No`=%s,Meal=%s,`No Of Days`=%s where `Customer Contact`=%s",(
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_no_of_day.get(),
                                                                            self.var_contact.get()
                                                                        ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Update","Room details has been successfully updated..",parent=self.root)
    
    def deleted(self):
        deleted=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if deleted>0:
            connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
            my_cursor=connection.cursor() 
            query="delete from room where `Customer Contact`=%s"
            value=(self.var_contact.get(),)  
            my_cursor.execute(query,value)           
        else:
            if not deleted:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
    
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomavailable.set(""),
        self.var_no_of_day.set(""),
        self.var_actualtotal.set(""),
        self.var_paidtax.set(""),
        self.var_total.set("")

    def search(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
        my_cursor=connection.cursor() 

        query = "SELECT * FROM room WHERE `" + str(self.search_var.get()) + "` LIKE %s"
        value = ('%' + self.txt_search.get() + '%',)  # Wrap in a tuple for parameterized query
        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i) 
            connection.commit()
        connection.close()
    
    #===============All Data fetch=======================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the contact number.",parent=self.root)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
            my_cursor=connection.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found.",parent=self.root)
            else:
                connection.commit()
                connection.close()
                # NAME
                show_data_frame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                show_data_frame.place(x=455,y=55,width=300,height=180)
                lbl_name=Label(show_data_frame,text="Name:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=0)
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)  # 98765437
                #GENDER
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)                     
                row=my_cursor.fetchone()
                lbl_name=Label(show_data_frame,text="Gender:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=30)
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)
                #email
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)                     
                row=my_cursor.fetchone()
                lbl_name=Label(show_data_frame,text="Email:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=60)
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)
                #NATIONALITY
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)                     
                row=my_cursor.fetchone()
                lbl_name=Label(show_data_frame,text="Nationality:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=90)
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)
                #ADDRESS
                connection=mysql.connector.connect(host="localhost",username="root",password="AshimtiW@07",database="hotel_management_system")
                my_cursor=connection.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)                     
                row=my_cursor.fetchone()
                lbl_name=Label(show_data_frame,text="Address:",font=("arial",12,"bold"))
                lbl_name.place(x=0,y=120)
                lbl=Label(show_data_frame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)  

    def total(self):
        # no of days
        in_date = self.var_checkin.get()
        out_date = self.var_checkout.get()
        in_date = datetime.strptime(in_date, "%Y/%m/%d")
        out_date = datetime.strptime(out_date, "%Y/%m/%d")
        no_of_days = (out_date - in_date).days
        self.var_no_of_day.set(abs(no_of_days))

        
        price=0
        if (self.var_meal.get()=="Breakfast"):price=150
        elif (self.var_meal.get()=="Lunch"):price=500
        elif (self.var_meal.get()=="Dinner"):price=800

        if (self.var_roomtype.get()=="Single"):price=price+1500
        elif (self.var_roomtype.get()=="Double"):price=price+1000
        elif (self.var_roomtype.get()=="Luxury"):price=price+3000

        net_price=price*no_of_days
        # paid tax
        self.var_paidtax.set(0.04*net_price)
        self.var_total.set(net_price+(0.04*net_price))
        self.var_actualtotal.set(net_price)


if __name__=="__main__":
    root=Tk()
    obj=Room_Booking(root)
    root.mainloop()