def mostrar_temas(lista_bzrp:list):            
    print("Lista de temas: ") 
    for cancion in lista_bzrp:
        mostrar_video(cancion)

def mostrar_video(un_video:dict):
    print(f"Titulo: {un_video['title']} -",
          f"Vistas: {un_video['views']/1000000} -",
          f"Tiempo: {un_video['length']/60}min -")