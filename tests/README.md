# Testing

### Running pytest
```
python3 -m pytest tests/
```
### Generating a report
```
python3 -m coverage run --source=src -m pytest tests
python3 -m coverage report # generates an terminal summary
python3 -m coverage html -d report # generates a html summary
```

This will work on your local machine or CSE machine. If you have any troubles delete all folders called "__pycache__"

