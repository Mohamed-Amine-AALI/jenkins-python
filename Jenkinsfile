pipeline {
    agent any
    environment { 
        USERNAME = 'mohamed-amine'
        FAVORITE_COLOR = 'blue'
    }

    stages {
        stage('Lister les variables') {
            steps {
                echo "USERNAME : ${USERNAME}"
                echo "FAVORITE_COLOR : ${FAVORITE_COLOR}"
                echo "env.USERNAME : ${env.USERNAME}"
                echo "env.FAVORITE_COLOR : ${env.FAVORITE_COLOR}"
            }
        }
        stage('Utilisation des variables') {
            steps {
                script {
                    env.HOBBY = 'coding'
                    env.FAVORITE_COLOR = 'red'
                }
                echo "env.HOBBY is ${env.HOBBY}"

                script {
                    env.HOBBY = 'eating'
                }
                echo "env.HOBBY is ${env.HOBBY}"

                echo "Favorite color is ${FAVORITE_COLOR}"
                echo "env.FAVORITE_COLOR : ${env.FAVORITE_COLOR}"
            }
        }
    }
}