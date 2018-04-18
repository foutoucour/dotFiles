#!/usr/bin/env fish

# ALIASES
alias gitka='gitk --all'
alias cd..='cd ..'
alias u='cd ..'
alias rm='rm -r'
alias cp='cp -r'
alias mkdir='mkdir -p'
alias h='history'
alias mv='mv -i'
alias grep='grep --color=auto'
alias ls='ls -h'
alias la='ls -a'
alias ll='ls -l'
alias r='refresh'
alias lg='ls -1 | grep -i \!*'
alias eg='env | grep -i \!*'
alias dc='docker-compose'

switch (uname)
case Darwin
    alias ls='ls -G'
case Linux
    alias ls='ls --color=auto'
end

# docker aliases
alias drmae='docker rm (docker ps -qa --no-trunc --filter "status=exited")'
alias drmi='docker rmi (docker images --filter "dangling=true" -q --no-trunc)'

set -x VIRTUALFISH_HOME $HOME/virtualenvs/
set -x EDITOR vim

# virtualenv for fish: http://virtualfish.readthedocs.io/
eval (python -m virtualfish)

echo "Setting PIPENV_VENV_IN_PROJECT so pipenv install venv in `root/.venv` folder."
set -x PIPENV_VENV_IN_PROJECT 1
# special case of $PATH: https://github.com/fish-shell/fish-shell/issues/527
set -gx PATH /usr/local/sbin /usr/local/bin $PATH
