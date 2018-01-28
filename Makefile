venv:
	virtualenv venv
	venv/bin/pip install -e "git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk"
	echo -e "\033[1;32mRun 'source facebookenv/bin/activate'\033[0m to activate venv"
run:
	venv/bin/python crushbook.py
