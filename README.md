# project_app_texoit
Este é o repositorio para a aplicação restful no segundo nivel de Richardson, que trabalha com dados de filmes
solicitada pelo teste da empresa TEXO IT, que foi desenvolvida usando um SO Linux Mint 21.1 e Python 3.10.
Para poder rodar os testes da aplicação utilize comando a seguir desde a pasta raiz do repositorio:
    
    source run_test.sh

Ou para rodar a aplicação no lcoalhost:7000:
    
    source run_api.sh


Logo a composição do repositorio tem a seguinte estrutura de arquivos:

```
/ -> raiz do repositorio
app_texoit/ -> pasta da aplicação
├── data -> pasta para os dados
│   ├── movielist.csv -> dados de input recebidos para o teste
├── errors ->  pasta para setuar os error handlers
│   ├── handlers.py
│   ├── __init__.py
│   └── templates -> pasta dos tempaltes dos erros
│       └── errors 
│           ├── 403.html
│           ├── 404.html
│           └── 500.html
├── __init__.py
├── main.py -> ponto de entrada do repositorio
├── movies -> pasta para aplicação principal
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py -> modelos de dados
│   └── routes.py -> arquivo dos endpoints
├── settings.py -> arquivo com as configurações
├── templates
│   └── base.html -> base template 
├── test
│   ├── __init__.py
│   ├── test.py -> arquivo com os testes
├── utils.py
└── wsgi.p 
```

## Descrição de metodos e retornos dos endpoints:

## GET
Este endpoint retorna a lista dos filmes na base de dados em formato json.
#### /read_movies
**Retorna:**

    [
      {
        "producers": "updated producers",
        "studios": "updated studios",
        "title": "updated title",
        "winner": "yes",
        "year": 1900
      },
      {
        "producers": "Jerry Weintraub",
        "studios": "Lorimar Productions, United Artists",
        "title": "Cruising",
        "winner": null,
        "year": 1980
      },
      ]

## GET
Este endpoint retorna os minimos e maximos dos intervalos.
#### /main_task
**Retorna:**

    {
      "max": [
        {
          "followingWin": 1990,
          "interval": 6,
          "previousWin": 1984,
          "producer": "Bo Derek"
        }
      ],
      "min": [
        {
          "followingWin": null,
          "interval": 0,
          "previousWin": 1980,
          "producer": "Allan Carr"
        },
        {
          "followingWin": null,
          "interval": 0,
          "previousWin": 1981,
          "producer": "Frank Yablans"
        },
        ...
      ]
    }


## POST
Este endpoint é para criação de novos filmes.
#### /create_movie/year=year/title=title/studios=studios/producers=producers/winner=winner
**Retorna:**

    {"status": "movie inserted" }


## PUT
Este endpoint é para atualização completa dos filmes.
#### /update_movie/id=id_number/year=year/title=:title/studios=studios/producers=producers/winner=winner
**Retorna:**

    {
      "data": {
        "id": 1,
        "producers": "abm",
        "studios": "goodstudios",
        "title": "thebestmovie",
        "winner": "yes",
        "year": 1987
      },
      "status": "data updated"
    }


## PATCH
Este endpoint é para atualização parcial dos filmes.
#### /patch_movie/id=id_number/year=year
#### /patch_movie/id=id_number/title=title
#### /patch_movie/id=id_number/studios=studios
#### /patch_movie/id=id_number/producers=producers
#### /patch_movie/id=id_number/winner=winner
**Retorna:**

    {
        "data": {
        "id": 1,
        "producers": "abm",
        "studios": "goodstudios",
        "title": "thebestmovie",
        "winner": "yes",
        "year": 200
      },
      "status": "data partially updated"
    }


## DELETE
Este endpoint permite eliminar filmes.
#### /delete_movie/id=id_number
**Retorna:**

    [
      {
        "status": "movie deleted"
      }
    ]

