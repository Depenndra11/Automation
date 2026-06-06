pipeline {
    agent any

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
                        script: 'docker --version',
                        returnStatus: true
                    ) == 0)

                    if (dockerAvailable) {
                        echo 'Docker found. Running tests in Docker.'

                        bat 'docker build -t automation-test .'
                        bat 'docker run --rm automation-test'
                    } else {
                        echo 'Docker not found. Running tests locally.'

                        bat 'pip install -r requirements.txt'
                        bat 'pytest -v'
                    }
                }
            }
        }
    }
}