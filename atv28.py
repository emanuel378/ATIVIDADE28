# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar
produtos = []
estoque = []
for i in range(5):
    pro =input(f"Digite o {i+1} produto:")
    quantidade= int(input(f"Digite a quantidade do {i+1} produto:"))
    produtos.append(pro)
    estoque.append(quantidade)
    


zerado = []
for i in range(5):
    if estoque[i]==0:
        zerado.append(produtos[i])
if zerado:
    print(f"Produtos com estoque zerado: {', '.join(zerado)}")
else:
    print("Todos tem no estoque")

#obs:se estoque o i dele for igual a 0 ele vai armazenar o produto mais a indice,tipo arroz e feijão