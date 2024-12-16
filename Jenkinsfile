pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-project.git' 
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install' 
            }
        }
    }
}
