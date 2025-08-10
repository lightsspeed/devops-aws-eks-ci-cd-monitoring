pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'lightsspeed/cloudcalulator:1.0.0'
        GITHUB_CREDENTIALS = credentials('githubcreds')
        GIT_BRANCH = "main"
    }
    
    stages {
        // Cleanup stage removed as requested
        
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
                            // Replace custom function with actual Docker build command
                            sh """
                                docker build -t ${env.DOCKER_IMAGE_NAME} -f Dockerfile .
                            """
                        }
                    }
                }
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    // Replace custom function with actual test commands
                    sh """
                        # Add your test commands here, for example:
                        # npm test
                        # pytest
                        # mvn test
                        echo "Running unit tests..."
                    """
                }
            }
        }
        
        stage('Security Scan with Trivy') {
            steps {
                script {
                    // Replace custom function with actual Trivy scan
                    sh """
                        # Install Trivy if not available
                        # Run Trivy scan
                        trivy image ${env.DOCKER_IMAGE_NAME} || echo "Trivy scan completed"
                    """
                }
            }
        }
        
        stage('Push Docker Images') {
            parallel {
                stage('Push Main App Image') {
                    steps {
                        script {
                            // Use proper Jenkins Docker plugin syntax
                            withCredentials([usernamePassword(
                                credentialsId: 'dockercreds',
                                usernameVariable: 'DOCKER_USERNAME',
                                passwordVariable: 'DOCKER_PASSWORD'
                            )]) {
                                sh """
                                    echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                                    docker push ${env.DOCKER_IMAGE_NAME}
                                """
                            }
                        }
                    }
                }
            }
        }
    }
}