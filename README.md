pycatfd 🐈
==========
_Cat facial detection and landmark recognition with Python_

<img src="https://user-images.githubusercontent.com/4701701/27982869-8a7db7f4-637c-11e7-8cff-19a911fa2621.jpg" width="500" />


## Dependencies
* [dlib](https://github.com/davisking/dlib)
* [opencv](https://opencv.org)


## Python Requirements
* Pillow
* requests
* scikit-image 


## Usage
Use `catfd.py` to detect cat faces and facial landmarks in individual images or 
an entire folder. The repository comes pre-trained, but can be re-trained using 
the `train.py` tool.


## Docker Container
A `Dockerfile` is provided to avoid having to install all dependencies manually, 
which can be quite tedious. First make sure that you have Docker installed on 
your system, and then to use the image, build it using the `build.sh` script, 
and then run it using the `run.sh` script from within the repository directory. 

If you would like to do this manually, you can run the following: 

1. Clone and enter the repository:
    ```shell
    git clone git@github.com:marando/pycatfd.git
    cd pycatfd
    ```

2. Build the image:
    ```shell
    docker build -t pycatfd .
    ```
3. Then issue this command to run it:
    ```shell
    docker run -it --rm -v "$PWD":/app pycatfd /bin/bash
    ```
