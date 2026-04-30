pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'playwright install'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest --alluredir=reports'
            }
        }

        stage('Allure') {
            steps {
                allure results: [[path: 'reports']]
            }
        }
    }
}