
#!/bin/bash

# howto install script

# enter root
echo 'Root required...'
sudo echo '...' 

# make sure man-db is up to date
echo 'checking that man is up to date...'
sudo apt-get upgrade man-db

# add aliases  ### unreliable: will have user do manually for now
#if [ "alias | grep 'alias howto' | wc" != 0 ]; then
#  echo "howto alias exists"
#else
#  echo "error noted, creating alias..."
#  echo "# created by howto-buntu (https://github.com/underscorejho/howto-buntu)" >> ~/.bashrc
#  echo "alias howto='python $HOME/bin/howto.py'" >> ~/.bashrc
#fi

# add executable permissions
chmod 744 howto/howto.py

# put in ~/bin CHECK ~/bin is in PATH and CHECK ~bin is a directory
if [[ "$PATH" == ?(*:)"$HOME/bin"?(:*) ]]; then
  echo "adding howto to $HOME/bin"
  cp howto/howto.py $HOME/bin/howto.py 
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
  echo "export PATH=$PATH:$HOME/bin" >> ~/.bashrc
  echo "copying howto.py to $HOME/bin/howto.py"
  cp howto/howto.py $HOME/bin/howto.py 
fi

# source .bashrc
. ~/.bashrc
