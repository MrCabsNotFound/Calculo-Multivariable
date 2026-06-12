import matplotlib

import matplotlib.pyplot as plt

import numpy as np

#x,y son arrays o listas

def VariasGraficas(x1,y1,y2,y3,y4,y5,y6,titulo='Comparativo Gráficas'):
    
    fig, axs = plt.subplots(2,3)
    fig.suptitle(titulo)
    axs[0,0].plot(x1, y1)
    axs[0,0].set_title('Grafica1')
    axs[0,0].grid()                                 #Cuadrícula subgráfica 1

    axs[0,1].plot(x1, y2)
    axs[0,1].set_title('Grafica2')
    axs[0,1].grid()                                 #Cuadrícula subgráfica 1

    axs[0,2].plot(x1, y3)
    axs[0,2].set_title('Grafica3')
    axs[0,2].grid()                                 #Cuadrícula subgráfica 1

    axs[1,0].plot(x1, y4)
    axs[1,0].set_title('Grafica4')
    axs[1,0].grid()                                 #Cuadrícula subgráfica 1


    axs[1,1].plot(x1, y5)
    axs[1,1].set_title('Grafica5')
    axs[1,1].grid()                                 #Cuadrícula subgráfica 1

    axs[1,2].plot(x1, y6)
    axs[1,2].set_title('Grafica6')
    axs[1,2].grid()                                 #Cuadrícula subgráfica 1

    plt.show()


#Grafica automatizada de las funciones trigonométricas con Varias Graficas
x=np.linspace(-2,2)
VariasGraficas(x,np.sinh(x),np.cosh(x),np.tanh(x),1/np.sinh(x),1/np.cosh(x),1/np.tanh(x),'Comparativo Hiperbólicas')



print('Comandos de numpy para crear vectores filas')


a = 5  #extremo izquierdo
b = 50 #extremo derecho
n = 10 #número de puntos en el intervalo
x1 = np.linspace(a,b,n)   #intervalo con puntos uniformemente distribuidos
x2 = np.logspace(-2,5,8) #potencias desde 10^-2 hasta 10^5

x2 = np.logspace(-2,5,8,base=2) #cuarto input es la base de la potencia. 2^-2 hasta 2^5
print(x2)

#Funciones Elementales con Numpy

x1 = np.linspace(-3,3,51)
y1 = np.exp(x1)
y2 = np.absolute(x1)
y3 = np.sin(x1)
y4 = np.sign(x1)
#Funcion cosecante  divida 1 dentro de seno
y5 = 1/y3

print(y2)

y =range(1,21,2)


print()
print('Gráficas con Matplotlib usando plt')

x = np.linspace(-10,10,51)
y = np.asinh(x)


plt.plot(x,y)   #Realiza la gráfica
#plt.show()      #Despliega la gráfica

#Comandos adicionales para graficar

plt.plot(x,y,'r*')   #los marcadores pueden ser asteriscos *, diamantes d, líneas discontinuas
plt.title('Gráfica de seno hiperbólico inverso') #Título de la gráfica
plt.xlabel('x')  #Rótulo en el eje horizontal
plt.ylabel('y')  #Rótulo en el eje vertical
plt.xlim([-10,10])  #Límites en x de la gráfica
plt.ylim([-3,3])  #Límites en y de la gráfica
plt.grid()    #Coloca una cuadrícula para la gráfica


plt.show()

#2  o más gráficas en una misma ventana

x = np.linspace(-5,5,20)
y1 = np.exp(x)
y2 = np.exp2(x)   #Función exponencial de base 2

plt.plot(x,y1, 'b-*')
plt.plot(x,y2,'g--')
plt.legend(['e^x', '2^x'],loc='center left')
plt.title('Comparativo entre diferentes funciones exponenciales')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
#plt.ylim(0,100)
plt.xlim(-5,5)
plt.grid()
plt.savefig('Gráficacomparativa.png')


plt.show()


print()
print('Graficas de funciones trigonométricas')

from math import pi

x3 = np.linspace(-2*pi,2*pi,201)
ya = np.sin(x3)
yb = np.cos(x3)
yc = np.tan(x3)
yd = 1/ ya      #cosecante
ye = 1/ yb      #secante
yf = 1/ yc      #cotangente
plt.plot(x3,ya,x3,yb,x3,yc)
plt.title('Gráficas de las funciones trigonométricas')
plt.legend(['Seno','Coseno', 'Tangente'],loc='upper right')
plt.grid()
plt.ylim(-10,10)
plt.xlim(-7,9)


plt.show()


print()
print('Gráficas con el comando subplot')

fig, axs = plt.subplots(2,3)
fig.suptitle('Comparativo funciones trigonométricas')
axs[0,0].plot(x3, ya)
axs[0,0].set_title('Seno')
axs[0,0].grid()                                 #Cuadrícula subgráfica 1

axs[0,1].plot(x3, yb)
axs[0,1].set_title('Coseno')
axs[0,1].grid()                                 #Cuadrícula subgráfica 1

axs[0,2].plot(x3, yc)
axs[0,2].set_title('Tangente')
axs[0,2].set_ylim([-10,10])
axs[0,2].grid()                                 #Cuadrícula subgráfica 1

axs[1,0].plot(x3, yd)
axs[1,0].set_title('Cotangente')
axs[1,0].set_ylim([-10,10])
axs[1,0].grid()                                 #Cuadrícula subgráfica 1


axs[1,1].plot(x3, ye)
axs[1,1].set_title('Cosecante')
axs[1,1].set_ylim([-10,10])
axs[1,1].grid()                                 #Cuadrícula subgráfica 1

axs[1,2].plot(x3, yf)
axs[1,2].set_title('Cotangente')
axs[1,2].set_ylim([-10,10])
axs[1,2].grid()                                 #Cuadrícula subgráfica 1

plt.show()


print('Definiciones o Funciones en Python')


def VariasGraficas(x1,y1,y2,y3,y4,y5,y6,titulo='Comparativo Gráficas'):
    
    fig, axs = plt.subplots(2,3)
    fig.suptitle(titulo)
    axs[0,0].plot(x1, y1)
    axs[0,0].set_title('Grafica1')
    axs[0,0].grid()                                 #Cuadrícula subgráfica 1

    axs[0,1].plot(x1, y2)
    axs[0,1].set_title('Grafica2')
    axs[0,1].grid()                                 #Cuadrícula subgráfica 1

    axs[0,2].plot(x1, y3)
    axs[0,2].set_title('Grafica3')
    axs[0,2].grid()                                 #Cuadrícula subgráfica 1

    axs[1,0].plot(x1, y4)
    axs[1,0].set_title('Grafica4')
    axs[1,0].grid()                                 #Cuadrícula subgráfica 1


    axs[1,1].plot(x1, y5)
    axs[1,1].set_title('Grafica5')
    axs[1,1].grid()                                 #Cuadrícula subgráfica 1

    axs[1,2].plot(x1, y6)
    axs[1,2].set_title('Grafica6')
    axs[1,2].grid()                                 #Cuadrícula subgráfica 1

    plt.show()


#Grafica automatizada de las funciones trigonométricas con Varias Graficas

VariasGraficas(x3,ya,yb,yc,yd,ye,yf,'Comparativo Trigonométricas')


x=np.linspace(-2,2)
VariasGraficas(x,np.sinh(x),np.cosh(x),np.tanh(x),1/np.sinh(x),1/np.cosh(x),1/np.tanh(x),'Comparativo Hiperbólicas')

















