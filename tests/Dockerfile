FROM python:3.8

# Working directory
COPY .. /fortigate_api
WORKDIR /fortigate_api

# Install dependencies
RUN python -m pip install --upgrade pip && \
    pip install poetry && \
    poetry install && \
    poetry export --with dev --format=requirements.txt --output=requirements.txt && \
    pip install -r requirements.txt

# Tests
RUN rm /fortigate_api/__init__.py
RUN pylint fortigate_api tests
RUN mypy --namespace-packages --explicit-package-bases fortigate_api tests
RUN pytest -v -m "not skip" tests
RUN pydocstyle .
RUN rst-lint README.rst CHANGELOG.rst
