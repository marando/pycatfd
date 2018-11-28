FROM ubuntu

RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && \
    apt-get -y update && \
    apt-get install -y \
    git \
    cmake \
    wget \
    unzip \
    python \
    python-pip \
    python-opencv \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib ;\
    cd dlib/ ;\
    python setup.py install --yes USE_AVX_INSTRUCTIONS ;\
    cd ~ && rm -r dlib/

RUN pip install pillow && \
    pip install requests && \
    pip install scikit-image

WORKDIR app