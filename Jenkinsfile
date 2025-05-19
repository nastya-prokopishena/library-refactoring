pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /tmp:/tmp'
        }
    }

    environment {
        MONGO_URI = 'mongodb://mongo:27017'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest tests/ --junitxml=test-results/results.xml'
            }
            post {
                always {
                    junit 'test-results/results.xml'
                }
            }
        }

        stage('Run application') {
            steps {
                sh 'python run.py &'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}