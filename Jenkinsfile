pipeline {
    agent {
        docker {
            image 'abhishekf5/maven-abhishek-docker-agent:v1'
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
