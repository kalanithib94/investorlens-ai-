# Enhanced Risk Scoring Algorithm

## Current Simple Algorithm
```python
if runway >= 18: risk = 20
elif runway >= 12: risk = 40  
elif runway >= 6: risk = 65
else: risk = 85
```

## Enhanced Multi-Factor Algorithm

### Factors to Consider:

1. **Runway Risk (40% weight)**
   - < 3 months: 100 points
   - 3-6 months: 80 points
   - 6-12 months: 60 points
   - 12-18 months: 30 points
   - 18+ months: 10 points

2. **Burn Rate vs Revenue (30% weight)**
   - burn_rate > arr/12: 100 points (spending more than earning)
   - burn_rate > arr/24: 60 points
   - burn_rate < arr/24: 20 points

3. **Growth Trend (20% weight)**
   - ARR declining: 80 points
   - ARR flat: 50 points
   - ARR growing < 20%: 30 points
   - ARR growing > 20%: 10 points

4. **Employee Efficiency (10% weight)**
   - Revenue per employee < $50K: 80 points
   - Revenue per employee $50K-$100K: 50 points
   - Revenue per employee > $100K: 20 points

### Formula:
```python
risk_score = (
    runway_risk * 0.4 +
    burn_vs_revenue * 0.3 +
    growth_trend * 0.2 +
    efficiency * 0.1
)
```

### Example Calculation:

**Company: PayFlow Secure**
- Runway: 10 months → 60 points (weight 0.4) = 24
- Burn vs Revenue: $95K burn, $82K monthly revenue → 60 points (weight 0.3) = 18
- Growth: Unknown, assume flat → 50 points (weight 0.2) = 10
- Efficiency: $980K / 18 employees = $54K → 50 points (weight 0.1) = 5

**Total Risk Score: 24 + 18 + 10 + 5 = 57 (Medium-High Risk)**

## Benefits:
- More nuanced scoring
- Considers multiple factors
- More accurate predictions
- Better decision support

