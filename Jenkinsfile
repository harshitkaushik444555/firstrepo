pipeline {
    agent {
        docker {
            image 'maven:3.9.9-eclipse-temurin-11'
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
                sh 'mvn clean package' 
            }
        }
    }
}
