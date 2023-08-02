# Description
Imagine you spent 50 US dollars but before that you had converted it from russian rubles into british pounds, then into euros, and finally into US dollars.
The question is, how much of the russian rubles you spent to obtain those 50 US dollars? 

This small [**FastAPI**](https://fastapi.tiangolo.com/) webapp answers this question

# Up and at'em
Open your command prompt (Windows) or terminal (Linux/MacOS) inside the downloaded project. 
## Local run
Presuming you are inside the root of the project.
Create python environment and install necessary requirements:
```
pip install -r requirements.txt
```
Then initiate the app to connect to it in the browser:
```
uvicorn app.main:app 
```
Proceed into the browser and follow further instructions from there.
The idea is that you need to write request similar to the following in a search line:
```
.../<amount of spent currency>/<3-letter codes of currencies, separated with '-'>
```
After a short time, you will receive desired statistics.

## Docker run
You can build the project manually or by utilising dockerhub.

### Manual image build
Presuming you are inside the root of the project.
Let's build a docker image: 
```
docker build -t <give your name to the project> .
```
### Dockerhub image
Execute the following command inside the command prompt or the terminal:
```
docker pull iiakyjiuh/k8s-example
```
It will download the built image of the project. 

### Run
Now let's run the container from that image interactively:
```
docker run -it -p 80:80 <previously specified name>
```
In order to connect to the instance, fill __localhost:80__ in a search bar.

N.B. You can stop the container with _Ctrl/CMD + C_ command in the command prompt or the terminal.
