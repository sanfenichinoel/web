
一个配置
```bash
apt update

apt install make
apt install zlib1g
apt install zlib1g-dev
apt install gcc
apt install g++
apt install libpcre3-dev
apt install libssl-dev
```

两个配置
```bash
apt install wget

cd /usr/local/src
wget http://downloads.sourceforge.net/project/pcre/pcre/8.45/pcre-8.45.tar.gz

tar zxvf pcre-8.45.tar.gz
cd pcre-8.45.tar.gz
./configure
make && make install

cd /usr/local/src
wget http://nginx.org/download/nginx-1.23.2.tar.gz
tar zxvf nginx-1.23.2.tar.gz
cd nginx-1.23.2.tar.gz
./configure
make && make install
```


别的什么无关的题外话  
```bash
pip3 uninstall uvicorn
pip3 install hypercorn
pip3 install --upgrade websockets
```
