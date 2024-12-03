# Conversor DOCX para PDF

Uma aplicação simples em Python com interface gráfica (usando `tkinter`) para converter arquivos `.docx` em PDFs.

## 🛠 Funcionalidades

- Selecionar um arquivo `.docx` para conversão.
- Escolher a pasta de saída para salvar o PDF.
- Conversão rápida e eficiente com um clique.

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina e as seguintes bibliotecas instaladas:

- [`python-docx`](https://pypi.org/project/python-docx/): Para manipulação de arquivos `.docx`.
- [`fpdf`](https://pypi.org/project/fpdf/): Para criação de arquivos PDF.

### Instalando as dependências:

Use o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install python-docx fpdf
 ```
1.Clone o repositório:

 ```

git clone https://github.com/seu-usuario/conversor-docx-pdf.git
cd conversor-docx-pdf

 ```



2. Certifique-se de que todas as dependências estão instaladas (veja a seção "Pré-requisitos").

3. Execute o programa principal:

   ```bash
   python app.py
   ```

4. Na interface gráfica:
   - Clique em "Selecionar" para escolher o arquivo `.docx` a ser convertido.
   - Escolha a pasta de saída onde o arquivo PDF será salvo.
   - Clique no botão "Iniciar Conversão" para converter e salvar o arquivo.

5. O arquivo PDF será gerado na pasta de saída especificada.

## 📂 Estrutura do Projeto

```
conversor-docx-pdf/
├── app.py          # Código principal da aplicação
├── README.md       # Documentação do projeto
└── requirements.txt # Dependências do projeto (opcional)
```

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---


