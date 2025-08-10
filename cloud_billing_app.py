import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Cloud Billing Calculator",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}

.resource-card {
    background-color: #000000;
    padding: 1rem;
    border-radius: 10px;
    border-left: 4px solid #1f77b4;
    margin: 0.5rem 0;
}

.cost-highlight {
    background-color: #000000;
    padding: 0.8rem;
    border-radius: 8px;
    border: 2px solid #1f77b4;
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
}

.optimization-tip {
    background-color: #000000;
    padding: 0.5rem;
    border-radius: 5px;
    border-left: 3px solid #32cd32;
    margin: 0.3rem 0;
}
</style>
""", unsafe_allow_html=True)

def load_config():
    """Load pricing configuration for different cloud resources."""
    config = {
        "currency": "₹",
        "resources": {
            "vm": {
                "name": "Virtual Machine",
                "rate": 3.50,
                "unit": "hours",
                "description": "Standard VM instance",
                "icon": "🖥️"
            },
            "database": {
                "name": "Database",
                "rate": 5.25,
                "unit": "hours",
                "description": "Managed database service",
                "icon": "🗄️"
            },
            "storage": {
                "name": "Storage",
                "rate": 0.08,
                "unit": "GB-hours",
                "description": "Block storage",
                "icon": "💾"
            },
            "cdn": {
                "name": "CDN",
                "rate": 0.12,
                "unit": "GB transferred",
                "description": "Content Delivery Network",
                "icon": "🌐"
            },
            "load_balancer": {
                "name": "Load Balancer",
                "rate": 2.80,
                "unit": "hours",
                "description": "Application load balancer",
                "icon": "⚖️"
            },
            "lambda": {
                "name": "Serverless Functions",
                "rate": 0.000021,
                "unit": "requests",
                "description": "Pay per request",
                "icon": "⚡"
            },
            "api_gateway": {
                "name": "API Gateway",
                "rate": 0.0035,
                "unit": "API calls",
                "description": "API management service",
                "icon": "🔌"
            },
            "monitoring": {
                "name": "Monitoring",
                "rate": 1.20,
                "unit": "hours",
                "description": "Infrastructure monitoring",
                "icon": "📊"
            }
        }
    }
    return config

def calculate_cost(usage, rate):
    """Calculate the total cost and round to 2 decimal places."""
    return round(usage * rate, 2)

def get_optimization_tips(resource_key, cost):
    """Get optimization tips based on resource type."""
    tips = {
        "vm": [
            "💡 Use spot instances for non-critical workloads (up to 90% savings)",
            "⏰ Schedule VMs to shut down during off-hours",
            "📊 Right-size instances based on actual usage patterns"
        ],
        "database": [
            "📚 Use read replicas for read-heavy workloads",
            "🔄 Consider serverless database options for variable workloads",
            "🗜️ Enable automatic scaling based on demand"
        ],
        "storage": [
            "📦 Archive old data to cheaper storage tiers",
            "🗜️ Enable compression and deduplication",
            "🔄 Implement lifecycle policies for automated management"
        ],
        "cdn": [
            "🌍 Optimize cache settings to reduce origin requests",
            "🗜️ Enable compression for text-based content",
            "📊 Monitor cache hit ratios and optimize accordingly"
        ],
        "load_balancer": [
            "⚖️ Use application-aware load balancing",
            "🔄 Implement health checks to avoid unhealthy instances",
            "📊 Monitor request patterns for optimal scaling"
        ],
        "lambda": [
            "⚡ Optimize function memory allocation",
            "🔄 Use provisioned concurrency for consistent performance",
            "📊 Monitor function duration and optimize code"
        ],
        "api_gateway": [
            "🚀 Implement caching to reduce backend calls",
            "🔐 Use API keys and throttling effectively",
            "📊 Monitor API usage patterns"
        ],
        "monitoring": [
            "📊 Use custom metrics only when necessary",
            "⏰ Adjust log retention periods appropriately",
            "🔍 Focus monitoring on critical business metrics"
        ]
    }
    
    general_tips = [
        "💰 Set up billing alerts to avoid surprises",
        "📈 Use reserved instances for predictable workloads",
        "🎯 Implement auto-scaling to match demand"
    ]
    
    resource_tips = tips.get(resource_key, [])
    return resource_tips + general_tips[:2]

def main():
    # Header
    st.markdown('<h1 class="main-header">☁️ Cloud Billing Calculator</h1>', unsafe_allow_html=True)
    
    # Load configuration
    config = load_config()
    currency = config["currency"]
    
    # Sidebar
    st.sidebar.title("📋 Calculator Settings")
    
    # Mode selection
    calc_mode = st.sidebar.selectbox(
        "Calculation Mode",
        ["Single Resource", "Multiple Resources", "Resource Comparison"]
    )
    
    # Initialize session state
    if 'calculations' not in st.session_state:
        st.session_state.calculations = []
    
    # Main content based on mode
    if calc_mode == "Single Resource":
        single_resource_calculator(config, currency)
    elif calc_mode == "Multiple Resources":
        multiple_resource_calculator(config, currency)
    else:
        resource_comparison(config, currency)
    
    # Calculation history
    if st.session_state.calculations:
        st.sidebar.markdown("---")
        st.sidebar.subheader("📝 Recent Calculations")
        for i, calc in enumerate(reversed(st.session_state.calculations[-5:])):
            st.sidebar.write(f"**{calc['resource']}**: {currency}{calc['cost']:.2f}")

def single_resource_calculator(config, currency):
    st.subheader("🎯 Single Resource Calculator")
    
    # Resource selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        selected_resource = st.selectbox(
            "Select Cloud Resource",
            list(config["resources"].keys()),
            format_func=lambda x: f"{config['resources'][x]['icon']} {config['resources'][x]['name']}"
        )
    
    resource = config["resources"][selected_resource]
    
    with col2:
        st.markdown(f"""
        <div class="resource-card">
            <h4>{resource['icon']} {resource['name']}</h4>
            <p><strong>Description:</strong> {resource['description']}</p>
            <p><strong>Rate:</strong> {currency}{resource['rate']} per {resource['unit']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Usage input
    st.markdown("### 📊 Usage Input")
    usage = st.number_input(
        f"Enter usage ({resource['unit']})",
        min_value=0.0,
        value=0.0,
        step=0.1,
        help=f"Enter the amount of {resource['unit']} used"
    )
    
    if usage > 0:
        cost = calculate_cost(usage, resource['rate'])
        
        # Cost display
        st.markdown("### 💰 Cost Calculation")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Usage", f"{usage} {resource['unit']}")
        with col2:
            st.metric("Rate", f"{currency}{resource['rate']}")
        with col3:
            st.metric("Total Cost", f"{currency}{cost:.2f}")
        
        # Detailed breakdown
        st.markdown(f"""
        <div class="cost-highlight">
            💸 <strong>Calculation:</strong> {usage} × {currency}{resource['rate']} = {currency}{cost:.2f}
        </div>
        """, unsafe_allow_html=True)
        
        # Save calculation
        if st.button("💾 Save Calculation"):
            st.session_state.calculations.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'resource': resource['name'],
                'usage': usage,
                'unit': resource['unit'],
                'rate': resource['rate'],
                'cost': cost
            })
            st.success("Calculation saved!")
        
        # Optimization tips
        st.markdown("### 💡 Optimization Tips")
        tips = get_optimization_tips(selected_resource, cost)
        for tip in tips:
            st.markdown(f'<div class="optimization-tip">{tip}</div>', unsafe_allow_html=True)

def multiple_resource_calculator(config, currency):
    st.subheader("📊 Multiple Resources Calculator")
    
    # Resource selection
    selected_resources = st.multiselect(
        "Select Cloud Resources",
        list(config["resources"].keys()),
        format_func=lambda x: f"{config['resources'][x]['icon']} {config['resources'][x]['name']}"
    )
    
    if not selected_resources:
        st.info("👆 Please select one or more resources to calculate costs")
        return
    
    # Usage inputs
    st.markdown("### 📊 Usage Inputs")
    usage_data = {}
    
    cols = st.columns(min(len(selected_resources), 3))
    
    for i, resource_key in enumerate(selected_resources):
        resource = config["resources"][resource_key]
        col_idx = i % 3
        
        with cols[col_idx]:
            st.markdown(f"**{resource['icon']} {resource['name']}**")
            usage = st.number_input(
                f"Usage ({resource['unit']})",
                min_value=0.0,
                value=0.0,
                step=0.1,
                key=f"usage_{resource_key}"
            )
            
            if usage > 0:
                cost = calculate_cost(usage, resource['rate'])
                usage_data[resource_key] = {
                    'name': resource['name'],
                    'icon': resource['icon'],
                    'usage': usage,
                    'unit': resource['unit'],
                    'rate': resource['rate'],
                    'cost': cost
                }
                st.write(f"Cost: {currency}{cost:.2f}")
    
    # Results
    if usage_data:
        st.markdown("### 💰 Cost Summary")
        
        # Calculate total
        total_cost = sum(item['cost'] for item in usage_data.values())
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Resources Used", len(usage_data))
        with col2:
            st.metric("Total Cost", f"{currency}{total_cost:.2f}")
        with col3:
            avg_cost = total_cost / len(usage_data)
            st.metric("Average per Resource", f"{currency}{avg_cost:.2f}")
        
        # Detailed table
        df_data = []
        for key, item in usage_data.items():
            percentage = (item['cost'] / total_cost) * 100
            df_data.append({
                'Resource': f"{item['icon']} {item['name']}",
                'Usage': f"{item['usage']} {item['unit']}",
                'Rate': f"{currency}{item['rate']}",
                'Cost': f"{currency}{item['cost']:.2f}",
                'Percentage': f"{percentage:.1f}%"
            })
        
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True)
        
        # Cost breakdown chart
        st.markdown("### 📊 Cost Breakdown")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig_pie = px.pie(
                values=[item['cost'] for item in usage_data.values()],
                names=[f"{item['icon']} {item['name']}" for item in usage_data.values()],
                title="Cost Distribution"
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Bar chart
            fig_bar = px.bar(
                x=[item['name'] for item in usage_data.values()],
                y=[item['cost'] for item in usage_data.values()],
                title="Cost by Resource",
                labels={'x': 'Resource', 'y': f'Cost ({currency})'}
            )
            st.plotly_chart(fig_bar, use_container_width=True)

def resource_comparison(config, currency):
    st.subheader("🔍 Resource Comparison")
    
    st.info("Compare costs across different usage scenarios")
    
    # Select resources to compare
    resources_to_compare = st.multiselect(
        "Select resources to compare",
        list(config["resources"].keys()),
        format_func=lambda x: f"{config['resources'][x]['icon']} {config['resources'][x]['name']}"
    )
    
    if len(resources_to_compare) < 2:
        st.warning("Please select at least 2 resources to compare")
        return
    
    # Usage scenarios
    st.markdown("### 📊 Usage Scenarios")
    scenario_name = st.text_input("Scenario Name", "Production Workload")
    
    # Create comparison data
    comparison_data = []
    
    cols = st.columns(min(len(resources_to_compare), 3))
    
    for i, resource_key in enumerate(resources_to_compare):
        resource = config["resources"][resource_key]
        col_idx = i % 3
        
        with cols[col_idx]:
            st.markdown(f"**{resource['icon']} {resource['name']}**")
            st.write(f"Rate: {currency}{resource['rate']} per {resource['unit']}")
            
            usage = st.number_input(
                f"Usage ({resource['unit']})",
                min_value=0.0,
                value=1.0,
                step=0.1,
                key=f"compare_{resource_key}"
            )
            
            cost = calculate_cost(usage, resource['rate'])
            comparison_data.append({
                'Resource': f"{resource['icon']} {resource['name']}",
                'Usage': f"{usage} {resource['unit']}",
                'Rate': resource['rate'],
                'Cost': cost,
                'Cost per Unit': resource['rate']
            })
    
    if comparison_data:
        # Comparison table
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)
        
        # Comparison chart
        fig = px.bar(
            df,
            x='Resource',
            y='Cost',
            title=f"Cost Comparison - {scenario_name}",
            text='Cost'
        )
        fig.update_traces(texttemplate=f'{currency}%{{text:.2f}}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
        
        # Cost efficiency analysis
        st.markdown("### 📈 Cost Efficiency Analysis")
        most_expensive = df.loc[df['Cost'].idxmax()]
        least_expensive = df.loc[df['Cost'].idxmin()]
        
        col1, col2 = st.columns(2)
        with col1:
            st.error(f"🔴 Most Expensive: {most_expensive['Resource']} - {currency}{most_expensive['Cost']:.2f}")
        with col2:
            st.success(f"🟢 Most Economical: {least_expensive['Resource']} - {currency}{least_expensive['Cost']:.2f}")

if __name__ == "__main__":
    main()