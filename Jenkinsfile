pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "checking out"
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install' 
            }
        }
    }
}
