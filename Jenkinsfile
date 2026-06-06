pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_TYPE',
            choices: ['regression', 'smoke', 'all'],
            description: 'Select which test suite to run'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Depenndra11/Automation.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def dockerAvailable = (bat(
                        script: 'docker info',
                        returnStatus: true
                    ) == 0)

                     def dockerfileExists = fileExists('Dockerfile')

                    if (dockerAvailable && dockerfileExists) {
                        echo 'Docker available and Dockerfile found.'

                        bat 'docker build -t automation-test .'
                        bat 'docker run --rm automation-test'
                    } else {
                        echo 'Docker unavailable. Running locally.'

                        bat 'pip install -r requirements.txt'
                        bat 'pytest -v'
                    }
                }
            }
        }
    }
}