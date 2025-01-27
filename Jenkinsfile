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
                script {
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || echo "No requirements.txt found"
                    '''
                }
            }
        }

        stage('Run Test Script') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    python hw_jenkins/test_database.py
                    '''
                }
            }
        }

        stage('Publish Results') {
            steps {
                junit 'hw_jenkins/test_results.xml'
            }
        }
    }
      

}
