/**
 * Dashboard Component - Main portfolio overview
 * Demonstrates: React components, state management, data visualization
 */

import { useState, useEffect } from 'react';
import { TrendingUp, AlertTriangle, Building2, Activity } from 'lucide-react';
import CompanyCard from '../CompanyCard/CompanyCard';
import AlertPanel from '../AlertPanel/AlertPanel';
import { companiesAPI, alertsAPI } from '../../services/api';

const Dashboard = () => {
  const [companies, setCompanies] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [alertStats, setAlertStats] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortBy, setSortBy] = useState('risk_score'); // risk_score, current_arr, name
  const [filterIndustry, setFilterIndustry] = useState('all');
  const [showAddModal, setShowAddModal] = useState(false);

  // Fetch data on mount
  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      setLoading(true);
      setError(null);

      // Fetch companies and alerts in parallel
      const [companiesData, alertsData, statsData] = await Promise.all([
        companiesAPI.getAll(),
        alertsAPI.getAll({ unresolved_only: true, limit: 10 }),
        alertsAPI.getStats(),
      ]);

      setCompanies(companiesData);
      setAlerts(alertsData);
      setAlertStats(statsData);
    } catch (err) {
      console.error('Error fetching dashboard data:', err);
      setError('Failed to load dashboard data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Filter and sort companies
  const filteredAndSortedCompanies = () => {
    let filtered = [...companies];
    
    // Apply filter
    if (filterIndustry !== 'all') {
      filtered = filtered.filter(c => c.industry === filterIndustry);
    }
    
    // Apply sort
    filtered.sort((a, b) => {
      if (sortBy === 'risk_score') return (b.risk_score || 0) - (a.risk_score || 0); // High to low
      if (sortBy === 'current_arr') return (b.current_arr || 0) - (a.current_arr || 0); // High to low
      if (sortBy === 'name') return (a.name || '').localeCompare(b.name || '');
      return 0;
    });
    
    return filtered;
  };

  const displayedCompanies = filteredAndSortedCompanies();

  // Calculate portfolio stats
  const portfolioStats = {
    totalCompanies: companies.length,
    activeCompanies: companies.filter(c => c.is_active).length,
    avgRiskScore: companies.length > 0 
      ? Math.round(companies.reduce((sum, c) => sum + c.risk_score, 0) / companies.length)
      : 0,
    totalAlerts: alertStats.total_unresolved || 0,
    criticalAlerts: alertStats.critical || 0,
  };

  // Button handlers
  const handleAddCompany = () => {
    setShowAddModal(true);
  };

  const handleSubmitCompany = async (formData) => {
    try {
      await companiesAPI.create(formData);
      setShowAddModal(false);
      fetchDashboardData(); // Refresh data
      alert('Company added successfully!');
    } catch (err) {
      console.error('Error adding company:', err);
      alert('Failed to add company. Please try again.');
    }
  };

  const handleSort = () => {
    // Cycle through sort options
    const sortOptions = ['risk_score', 'current_arr', 'name'];
    const currentIndex = sortOptions.indexOf(sortBy);
    const nextIndex = (currentIndex + 1) % sortOptions.length;
    setSortBy(sortOptions[nextIndex]);
    
    const sortLabels = { risk_score: 'Risk Score', current_arr: 'Revenue (ARR)', name: 'Name' };
    alert(`Sorted by: ${sortLabels[sortOptions[nextIndex]]}`);
  };

  const handleFilter = () => {
    const industries = ['all', 'AI', 'SaaS', 'FinTech', 'Healthcare', 'Retail', 'CleanTech', 'EdTech', 'Security'];
    const currentIndex = industries.indexOf(filterIndustry);
    const nextIndex = (currentIndex + 1) % industries.length;
    setFilterIndustry(industries[nextIndex]);
    
    alert(industries[nextIndex] === 'all' ? 'Showing All Companies' : `Filtered by: ${industries[nextIndex]}`);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center">
          <Activity className="w-12 h-12 mx-auto mb-4 text-primary-600 animate-pulse" />
          <p className="text-gray-600">Loading portfolio data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center">
          <AlertTriangle className="w-12 h-12 mx-auto mb-4 text-danger-500" />
          <p className="text-gray-800 font-semibold mb-2">Error Loading Dashboard</p>
          <p className="text-gray-600 mb-4">{error}</p>
          <button onClick={fetchDashboardData} className="btn-primary">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">InvestorLens AI</h1>
              <p className="text-gray-600 mt-1">Portfolio Intelligence Platform</p>
            </div>
            <button onClick={handleAddCompany} className="btn-primary">
              + Add Company
            </button>
          </div>
        </div>
      </header>

      {/* Add Company Modal */}
      {showAddModal && (
        <AddCompanyModal 
          onClose={() => setShowAddModal(false)}
          onSubmit={handleSubmitCompany}
        />
      )}

      {/* Stats Cards */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <StatCard
            title="Portfolio Companies"
            value={portfolioStats.totalCompanies}
            icon={<Building2 className="w-6 h-6" />}
            iconColor="text-primary-600"
            bgColor="bg-primary-50"
          />
          <StatCard
            title="Average Risk Score"
            value={portfolioStats.avgRiskScore}
            icon={<TrendingUp className="w-6 h-6" />}
            iconColor="text-success-600"
            bgColor="bg-success-50"
            trend={portfolioStats.avgRiskScore < 50 ? 'Low Risk' : 'Monitor'}
          />
          <StatCard
            title="Active Alerts"
            value={portfolioStats.totalAlerts}
            icon={<AlertTriangle className="w-6 h-6" />}
            iconColor="text-warning-600"
            bgColor="bg-warning-50"
          />
          <StatCard
            title="Critical Alerts"
            value={portfolioStats.criticalAlerts}
            icon={<AlertTriangle className="w-6 h-6" />}
            iconColor="text-danger-600"
            bgColor="bg-danger-50"
          />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Companies Grid */}
          <div className="lg:col-span-2">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-bold text-gray-900">Portfolio Companies</h2>
              <div className="flex gap-2">
                <button onClick={handleFilter} className="btn-secondary text-sm">
                  Filter {filterIndustry !== 'all' && `(${filterIndustry})`}
                </button>
                <button onClick={handleSort} className="btn-secondary text-sm">
                  Sort {sortBy === 'risk_score' ? '(Risk)' : sortBy === 'current_arr' ? '(ARR)' : '(Name)'}
                </button>
              </div>
            </div>

            {companies.length === 0 ? (
              <div className="card text-center py-12">
                <Building2 className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                <p className="text-gray-600">No companies in portfolio yet.</p>
                <button onClick={handleAddCompany} className="btn-primary mt-4">Add Your First Company</button>
              </div>
            ) : displayedCompanies.length === 0 ? (
              <div className="card text-center py-12">
                <Building2 className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                <p className="text-gray-600">No companies match the current filter.</p>
                <button onClick={() => setFilterIndustry('all')} className="btn-secondary mt-4">Clear Filter</button>
              </div>
            ) : (
              <div className="grid grid-cols-1 gap-4">
                {displayedCompanies.map((company) => (
                  <CompanyCard key={company.id} company={company} />
                ))}
              </div>
            )}
          </div>

          {/* Alerts Panel */}
          <div className="lg:col-span-1">
            <AlertPanel alerts={alerts} stats={alertStats} />
          </div>
        </div>
      </div>
    </div>
  );
};

// Stat Card Component
const StatCard = ({ title, value, icon, iconColor, bgColor, trend }) => {
  return (
    <div className="card">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-gray-600 mb-1">{title}</p>
          <p className="text-2xl font-bold text-gray-900">{value}</p>
          {trend && (
            <p className="text-sm text-gray-500 mt-1">{trend}</p>
          )}
        </div>
        <div className={`p-3 rounded-lg ${bgColor}`}>
          <div className={iconColor}>{icon}</div>
        </div>
      </div>
    </div>
  );
};

// Add Company Modal Component
const AddCompanyModal = ({ onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    name: '',
    industry: 'AI',
    stage: 'Seed',
    current_arr: '',
    monthly_burn_rate: '',
    runway_months: '',
    employee_count: '',
    risk_score: '',
    is_active: true
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Convert string numbers to actual numbers
    const processedData = {
      ...formData,
      current_arr: parseFloat(formData.current_arr) || 0,
      monthly_burn_rate: parseFloat(formData.monthly_burn_rate) || 0,
      runway_months: parseInt(formData.runway_months) || 0,
      employee_count: parseInt(formData.employee_count) || 0,
      risk_score: parseInt(formData.risk_score) || 50
    };
    onSubmit(processedData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 max-w-md w-full mx-4 max-h-[90vh] overflow-y-auto">
        <h2 className="text-2xl font-bold mb-4">Add New Company</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Company Name *</label>
            <input
              type="text"
              name="name"
              required
              value={formData.name}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., Acme Corp"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Industry *</label>
            <select
              name="industry"
              required
              value={formData.industry}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="AI">AI</option>
              <option value="SaaS">SaaS</option>
              <option value="FinTech">FinTech</option>
              <option value="Healthcare">Healthcare</option>
              <option value="Retail">Retail</option>
              <option value="CleanTech">CleanTech</option>
              <option value="EdTech">EdTech</option>
              <option value="Security">Security</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Stage *</label>
            <select
              name="stage"
              required
              value={formData.stage}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="Seed">Seed</option>
              <option value="Series A">Series A</option>
              <option value="Series B">Series B</option>
              <option value="Series C">Series C</option>
              <option value="Series D+">Series D+</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Annual Recurring Revenue (ARR)</label>
            <input
              type="number"
              name="current_arr"
              value={formData.current_arr}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 2500000"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Monthly Burn Rate</label>
            <input
              type="number"
              name="monthly_burn_rate"
              value={formData.monthly_burn_rate}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 150000"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Runway (Months)</label>
            <input
              type="number"
              name="runway_months"
              value={formData.runway_months}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 12"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Employee Count</label>
            <input
              type="number"
              name="employee_count"
              value={formData.employee_count}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 25"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Risk Score (0-100)</label>
            <input
              type="number"
              name="risk_score"
              min="0"
              max="100"
              value={formData.risk_score}
              onChange={handleChange}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="e.g., 35"
            />
          </div>

          <div className="flex gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
            >
              Add Company
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Dashboard;

