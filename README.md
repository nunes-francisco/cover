# Cover
Template para Microserviço python.

# `<Nome do Artefato>`

![Capa](assets/cover3.png)

## PRIMEIRAS PROVIDÊNCIAS

> 🚨 **I M P O R T A N T E **
>
> Estas informações dizem respeito a este template.
>
> Não se esqueça,  limpe estas sessões e insira informações sobre a sua aplicação.
> Por exemplo, apesar de todas as variáveis de ambinete estarem disponíveis é importante que aqui você mencione apenas o que sua aplicação irá utilizar, para que a informação fique precisa.
> Troque a imagem de capa coloque uma que faça referencia a sua aplicação.

## ✨Como criar seu repositório apartir deste template:

1. 🗺️  No Github, navegue até a página principal do repositório.
2. ♻️ Acima da lista de arquivos , clique em **"Use this template"**.
3. 🆕 Selecione **"Create new repository"**.
4. ⏳ Aguarde aproximadamente **20s** para que o processo de **CI** conclua a tarefa de renomear o projeto e editar arquivos.
5. 🎭 Clone seu seu repositório e execute algumas tarefas listadas abaixo.👇

> Olá! Você acabou de criar um novo projeto e baixou. Coisas boas vem por por aí. 🤘🏼
>
> Antes de continuar é necessário tomar algumas providências e verificar alguns pontos.
> Vamos lá:
>
> 1 - Editar o arquivo `pytest.ini` substituindo o trecho `<ROOT DIR>` para o nome do projeto
> 2 - Escolher uma imagem para servir de capa ao seu projeto. Basta salvar em `./assets/cover.png`
> 3 - Excluir esta seção do **README.md **

6. 👨‍💻 Apartir deste ponto você já pode codificar. 🚥 🏁

🔗 [Mais informações sobre como criar repositórios apartir de um template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

## Executando os testes unitários

Para executar os testes unitários se posicione na raiz do projeto e execute os comandos abaixo.
A configuração dos testes já está feita em `./pytest.ini`

```
pip install -r ./requirements.dev
pytest
```

## Variáveis de ambiente

As variáveis de ambiente abaixo são necessárias para o pleno funcionamento da solução.
Nesta configuração todas as váriaveis que correspomdem aos parâmetros de execução foram e serão criadas no [**secrets** ](https://docs.github.com/en/actions/security-guides/encrypted-secrets)do Github, bem como todo dado sensível.

Deixar apenas aquelas que realmente irá usar, removendo as demais dos arquivos, `docker-compose.yml`, `configuration.py` ou `settings.py`.
Isso evitará a propagação de parâmetros desnecessáriamente e evita poluir o ambiente para análises.

> **A V I SO ! 📣**
>Ao editar este documento mantenha nele apenas as informações relativas a sua aplicação, exibindo apenas as variáveis ( parâmetros ) que ela utiliza.

| Parâmetro                    | Propósito                                                                 | Exemplo                                |
| ----------------------------- | -------------------------------------------------------------------------- | -------------------------------------- |
| `DATABASE_URL`    | 🔗 URL  de conexão ao Redis                                   | `redis://localhost:6379`             |
| `MONGODB_POSTAGE_DATABASE_URL` | 🔗 URL  de conexão ao  Mongodb                                 | `mongodb://127.0.0.1:27017`          |
| `CASSANDRA_DATABASE_URL` | 🔗 URL  de conexão ao Cassandra                              | `127.0.0.1:9042`                     |
| `HTTP_PORT`              | 🚪 Porta HTTP do artefato                                                  | `8080`                               |
| `LOG_LEVEL`              | 🎚 Nível de geração de log                                              | `DEBUG, INFO, ERROR, CRTICAL, NOSET` |

##### 🐳Variáveis de ambiente usadas internamente no container

| Variável               | Propósito                                                                                                | Valor                          |
| ----------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `PYTHONPATH`          | 🔧 Path absoluto do artefato no container                                                                 | `/app`                       |
| `REGISTRY_URL`     | 🔗 URL do registro local, repositório de imagens Docker                                                  | `registry.local.com` |
| `GIT_ACCESS_TOKEN` | 🔑Token de acesso ao Github                                                                               | `terdsfdsdhjh-sfhfsdgfk` |
| `SERVICE_NAME`     | ⚙️ Nomeia o artefato, recbe seu valor dinamicamente                                                     | `SRVICE_NAME=${SRVICE_NAME}` |
| `TAG`              | 🏷 Tag da imagem do contêiner, valor dinamicamente do GitHub e deve cosrresponder a versão do artefato. | `TAG=0.1.0`               |

Sugere-se criar um arquivo `.env` com as variáveis citadas, quando estiver usando container standalone ou ao executar um serviço Swarm individual.

## Lançamento em produção 🚀

Este template carrega consigo um processo de CI com um workflow elaborado para proporcionar o máximo de conforto neste momento.

Com pequenos movimentos você irá colocar sua aplicação no ar em poucos minutos. Todo o processo desencadeará quando uma **TAG** for criada e publicada no Github.

> 👀 **O B S E R V A Ç Ã O**
>
> Para que haja coerência no fluxo, sugere-se que a **TAG** que você criar corresponda a versão da sua aplicação.

> 🚨 **I M P O R T A N T E**
>
> Toda versão de lançamento deve obrigatoriamente começar por **0.1.0** . Considere sempre as regras primárias do [Semantic Version-2.0.0](https://semver.org/lang/pt-BR/)
>
> Versionamento semântico, [resumo](https://github.com/mindbe/DevOps/blob/master/doc/git/versionamento-semantico-git-tag.md).

Exemplo:

Versão da aplicação:

```python
__version__ = '0.1.0'
```

Tag:

```bash
git tag -a -m "Versão minima viável" 0.1.0
```

#### Iniciando o processo de CI

Resumidamente o processo de **CI** é iniciado quando uma `tag` é lançada no Github, este evento inicia a sequencia de `jobs` no workflow do **Github Action** colocando a aplicação no ar.

A sequencia do comandos abaixo demostram como você de ve proceder:

1. Realize o `commit` das suas alterações:

   ```bash
   git commit -m "feat: Permite o envio de menssagem via app" module.py
   ```
2. Crie sua `tag` com valor correspondente a versão da sua aplicação:

   ```bash
   git tag -a -m "Feature com envio de menssagens para app" 0.1.0
   ```
3. Suba seu suas alterações no Github:

   ```bash
   git push
   ```

   Ou:

   ```bash
   git push origin master
   ```
4. Suba sua `tag`:
   Enviando uma tag unica:

   ```bash
   git push orgin 0.1.0
   ```

   Enviando todas as suas tags ( *Use com parcimônia* ):

   ```bash
   git push --tags
   ```

#### Bônus sobre tags

Abaixo segue alguns comandos de suporte que poderão ser uteis no dia-dia:

- Listando as tag criadas:

  ```bash
  git tag -l
  ```
- Removendo uma tag local ( *stagin área* ):

  ```bash
  git tag -d 0.1.0
  ```
- Removendo uma tag remota:

  ```bash
  git push origin --delete 0.1.0
  ```
- Removendo todas as tags local:

  ```bash
  git tag -d $(git tag -l)
  ```
- Removendo todas as tags remotes:

  ```bash
  git push origin --delete $(git tag -l)
  ```

Para saber mais sobre tags [clique aqui](https://github.com/mindbe/DevOps/blob/master/doc/git/usando_tags_no_git.md).

> 🚨 **I M P O R T A N T E **
>
> Estas informações dizem respeito a este template.
>
> Não se esqueça,  limpe estas sessões e ensira informações sobre a sua aplicação.
> Por exemplo, apesar de todas as variáveis de ambinete estarem disponíveis é importante que aqui você mencione apenas o que sua aplicação irá utilizar, para que a informação fique precisa.
> Troque a imagem de capa coloque uma que faça referencia a sua aplicação.
