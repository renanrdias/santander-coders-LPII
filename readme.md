# Projeto do módulo - Lógica de Programação II

### Parte 1

O grupo foi convidado para auxiliar no desenvolvimento e gerência anual de um sistema de pessoas na empresa. Para cada ano, você possui informações de todas as movimentações da empresa, como admissões, promoções e demissões, de 2010 até 2023. (uma pasta por ano)

Desenvolva o sistema que faça, de forma automática, a gerência de todas as pessoas da empresa. No final, o projeto deve:
1.	Criar um arquivo JSON, a cada ano, contendo todas as informações importantes dos funcionários.
2.	Criar um arquivo log para todas as demissões de pessoas. (e.g. txt)

### Parte 2

Além disso, a cada ano a empresa faz um evento de confraternização de final de ano para funcionários. Dentro do cadastro, adicione informações sobre o comparecimento a cada ano do evento. 

Infelizmente, essa festa contém alguns penetras, e você quer avaliar quantas pessoas não autorizadas entraram na confraternização. Faça uma validação do usuário (isto é, se o ID e o Nome usado no evento realmente batem com o cadastro) e crie um arquivo para armazenar essas informações de pessoas, de modo a evitar que essa pessoa seja proibida de entrar em outros anos. 

Crie também funcionalidades que você julgar interessante para o projeto. 😊


## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências necessárias.

```bash
pip install -r requirements.txt
```

## Uso

```python
python main.py
``` 

## Observações

O projeto foi desenvolvido sobre uma plataforma baseada em unix. Para rodá-lo em sistema windows, pode ser necessário substituir o caracter "/" por "\\" para evitar erros na definição dos caminhos aos diretórios e arquivos. Essa substituição deve ser feita nos arquivos: 
- dl.cfg 
- funcionarios_final.py
- penetras.py

## License

[MIT](https://choosealicense.com/licenses/mit/)