# Atividades pendentes
1. Instalar terraform
    * tfswitch
        * Ref.: https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started
    * ethtool

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

1. Criar arquivo .aliasrc
    * importar o arquivo no shell padrão do usuário (.bashrc ou .zshrc)
    * Adicionar chaves
        * Datadog
        * Incapsula
        * GoLang
        * Docker BuildKit
        * EDITOR
    * https://github.com/bash-my-aws/bash-my-aws

1. Fazer terraform para configuração de VPC da vida
    * terraform provider openvpn cloud
        * criar ec2
        * criar security group
        * criar ssh key
        * configurar openvpn
        * pegar token no openvpn cloud
        * passar token para o aplicativo do openvpn cloud na ec2 da aws

1. Instalar exercism

1. Instalar https://docs.instruqt.com/getting-started/set-up-instruqt

# Configuração do docker tookit
* Adicionar as envvars no arqruivo .aliasrc:
    * export DOCKER_BUILDKIT=1
    * export COMPOSE_DOCKER_CLI_BUILD=1

* Configurar PATH para ter o ~/.local/bin
