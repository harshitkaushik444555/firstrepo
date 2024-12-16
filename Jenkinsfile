pipeline {
    agent {
        docker{
            image: maven:3.9.9
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
