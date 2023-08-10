import tkinter as tk

Large_font_style=("Arial",40,"bold")
Small_font_style=("Arial",16)
digit_font_style=("Arial",24,"bold")
Default_font_style=("Arial",20)
Off_white="#F8FAFF"
Light_gray="#F5F5F5"
Light_blue="#CCEDFF"
LAbel_color="#000000"
White="#FFFFFF"

class Calculator:

    def __init__(self):

        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expressiom=""
        self.current_expression=""

        self.display_frame=self.create_display_frame()
        self.total_label, self.label=self.create_display_label()

        self.digits={
             1:(1,1), 2:(1,2), 3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3),0:(4,2),'.':(4,1)
        }
        self.operator={'/':'\u00F7','*':'\u00D7','+':'+','-':'-'}
        self.buttons_frame=self.create_button_frame()

        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
             self.buttons_frame.rowconfigure(x,weight=1)
             self.buttons_frame.columnconfigure(x,weight=1)
        self.create_operator()
        self.create_digit_buttons()
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.bind_keys()
       
    def create_digit_buttons(self):
         
         for digits,grid_value in self.digits.items():
              button= tk.Button(self.buttons_frame, text=str(digits),bg=White,fg=LAbel_color,font=digit_font_style,borderwidth=0,command= lambda x=digits:self.add_to_expression(x))
              button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def create_operator(self):
         i=0
         for op,symbol in self.operator.items():
              
              button=tk.Button(self.buttons_frame,text=symbol,bg=Off_white,fg=LAbel_color,font=Default_font_style,borderwidth=0,command=lambda x=op: self.add_operator(x))
              button.grid(column=4,row=i,sticky=tk.NSEW)
              i+=1

    def create_equal_button(self):
          button=tk.Button(self.buttons_frame,text="=",bg=Light_blue,fg=LAbel_color,font=Default_font_style,borderwidth=0,command=self.evaluate)
          button.grid(column=3,row=4,columnspan=2,sticky=tk.NSEW)

    def create_clear_button(self):
         button=tk.Button(self.buttons_frame,text="C",bg=Off_white,fg=LAbel_color,font=Default_font_style,borderwidth=0,command=self.clear)
         button.grid(column=1,row=0,sticky=tk.NSEW)

    def create_square_button(self):
         button=tk.Button(self.buttons_frame,text="x\u00b2",bg=Off_white,fg=LAbel_color,font=Default_font_style,borderwidth=0,command=self.square)
         button.grid(column=2,row=0,sticky=tk.NSEW)

    def square(self):
         self.current_expression=str(eval(f"{self.current_expression}**2"))
         self.update_label()
    
    def create_sqrt_button(self):
         button=tk.Button(self.buttons_frame,text="\u221ax",bg=Off_white,fg=LAbel_color,font=Default_font_style,borderwidth=0,command=self.squareroot)
         button.grid(column=3,row=0,sticky=tk.NSEW)

    def squareroot(self):
         self.current_expression=str(eval(f"{self.current_expression}**0.5"))
         self.update_label()
    def create_display_frame(self):
         frame = tk.Frame(self.window,height=221,bg=Light_gray)     
         frame.pack(expand=True, fill="both")    
         return frame
    

    def create_button_frame(self):
         frame = tk.Frame(self.window)
         frame.pack(expand=True, fill="both")
         return frame
    
    def create_display_label(self):
         total_label=tk.Label(self.display_frame,text=self.total_expressiom, anchor=tk.E,bg=Light_gray,fg=LAbel_color, padx=24, font=Small_font_style)
         total_label.pack(expand=True, fill="both")
         label=tk.Label(self.display_frame,text=self.current_expression, anchor=tk.E,bg=Light_gray,fg=LAbel_color, padx=24, font=Large_font_style)
         label.pack(expand=True, fill="both")
         return total_label,label
    
    def update_total_label(self):
         expression = self.total_expressiom
         for op,symbol in self.operator.items():
              expression=expression.replace(op,f'{symbol}')
         self.total_label.config(text=expression)

    def update_label(self):
         self.label.config(text=self.current_expression[:11])

    def add_to_expression(self,value):
         self.current_expression += str(value)
         self.update_label()
    def clear(self):
         self.current_expression=""
         self.total_expressiom=""
         self.update_total_label()
         self.update_label()

    
    def add_operator(self,operator):
         self.current_expression+=operator
         self.total_expressiom+=self.current_expression
         self.current_expression=""
         self.update_total_label()
         self.update_label()

    def evaluate(self):
         self.total_expressiom+= self.current_expression
         self.update_total_label()
         try:
               self.current_expression=str(eval(self.total_expressiom))
               self.total_expressiom=""
         except Exception as e:
              self.current_expression="Error"
         finally:
               self.update_label()

    def bind_keys(self):
         self.window.bind("<Return>", lambda event: self.evaluate)

         for keys in self.digits:
              self.window.bind(str(keys), lambda event,digit=keys :self.add_to_expression(digit))
         for op in self.operator:
              self.window.bind(str(op), lambda event,digit=op :self.add_to_expression(digit))
         
    
    def run(self):
        self.window.mainloop()

if __name__=="__main__":
        calc=Calculator()
        calc.run()

    
        