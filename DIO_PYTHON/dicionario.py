contatos ={
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766","extra":{"a": 1}},
    
}

telefone = contatos["giovanna@gmail.com"]["telefone"]

print(telefone)


extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)


for chave in contatos:
    print(chave,contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave,valor)






pessoa = {"nome":"Guilherme","idade":28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"
print(pessoa)



contatos = {
        "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},

}

resultado = contatos.keys()
print(resultado)

novo_diconario = {"a":100, 1:"teste", "b":"python"}
print(novo_diconario.keys())



resultado = contatos.pop("guilherme@gmail.com")
print(resultado)

resultado = contatos.pop("guilherme@gmail.com","Não encontrou")
print(resultado)




contato = {"nome":"Guilherme", "telefone":"3333-2221"}

contato.setdefault("nome", "Giovanna")
print(contato)

contato.setdefault("idade", 28)
print(contato)



contatos ={
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766","extra":{"a": 1}},
    
}




resultado = "guilherme@gmail.com" in contatos
print(resultado)

resultado = "megui@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]
print(resultado)

resultado = "telefone" in contatos ["guilherme@gmail.com"] 
print(resultado)
                                                            