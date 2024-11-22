database = {"cadastros":[
    
    {"fornecedores":[

        {"login":"serjinho",
         "senha":"DaleDele"},

        {"login":"thaisTralando",
         "senha":"DoiPapai"}

    ]},


    {"usuarios":[

        {"login":"irmaoDoSerjinho",
         "senha": "DeleDole"},

        {"login": "xaolinMatador",
         "senha": "7070"}
        

    ]}

]}



class NotFoundError(Exception):
    pass

class NadaCadastrado(Exception):
    pass

def todosCadastros():
    return database["cadastros"]

def todosFornecedores():
    return database["cadastros"][0]

def todosUsuarios():
    return database["cadastros"][1]

def loginFornecedor(login, senha):
    fornecedores = database["cadastros"][0]["fornecedores"]
    
    for fornecedor in fornecedores:
        if fornecedor["login"] == login and fornecedor["senha"] == senha:
            return True

def loginUsuario(login, senha):  
    usuarios = database["cadastros"][1]["usuarios"]
    
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            return True
    return False
               
def deleteUsuario(login, senha):
    usuarios = database["cadastros"][1]
    for usuario in usuarios:
        if usuarios[usuario]["login"] == login and usuarios[usuario]["senha"] == senha:
            return usuarios.remove(usuario)
       
        
def deleteFornecedor(login, senha):
    fornecedores = database["cadastros"][0]
    for fornecedor in fornecedores:
        if fornecedores[fornecedor]["login"] == login and fornecedores[fornecedor]["senha"] == senha:
            return fornecedores.remove(fornecedor)
        
        
      


def cadastrarUsuarios(dicionario_usuario):
    return database["cadastros"][1].append(dicionario_usuario)

def cadastrarFornecedor(dicionario_fornecedor):
    return database["cadastros"][0].append(dicionario_fornecedor)




