pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Depenndra11/Automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}