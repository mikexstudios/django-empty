#!/bin/bash
# Renames the bundled 'app' to whatever you want. 

if [ -z $1 ]; then
    echo 'Need to specify new app name!'
    exit
fi

#Note that $0 contains the full path of the script being executed.
script_path=`dirname $0`
cd ${script_path}

#Now go through each of the spots where we had to hardcode app and replace it with
#our new name. We rename the directories last. 
#-i means inplace editing.

#urls.py
sed -i "s/app\.urls/$1\.urls/g" urls.py
sed -i "s/app\.views/$1\.views/g" urls.py

#app/urls.py
sed -i "s/app\.views/$1\.views/g" app/urls.py

#app/views.py
sed -i "s/app\/home/$1\/home/g" app/views.py

#app/templates/app/home.html. Replace only first line.
sed -i "1s/app/$1/g" app/templates/app/home.html

#Now for the app/templates/django_rpx_plus/*.html files
sed -i "1s/app/$1/g" app/templates/app/*.html

#Now rename our directories
#app/templates/app/ 
mv app/templates/app app/templates/$1

#app/
mv app $1

echo 'All done!'

