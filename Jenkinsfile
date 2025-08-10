pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'lightsspeed/cloudcalulator:1.0.0'
        GITHUB_CREDENTIALS = credentials('githubcreds')
        GIT_BRANCH = "main"
    }
    
    // stages {
    //     stage('Cleanup Workspace') {
    //         steps {
    //             script {
    //                 cleanWs()
    //             }
    //         }
    //     }
        
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.GIT_BRANCH}"]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/lightsspeed/devops-aws-eks-ci-cd-monitoring.git',
                        credentialsId: 'githubcreds'
                    ]]
                ])
            }
        }
        
        stage('Build Docker Images') {
            parallel {
                stage('Build Main App Image') {
                    steps {
                        script {
                            docker_build(
                                imageName: env.DOCKER_IMAGE_NAME,
                                dockerfile: 'Dockerfile',
                                context: '.'
                            )
                        }
                    }
                }
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    run_tests()
                }
            }
        }
        
        stage('Security Scan with Trivy') {
            steps {
                script {
                    trivy_scan()
                }
            }
        }
        
        stage('Push Docker Images') {
            parallel {
                stage('Push Main App Image') {
                    steps {
                        script {
                            docker_push(
                                imageName: env.DOCKER_IMAGE_NAME,
                                credentials: 'dockercreds'
                            )
                        }
                    }
                }
            }
        }
    }
}
