#!/bin/bash

function install_dependencies (){
    apt-get update
    pip3 install urllib
    pip3 install clipboard
}

function config_command_usage (){
    chmod +x posty.py
    cp posty.py /usr/bin/posty
}

function install (){
    echo "Starting installation."
    install_dependencies
    config_command_usage
    echo "Done"
}

install