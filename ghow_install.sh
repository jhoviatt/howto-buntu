
#!/bin/bash

# ghow install script

# enter root
echo 'Root required...'
sudo echo '...' 

# add aliases   ### unreliable: will have user do manually for now
#if [ "alias | grep 'alias googlehowto' | wc" != 0 ]; then
#  echo "googlehowto alias exists"
#else
#  echo "error noted, creating alias..."
#  echo "# created by howto-buntu (https://github.com/underscorejho/howto-buntu)" >> ~/.bashrc
#  echo "alias googlehowto='python $HOME/bin/ghow.py'" >> ~/.bashrc
#fi
#
#if [ "alias | grep 'alias ghow' | wc" != 0 ]; then
#  echo "ghow alias exists"
#else
#  echo "error noted, creating alias..."
#  echo "# created by howto-buntu (https://github.com/underscorejho/howto-buntu)" >> ~/.bashrc
#  echo "alias ghow='googlehowto'" >> ~/.bashrc
#fi

# add executable permissions
chmod 744 ghow/ghow.py

# put in ~/bin CHECK ~/bin is in PATH and CHECK ~bin is a directory
if [[ "$PATH" == ?(*:)"$HOME/bin"?(:*) ]]; then
  echo "adding ghow to $HOME/bin"
  cp ghow/ghow.py $HOME/bin/ghow.py 
else 
  if [-d $HOME/bin]; then
    echo "..."
  else
    echo "$HOME/bin not found..."
    echo "creating $HOME/bin..."
    mkdir $HOME/bin 
  fi
  echo "$HOME/bin not in $PATH..."
  echo "adding $HOME/bin to $PATH..."
  $PATH = $PATH:$HOME/bin 
  echo "copying ghow.py to $HOME/bin/ghow.py"
  cp ghow/ghow.py $HOME/bin/ghow.py 
fi

# source .bashrc
. ~/.bashrc
