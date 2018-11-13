#!groovy​
import hudson.tasks.test.AbstractTestResultAction


pipeline {
    agent {
        label 'master'
    }
    environment {
        PYTHONIOENCODING = 'UTF-8'
    }

    stages {
        stage('Build') {
            steps {
			    sh 'whoami'
				sh 'docker-compose -f ./docker-compose-test-runner.yml build'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose up -d' //start widget hosting
                sh 'docker-compose -f ./docker-compose-test-runner.yml up'
            }
            post {
                always {
                    sh 'docker-compose down'
                    sh 'docker-compose -f ./docker-compose-test-runner.yml down'
                    sh 'chmod -R o+xw allure-results'
                }
            }
        }
        stage('Report') {

            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {    
            junit 'junit-results/report.xml'
            script{    
                def slackMsg = """Build ${currentBuild.result}: <${env.BUILD_URL}|${env.JOB_NAME} #${env.BUILD_NUMBER}> \n <${env.BUILD_URL}allure/|Report>"""
			    def notificationColor = currentBuild.result =='SUCCESS' ? "#00e600" : "#ff0000"
                slackSend botUser: true, channel: '#general', color: notificationColor, message: slackMsg, teamDomain: 'https://myfirstslack-co.slack.com', tokenCredentialId: 'slack-jenkins-secret'
            }     
        }
    }
}