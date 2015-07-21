#!/bin/sh -x
#creating a module(class) (on the server):

echo creating module: $1

cd /etc/puppet/modules 
sudo puppet module generate my-$1
sudo mv my-$1 $1   
cd $1 
sudo mkdir templates 
cd manifests
