pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'whoami'
      }
    }
    stage('test') {
      steps {
        sh 'whoami'
      }
      post {
        always {
          sh 'whoami'
        }
      }    
    }
  }
}
