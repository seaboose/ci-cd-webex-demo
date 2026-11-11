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

    post {
        always {
            withCredentials([
                string(credentialsId: 'webex-bot-token',
                       variable: 'WEBEX_BOT_TOKEN'),
                string(credentialsId: 'webex-room-id',
                       variable: 'WEBEX_ROOM_ID')
            ]) {
                script {
                    withEnv(["JENKINS_BUILD_STATUS=${currentBuild.currentResult}"]) {
                        sh 'python3 notify_webex.py'
                    }
                }
            }
        }
    }
}