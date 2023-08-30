Saque

- keywords only, ou seja, Sacar (*,parâmetros) 
- Sugestão de parâmetros: saldo, valor, extrato, limite, numero_saques e limite_saques
- Sugestão de retorno: saldo e extrato

Depósito

- Posicional only, ou seja, Depositar (parâmetros,/)
- Sugestão de parâmetros: saldo, valor e extrato
- Sugestão de retorno: saldo e extrato

Extrato

- Posicional only e keyword only, Visualizar_extrato (posicionais,/,keywords)
- Argumentos posicionais: saldo
- Argumentos nomeados: extrato

Criar usuário(cliente)

- A função deve armazegar usuários em uma lista
- Usuário é composto por: nome, data de nascimento, cpf e endereço
- O endereço é uma string com o formato: logradouro, nro-bairro-cidade/sigla do estado
- Deve ser armazenado apenas os números do CPF
- Não se pode cadastrar 2 usuários com o mesmo CPF

Criar conta corrente

- A função deve armazenar contas em uma lista
- Uma conta é composta por: agência, número da conta e usuário
- O número da conta é sequencial, iniciando em 1
- O número da agência é fixo: "0001"
- O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário
- Para uma conta existir, ela precisa ser vinculada a um usuário, ou seja, ela é criada depois

Dica

- Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista
- Procura-se um usuário por meio do CPF para vinculá-lo a uma conta corrente