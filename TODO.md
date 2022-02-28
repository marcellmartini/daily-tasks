# Atividades pendentes
1. Instalar terraform
    * tfswitch
    * Ref.: https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started

1. Instalar zoom
1. python3-pip
    1. sudo apt install python3-pip
    1. sudo apt install python3.8-venv
    1. python3 -m pip install --user virtualenv
    1. Antigen pip, pyenv

    * Ref.: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. tfswitch
    1. curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | bash

1. GIT + VS code
    1. Configurar o git para usar o vscode como editor de commit
    1. Configurar o usuário geral do git (email e name)

    * Ref.: https://blog.geekhunter.com.br/visual-studio-code-como-editor-do-git/#Como_configurar_o_VS_Code_como_editor_default_do_Git

1. Instalar awscli pela aws
    * Ref.: https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html


* Criar arquivo .aliasrc
    * importar o arquivo no shell padrão do usuário (.bashrc ou .zshrc)
    * Adicionar chaves
        * Datadog
        * Incapsula
        * GoLang
        * Docker BuildKit
        * EDITOR
    * https://github.com/bash-my-aws/bash-my-aws

# Configuração do docker tookit
* Adicionar as envvars no arqruivo .aliasrc:
    * export DOCKER_BUILDKIT=1
    * export COMPOSE_DOCKER_CLI_BUILD=1

* Configurar PATH para ter o ~/.local/bin
