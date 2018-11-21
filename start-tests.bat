py -m pip install -r requirements.txt
py -u -m pytest -n 1 tests/test_uz.py --junitxml=junit-results/report.xml --alluredir=allure-results --verbose --is_remote_driver=false