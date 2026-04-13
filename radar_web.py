import requests 

def rastrear_en_mercadolibre(nombre_producto):
    print(f"📡 Enviando dron a Mercado Libre para buscar: '{nombre_producto}'...")
    
    url = f"https://api.mercadolibre.com/sites/MLM/search?q={nombre_producto}"
    
    # 1. EL DISFRAZ: Falsificamos nuestra identidad para parecer un navegador Google Chrome normal
    disfraz = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # 2. Le ponemos el disfraz al dron al momento de tocar la puerta
        respuesta = requests.get(url, headers=disfraz)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            lista_resultados = datos["results"]
            
            if len(lista_resultados) > 0:
                primer_producto = lista_resultados[0]
                
                titulo = primer_producto["title"]
                precio = primer_producto["price"]
                enlace = primer_producto["permalink"]
                
                print("\n✅ ¡Objetivo Encontrado!")
                print("-" * 50)
                print(f"📦 Producto: {titulo}")
                print(f"💰 Precio:   ${precio:,.2f} MXN")
                print(f"🔗 Comprar:  {enlace}")
                print("-" * 50)
            else:
                print("❌ No se encontraron productos con ese nombre.")
                
        elif respuesta.status_code == 403:
             print("🛑 Error 403: El guardia de Mercado Libre nos descubrió y nos bloqueó el paso.")
        else:
            print(f"⚠️ Error inesperado. Código: {respuesta.status_code}")
            
    except Exception as e:
        print(f"🔥 Ocurrió un error crítico: {e}")

# ==========================================
# ZONA DE PRUEBAS
# ==========================================
rastrear_en_mercadolibre("Nintendo Switch OLED")
rastrear_en_mercadolibre("Cargador UGREEN 65w")