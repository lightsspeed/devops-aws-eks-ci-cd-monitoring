# ☁️ Cloud Billing Calculator

A comprehensive multi-resource cloud billing calculator with both CLI and web interfaces. Calculate costs for various cloud services including VMs, databases, storage, CDN, and more with real-time cost optimization suggestions.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

## 🌟 Features

### 🖥️ CLI Version

- **Multi-Resource Support**: Calculate costs for 8+ cloud services
- **Interactive Menu**: Easy-to-use command-line interface
- **Detailed Billing**: Professional invoice-style summaries
- **Cost Optimization**: Personalized tips for each resource
- **Error Handling**: Robust input validation and type casting

### 🌐 Web Interface (Streamlit)

- **Three Calculation Modes**: Single, Multiple, and Comparison modes
- **Interactive Visualizations**: Pie charts, bar charts, and metrics
- **Real-time Calculations**: Instant cost updates as you type
- **Calculation History**: Save and track your cost estimates
- **Professional UI**: Modern design with custom styling
- **Resource Cards**: Detailed information for each cloud service

## 🚀 Supported Cloud Resources

| Resource             | Icon | Rate      | Unit           | Description               |
| -------------------- | ---- | --------- | -------------- | ------------------------- |
| Virtual Machine      | 🖥️   | ₹3.50     | hours          | Standard VM instance      |
| Database             | 🗄️   | ₹5.25     | hours          | Managed database service  |
| Storage              | 💾   | ₹0.08     | GB-hours       | Block storage             |
| CDN                  | 🌐   | ₹0.12     | GB transferred | Content Delivery Network  |
| Load Balancer        | ⚖️   | ₹2.80     | hours          | Application load balancer |
| Serverless Functions | ⚡   | ₹0.000021 | requests       | Pay per request           |
| API Gateway          | 🔌   | ₹0.0035   | API calls      | API management service    |
| Monitoring           | 📊   | ₹1.20     | hours          | Infrastructure monitoring |

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Clone the Repository

```bash
git clone https://github.com/yourusername/cloud-billing-calculator.git
cd cloud-billing-calculator
```

### Install Dependencies

#### For CLI Version Only:

```bash
# No additional dependencies required
python cloud_billing_cli.py
```

#### For Web Interface:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas plotly
```

## 🎯 Usage

### CLI Version

```bash
python cloud_billing_cli.py
```

**Example Output:**

```
🌥️  Multi-Resource Cloud Billing Calculator
==================================================

Available Cloud Resources:
============================================================
VM             | Virtual Machine      | ₹3.5     per hours
DATABASE       | Database            | ₹5.25    per hours
============================================================

Select a resource: vm
Enter usage for Virtual Machine (hours): 24.5

==================================================
BILLING SUMMARY
==================================================
Total cost for 24.5 hours is ₹85.75
==================================================
```

### Web Interface (Streamlit)

```bash
streamlit run cloud_billing_app.py
```

Or if streamlit command not found:

```bash
python -m streamlit run cloud_billing_app.py
```

The app will open in your browser at `http://localhost:8501`

## 🖼️ Screenshots

### CLI Interface

```
🌥️  Multi-Resource Cloud Billing Calculator
------------------------------
Current hourly rate: ₹3.00

Enter the number of hours the VM ran: 12.5
==================================================
BILLING SUMMARY
==================================================
Total cost for 12.5 hours is ₹37.50
==================================================
```

### Web Interface Features

- **Dashboard View**: Overview of all resources and costs
- **Interactive Charts**: Visual cost breakdown with pie and bar charts
- **Resource Comparison**: Side-by-side cost analysis
- **Optimization Tips**: Contextual advice for cost reduction

## 🏗️ Project Structure

```
cloud-billing-calculator/
├── cloud_billing_cli.py          # CLI application
├── cloud_billing_app.py          # Streamlit web application
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker container configuration
├── docker-compose.yml             # Docker Compose setup
├── nginx.conf                     # Nginx reverse proxy config
├── .dockerignore                  # Docker ignore file
├── .github/                       # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml                 # CI/CD pipeline
├── tests/                         # Test files
│   ├── __init__.py
│   └── test_cloud_billing.py     # Unit tests
├── README.md                      # Project documentation
├── LICENSE                        # MIT license
├── .gitignore                     # Git ignore file
├── screenshots/                   # Application screenshots
│   ├── cli_demo.png
│   ├── web_dashboard.png
│   └── cost_charts.png
└── docs/                          # Additional documentation
    ├── API.md                     # API documentation
    ├── CONTRIBUTING.md            # Contribution guidelines
    └── DEPLOYMENT.md              # Deployment guide
```

## 🔧 Configuration

### Customizing Resource Rates

Edit the `load_config()` function in either file to modify:

- Resource rates
- Currency symbol
- Available resources
- Resource descriptions

```python
config = {
    "currency": "₹",  # Change currency symbol
    "resources": {
        "vm": {
            "rate": 3.50,  # Modify rates
            # ... other properties
        }
    }
}
```

## 📊 Key Programming Concepts

This project demonstrates:

- **Type Casting**: String to float conversion with validation
- **Error Handling**: Try-catch blocks for user input
- **Floating-Point Arithmetic**: Precise cost calculations
- **String Formatting**: Professional output formatting
- **Object-Oriented Design**: Modular function structure
- **Data Visualization**: Interactive charts with Plotly
- **Web Development**: Modern UI with Streamlit

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Adding New Features

- New cloud resources
- Additional calculation modes
- Enhanced visualizations
- Mobile-responsive design

### Bug Reports

Please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

#### Streamlit Command Not Found

```bash
# Try using Python module
python -m streamlit run cloud_billing_app.py

# Or install with --user flag
pip install --user streamlit
```

#### Import Errors

```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Verify installation
python -c "import streamlit, pandas, plotly; print('All modules imported successfully')"
```

#### Display Issues

- Ensure your terminal supports UTF-8 for proper emoji display
- Use a modern browser for the web interface
- Check browser console for JavaScript errors

## 📋 Requirements

### Python Dependencies

```
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.15.0
```

### System Requirements

- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: 512MB minimum (2GB recommended)
- **Python**: 3.7 or higher
- **Browser**: Chrome, Firefox, Safari, or Edge (for web interface)

## 🐳 Docker Support

### Quick Start with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run individual container
docker build -t cloud-billing-calculator .
docker run -p 8501:8501 cloud-billing-calculator
```

### Production Deployment

```bash
# Run with nginx reverse proxy
docker-compose --profile production up -d
```

### Docker Hub

Pull the pre-built image:

```bash
docker pull yourusername/cloud-billing-calculator:latest
```

## 🚀 CI/CD Pipeline

### GitHub Actions Workflow

- **✅ Automated Testing**: Unit tests, linting, security scans
- **✅ Multi-platform Builds**: AMD64 and ARM64 Docker images
- **✅ Security Scanning**: Vulnerability checks with safety and bandit
- **✅ Code Quality**: Black formatting, isort imports, flake8 linting
- **✅ Automated Deployment**: Staging and production environments
- **✅ Container Registry**: Docker Hub and GitHub Container Registry

### Build Status

![CI/CD](https://github.com/yourusername/cloud-billing-calculator/workflows/CI/CD%20Pipeline/badge.svg)
![Docker](https://img.shields.io/docker/pulls/yourusername/cloud-billing-calculator)
![Security](https://img.shields.io/badge/security-scanned-green)

### Deployment Environments

- **Development**: Auto-deploy on `develop` branch
- **Staging**: Auto-deploy on `develop` branch
- **Production**: Auto-deploy on GitHub releases

## 🔄 Version History

### v3.0.0 (Current)

- ✅ Docker containerization support
- ✅ GitHub Actions CI/CD pipeline
- ✅ Multi-platform container builds
- ✅ Production-ready deployment configs
- ✅ Automated testing and security scans
- ✅ Nginx reverse proxy support

### v2.0.0

- ✅ Added Streamlit web interface
- ✅ Interactive visualizations with Plotly
- ✅ Multiple calculation modes
- ✅ Calculation history feature
- ✅ Enhanced optimization tips

### v1.0.0

- ✅ CLI-based calculator
- ✅ Multi-resource support
- ✅ Basic cost calculations
- ✅ Error handling

## 🗺️ Roadmap

### Upcoming Features

- [ ] **Cost Alerts**: Set budget thresholds with notifications
- [ ] **Export Options**: PDF/Excel report generation
- [ ] **Currency Conversion**: Support for multiple currencies
- [ ] **Historical Data**: Track costs over time
- [ ] **Cloud Provider Integration**: Real-time pricing APIs
- [ ] **Mobile App**: React Native version
- [ ] **Database Backend**: Persistent storage for calculations
- [ ] **Kubernetes Deployment**: Helm charts and K8s manifests
- [ ] **API Endpoints**: REST API for external integrations

### Enhancement Ideas

- [ ] **Advanced Analytics**: Trend analysis and forecasting
- [ ] **Team Collaboration**: Multi-user support
- [ ] **Custom Resources**: User-defined resource types
- [ ] **Backup/Restore**: Configuration import/export
- [ ] **Dark Mode**: Alternative UI theme

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - _Initial work_ - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- **Streamlit Team** - For the amazing web framework
- **Plotly** - For interactive visualization capabilities
- **Python Community** - For the robust ecosystem
- **Cloud Providers** - For pricing structure inspiration

## 📞 Support

- **Documentation**: Check the [docs/](docs/) folder
- **Issues**: [GitHub Issues](https://github.com/yourusername/cloud-billing-calculator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/cloud-billing-calculator/discussions)
- **Email**: your.email@example.com

## 🌟 Show Your Support

Give a ⭐️ if this project helped you calculate your cloud costs!

---

**Made with ❤️ for the cloud computing community**
