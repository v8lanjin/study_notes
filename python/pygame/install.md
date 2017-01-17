### 给python2 安装pygame  
```
sudo apt-get install python-pygame  
```
或者  
```
sudo apt-get install libsdl1.2-dev  
pip install pygame
```

### 给python3 安装pygame  

```
sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev  libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion  libportmidi-dev  
sudo pip3 install pygame
```

### 手工安装

```
mkdir tmp
cd tmp

# download and install SDL
wget http://www.libsdl.org/release/SDL-1.2.14.tar.gz
tar -xzvf SDL-1.2.14.tar.gz
cd SDL-1.2.14
./configure 
sudo make all
```
