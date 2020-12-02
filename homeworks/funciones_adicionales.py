def unos_por_posicion(a):
    '''
    unos_por_posicion
    
    Esta función guarda el arreglo generado a partir 
    del resto que deja cada número del arreglo "a"     #esta función al final no la ocupé dado que enontré
    al ser dividido por 2.                             #una forma más fácil de hacer lo que se pedía
    
    '''
    vector_binario=a%2
    return(vector_binario)

def df_filtrado(df,column,lista_de_busqueda):
    '''
    df_filtrado
    
    Esta función se encarga de crear un dataframe que solo contiene la 
    información de los valores contenidos en una lista dada.
    
    Parámetros
    ----------
    
    df: pd.DataFrame
    column: str , columna de interés
    lista_de_busqueda: list , lista con los valores de interés
    
    '''
    lista=[]
    
    for i in list(df.index.values):
        for j in lista_de_busqueda:
            if df[column][i]==j:
                lista.append(i)
                
    df_nuevo=df.filter(items=lista,axis=0)
    
    return(df_nuevo)
        



    