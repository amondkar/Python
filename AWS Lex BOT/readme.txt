pipenv shell

pipenv install numpy
pipenv install pandas 
pip install awslambdaric

pipenv lock

docker build -t lex-product-fulfillment .
docker run -p 9000:8080  lex-product-fulfillment:latest 
docker run --name lex-product-fulfillment_1  -it lex-product-fulfillment 
docker tag lex-product-fulfillment lex-product-fulfillment
docker tag lex-product-fulfillment amondkar/lex-product-fulfillment
docker login
docker image push amondkar/lex-product-fulfillment


AWS ket : AKIAWZSAMPEHXZSUNO4E/GqSoai0wQcc1LQNhs71dhkV7bXUoc5ku9IPI1SgF

aws ecr create-repository --repository-name lex-product-fulfillment --image-scanning-configuration scanOnPush=true
docker tag lex-product-fulfillment 467212728591.dkr.ecr.us-east-1.amazonaws.com/lex-product-fulfillment:latest
aws ecr get-login-password | docker login --username AWS --password-stdin 467212728591.dkr.ecr.us-east-1.amazonaws.com
docker push 467212728591.dkr.ecr.us-east-1.amazonaws.com/lex-product-fulfillment:latest



-- Create Package
mkdir -p Layers/Pandas
mkdir -p Layers/Numpy

sls plugin install -n serverless-python-requirements
pipenv install numpy
sls deploy

pythonRequirements: arn:aws:lambda:us-east-1:467212728591:layer:Pandas:1

pipenv install pandas
sis deploy
 pythonRequirements: arn:aws:lambda:us-east-1:467212728591:layer:Numpy:1


mkdir folder
cd folder
virtualenv v-env
source ./v-env/bin/activate
pip install numpy==1.19.0
pip install pandas==1.2.0
deactivate

mkdir python
cd python
cp -r ../v-env/lib/python3.7/site-packages/* .
cd ..
zip -r panda_layer.zip python

aws lambda publish-layer-version --layer-name pandas --zip-file fileb://panda_layer.zip --compatible-runtimes python3.6

aws lambda publish-layer-version --layer-name pandas-numpy --zip-file fileb://panda_layer.zip --compatible-runtimes python3.7


zip -r pdnp_layer.zip python

aws lambda publish-layer-version --layer-name pandas-numpy --zip-file fileb://pdnp_layer.zip --compatible-runtimes python3.6






 PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!\n\nImporting the numpy C-extensions failed. This error can happen for\nmany reasons, often due to issues with your setup or how NumPy was\ninstalled.\n\nWe have compiled some common reasons and troubleshooting tips at:\n\n    https://numpy.org/devdocs/user/troubleshooting-importerror.html\n\nPlease note and check the following:\n\n  * The Python version is: Python3.7 from \"/var/lang/bin/python3.7\"\n  * The NumPy version is: \"1.21.0\"\n\nand make sure that they are the versions you expect.\nPlease carefully study the documentation linked above for further help.\n\nOriginal error was: No module named 'numpy.core._multiarray_umath'\n",
