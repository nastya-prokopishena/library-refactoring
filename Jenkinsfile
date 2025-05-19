pipeline {
    agent any

    environment {
        MONGO_URI = 'mongodb://mongo:27017'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh 'python3 -m pytest tests/ --junitxml=test-results/results.xml'
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