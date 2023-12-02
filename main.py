a = 1
ord_g = 5
dati_L = []
dati_G = []
try:
    import matplotlib.pyplot as plt
    import numpy as np

except:
    print("errore rappresentazione grafica")
    a = 0


def generation(x: float , y: float , k:int = 4):
    return k*(x*y)


n_gen = int(input("Quante generazioni>"))
#n_l = None
#n_tot = None
L = 0.57
G = 1-L

for h in range(n_gen):
    L = generation(L , G)
    G = 1-L
    if a:
        dati_L.append(L)
        dati_G.append(G)
    else:
        print(f"Leoni:{L} , Gazzelle: {G}")

if dati_L:
    d_L = np.array(dati_L).round(ord_g)
    d_G = np.array(dati_G).round(ord_g)
    x = np.arange(0.0 , 1 , 1/len(dati_L))
    plt.plot(x , d_L ,"g", x , d_G , "y")
    plt.legend(["Leoni" , "Gazzelle"] , loc="upper left" , borderaxespad= -4.0)
    plt.show()
    