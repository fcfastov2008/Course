pipeline {
    agent any
    stages {
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'bash -c "source venv/bin/activate"'
            }
        }
    }
}
