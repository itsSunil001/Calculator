import tkinter as tk
from tkinter import messagebox
import math as m
font_current=('Arial', 17 ,'bold')
font_total=('Arial', 16 )
button_font=('cascadia', 21 )
op_font=('cascadia', 21,"bold" )
special_font=('cascadia', 15,"bold" )
backgroud_color = "#404258"
display_color = '#B3E5BE'
button_color='#2C3333'
op_color='#B2B2B2'
clear_color='#E96479'
class new:
    def __init__(self):
        self.main=tk.Tk() 
        self.main.geometry('290x420')
        self.main.resizable(0,0)
        self.main.attributes('-topmost',True)
        self.main.title('Calculator')
        self.main.configure(bg=backgroud_color)
        self.current_value=""
        self.total_value=""
        self.button={
            7:(2,1),8:(2,2),9:(2,3),
            4:(3,1),5:(3,2),6:(3,3),
            3:(4,1),2:(4,2),1:(4,3),
            '.':(5,1),0:(5,2)        }
        self.op={'/':'\u00F7','*':'\u00D7','-':'-','+':'+'}
        self.df=self.display_frame()
        self.bf=self.button_frame()
        self.current,self.total=self.answer_label()
        self.number_button()
        self.operator_button()
        self.clear=self.clear_button()
        self.one=self.one_clear_button()
        self.equal=self.equal_button()
        self.squr=self.squar_button()
        self.r=self.root_button()
        self.one_divid=self.one_divid_button()
        self.percentage=self.percentage_button()
        self.minus=self.minus_button()
        for i in range(1,5):
            self.bf.rowconfigure(i, weight=1)
            self.bf.columnconfigure(i, weight=1)
    def display_frame(self):
        f=tk.Frame(self.main,height=90,bg=display_color,borderwidth=1,relief=tk.FLAT)
        f.pack(pady=7,padx=7,fill='both')
        return f
    def button_frame(self):
        f1=tk.Frame(self.main,height=390,borderwidth=0,bg=backgroud_color)
        f1.pack(fill='both',padx=7)
        return f1
    def answer_label(self):
        current=tk.Label(self.df,text=self.current_value,font=font_current,anchor=tk.E,bg=display_color)
        current.pack(fill='both',padx=4)
        total=tk.Label(self.df,text=self.total_value,font=font_total,anchor=tk.E,bg=display_color)
        total.pack(fill='both',padx=4)
        return current,total
    def number_button(self):
        for i,j in self.button.items():
            self.place=tk.Button(self.bf,text=str(i),bg=button_color,fg='white',borderwidth=0,relief=tk.FLAT,font=button_font,command=lambda lam=i:self.add_express(lam))
            self.place.grid(row=j[0],column=j[1],sticky=tk.NSEW,padx=0.5,pady=0.5)
    def operator_button(self):
        s1=1
        for i,j in self.op.items():
            self.place1=tk.Button(self.bf,text=j,fg=backgroud_color,bg=op_color,font=op_font,borderwidth=0,relief=tk.FLAT,command=lambda x=i:self.add_oprator(x))
            self.place1.grid(row=s1,column=4,sticky=tk.NSEW,padx=0.5,pady=0.5)
            s1+=1
    def clear_button(self):
            place2=tk.Button(self.bf,text="C",fg='white',bg=clear_color,font=op_font,borderwidth=0,relief=tk.FLAT,command=self.clear_all)
            place2.grid(row=0,column=3,sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place2
    def one_clear_button(self):
        place3=tk.Button(self.bf,text="\u232b",fg='white',bg=clear_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.one_clear_func)
        place3.grid(row=0,column=4,sticky=tk.NSEW,padx=0.5,pady=0.5)
        return place3
    def equal_button(self):
            place4=tk.Button(self.bf,text="=",fg='white',bg=display_color,font=op_font,borderwidth=0,relief=tk.FLAT,command=self.answer_func)
            place4.grid(row=5,column=3,columnspan=2, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place4
    def squar_button(self):
            place5=tk.Button(self.bf,text="x\u00b2",fg=backgroud_color,bg=op_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.sq_func)
            place5.grid(row=1,column=3, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place5
    def root_button(self):
            place6=tk.Button(self.bf,text="\u221ax",fg=backgroud_color,bg=op_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.root_func)
            place6.grid(row=1,column=2, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place6
    def one_divid_button(self): 
            place7=tk.Button(self.bf,text="1/x",fg=backgroud_color,bg=op_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.one_divide_func)
            place7.grid(row=1,column=1, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place7
    def percentage_button(self): 
            place8=tk.Button(self.bf,text="!",fg=backgroud_color,bg=op_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.percentage_func)
            place8.grid(row=0,column=1, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place8
    def minus_button(self): 
            place9=tk.Button(self.bf,text="+/-",fg=backgroud_color,bg=op_color,font=special_font,borderwidth=0,relief=tk.FLAT,command=self.minus_func)
            place9.grid(row=0,column=2, sticky=tk.NSEW,padx=0.5,pady=0.5)
            return place9
    def minus_func(self):
        temp=self.current_value[-1:]
        temp1=self.current_value[-2:]
        if self.current_value=='': 
            self.current_value='-'
            self.update_current()
        elif self.current_value[0]=='-': 
            self.current_value=self.current_value[1:]
            self.update_current()
        elif temp=='*' or temp=='/'or temp=='+' or temp=='-':
            if temp1!='*-' and temp1!='+-' and temp1!='--' and temp1!='/-':
                self.current_value=self.current_value+'-'
                self.update_current()
            else:
                self.current_value=self.current_value[:-1]
                self.update_current()
        elif self.current_value[0]!='-':
            try:
                temp2=self.current_value[-2]
                if temp2=="-":
                    self.current_value=self.current_value[:-2]+temp
                    self.update_current()
                elif temp2=="-" or temp2=="/" or temp2=="*" or temp2=="+":
                    self.current_value=self.current_value[:-1]+'-'+temp
                    self.update_current()
                else:
                    self.current_value='-'+self.current_value
                    self.update_current()
            except:
                    self.current_value='-'+self.current_value
                    self.update_current()
    def percentage_func(self):
        if self.total_value=='':
            try:
                ans=1
                for i in range(1,int(self.current_value)+1):
                    ans*=i
                self.total_value=ans
                self.update_total()
                self.current_value=self.current_value+'!'
                self.update_current()
            except Exception as e:
                messagebox.showerror('Error',format(e))
                self.clear_all()
    def one_divide_func(self):
        if self.current_value=='':
            try:
                self.total_value=eval(f'1/{self.current_value}')
                self.update_total()
            except:
                pass
        else:
            try:
                self.total_value=eval(f'1/{self.current_value}')
                self.update_total()
            except:
                messagebox.showerror('ValueError','You must enter a valid value')
    def root_func(self):
        if self.total_value =='':
            try:
                self.total_value=m.sqrt(float(self.current_value))
                self.update_total()
            except:
                messagebox.showerror('ValueError','You must enter a valid value')
                self.clear_all()
        else:
            self.current_value="{:.1f}".format(float(self.total_value))
            self.total_value=m.sqrt(float(self.total_value))
            self.update_current()
            self.update_total()
    def sq_func(self):
        if self.total_value =='':
            try:
                self.total_value="{:.2f}".format(m.pow(float(self.current_value),2))
                self.update_total()
            except: 
                messagebox.showerror('ValueError','You must enter a valid value')
                self.clear_all()
        else:
            try:
                self.current_value="{:.0f}".format(float(self.total_value))
                self.total_value="{:.2f}".format(m.pow(float(self.total_value),2))
                self.update_current()
                self.update_total()
            except Exception as e:
                messagebox.showerror('Error',format(e))
                self.clear_all()
    def add_express(self,lam):
        self.current_value+=str(lam)
        self.update_current()
    def clear_all(self):
        self.current_value=''
        self.total_value=''
        self.update_current()
        self.update_total()
    def one_clear_func(self):
        self.current_value=self.current_value[0:-1]
        self.update_current()
        self.total_value=''
        self.update_total()
    def add_oprator(self,lam):
        temp1=self.current_value[-2:]
        try:
            s1=self.current_value[-1]
            if s1=='/' or s1=='*' or s1=='-' or s1=='+':
                if temp1!='/-' and temp1!='+-' and temp1!='*-' and temp1!='--':
                    self.current_value=self.current_value[0:-1]+s1.replace(s1,lam)
                    self.update_current()
            else:
                self.total.config(text='')
                self.current_value +=lam
                self.update_current()
        except:
            pass
    def update_current(self):
        e = self.current_value
        for operator, symbol in self.op.items():
            e = e.replace(operator,f'{symbol}')
        self.current.config(text=e)
    def answer_func(self):
        try:
            self.total_value=eval(self.current_value)
            self.update_total()
        except:
            messagebox.showerror('SyntaxError:','You must enter a valid value')
            self.clear_all()
    def update_total(self):
        self.total_value=str(self.total_value)
        self.total.config(text=self.total_value[:22])
    def run(self):
        self.main.mainloop()
if __name__=='__main__':
    object=new()
    object.run()