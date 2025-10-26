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
            <button className="btn-primary">
              + Add Company
            </button>
          </div>
        </div>
      </header>

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
                <button className="btn-secondary text-sm">Filter</button>
                <button className="btn-secondary text-sm">Sort</button>
              </div>
            </div>

            {companies.length === 0 ? (
              <div className="card text-center py-12">
                <Building2 className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                <p className="text-gray-600">No companies in portfolio yet.</p>
                <button className="btn-primary mt-4">Add Your First Company</button>
              </div>
            ) : (
              <div className="grid grid-cols-1 gap-4">
                {companies.map((company) => (
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

export default Dashboard;

