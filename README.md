# O Projeto Vacina+

Projeto desenvolvido para o processo seletivo do EDITAL Nº 046/2020 – LAIS/UFRN, na Fase 2 - Sistemas de informação e
Sistemas inteligentes.

O Projeto Vacina+ permite que os estabelecimentos de saúde tenham controle e forneçam um meio de acessibilidade para
agendamento de vacinação da população. Até o presente momento, está habilitado o gerenciamento de estabelecimentos de
saúde, vacinas, estoques e agendamentos.

O Diagrama de Entidade e Relacionamento do projeto está disponível [aqui](SQL/vaccine_card.png), e alguns SQL de 
consultas estão disponíveis no diretório [SQL](SQL/).

---

## Acesso ao Heroku

Acesse [aqui o projeto hospedado no Heroku](https://warm-wildwood-36848.herokuapp.com/) em sua versão de
desenvolvimento. Ou utilize o link a seguir:
> https://warm-wildwood-36848.herokuapp.com/

* **Usuário**: lais
* **Senha**: lais

---

Por estar utilizando um Free Dyno, o sistema pode ficar offline em alguns momentos. Caso isso aconteça, por favor nos
comunique!

---

## Apps/Módulos

#### Core

O app **Core** é responsável por organizar as _urls_ para cada APP. Também é responsável por manter os diretórios de
arquivos estáticos, templates e funções que podem ser utilizadas por todo o projeto. Dentro do **Core** está a pasta _
settings_ com os arquivos de configuração do Django até o momento.

#### API

O app **API** é responsável pelas _viewsets_ e _routers_ do projeto. Cada app possui o seu arquivo com os serializers,
responsáveis por transformar os dados para transmitir pela API.

#### Logistic

O app **Logistic** é responsável por gerenciar os _models_, as _views_ e as _urls_ referentes a logística das vacinas.
Informações sobre cidade, estado, estabelecimento de saúde, lote e estoque estão presentes neste app. Dentro desse app
existe o comando create_cluster, responsável por subir ao banco de dados informações sobre os estados e cidades do país.

#### Scheduling

O app **Scheduling** é responsável por gerenciar os _models_, as _views_ e as _urls_ referentes, nesse momento inicial
do projeto, aos agendamentos de vacinação. Informações sobre o evento e o registro de vacinação estão presentes neste
app. Nesse app está presenta também a funcão _overridden_ do _save_ Evento, para quando houver qualquer atualização ser
disparado um e-mail para o paciente.

#### Vaccination

O app **Vaccination** é responsável por gerenciar os _models_, as _views_ e as _urls_, nesse momento inicial do projeto,
os dados referentes as vacinas e os reforços das vacinas.

#### App

O app **App** é responsável por gerenciar as _views_ e as _urls_ que dão acesso à visualização por parte do paciente, no
qual pode fazer visualizar o cartão de vacina, agendar uma vacinação e verificar os agendamentos efetuados.

---

## Configuração do Projeto

### Tecnologias

O Projeto Vacina+ está mantido seu _backend_ com a linguagem Python 3.7, sob o _framework_ Django 3.1. Além destes, o
projeto inclui: [Django-rest-framework](https://www.django-rest-framework.org/) para o gerenciamento do _webservice_ e
o [Django-simple-history](https://django-simple-history.readthedocs.io/en/latest/) para gerir o histórico de
atualização do agendamento de vacinação.

O _frontend_ foi desenvolvido utilizando HTML5, CSS e JS com suporte do
_framework_ [Bootstrap4](https://getbootstrap.com/) e do [CoreUI](https://coreui.io/). Além deles, foram utilizados plugins
que dão suporte, como: [Select2](https://select2.org/), [Toastr](https://github.com/CodeSeven/toastr)
, [Momentjs](https://momentjs.com/), [Bootstrap-datapicker](https://bootstrap-datepicker.readthedocs.io/en/latest/),
entre outros.

### Primeiros passos

Inicialmente, é necessário criar o ambiente virtual e então executar o seguinte comando para instalar as dependências do projeto Python:
> pip install -r requeriments.txt

Configure o acesso ao banco de dados e então efetue a migração dos _models_:
> python manage.py migrate

E, então inicie o projeto com o seguinte comando:
> python manage.py runserver

Caso o navegador não abra o projeto, clique no link a seguir ou abra uma nova aba e digite:
> http://localhost:8000

---

#### Opcional

Caso queira carregar as informações dos estados e cidades, pode utilizar o comando a seguir na raiz do projeto, após ter
executado as migrações:
> python manage.py create_cluster

---

### Docker habilitado!

Caso tenha habilidade com o Docker, o projeto possui a configuração para criar os containers do projeto e do banco de
dados!
Lembre de configurar as variáveis de ambiente para que o projeto funcione corretamente, tá?

Para criar os containers e executar o projeto, basta digitar na raiz no diretório que está o arquivo **docker-compose.yml**:
> docker-compose up -d —build

---

## Variáveis de Ambiente

| Variavel de Ambiente | Possíveis valores |
| --- | --- |
| DJANGO_SETTINGS_MODULE | vaccine_card.settings.local |
| DJANGO_SECRET_KEY | pode ser gerado pela função do django _get_random_secret_key()_ ou _secrets.token_urlsafe()_ do Python 3.6+ |
| EMAIL_HOST | smtp.gmail.com |
| EMAIL_PORT | 587 |
| EMAIL_HOST_USER | sender@gmail.com |
| EMAIL_HOST_PASSWORD | P4s$W0rd |
| EMAIL_USE_TLS | True |
| EMAIL_RECIPIENT | recipient@gmail.com |
| DATABASE_URL | URL de conexão com o banco de dados* |

[*] A variável de ambiente DATABASE_URL é utilizado apenas no _deploy_, caso queira utilizar a versão local, as
configurações do banco de dados podem ser definidas diretamente no arquivo settings/local.py.

---

## Implementações futuras

1. Testes automatizados;
1. Cadastro de Dias e Horários possíveis para vacinação;
1. Concluir os fluxos solicitados na avaliação;
1. Carregamento de cidade com base no estado, assim como na _view_ de agendamento do paciente;
1. Login com Google OAuth2;
1. Perfis de acesso;
1. Construção do Websocket;
1. Implementação do Push Notification;
1. Criar blocos de agendamento;
1. Relatórios que deem suporte a melhoria do agendamento e da vacinação.
