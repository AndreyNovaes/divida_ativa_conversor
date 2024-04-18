# Configuração de Ambiente Python Conversor de Dívida Ativa

Este guia fornece instruções detalhadas para configurar um ambiente Python isolado, destinado à sanitização de dados do nosso sistema de dívida ativa. As instruções são válidas para sistemas operacionais Windows e macOS.

## Pré-requisitos

1. **Instalação do Python**:

Certifique-se de que o Python 3 está instalado em seu sistema. Verifique isso executando:

```bash
python --version
```

ou

```bash
python3  --version
```

Se o Python não estiver instalado, baixe-o do [site oficial do Python](https://www.python.org/downloads/).

2. **Instalação do Git**:

Para Windows, baixe e instale o Git de [Git for Windows](https://gitforwindows.org/). Durante a instalação, selecione "Use Git from the Windows Command Prompt" para garantir que o Git pode ser usado facilmente no CMD.

## Configuração Inicial

### Clonagem do Projeto

1. Abra o Prompt de Comando (Windows) ou Terminal (macOS).

2. Navegue até o diretório onde deseja armazenar o projeto, usando:

```bash
cd caminho/desejado
```

3. Clone o projeto do GitHub:

```bash
git clone https://github.com/AndreyNovaes/divida_ativa_conversor.git && cd divida_ativa_conversor
```

Isso criará uma pasta `divida_ativa_conversor` no diretório atual e entrará dentro dele,

### Instalação e Uso do Visual Studio Code

## Teste

1. **Instalação do Visual Studio Code**:
   - Baixe o Visual Studio Code do [site oficial do VS Code](https://code.visualstudio.com/).
   - Siga as instruções de instalação específicas para o seu sistema operacional (Windows, macOS, ou Linux).

2. **Abrindo o projeto no Visual Studio Code**:
   - Abra o Prompt de Comando (Windows) ou Terminal (macOS).
   - Navegue até o diretório do projeto onde você clonou o repositório. Por exemplo:

     ```bash
     cd caminho/para/divida_ativa_conversor
     ```

   - Execute o comando abaixo para abrir o diretório do projeto no VS Code:

     ```bash
     code .
     ```

   Este comando abrirá todos os arquivos do projeto dentro do Visual Studio Code, permitindo fácil acesso e edição.

### Preparação dos Dados

1. Solicite o arquivo não sanitizado ao responsável.

2. Salve o arquivo na sua máquina.

3. Mova o arquivo para a pasta `Input` dentro do diretório do projeto clonado,
4. Recomenda-se mover o arquivo de forma livre para dentro da pasta input, de forma simples, clicar, segurar e arrasta-lo para a pasta input.
5. ou Tente usar o terminal com os comandos abaixo:

```bash
move caminho\\do\\arquivo\\RegistroDeDados.xlsx caminho\\do\\seu\\projeto\\divida_ativa_conversor\\Input\\
```

ou para `.csv`:

```bash
move caminho\\do\\arquivo\\RegistroDeDados.csv caminho\\do\\seu\\projeto\\divida_ativa_conversor\\Input\\
```

## Configuração de Ambiente Python

### Windows

1. **Criar o ambiente virtual**:

Navegue até o diretório do projeto e crie o ambiente virtual:

```bash
cd caminho\\do\\seu\\projeto\\divida_ativa_conversor
python -m venv venv
```

2. **Ativar o ambiente virtual**:

```bash
.\\venv\\Scripts\\activate
```

3. **Instalar dependências**:

Certifique-se de que o arquivo `requirements.txt` está no diretório do projeto. Instale as dependências com:

```bash
pip install -r requirements.txt
```

4. **Executar o script**:

```bash
python collect_info.py
```

## Desativar o ambiente virtual

Para sair do ambiente virtual, você pode usar o comando `deactivate` em ambos os sistemas:

```bash
deactivate
```
