#import tkinter widgets
from tkinter import *
from tkinter.filedialog import asksaveasfile 
  

#create first window
first_menu=Tk()
#set title and appearance of window, position on the screeen
first_menu.title('Products Database')
first_menu.geometry('250x100+500+200')
#we open the file
products=open('Products.txt')
    #assign all lines in the file to a variable lines, to make it as a list, so it's possible going
    #through each line 
myfile=products.readlines()

#creation of a menu bar linked to our main window first_menu
menu_bar=Menu(first_menu)

#we link menu_bar to our menu,
option=Menu(menu_bar,tearoff=0)

       
#we define a function to close a window       
def close():
    first_menu.destroy() 


#definition of a function called ok, that create a new window to do our search
#function will work when we click on 'search' in the first menu
def mySearch(): 
    
    nw=Tk()
    nw.title('Search:')
    nw.geometry('350x200+500+200')
    

    menu_bar=Menu(nw)
    option=Menu(menu_bar,tearoff=0)
    menu_bar.add_command(label='New Search...',command=mySearch)
    menu_bar.add_separator()
    menu_bar.add_command(label='Quit',command=nw.quit)
    nw.config(menu=menu_bar)

    
    radio=IntVar(nw)
    R1 = Radiobutton(nw, text="Product Code", variable=radio, value=0)  
    R1.pack( anchor = W)  
    R2 = Radiobutton(nw, text="Type", variable=radio, value=1)  
    R2.pack( anchor = W )  
    R3 = Radiobutton(nw, text="Department", variable=radio, value=2) 
    R3.pack( anchor = W)  
    R4 = Radiobutton(nw, text="Price", variable=radio, value=3)  
    R4.pack( anchor = W)  
    R5 = Radiobutton(nw, text="Colour", variable=radio, value=4)  
    R5.pack( anchor = W)  
    R6 = Radiobutton(nw, text="Availability", variable=radio, value=5)  
    R6.pack( anchor = W) 

    
    label=Label(nw,text="Enter your value:")
    
    label.pack()
    
    entry1=Entry(nw)
    #bind an event to entry1, when you click with the mouse placeholder will be deleted
    entry1.bind("<FocusIn>", lambda args: entry1.delete('0', 'end'))
    #create placeholder  for entry1 and insert it 
    entry1.insert(0, 'i.e. 171251 or Red')
    #display it in the window
    entry1.pack() 

    #definition of a records function, that will do our search and print our results in a third
    #new window
    def records():
              
        
        third_window=Tk()
        third_window.title('Your record(s)')
        third_window.geometry('650x180')

        scrollbar = Scrollbar(third_window)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        records=search(myfile,radio.get(),entry1.get())
        
        menu_bar=Menu(third_window)

        def Export(): 
            files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
            text = records
            file = asksaveasfile(filetypes = files, defaultextension = files) 
            file.write(text)
        
        option=Menu(menu_bar,tearoff=0)
        menu_bar.add_command(label='New Search...',command=mySearch)
        menu_bar.add_command(label='Export...',command=Export)
        menu_bar.add_separator()
        menu_bar.add_command(label='Quit',command=first_menu.quit)
        
       
        mylist = Listbox(third_window, yscrollcommand = scrollbar.set )
        
        for line in records.split('\n'):
            mylist.insert(END,line)

        mylist.pack(fill=BOTH)
        scrollbar.config(command=mylist.yview)

        third_window.config(menu=menu_bar)
        nw.destroy()   

    
    buttonOk=Button(nw,text='Ok',command=records)
    buttonOk.pack()

    #destroy the first window as we are not using it anymore 
    first_menu.destroy()


#we create and add different option (submenu) for our main menu and we assign different label to them
option.add_command(label='New Search...',command=mySearch)
#separator create a line to separate labels
option.add_separator()
option.add_command(label='Quit',command=first_menu.quit)

#creation of the main label/menu for our dropdown menu on the bar
menu_bar.add_cascade(label='Options',menu=option)
help=Menu(menu_bar,tearoff=0)
help.add_command(label='Help')
menu_bar.add_cascade(label='Help',menu=help) 

#config set up our menu and attaches menu_bar to it
#without menu won't be displayed
first_menu.config(menu=menu_bar)


def search(myfile,selected,data):
    
    #we create a variable called lst and assign an empty string to it
    lst=""
    #we loop through each line in files
    for line in myfile:
        #split help us to isolate each line
        splitUp=line.split(",")
        #our selected choice in the radiobutton widget is used as index to look into a specific
        #record/column/field in our file
        cell=splitUp[selected]
        #if that data is in the line
        if data.lower() in cell.lower():
            #we add it to the string 'lst'
            lst+=line
    #return the final lst at the end of the cycle        
    return lst         

    


searchBut=Button(first_menu,text="Search",command=mySearch)
searchBut.pack()

button2 =Button(first_menu, text="Close", command=close)
button2.pack()

mainloop()  
