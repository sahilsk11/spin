command=$1
source src/env/bin/activate;
cd src;

if [ $command = "start" ]
then
	python3 app.py
elif [ $command = "build" ]
then
	python3 app.py build
	pip freeze;
elif [ $command = "install" ]
then
	pip install $2	
fi
deactivate
cd ..;
