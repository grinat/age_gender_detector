### age_gender_detector
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/grinat/age_gender_detector)

Detect age and gender via rest api

[Docs](https://age-gender-detector-v1.herokuapp.com)

Used pre-trained model from: [https://github.com/yu4u/age-gender-estimation](https://github.com/yu4u/age-gender-estimation)

### Usage
```
docker run -d -p 5101:5101 grinat0/age_gender_detector
```
And open http://localhost:5101 for see docs/examples

### Build, deploy, develop
#### Develop
```
pip3 install -r requirements.txt
make dev
```
or
```
docker-compose up
```

#### Build docker image
```
make build-docker-image
make run-docker-image # run image
```

#### Without docker
```
pip3 install -r requirements.txt
make prod
```

### Testing
```
make unittest
```
or
```
python -m unittest
```
