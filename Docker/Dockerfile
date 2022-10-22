FROM python:buster
# Use official python image with Debian Buster base OS
MAINTAINER Peter Vaillancourt "pzv2@cornell.edu"

# Uses bash for shell commands during build
SHELL ["/bin/bash","-c"]

USER root

# Update and add some packages
RUN apt-get update -y && apt-get install -y \
    sudo \
    cmake \
    man \
    bash-completion \
    nano \ 
    vim \ 
    less \
    htop \
    git \
    tmux 

# set up user
RUN useradd -mr -G sudo dev 
RUN passwd -d dev
RUN echo "dev  ALL=(ALL)       NOPASSWD: ALL"  >> /etc/sudoers
RUN chown -R dev /home/dev

WORKDIR /home/dev

RUN mkdir /opt/app
RUN chown -R dev /opt/app
ENV PATH=$PATH:/home/dev/.local/bin

COPY vimrc /home/dev/.vimrc

USER dev

# Install pip and requirements
COPY requirements.txt /var/tmp/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /var/tmp/requirements.txt

RUN git clone https://github.com/Lived-Experience/ptf-2022-hackathon.git

RUN ldconfig
