Install packages:

* https://github.com/zsh-users/zsh-syntax-highlighting
* https://github.com/zsh-users/zsh-autosuggestions
* https://github.com/zsh-users/zsh-completions
* https://github.com/junegunn/fzf#installation
* https://github.com/lincheney/fzf-tab-completion.git
* sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"\n\n
* https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-completion.html#cli-command-completion-linux
* https://github.com/romkatv/powerlevel10k#configuration

Plugins:
plugins=(
  aws
  command-not-found
  docker
  emoji
  fzf
  fzf-alias
  git
  helm
  kubectl
  kube-ps1
  minikube
  golang
  terraform
  zsh-completions
  zsh-autosuggestions
)


ref:
* https://medium.com/@herryhan2435/using-aws-cli-with-fzf-on-ohmyzsh-ec995ee3784f
# FZF configure
https://github.com/junegunn/fzf#settings

## fzf-zsh-completion
## then edit ~/.zsh file.
source $HOME/.oh-my-zsh/custom/plugins/fzf-tab-completion/zsh/fzf-zsh-completion.sh
## only aws command completion
zstyle ':completion:*:*:aws' fzf-search-display true
## or for everything
zstyle ':completion:*' fzf-search-display true
## fzf configure
export FZF_DEFAULT_OPTS=" --height 40% --layout=reverse"
export FZF_CTRL_T_OPTS="-m --preview 'bat -n --color=always {}' --bind 'ctrl-/:change-preview-window(down|hidden|)'"
export FZF_ALT_C_OPTS="-m --preview 'tree -C {}'"
#[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
