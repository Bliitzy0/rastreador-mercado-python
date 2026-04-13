import requests 

def hackear_tienda_de_practica():
    print("📡 Redirigiendo el dron a la Tienda de Entrenamiento (FakeStore)...")
    
    # Endpoint de la tienda de práctica (categoría: electrónicos)
    url = "https://fakestoreapi.com/products/category/electronics"
    
    try:
        # Aquí no necesitamos disfraz, la puerta está abierta
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            # Traducimos la respuesta a una Lista de Diccionarios
            lista_productos = respuesta.json()
            
            print("\n✅ ¡Sistemas vulnerados! Accediendo al catálogo:\n")
            print("=" * 50)
            
            # Recorremos la lista para sacar cada producto
            for producto in lista_productos:
                titulo = producto["title"]
                precio = producto["price"] # En esta tienda de prueba los precios están en USD
                
                print(f"📦 Producto: {titulo}")
                print(f"💰 Precio:   ${precio:,.2f} USD")
                print("-" * 50)
                
        else:
             print(f"🛑 Error inesperado. Código: {respuesta.status_code}")
            
    except Exception as e:
        print(f"🔥 Ocurrió un error crítico: {e}")

# ==========================================
# ZONA DE EJECUCIÓN
# ==========================================
hackear_tienda_de_practica()