pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'df -h'
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
