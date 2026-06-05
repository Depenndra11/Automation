pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Depenndra11/Automation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t automation-tests .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm automation-tests'
            }
        }
    }
}