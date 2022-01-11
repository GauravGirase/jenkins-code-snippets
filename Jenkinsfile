pipeline {
    agent any
    environment {
    def param = readJSON file: 'config.json'
    msg = "${param.name}"
  
  }
    
    stages {
        
        stage('Printing an output') {
            steps {
              echo "${msg}"
            }
        }
    
    }
}
