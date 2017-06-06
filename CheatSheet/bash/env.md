'''bash  
export PS1="\[\e[36;1m\]\u\[\e[0m\]@\[\e[33;1m\]\h\[\e[0m\]:\[\e[31;1m\]\w\[\e[0m\]\n\$ "
#export PS1="\[\e[36;1m\]\u\[\e[0m\]:\[\e[31;1m\]\w\[\e[0m\]\n\$ "
alias tmux='tmux -2'
POWERLINE_SCRIPT=/usr/share/powerline/bindings/bash/powerline.sh
if [ -f $POWERLINE_SCRIPT ]; then
    source $POWERLINE_SCRIPT
fi  
'''
