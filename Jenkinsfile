pipeline {
    agent {
        docker {
            image 'maven:latest'
        }
    }

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
