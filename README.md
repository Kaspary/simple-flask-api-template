# Getting Started
- Environment
    - É necessário criar um arquivo com o nome ".env" na raiz do projeto flesk (pasta "api/"), onde devem ser configurado as variáveis de ambiente, com o seguinte layout.
    ```
    SERVER_NAME=<Ex: 127.0.0.1:5000>
    FLASK_ENV=<Ex: development ; Ex: production>
    SECRET_KEY=<Ex: 2>HeLzj"vr#6&cZ7=/,GJBM~8-=SVbMZHE9;t;yQmbWr<yF_)by(%W;+(QC<trrFe}F@*5/$.#&pCwk)>
    JWT_EXPIRATION_DELTA=<Ex: 24>
    DEBUG=<Ex: True>
    TESTING=<Ex: True>
    SQLALCHEMY_DATABASE_URI=<Ex: sqlite:///db.sqlite>
    ```
## Development environment

1.	Software dependencies
    - Python: 3.8.

2.	Installation process
    - Instalar dependências com `pip install -r requirements.txt`.

3. Start server
    - Criar o schema inicial do banco, isto pode ser feito com o comando `flask db init`;
    - Cadastrar um usuário, isto pode ser utilizado o comando `flask user create my_user --admin`. Este comando irá criar um usuário administrador, com o username "my_user";
    - Executar `flask run`.
# Commands
- Comandos para gerenciamento de usuários
    - `flask user create`
    - `flask user list`
    - `flask user delete`
    - `flask user activation`
    - `flask user newpassword`



## Base Url:
- http://127.0.0.1:5000

## Headers:
- Authorization: **JWT \<token\>**
    - Exemplo: `Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjU0NDcwMTEsImlhdCI6MTYyNTM2MDYxMSwibmJmIjoxNjI1MzYwNjExLCJpZGVudGl0eSI6MX0.sG-2Hb8fP83T1x5IkMmy6oifDXGs5w7WlSxr0XzWhfY`

## Rotas:
- Autenticação
	- Rota: http://127.0.0.1:5000/auth
    - Retorna um json web token, para consultar as rotas que exigem autenticação. Este token possui uma validade de 24 horas, ao fim deste período, deve ser realizada uma nova autenticação.
    - Método: **POST**
    - Exemplo:
        ```json
        {
            "username":"user",
            "password":"user1234"
        }
	- Resposta:
    	```json
        {
        	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGtiOiJIUzI1NiJ9.eyJleHAiOjE2MjU1ODk2NDgsIml
            hdCI6MTYyNTUwMzI0OCwibmJmIjoxNjI1NTAzMjQ4LCJpZGVudGl0esi6Mn0._xhhjXEy-ntnF2iSL-w2
            S9ehfn3lTNkmPJ33bpUR-ec"
        }
