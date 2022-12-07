pipeline {
    agent any
    environment { 
        USERNAME = 'mohamed-amine'
        FAVORITE_COLOR = 'blue'
    }

    stages {
        stage('Lister les variables') {
            steps {
                echo "Username engine is ${USERNAME}"
                echo "Favorite color is ${FAVORITE_COLOR}"
                sh 'printenv'
            }
        }
        stage('Utilisation des variables') {
            steps {
                script {
                    env.HOBBY = 'coding'
                    env.FAVORITE_COLOR = 'red'
                }
                echo "Favorite color is ${FAVORITE_COLOR}"
            }
        }
    }
}