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
				sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose up'
            }
            post {
                always {
                    sh 'docker-compose down'
                    sh 'sudo chmod -R o+xw allure-results'
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
            step([$class    : 'XUnitBuilder',
                  thresholds: [[$class: 'FailedThreshold', failureThreshold: '1']],
                  tools     : [
                          [$class: 'JUnitType', pattern: 'junit-results/report.xml']
                  ]
            ])
            script{    
                def slackMsg = """Build ${currentBuild.result}: <${env.BUILD_URL}|${env.JOB_NAME} #${env.BUILD_NUMBER}> \n ${testStatuses()}. <${env.BUILD_URL}allure/|Report>"""
			    slackSend botUser: true, channel: '#general', color: notificationColor, message: slackMsg, teamDomain: 'https://myfirstslack-co.slack.com', tokenCredentialId: 'slack-jenkins-secret'
            }     
        }
    }
}

@NonCPS
def testStatuses() {
    def testStatus = ""
    AbstractTestResultAction testResultAction = currentBuild.rawBuild.getAction(AbstractTestResultAction.class)
    if (testResultAction != null) {
        def total = testResultAction.totalCount
        def failed = testResultAction.failCount
        def skipped = testResultAction.skipCount
        def passed = total - failed - skipped
        testStatus = "Test Status: Passed: ${passed}, Failed: ${failed} ${testResultAction.failureDiffString}, Skipped: ${skipped}"

        if (failed == 0) {
            currentBuild.result = 'SUCCESS'
        }
    }
    return testStatus
}