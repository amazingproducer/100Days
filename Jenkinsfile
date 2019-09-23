pipeline {
  agent { docker { image 'python:3.7.2' } }
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
          ssh 'whoami'
        }
      }    
    }
  }
}
