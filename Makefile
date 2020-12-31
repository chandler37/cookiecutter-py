# If you have difficulty with this Makefile, you might install the latest GNU
# Make via Homebrew (https://brew.sh/) [try `brew install make`] and try again
# using `gmake`. If that doesn't work you might want to install the latest bash
# via `brew install bash` and update your PATH to prefer it over the older
# MacOS-provided bash.

# /bin/sh is the default; we want bash so we can 'source venv/bin/activate':
SHELL := $(shell which bash)

ACTIVATE_VENV := source venv/bin/activate

PYTHON3 := $(shell command -v python3 2> /dev/null)

.PHONY: help
help:
	@echo "Read ./README.md to get started."

# On MacOS `pip`/`python` are Python 2.7 (either via Homebrew `python@2` or,
# frighteningly, the stock Python provided by Apple), not Python
# 3. `pip3`/`python3` (using python version 3) are courtesy of the `python`
# package from [Homebrew](https://brew.sh/). Once we create a venv/ directory,
# though, we can activate it via `source venv/bin/activate` and then say
# `python` or `pip` and get version 3. (We could also, equivalently, say
# `python3` and `pip3`.)
.PHONY: install_tools
install_tools:
	@echo "If brew is not found, you need to install Homebrew; see https://brew.sh/"
	brew update
	brew install python

venv:
ifndef PYTHON3
	$(error "python3 is not available; please run make install_tools")
endif
	$(PYTHON3) -m venv venv
	@echo "The virtualenv is not active unless you run the following:"
	@echo "source venv/bin/activate"
	@echo ""
	@echo "But if you use the Makefile it activates it for you temporarily."

.PHONY: install
install: venv/installation.success

venv/installation.success: requirements.txt | venv
	$(ACTIVATE_VENV) && pip install -U pip && pip3 install -r $<
	touch $@

.PHONY: shell
shell: | venv/installation.success
	$(ACTIVATE_VENV) && PYTHONSTARTUP=interactive.py ipython

.PHONY: run
run: | venv/installation.success
	$(ACTIVATE_VENV) && python3 {{cookiecutter.project_slug}}-runner.py $(ARGS)

.PHONY: test
test: | venv/installation.success
	$(ACTIVATE_VENV) && python3 run_tests.py

.PHONY: upgrade
upgrade: unfreezeplus venv/installation.success test
	@echo "The upgraded third-party dependencies might work... at least tests passed."

.PHONY: unfreezeplus
unfreezeplus:
	@git diff-index --quiet HEAD || { echo "not in a clean git workspace; run 'git status'"; exit 1; }
	rm -f venv/installation.success
	# If this fails, `deactivate; make clean` and try again:
	$(ACTIVATE_VENV) && { pip3 freeze | xargs pip3 uninstall -y; }
	sed -i "" -e "s/=.*//" requirements.txt
	$(ACTIVATE_VENV) && pip3 install -r requirements.txt
	$(ACTIVATE_VENV) && pip3 freeze > requirements.txt

.PHONY: clean
clean:
	rm -fr venv **/*.pyc **/__pycache__ .cache .pytest_cache

.DEFAULT_GOAL := help
