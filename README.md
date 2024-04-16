
# Configuração de Ambiente Python Conversor dívida ativa

Este guia fornece instruções passo a passo para configurar um ambiente Python isolado, criado para sanitizar dados do nosso sistema de dívida ativa, usando em sistemas operacionais Windows ou macOS.

## Pré-requisitos

Antes de iniciar, certifique-se de que o Python 3 está instalado em seu sistema. Você pode verificar isso executando:

```bash
python  --version
```

ou

```bash
python3  --version
```

Se o Python não estiver instalado, você pode baixá-lo do [site oficial do Python](https://www.python.org/downloads/).

## Faça o download do projeto via google drive

1. <https://drive.google.com/drive/folders/1s1ywYf0thoJoRLEvpoTZV7Pe-9xbAZOB?usp=drive_link>

## Capturar o arquivo xlsx ou csv não sanitizado

1.Pedir o arquivo não sanitizado ao sinceti e/ou a pessoa responsável pelo mesmo.

2.Guarde o arquivo no seu computador local, no seu ambiente para a sanitização.

3.Utilize a pasta Input e coloque o arquivo dentro da pasta do projeto.

4.Renomeie o arquivo para RegistroDeDados.xlsx ou RegistroDeDados.csv, dependendo do tipo de arquivo

## Configuração no Windows

1. **Criar o ambiente virtual**:

Abra o Prompt de Comando e navegue até o diretório do seu projeto usando `cd caminho/do/seu/projeto`, neste caso seria no path onde o arquivo collect_info.py se encontra. Então, execute:

```bash
python -m venv venv
```

2. **Ativar o ambiente virtual**:
Para ativar o ambiente virtual, execute:

```bash
.\venv\Scripts\activate
```

3. **Instalar dependências**:

Certifique-se de que o arquivo `requirements.txt` está no diretório do projeto. Instale as dependências com:

```bash
pip install -r requirements.txt
```

4. **Executar o script**:

Execute o script Python com:

```bash
python collect_info.py
```

## Configuração no macOS

1. **Criar o ambiente virtual**:

Abra o Terminal e navegue até o diretório do seu projeto com `cd caminho/do/seu/projeto`. Execute:

```bash
python3 -m venv venv
```

2. **Ativar o ambiente virtual**:

Para ativar o ambiente virtual no macOS, use:

```bash
source venv/bin/activate
```

3. **Instalar dependências**:

Assegure-se de que o arquivo `requirements.txt` está no diretório do projeto. Instale as dependências com:

```bash
pip install -r requirements.txt
```

4. **Executar o script**:

Execute o script Python com:

```bash
python3 collect_info.py
```

## Desativar o ambiente virtual

Para sair do ambiente virtual, você pode usar o comando `deactivate` em ambos os sistemas:

```bash
deactivate
```
