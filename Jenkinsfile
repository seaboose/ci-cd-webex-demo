pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile calculator.py'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }
}
