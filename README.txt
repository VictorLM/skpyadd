REQUER PYTHON 3.X E LIB skpy (pip install skpy)

1 - Atualizar a lista de contatos no arquivo contacts.json
MODELO contacts.json:

[
    {
        "nome": "Nome do contato (não requerido)",
        "id": "Id do contato no Skype (requerido)"
    },
    {
        "nome": "Nome do contato (não requerido)",
        "id": "Id do contato no Skype (requerido)"
    }
]

2 - Pegar o token de acesso do usuário Skype executando: python getToken.py
3 - Executar: python addContacts.py para adicionar os contatos listados no arquivo contacts.json
