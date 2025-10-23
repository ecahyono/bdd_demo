# BDD Demo

This is a Behavior-Driven Development (BDD) project using Behave and Selenium for web automation testing.

## Features

- Login functionality testing for CURA Healthcare Service
- Automated browser setup and teardown
- CI/CD integration with GitHub Actions
- Comprehensive logging with log file generation
- Test artifacts upload in CI pipeline (GitHub Actions)

## Project Structure

- `features/`: Contains BDD feature files and step definitions
  - `login.feature`: Login scenarios
  - `steps/login_steps.py`: Step implementations
  - `environment.py`: Browser setup and teardown
- `requirements.txt`: Python dependencies
- `.github/workflows/main.yml`: CI pipeline
- `test_execution.log`: Generated log file containing detailed execution logs (created after test runs)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   behave
   ```

3. Run in headless mode (for CI):
   ```bash
   HEADLESS=true behave
   ```

## Code Quality

- Linted with flake8
- Follows PEP 8 style guidelines
- Includes docstrings for functions
- Comprehensive logging for debugging and monitoring

## Logging

The project includes detailed logging throughout the test execution:

- **Step-level logging**: Each step in the login scenarios logs its actions and results
- **Browser lifecycle logging**: Logs browser initialization, navigation, and cleanup
- **Scenario logging**: Logs the start and end of each test scenario

Logs are automatically saved to `test_execution.log` after each scenario run.

To view logs during test execution, run:
```bash
behave -v
```

To view the log file after execution:
```bash
cat test_execution.log
```
