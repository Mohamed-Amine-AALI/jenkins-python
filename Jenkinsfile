pipeline {
    agent any
    environment { 
        username = 'mohamed-amine'
        favoritecolor = 'blue'
    }

    stages {
        stage('Lister les variables') {
            steps {
                steps {
                    sh 'printenv'
                }
            }
        }
        stage('Utilisation des variables') {
            steps {
                environment { 
                    hobby = 'coding'
                    favoritecolor = 'red'
                }
            }
        }
    }
}