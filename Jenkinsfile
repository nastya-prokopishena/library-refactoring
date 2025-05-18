pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Клонування репозиторію...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Встановлення залежностей...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Запуск тестів...'
                sh '. venv/bin/activate && pytest tests --junitxml=tests_result/results.xml'
            }
            post {
                always {
                    junit 'tests_result/results.xml'
                }
            }
        }
    }
}
