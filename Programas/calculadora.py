from tkinter import *

ventana = Tk()
ventana.title('Calculadora')

i = 0

#entrada
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5 )

#funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    return

def click_borrar():
    e_texto.delete(0, END)
    i = 0

def hacer_ecuacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

#botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 16, height = 2, command = lambda: click_boton(0))

boton_borr = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: click_borrar())
boton_par1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_par2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punt = Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))

boton_suma = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_divi = Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_mult = Button(ventana, text = "*", width = 5, height = 2, command = lambda: click_boton("*"))
boton_rest = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_igua = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_ecuacion())

#agregar botones en pantalla
boton_borr.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_par1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_par2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_divi.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punt.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igua.grid(row = 5, column = 3, padx = 5, pady = 5)

ventana.mainloop()