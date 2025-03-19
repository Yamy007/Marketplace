pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Yamy007/Marketplace.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh 'source $VENV_DIR/bin/activate && pip install -r backend/requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'source $VENV_DIR/bin/activate && python backend/manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source $VENV_DIR/bin/activate && python backend/manage.py test apps.user.tests'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', fingerprint: true
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Check logs for details.'
        }
    }
}
