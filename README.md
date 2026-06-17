# SecretRadar Edu

O **SecretRadar Edu** é uma ferramenta open source educacional feita em Python para detectar possíveis credenciais expostas em projetos locais, como API keys, tokens, senhas e chaves privadas.

A proposta do projeto é ajudar estudantes e desenvolvedores iniciantes a identificarem riscos antes de publicarem seus códigos em repositórios públicos.

## Objetivo

O objetivo do SecretRadar Edu é analisar arquivos de uma pasta local e procurar por padrões que possam indicar credenciais expostas. A ferramenta mostra um relatório simples no terminal e mascara parte do conteúdo encontrado, evitando expor ainda mais as informações sensíveis.

Este projeto tem foco defensivo e educativo. Ele não explora vulnerabilidades, não valida credenciais e não envia nenhum dado para servidores externos.

## Aviso ético

Esta ferramenta deve ser usada apenas em projetos próprios ou em projetos nos quais você tenha autorização para realizar a análise.

O SecretRadar Edu foi criado com finalidade educacional, como forma de conscientizar sobre boas práticas no tratamento de credenciais em projetos de software.

## Funcionalidades iniciais

* Analisa arquivos de uma pasta local;
* Procura padrões como `api_key`, `token`, `password`, `senha` e `secret`;
* Detecta possíveis chaves privadas;
* Mostra um relatório simples no terminal;
* Mascara parte do conteúdo encontrado;
* Ignora pastas como `.git`, `venv`, `.venv` e `__pycache__`.

## Estrutura inicial do projeto

```text
secret-radar-edu/
├── .gitignore
├── exemplo.env
├── README.md
└── secretradar.py
```

## Requisitos

Para executar o projeto, é necessário ter o Python instalado.

Versão recomendada:

```text
Python 3.10 ou superior
```

## Como usar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/secret-radar-edu.git
cd secret-radar-edu
```

Execute a ferramenta informando a pasta que deseja analisar:

```bash
python secretradar.py caminho/da/pasta
```

Exemplo analisando a própria pasta do projeto:

```bash
python secretradar.py .
```

## Exemplo de arquivo para teste

O projeto possui um arquivo chamado `exemplo.env` com dados falsos para testar a ferramenta:

```env
API_KEY=abc123456789teste
TOKEN=token_fake_123456789
PASSWORD=minhaSenhaTeste123
SECRET=segredoFake123456789
```

Esses valores são fictícios e servem apenas para demonstrar o funcionamento do scanner.

## Exemplo de saída

Ao executar a ferramenta, a saída pode ser parecida com:

```text
Possíveis credenciais encontradas:

Arquivo: ./exemplo.env
Linha: 1
Conteúdo mascarado: API_***************este
----------------------------------------

Total de achados: 4
Aviso: os resultados podem conter falsos positivos.
```

## Impacto social

O projeto busca contribuir com a conscientização sobre segurança em projetos de software livre. Muitos estudantes e desenvolvedores iniciantes podem acabar publicando senhas, tokens ou chaves sem perceber. O SecretRadar Edu ajuda a identificar esse tipo de risco de forma simples e educativa.

## Próximos passos

* Melhorar os padrões de detecção;
* Separar o código em módulos;
* Criar testes automatizados;
* Gerar relatório em JSON;
* Adicionar classificação por severidade;
* Criar documentação com boas práticas sobre uso de arquivos `.env`.

## Contribuição

Contribuições são bem-vindas. O projeto ainda está em fase inicial e pode receber melhorias na detecção de padrões, documentação, testes e organização do código.

## Licença

Este projeto será disponibilizado sob uma licença open source.
