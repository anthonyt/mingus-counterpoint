#!/bin/bash
#
#	mingus build script
#	Builds mingus, registers at PyPi, generates documentation and uploads to Google code

VERSION=`cat ~/mingus/setup.py | grep version | awk -F = '{print $2}' | awk -F \" '{print $2}'`

echo "*******************************************************************************"
echo "*****                     mingus :: Automatic Build                       *****"                     
echo "*****                  Building mingus version $VERSION                   *****"
echo "*******************************************************************************"
echo
echo "              Generate Documentation and Distribute to Google Code"
echo
echo "*******************************************************************************"
sudo rm -r ./build/ && sudo python setup.py install
~/mingus/doc/distribute_docs.sh
echo "*******************************************************************************"
echo
echo "                 Registering package mingus-$VERSION at PyPi"
echo
echo "*******************************************************************************"
python setup.py register
echo "*******************************************************************************"
echo
echo "          Uploading source distribution and windows installer to PyPi"
echo
echo "*******************************************************************************"
sudo python setup.py sdist bdist_wininst upload
echo "*******************************************************************************"
echo
echo "              Uploading source and windows installer to Google Code"
echo
echo "*******************************************************************************"
echo "Uploading windows installer"
python googlecode_upload.py -p mingus -s "mingus-$VERSION - windows installer" -u rhijnauwen -l Featured /home/bspaans/mingus/dist/mingus-$VERSION.win32.exe

echo
echo "Uploading source distribution"
python googlecode_upload.py -p mingus -s "mingus-$VERSION - source tarball" -u rhijnauwen -l Featured /home/bspaans/mingus/dist/mingus-$VERSION.tar.gz
