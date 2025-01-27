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
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install psycopg2-binary
                    pip install pytest
                    pip install -r requirements.txt || echo "No requirements.txt found"
                    '''
                }
            }
        }

        stage('Run Test Script') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    pytest hw_jenkins/test_database.py --junitxml=test-results.xml
                    '''
                }
            }
        }

        stage('Publish Results') {
            steps {
                 junit '**/test-results.xml'
            }
        }
    }
      post {
        always {
            mail to: 'InsertYour@Mail.Here',
                 subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Check the Jenkins console for details: ${env.BUILD_URL}"
        }
    }

}
