pipeline {
    agent {
        label 'master'
    }

    environment {
        MONGO_URI = 'mongodb://mongo:27017'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    python --version
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest tests/ --junitxml=test-results/results.xml'
            }
            post {
                always {
                    junit 'test-results/results.xml'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}