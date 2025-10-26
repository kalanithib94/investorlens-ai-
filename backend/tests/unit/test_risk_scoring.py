"""
Unit tests for risk scoring logic.
Demonstrates: Unit testing, test cases, assertions
"""

import pytest


def calculate_basic_risk_score(runway_months: int, burn_rate: float, arr: float) -> int:
    """
    Simple risk scoring algorithm for testing.
    
    Args:
        runway_months: Months of runway remaining
        burn_rate: Monthly burn rate
        arr: Annual Recurring Revenue
        
    Returns:
        Risk score (0-100, where 100 is highest risk)
    """
    risk_score = 50  # Start with medium risk
    
    # Runway factor
    if runway_months < 6:
        risk_score += 30
    elif runway_months < 12:
        risk_score += 15
    elif runway_months >= 18:
        risk_score -= 15
    
    # Burn rate factor
    if burn_rate > 0 and arr > 0:
        burn_to_revenue_ratio = (burn_rate * 12) / arr
        if burn_to_revenue_ratio > 0.5:
            risk_score += 20
        elif burn_to_revenue_ratio < 0.2:
            risk_score -= 10
    
    # Cap between 0-100
    return max(0, min(100, risk_score))


class TestRiskScoring:
    """Test cases for risk scoring algorithm."""
    
    def test_high_risk_low_runway(self):
        """Test that low runway increases risk score."""
        score = calculate_basic_risk_score(
            runway_months=3,
            burn_rate=100000,
            arr=500000
        )
        assert score >= 70, "Low runway should result in high risk"
    
    def test_low_risk_high_runway(self):
        """Test that high runway decreases risk score."""
        score = calculate_basic_risk_score(
            runway_months=24,
            burn_rate=50000,
            arr=1000000
        )
        assert score <= 40, "High runway should result in low risk"
    
    def test_medium_risk_medium_runway(self):
        """Test medium runway gives medium risk."""
        score = calculate_basic_risk_score(
            runway_months=12,
            burn_rate=75000,
            arr=750000
        )
        assert 40 <= score <= 60, "Medium runway should result in medium risk"
    
    def test_high_burn_rate_increases_risk(self):
        """Test that high burn rate relative to revenue increases risk."""
        score = calculate_basic_risk_score(
            runway_months=12,
            burn_rate=100000,  # High burn
            arr=600000  # Moderate revenue
        )
        assert score >= 60, "High burn rate should increase risk"
    
    def test_score_bounds(self):
        """Test that risk score stays within 0-100 bounds."""
        # Extreme low risk scenario
        low_score = calculate_basic_risk_score(
            runway_months=36,
            burn_rate=10000,
            arr=5000000
        )
        assert 0 <= low_score <= 100
        
        # Extreme high risk scenario
        high_score = calculate_basic_risk_score(
            runway_months=1,
            burn_rate=500000,
            arr=100000
        )
        assert 0 <= high_score <= 100
    
    def test_zero_values(self):
        """Test handling of zero values."""
        score = calculate_basic_risk_score(
            runway_months=12,
            burn_rate=0,
            arr=0
        )
        assert isinstance(score, int)
        assert 0 <= score <= 100

