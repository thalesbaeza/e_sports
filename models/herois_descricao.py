from database import tabelas

def api_herois_descricao(dicionario, nur_req):
    try: 
        if len(dicionario[nur_req]) > 0:
            lista = []
            data = []
            data2 = []
            remover = ['roles']
                
        for a in list(dicionario[nur_req]):
            if a not in remover:
                lista.append(a)
                        
        for b in lista:
            data.append(dicionario[nur_req][b])

            tabelas.criar_herois_descricao()
            tabelas.inserir_herois_descricao(data)

        try:
            for c in range(0,7):
                if len(dicionario[0]['roles']) > 0:
                    data2.append(dicionario[nur_req]['id'])
                    data2.append(dicionario[nur_req]['roles'][c])

                    tabelas.criar_herois_estilo()
                    tabelas.inserir_herois_estilo(data2)

                    data2.clear()
                        
        except:
            pass

    except:
        print("Requisição sem retorno")