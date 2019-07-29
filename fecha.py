
#!/usr/bin/python   
# -*- coding: utf-8 -*- 


from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog as FileDialog
from datetime import date, datetime
import calendar
import sqlite3 # modulo de conexion con sqlite3 
from PIL import ImageTk, Image


class Product:
    #conexion con la base de datos
    db_lab = 'vitasis.db'
    def __init__(self, window):
        
        self.wind = window
        self.wind.title('Vitasis Laboratorio Médico')
        self.wind.configure(background = 'gray')
        self.wind.geometry('1210x823')
        #self.wind.resizable(0, 0)
        

        #carga de la imagen
        img = Image.open('logo QR.png')
        self._image_logo = ImageTk.PhotoImage(img) 
        widget = tk.Label(self.wind, image = self._image_logo).grid( row= 0, column = 0, sticky = W)

        #Pestañas

        self.note_book = ttk.Notebook(self.wind)
        #self.note_book.pack()
        self.tab2 = ttk.Frame(self.note_book)

        #self._tab_control = ttk.Notebook(self.wind)
        self.note_book.grid(row= 1, column = 0) 
        self.note_book.add(self.tab2, text="Pacientes", compound=tk.TOP)
             
        style = ttk.Style()
        style.theme_use("classic")

        #creando el contenedor Buscar paciente
        self.frame = LabelFrame(self.tab2, text = 'Corte de mes', labelanchor = N, font = ('bold'))
        self.frame.grid(row = 0, column = 0, padx = 5, pady = 20, ipadx = 30, sticky = W)
        self.frame.configure(background = 'gray')
        
                
        Label(self.frame, text = 'Fecha de inicio: ', bg = 'gray').grid(row = 1, column = 0, sticky = W + E)
        self.fecha_inicial = Entry(self.frame, width = 10)
        self.fecha_inicial.focus()
        self.fecha_inicial.grid(row = 1, column = 1, pady = 10, sticky = W)
        

        Label(self.frame, text = 'Fecha final: ', bg = 'gray',).grid(row = 2, column = 0, sticky = W + E)
        self.fecha_final = Entry(self.frame, width = 10)
        self.fecha_final.grid(row = 2, column = 1, pady = 10, sticky = W )
           
               
        Button(self.frame, text = 'Seleccionar mes', command = self.get_pacients).grid(row = 2, column = 2, pady = 10, padx = 10, sticky = W + E ) 
        #self.get_pacients()
        
      
 
    def run_query(self, query, parameters = ()): # Ejecutar consulta para la tabla paciente
        with sqlite3.connect(self.db_lab) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
        # Consulta de datos
        
        query = ('SELECT * FROM paciente WHERE fecha_de_estudio BETWEEN ? AND ?', self.fecha_i, self.fecha_f)
        #'SELECT * FROM paciente WHERE fecha_de_estudio BETWEEN "self.fecha_i" AND "self.fecha_f"'
        db_rows = self.run_query(query)

        
    def get_pacients(self):
            
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20')
        
        self.tree2 = ttk.Treeview(self.frame, show='headings', height=30, columns=columns)
        self.tree2.grid(row=3, column=0, columnspan=12, rowspan = 1000, sticky = tk.W+tk.E+tk.N+tk.S, pady = 5)
        
        self.tree2.column("#1", width=70, anchor = tk.CENTER )
        self.tree2.column("#2", width=150, stretch=tk.NO)
        self.tree2.column("#3", width=150)
        self.tree2.column("#4", width=150, stretch=tk.NO)
        self.tree2.column("#5", width=50, stretch=tk.NO)
        self.tree2.column("#6", width=100, stretch=tk.NO)
        self.tree2.column("#7", width=300) # Prueba Clinica 1
        self.tree2.column("#8", width=300) # Prueba Clinica 2
        self.tree2.column("#9", width=300) # Prueba Clinica 3
        self.tree2.column("#10", width=300) # Prueba Clinica 4
        self.tree2.column("#11", width=300) # Prueba Clinica 5
        self.tree2.column("#12", width=200) # Fecha de estudio
        self.tree2.column("#13", width=200) # Fecha de entrega
        self.tree2.column("#14", width=150) # Atendido
        self.tree2.column("#15", width=150) # Promocion
        self.tree2.column("#16", width=150) #Subtotal
        self.tree2.column("#17", width=150) # Anticipo
        self.tree2.column("#18", width=150) # Total
        self.tree2.column("#19", width=150) # Saldo a pagar
        self.tree2.column("#20", width=150) # Saldo a pagar

        self.tree2.heading('#1', text='Folio', anchor=tk.CENTER)
        self.tree2.heading('#2', text='Nombre', anchor=tk.CENTER)
        self.tree2.heading('#3', text='Dirección', anchor=tk.CENTER)
        self.tree2.heading('#4', text='Teléfono', anchor=tk.CENTER)
        self.tree2.heading('#5', text='Edad', anchor=tk.CENTER)
        self.tree2.heading('#6', text='Sexo', anchor=tk.CENTER)
        self.tree2.heading('#7', text='Prueba Clinica 1', anchor=tk.CENTER)
        self.tree2.heading('#8', text='Prueba Clinica 2', anchor=tk.CENTER)
        self.tree2.heading('#9', text='Prueba Clinica 3', anchor=tk.CENTER)
        self.tree2.heading('#10', text='Prueba Clinica 4', anchor=tk.CENTER)
        self.tree2.heading('#11', text='Prueba Clinica 5', anchor=tk.CENTER)
        self.tree2.heading('#12', text='Fecha de estudio', anchor=tk.CENTER)
        self.tree2.heading('#13', text='Fecha de entrega', anchor=tk.CENTER)
        self.tree2.heading('#14', text='Atendido', anchor=tk.CENTER)
        self.tree2.heading('#15', text='Promoción', anchor=tk.CENTER)
        self.tree2.heading('#16', text='Subtotal', anchor=tk.CENTER)
        self.tree2.heading('#17', text='Anticipo', anchor=tk.CENTER)
        self.tree2.heading('#18', text='Total', anchor=tk.CENTER)
        self.tree2.heading('#19', text='Saldo a pagar', anchor=tk.CENTER)
        self.tree2.heading('#20', text='Status', anchor=tk.CENTER)    
    
        
        vsb = ttk.Scrollbar(self.tree2, orient="vertical", command=self.tree2.yview)
        vsb.grid(row=1, column=0, columnspan = 10, sticky='ns')
        self.tree2.configure(yscrollcommand = vsb.set)

        hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree2.xview)
        hsb.grid(row = 5, column = 0, columnspan = 10, rowspan = 100, sticky = tk.W+tk.E)
        self.tree2.configure(xscrollcommand = hsb.set)  
            
        self.fecha_i = datetime.strptime(self.fecha_inicial.get(), '%d, %b, %Y')
        self.fecha_f = datetime.strptime(self.fecha_final.get(), '%d, %b, %Y')
        print(self.fecha_inicial.get())
        print(self.fecha_final.get())
            
    # Limpiando la tabla
        records = self.tree2.get_children()
        for element in records:
            self.tree2.delete(element)
            # getting data
        query = ('SELECT * FROM paciente WHERE fecha_de_estudio BETWEEN ? AND ?', self.fecha_i, self.fecha_f)
        print(query)
        db_rows = self.run_query(query).fetchall()
        print(db_rows)
            # filling data
        #for row in db_rows:
        #    print(row)
        #    print(len(row))
        for row in db_rows:
            self.tree2.insert('', 0, text = row[0], values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]))


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()                       



