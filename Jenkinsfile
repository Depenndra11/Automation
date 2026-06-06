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
                        script: 'docker info',
                        returnStatus: true
                    ) == 0)

                    if (dockerAvailable) {
                        echo 'Docker daemon is running.'

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