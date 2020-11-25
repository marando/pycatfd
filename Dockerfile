FROM ubuntu

RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && \
    apt-get -y update && \
    apt-get install -y \
    git \
    cmake \
    wget \
    unzip \
    python3 \
    python3-pip \
    python3-opencv \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib ;\
    cd dlib/ ;\
    python3 setup.py install ;\
    cd ~ && rm -r dlib/

RUN pip3 install pillow && \
    pip3 install requests && \
    pip3 install scikit-image

WORKDIR app
