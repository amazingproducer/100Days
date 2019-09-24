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
        sh 'ls -lha'
      }
      post {
        always {
          sh 'uname -a'
        }
      }    
    }
  }
}
