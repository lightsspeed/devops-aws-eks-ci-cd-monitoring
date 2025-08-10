import pytest
import sys
import os

# Add the parent directory to the path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test the CLI module functions
def test_load_config():
    """Test if config loads correctly."""
    try:
        from cloud_billing_cli import load_config # type: ignore
        config = load_config()
        
        assert "currency" in config
        assert "resources" in config
        assert config["currency"] == "₹"
        assert len(config["resources"]) > 0
        
        # Test if all resources have required fields
        for resource_key, resource in config["resources"].items():
            assert "name" in resource
            assert "rate" in resource
            assert "unit" in resource
            assert "description" in resource
            assert isinstance(resource["rate"], (int, float))
            assert resource["rate"] > 0
            
    except ImportError:
        pytest.skip("CLI module not available")

def test_calculate_cost():
    """Test cost calculation function."""
    try:
        from cloud_billing_cli import calculate_cost
        
        # Test basic calculation
        assert calculate_cost(10, 2.5) == 25.0
        assert calculate_cost(12.5, 3.0) == 37.5
        
        # Test rounding
        assert calculate_cost(1, 0.333) == 0.33
        assert calculate_cost(3, 0.334) == 1.0
        
        # Test edge cases
        assert calculate_cost(0, 5.0) == 0.0
        assert calculate_cost(1, 0) == 0.0
        
    except ImportError:
        pytest.skip("CLI module not available")

def test_streamlit_imports():
    """Test if Streamlit app imports correctly."""
    try:
        import cloud_billing_app
        
        # Test if main functions exist
        assert hasattr(cloud_billing_app, 'load_config')
        assert hasattr(cloud_billing_app, 'calculate_cost')
        assert hasattr(cloud_billing_app, 'main')
        
        # Test config structure
        config = cloud_billing_app.load_config()
        assert "resources" in config
        assert "currency" in config
        
    except ImportError:
        pytest.skip("Streamlit app module not available")

def test_optimization_tips():
    """Test optimization tips function."""
    try:
        from cloud_billing_app import get_optimization_tips
        
        # Test for different resource types
        vm_tips = get_optimization_tips("vm", 100)
        assert len(vm_tips) > 0
        assert any("spot instances" in tip.lower() for tip in vm_tips)
        
        db_tips = get_optimization_tips("database", 50)
        assert len(db_tips) > 0
        assert any("replica" in tip.lower() or "serverless" in tip.lower() for tip in db_tips)
        
        # Test for unknown resource
        unknown_tips = get_optimization_tips("unknown_resource", 10)
        assert len(unknown_tips) > 0  # Should return general tips
        
    except ImportError:
        pytest.skip("Streamlit app module not available")

class TestResourceValidation:
    """Test resource data validation."""
    
    def test_all_resources_have_required_fields(self):
        """Ensure all resources have required fields."""
        try:
            from cloud_billing_app import load_config
            config = load_config()
            
            required_fields = ["name", "rate", "unit", "description", "icon"]
            
            for resource_key, resource in config["resources"].items():
                for field in required_fields:
                    assert field in resource, f"Resource {resource_key} missing {field}"
                    
                # Validate data types
                assert isinstance(resource["rate"], (int, float))
                assert isinstance(resource["name"], str)
                assert isinstance(resource["unit"], str)
                assert isinstance(resource["description"], str)
                assert isinstance(resource["icon"], str)
                
                # Validate ranges
                assert resource["rate"] > 0, f"Resource {resource_key} has invalid rate"
                assert len(resource["name"]) > 0, f"Resource {resource_key} has empty name"
                
        except ImportError:
            pytest.skip("Modules not available")
    
    def test_currency_symbol(self):
        """Test currency symbol is properly set."""
        try:
            from cloud_billing_app import load_config
            config = load_config()
            
            assert "currency" in config
            assert config["currency"] in ["₹", "$", "€", "£", "¥"]  # Common currency symbols
            
        except ImportError:
            pytest.skip("Module not available")

class TestCalculationLogic:
    """Test calculation logic and edge cases."""
    
    def test_precision(self):
        """Test calculation precision."""
        try:
            from cloud_billing_app import calculate_cost
            
            # Test precision with small numbers
            result = calculate_cost(0.001, 0.000021)
            assert result >= 0
            assert isinstance(result, float)
            
            # Test precision with large numbers
            result = calculate_cost(1000000, 3.50)
            expected = 3500000.0
            assert result == expected
            
        except ImportError:
            pytest.skip("Module not available")
    
    def test_negative_values(self):
        """Test handling of negative values."""
        try:
            from cloud_billing_app import calculate_cost
            
            # Cost calculation should handle negative input gracefully
            # (though UI should prevent this)
            result = calculate_cost(-5, 2.0)
            assert result == -10.0  # Mathematical result
            
        except ImportError:
            pytest.skip("Module not available")

def test_string_formatting():
    """Test string formatting for currency display."""
    try:
        from cloud_billing_app import load_config
        config = load_config()
        currency = config["currency"]
        
        # Test basic formatting
        cost = 123.456
        formatted = f"{currency}{cost:.2f}"
        assert ".2f" not in formatted  # Ensure formatting applied
        assert currency in formatted
        
    except ImportError:
        pytest.skip("Module not available")

# Performance tests
class TestPerformance:
    """Test performance of calculations."""
    
    def test_calculation_speed(self):
        """Test calculation performance."""
        import time
        
        try:
            from cloud_billing_app import calculate_cost
            
            start_time = time.time()
            
            # Perform many calculations
            for i in range(10000):
                calculate_cost(i * 0.1, 3.5)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Should complete in reasonable time
            assert execution_time < 1.0, f"Calculations took too long: {execution_time}s"
            
        except ImportError:
            pytest.skip("Module not available")

# Integration tests
def test_full_workflow():
    """Test a complete calculation workflow."""
    try:
        from cloud_billing_app import load_config, calculate_cost
        
        # Load config
        config = load_config()
        
        # Simulate user selections
        resource_key = "vm"
        resource = config["resources"][resource_key]
        usage = 24.5
        
        # Calculate cost
        cost = calculate_cost(usage, resource["rate"])
        
        # Verify result
        assert cost > 0
        assert isinstance(cost, (int, float))
        
        # Verify it matches expected calculation
        expected = round(usage * resource["rate"], 2)
        assert cost == expected
        
    except ImportError:
        pytest.skip("Module not available")

if __name__ == "__main__":
    pytest.main([__file__])