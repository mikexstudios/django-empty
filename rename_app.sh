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
#-i means inplace editing. Need to specify an extension that it is saved in. So ''.

#settings.py. NOTE: We hardcode lines here. This is bad, but oh well.
sed -i '' -e '107s|app|'$1'|' settings.py
sed -i '' -e 's|app.backends|'$1'.backends|' settings.py
sed -i '' -e 's|app.helpers|'$1'.helpers|' settings.py
sed -i '' -e 's|# app|# '$1'|' settings.py

#urls.py
sed -i '' -e 's|app.urls|'$1'.urls|g' urls.py
sed -i '' -e 's|app.views|'$1'.views|g' urls.py

#app/urls.py
sed -i '' -e 's|app.views|'$1'.views|g' app/urls.py

#app/views.py
sed -i '' -e 's|app/home|'$1'/home|g' app/views.py

#app/templates/app/home.html. Replace only first line.
sed -i '' -e '1s|app|'$1'|' app/templates/app/home.html

#Now for the app/templates/django_rpx_plus/*.html files
sed -i '' -e '1s|app|'$1'|' app/templates/app/*.html

#Now rename our directories
#app/templates/app/ 
mv app/templates/app app/templates/$1

#app/
mv app $1

echo 'All done!'

