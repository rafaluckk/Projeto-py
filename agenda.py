AGENDA = {}

AGENDA['rafael'] = {
    'telefone': '99223323',
    'email': ' rafael@gmail.com',
    'endereco': 'Av.1',
}

AGENDA['maria'] = {
    'telefone': '99533323',
    'email': ' maria@gmail.com',
    'endereco': 'Av.2',
}



def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print('--------------------------------------------')


