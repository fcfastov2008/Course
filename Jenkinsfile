pipeline {
    agent any
    stages {
        stage('Setup Python Environment') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh 'ls -la venv/bin'  // Перевірка вмісту папки
                sh '. venv/bin/activate'  // Спробуйте з . замість source
            }
        }
    }
}
