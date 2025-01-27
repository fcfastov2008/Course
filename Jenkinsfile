pipeline {
    agent any
    stages {
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'  // використовуємо . замість source
            }
        }
        stage('Run Test Script') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
