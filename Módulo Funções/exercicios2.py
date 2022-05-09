vendas = {
    'VE0001': (9868,'Concluído',''),'VE0002': (9642,'Concluído',''),
    'VE0003': (6007,'Concluído',''),'VE0004': (15562,'Concluído',''),
    'VE0005': (18752,'Cancelado','Estoque em Falta'),'VE0006': (16358,'Cancelado','Estoque em Falta'),
    'VE0007': (17045,'Concluído',''),'VE0008': (12230,'Concluído',''),
    'VE0009': (6747,'Concluído',''),'VE0010': (15114,'Concluído',''),
    'VE0011': (12497,'Concluído',''),'VE0012': (6001,'Concluído',''),
    'VE0013': (16227,'Cancelado','Cancelada pelo Cliente'),'VE0014': (16150,'Concluído',''),
    'VE0015': (17705,'Concluído',''),'VE0016': (9978,'Concluído',''),
    'VE0017': (4266,'Concluído',''),'VE0018': (11531,'Concluído',''),
    'VE0019': (10352,'Cancelado','Cancelada pelo Cliente'),'VE0020': (16544,'Concluído',''),
    'VE0021': (15488,'Concluído',''),'VE0022': (15828,'Concluído',''),
    'VE0023': (1218,'Concluído',''),'VE0024': (11560,'Concluído',''),
    'VE0025': (14220,'Concluído',''),'VE0026': (17839,'Concluído',''),
    'VE0027': (4050,'Concluído',''),'VE0028': (7594,'Cancelado','Estoque em Falta'),
    'VE0029': (19586,'Concluído',''),'VE0030': (8453,'Concluído',''),
    'VE0031': (3589,'Concluído',''),'VE0032': (13472,'Cancelado','Cancelada pelo Cliente'),
    'VE0033': (16994,'Concluído',''),'VE0034': (2139,'Concluído',''),
    'VE0035': (10173,'Concluído',''),'VE0036': (17784,'Cancelado','Estoque em Falta'),
    'VE0037': (12214,'Concluído',''),'VE0038': (5878,'Concluído',''),
    'VE0039': (2622,'Concluído',''),'VE0040': (9765,'Concluído',''),
    'VE0041': (8872,'Concluído',''),'VE0042': (16543,'Concluído',''),
    'VE0043': (8994,'Concluído',''),'VE0044': (4332,'Concluído',''),
    'VE0045': (19679,'Concluído',''),'VE0046': (14968,'Concluído',''),
    'VE0047': (6352,'Concluído',''),'VE0048': (11461,'Concluído',''),
    'VE0049': (5285,'Concluído',''),'VE0050': (11639,'Concluído',''),
    'VE0051': (6023,'Concluído',''),'VE0052': (4943,'Concluído',''),
    'VE0053': (5654,'Concluído',''),'VE0054': (11734,'Concluído',''),
    'VE0055': (2742,'Concluído',''),'VE0056': (5380,'Cancelado','Estoque em Falta'),
    'VE0057': (5578,'Concluído',''),'VE0058': (1897,'Concluído',''),
    'VE0059': (7857,'Concluído',''),'VE0060': (4472,'Concluído',''),
    'VE0061': (19874,'Concluído',''),'VE0062': (13323,'Cancelado','Cancelada pelo Cliente'),
    'VE0063': (5821,'Concluído',''),'VE0064': (4410,'Concluído',''),
    'VE0065': (16676,'Concluído',''),'VE0066': (10577,'Concluído',''),
    'VE0067': (10627,'Concluído',''),'VE0068': (1987,'Concluído',''),
    'VE0069': (13197,'Concluído',''),'VE0070': (15063,'Concluído',''),
    'VE0071': (14363,'Concluído',''),'VE0072': (10452,'Concluído',''),
    'VE0073': (15376,'Concluído',''),'VE0074': (4661,'Concluído',''),
    'VE0075': (13287,'Concluído',''),'VE0076': (8278,'Concluído',''),
    'VE0077': (7134,'Concluído',''),'VE0078': (16568,'Concluído',''),
    'VE0079': (17732,'Concluído',''),'VE0080': (5127,'Concluído',''),
    'VE0081': (4582,'Concluído',''),'VE0082': (14804,'Cancelado','Cancelada pelo Cliente'),
    'VE0083': (12362,'Concluído',''),'VE0084': (1148,'Concluído',''),
    'VE0085': (14018,'Concluído',''),'VE0086': (15891,'Concluído',''),
    'VE0087': (4517,'Concluído',''),'VE0088': (1770,'Concluído',''),
    'VE0089': (14926,'Concluído',''),'VE0090': (13627,'Concluído',''),
    'VE0091': (3047,'Concluído',''),'VE0092': (13924,'Concluído',''),
    'VE0093': (7158,'Concluído',''),'VE0094': (5942,'Concluído',''),
    'VE0095': (13480,'Concluído',''),'VE0096': (17686,'Concluído',''),
    'VE0097': (5722,'Cancelado','Cancelada pelo Cliente'),
    'VE0098': (16963,'Concluído',''),'VE0099': (14225,'Concluído',''),
    'VE0100': (12553,'Concluído','')
}

def calcular_stockout(dicionario):
    numerador = 0
    denominador = 0

    for venda in dicionario:
        valor, status, motivo = dicionario[venda]
        if status == 'Concluído':
            denominador += valor
        elif status == 'Cancelado' and motivo == 'Estoque em Falta':
            denominador += valor
            numerador += valor
    return numerador / denominador

print("{:.2%}".format(calcular_stockout(vendas)))

