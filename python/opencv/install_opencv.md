## 安装Opencv
1. sudo apt-get update
1. sudo apt-get upgrade
1. sudo apt-get install build-essential cmake pkg-config
1. sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
1. sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
1. sudo apt-get install libxvidcore-dev libx264-dev
1. sudo apt-get install libgtk-3-dev
1. sudo apt-get install libatlas-base-dev gfortran
1. sudo apt-get install python2.7-dev python3.5-dev





cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
    -D BUILD_EXAMPLES=ON ..