# Python Docker Example

Dead simple basic Python TDD application skeleton with Docker

## Customization

Add all dependencies to requirements.txt

Optional: Replace all instances of 'app' with your application name

## Test/Development cycle

1. Start the Docker application
2. Within the container, run `pip install -r requirements.txt`
3. Run app.hello module with `python -m app.hello`
4. Create a new function
5. Create a new unit test for your function with a name that follows the `*_test.py` pattern
6. Run all unit tests locally with `python -m unittest discover tests "*_test.py"`
7. Build the docker image for unit tests with `docker build -t python_docker_example:version1.0.test --target test .`
8. Run the unit tests docker image with `docker run python_docker_example:version1.0.test`
9. Build the docker image for the development build `docker build -t python_docker_example:version1.0.build --target build .`
10. Run the development docker image with `docker run python_docker_example:version1.0.build`
