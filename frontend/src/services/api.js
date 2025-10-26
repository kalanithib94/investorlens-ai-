/**
 * API Service - HTTP client for backend communication
 * Demonstrates: API integration, error handling, async operations
 */

import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 seconds
});

// Request interceptor (for adding auth tokens, etc.)
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor (for error handling)
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error
      console.error('API Error:', error.response.status, error.response.data);
    } else if (error.request) {
      // Request made but no response
      console.error('Network Error:', error.message);
    } else {
      // Something else happened
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);

// API methods

/**
 * Companies API
 */
export const companiesAPI = {
  // Get all companies
  getAll: async (params = {}) => {
    const response = await apiClient.get('/api/companies', { params });
    return response.data;
  },

  // Get single company
  getById: async (id) => {
    const response = await apiClient.get(`/api/companies/${id}`);
    return response.data;
  },

  // Create company
  create: async (data) => {
    const response = await apiClient.post('/api/companies', data);
    return response.data;
  },

  // Update company
  update: async (id, data) => {
    const response = await apiClient.put(`/api/companies/${id}`, data);
    return response.data;
  },

  // Delete company
  delete: async (id) => {
    const response = await apiClient.delete(`/api/companies/${id}`);
    return response.data;
  },

  // Get company news
  getNews: async (id, daysBack = 7) => {
    const response = await apiClient.get(`/api/companies/${id}/news`, {
      params: { days_back: daysBack }
    });
    return response.data;
  },

  // Get AI insights
  getInsights: async (id) => {
    const response = await apiClient.get(`/api/companies/${id}/insights`);
    return response.data;
  },
};

/**
 * Analysis API
 */
export const analysisAPI = {
  // Generate summary
  generateSummary: async (companyId) => {
    const response = await apiClient.post('/api/analysis/summarize', {
      company_id: companyId,
      include_news: true,
      include_metrics: true,
    });
    return response.data;
  },

  // Calculate risk score
  calculateRiskScore: async (companyId) => {
    const response = await apiClient.post('/api/analysis/risk-score', null, {
      params: { company_id: companyId }
    });
    return response.data;
  },

  // Competitive analysis
  analyzeCompetition: async (companyId) => {
    const response = await apiClient.post(`/api/analysis/competitive-analysis/${companyId}`);
    return response.data;
  },

  // Batch analyze
  batchAnalyze: async () => {
    const response = await apiClient.post('/api/analysis/batch-analyze');
    return response.data;
  },
};

/**
 * Alerts API
 */
export const alertsAPI = {
  // Get all alerts
  getAll: async (params = {}) => {
    const response = await apiClient.get('/api/alerts', { params });
    return response.data;
  },

  // Get single alert
  getById: async (id) => {
    const response = await apiClient.get(`/api/alerts/${id}`);
    return response.data;
  },

  // Mark as read
  markRead: async (id) => {
    const response = await apiClient.patch(`/api/alerts/${id}/read`);
    return response.data;
  },

  // Resolve alert
  resolve: async (id, resolvedBy = null) => {
    const response = await apiClient.patch(`/api/alerts/${id}/resolve`, {
      resolved_by: resolvedBy
    });
    return response.data;
  },

  // Get alert stats
  getStats: async () => {
    const response = await apiClient.get('/api/alerts/stats/summary');
    return response.data;
  },
};

/**
 * Health check
 */
export const healthCheck = async () => {
  const response = await apiClient.get('/health');
  return response.data;
};

export default apiClient;

