auto1 = {
    "Categoria": "Deportivo",
    "Modelo": "Audi",
    "Precio": "300,000"
    
    }

auto2 ={
        
    "Categoria": "Deportivo",
    "Modelo":  "Mercedez",
    "Precio": "400,000"    
        
    }



precio = input("Cual es tu presupuesto para un auto")
auto1["Precio"]=precio
print(auto1.get("Precio"))

for x in auto1.values():
    print(x)
    
print("Ejersisios de python\n")

teclado2 = {
        
   "Categoria": "Teclado",
   "Modelo": "Hyper X",
   "Precio": "950$"
        
   }
for x,y in teclado2.items():
    print(x," = ",y,".")
