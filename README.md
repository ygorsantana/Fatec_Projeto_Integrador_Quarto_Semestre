# Objetivo 🎯
Projeto Ecoponto 🚀 

Projeto desenvolvido com o principal intuito de gerar retorno financeiro, através da logística reversa. Incentivar indivíduos a entregar materiais recicláveis em postos de coleta específico para troca-lo por uma moeda específica que poderá se transacionada em comércios parceiros, estimulando a coleta dos materiais e também o comercial local.

# Used technologies 💻
    
    * Python
    * Django
    * MongoDB
    * Pytest


# Instalação ⚙
Para executar o projeto siga os passos a seguir

  * Clone o repositório na máquina
  ```sh
  git clone https://github.com/LuizaPascuotte/Fatec_Projeto_Integrador_Quarto_Semestre
  ```
  * Instale uma virtualenv
  ```sh
  pip install virtualenv
  ```
  * Crie um ambient virtual
  ```sh
  virtualenv venv 
  ```

  * Entre no ambiente virtual
  ```sh
  venv/Scripts/activate
  ```

  * Na raiz do projeto execute
  ```sh
  python manage.py runserver
  ```

# Build do FrontEnd (Para desenvolvimento)

É necessário após modificações no FrontEnd realizar o build do mesmo e upload para a pasta de backend no mesmo diretório do arquivo manage.py.

  * Para realizar o build
  ```sh
  yarn build 
  ```
  ou 

  ```sh
  npm run build
  ```
  A execução irá gerar um arquivo chamado build adicione-o no pasta do backend

# Estrutura de arquivos

## Bibliotecas 📚

### **Djongo**
A biblioteca Djongo realiza o manejamento do banco de dados NoSQL Mongo com o framework Django, por meio de models de ORM é possível executar o CRUD sem muito esforço, além de realizar a interpretação automática de SQL para NoSQL


### **request_manager_attenuare**
Biblioteca que encapsula a biblioteca request, e realiza o manejamento de erros como SSL, ConnectionError etc... E realiza diversas tentativas até que o output seja o desejado ou se as tentativas atinjam um número específico. Essa biblioteca também gera um objeto do tipo BeautifulSoup caso a resposta seja favorável.