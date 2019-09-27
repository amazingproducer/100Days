pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'whereis python333'
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
