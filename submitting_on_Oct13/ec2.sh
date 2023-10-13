#!/bin/bash



key_dir_path=~/Keypair_1.pem
server_address=ec2-user@ec2-54-199-19-55.ap-northeast-1.compute.amazonaws.com


# Logging in.
if [ "${1}" == "connect" ]; then
    ssh -i "${key_dir_path}" ${server_address}
fi

# Sending a file.
if [ "${1}" == "send" ]; then
    scp -i ${key_dir_path} \
        ${2} \
        ${server_address}:/home/ec2-user \

fi

# Pulling a file.
if [ "${1}" == "pull" ]; then
    scp -i ${key_dir_path} \
        ${server_address}:${2} \
        . \

fi




# End