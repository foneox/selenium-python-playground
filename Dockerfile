FROM python:3.7

WORKDIR /opt/app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

VOLUME "/opt/app/allure-results"
VOLUME "/opt/app/junit-results"

CMD rm -rf ./allure-results/* && python -u -m pytest -n 4 tests/ --junitxml=junit-results/report.xml --alluredir=allure-results --verbose --is_remote_driver=true