pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/fcfastov2008/Course.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                powershell '''
                python -m venv venv
                .\\venv\\Scripts\\Activate.ps1
                pip install --upgrade pip
                if (Test-Path "requirements.txt") {
                    pip install -r requirements.txt
                }
                '''
            }
        }

        stage('Run Test Script') {
            steps {
                powershell '''
                .\\venv\\Scripts\\Activate.ps1
                python hw_jenkins/test_database.py
                '''
            }
        }

        stage('Publish Results') {
            steps {
                junit 'hw_jenkins/test_results.xml'
            }
        }
    }

    post {
        always {
            emailext subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "Check the Jenkins console for details: ${env.BUILD_URL}",
                     to: 'malytskid@gmail.com'
        }
    }
}
