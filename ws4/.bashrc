# Show files in long format with hidden files and human-readable sizes
alias ll='ls -alh'

# Quick Git status for the current repository
alias gs='git status'

# Jump directly to the CS131 repository
alias cs131='cd ~/cs131'

# Create a directory and immediately enter it
mkcd() {
    mkdir -p "$1"
    cd "$1"
}

# Load additional aliases if they exist
if [ -f ~/.bash_aliases ]; then
    source ~/.bash_aliases
fi
