"""
Integration tests for API endpoints.
Demonstrates: API testing, CRUD operations, status codes
"""

import pytest
from fastapi import status


class TestCompaniesAPI:
    """Test cases for Companies API endpoints."""
    
    def test_create_company(self, client):
        """Test creating a new company."""
        company_data = {
            "name": "Test Startup Inc",
            "description": "A test company",
            "industry": "Technology",
            "stage": "Series A",
            "website": "https://teststartup.com"
        }
        
        response = client.post("/api/companies", json=company_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["name"] == company_data["name"]
        assert data["industry"] == company_data["industry"]
        assert "id" in data
    
    def test_get_companies_empty(self, client):
        """Test getting companies when none exist."""
        response = client.get("/api/companies")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_get_companies_list(self, client):
        """Test getting list of companies."""
        # Create two companies
        client.post("/api/companies", json={
            "name": "Company 1",
            "industry": "Technology"
        })
        client.post("/api/companies", json={
            "name": "Company 2",
            "industry": "Healthcare"
        })
        
        response = client.get("/api/companies")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 2
    
    def test_get_company_by_id(self, client):
        """Test getting a specific company by ID."""
        # Create company
        create_response = client.post("/api/companies", json={
            "name": "Test Company",
            "industry": "Technology"
        })
        company_id = create_response.json()["id"]
        
        # Get company
        response = client.get(f"/api/companies/{company_id}")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == company_id
        assert data["name"] == "Test Company"
    
    def test_get_nonexistent_company(self, client):
        """Test getting a company that doesn't exist."""
        response = client.get("/api/companies/99999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_update_company(self, client):
        """Test updating a company."""
        # Create company
        create_response = client.post("/api/companies", json={
            "name": "Original Name",
            "industry": "Technology"
        })
        company_id = create_response.json()["id"]
        
        # Update company
        update_data = {
            "name": "Updated Name",
            "current_arr": 1000000,
            "employee_count": 50
        }
        response = client.put(f"/api/companies/{company_id}", json=update_data)
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == "Updated Name"
        assert data["current_arr"] == 1000000
        assert data["employee_count"] == 50
    
    def test_delete_company(self, client):
        """Test deleting a company (soft delete)."""
        # Create company
        create_response = client.post("/api/companies", json={
            "name": "To Be Deleted",
            "industry": "Technology"
        })
        company_id = create_response.json()["id"]
        
        # Delete company
        response = client.delete(f"/api/companies/{company_id}")
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
        # Verify company still exists but is inactive
        get_response = client.get(f"/api/companies/{company_id}")
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.json()["is_active"] == False
    
    def test_create_duplicate_company(self, client):
        """Test that creating duplicate company fails."""
        company_data = {
            "name": "Unique Company",
            "industry": "Technology"
        }
        
        # Create first company
        response1 = client.post("/api/companies", json=company_data)
        assert response1.status_code == status.HTTP_201_CREATED
        
        # Try to create duplicate
        response2 = client.post("/api/companies", json=company_data)
        assert response2.status_code == status.HTTP_400_BAD_REQUEST


class TestHealthEndpoint:
    """Test health check endpoint."""
    
    def test_health_check(self, client):
        """Test that health endpoint returns success."""
        response = client.get("/health")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "healthy"
    
    def test_root_endpoint(self, client):
        """Test root endpoint."""
        response = client.get("/")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "message" in data
        assert "docs" in data

