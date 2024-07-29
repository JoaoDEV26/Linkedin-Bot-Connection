# LinkedIn Connection Bot

Este projeto utiliza Selenium para automatizar o processo de conexão com pessoas no LinkedIn. O script abre o LinkedIn, faz login, pesquisa por uma categoria de trabalho , filtra os resultados por pessoas, e envia uma mensagem personalizada ao se conectar.

## Pré-requisitos

- Python 3.x
- Selenium
- WebDriver para o navegador que você está usando (neste caso, ChromeDriver)

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/linkedin-connection-bot.git
    cd linkedin-connection-bot
    ```

2. **Instale as dependências:**

    ```bash
    pip install selenium
    ```

3. **Baixe o WebDriver:**

    Baixe o ChromeDriver de acordo com a versão do seu navegador [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e coloque o executável no PATH do seu sistema ou no mesmo diretório do script.

## Uso

1. **Configure suas credenciais do LinkedIn:**

    No script `credentials.txt`, substitua as variáveis `user`, `senha`, `profissao` e `texto` com seu e-mail e senha do LinkedIn, a profissao que deseja buscar juntamente com a mensagem a ser enviada.

    ```plaintext
    user:seuemail@example.com
    senha:suasenha
    profissao:profissao a procurar
    texto:texto para mensagem
    ```

2. **Execute o script:**

    ```bash
    python linkedin_connection_bot.py
    ```

    O script irá:

    - Abrir o LinkedIn.
    - Fazer login com as credenciais fornecidas.
    - Pesquisar pela profissão definida.
    - Filtrar os resultados por pessoas.
    - Clicar nos botões "Conectar".
    - Enviar uma mensagem personalizada para cada pessoa.

## Observações

- **Segurança:** É altamente recomendado utilizar um método seguro para gerenciar suas credenciais, como variáveis de ambiente ou um gerenciador de senhas. Nunca compartilhe suas credenciais em um repositório público.

- **Limitações:** Automação em plataformas como LinkedIn pode violar seus Termos de Serviço. Use este script por sua conta e risco.

## Contribuição

Se você quiser contribuir com este projeto, sinta-se à vontade para abrir um Pull Request ou criar uma Issue.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
