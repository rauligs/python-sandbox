# Python Sandbox
Learning Python fundamentals and playground for programming features and third-party libraries through testing

## Installation
1. Install python `$ brew install python3`
2. Install `[pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)`
3. Activate the environment: `$ pipenv shell`
4. Install dependencies from `Pipfile`: `$ pipenv install --dev`

### Installing additional packages
```
$ pipenv install <package>
```
```
$ pipenv install --dev <package>
```
See [here](https://pipenv.readthedocs.io/en/latest/install/#installing-packages-for-your-project) for more.

## Testing
```
$ pytest -v --cov-report term-missing --cov=. --cov-fail-under=100
```

## Code formatting
```
$ yapf --style=google -i *.py
```