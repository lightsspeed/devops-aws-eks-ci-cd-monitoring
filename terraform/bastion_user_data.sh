#!/bin/bash
sudo apt-get update -y
sudo apt-get install snapd -y

# Install AWS CLI
sudo snap install aws-cli --classic

# Install Helm
sudo snap install helm --classic

# Install Kubectl
sudo snap install kubectl --classic


OUTPUT_FILE="/versions.txt"

# Capture versions
{
    echo "Helm Version:"
    helm version 2>/dev/null || echo "Helm not installed"
    echo ""

    echo "kubectl Version:"
    kubectl version  2>/dev/null || echo "kubectl not installed"
    echo ""

    echo "AWS CLI Version:"
    aws --version 2>/dev/null || echo "AWS CLI not installed"
    echo ""
} > "$OUTPUT_FILE"