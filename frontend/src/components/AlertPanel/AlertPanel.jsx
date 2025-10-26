/**
 * Alert Panel Component - Display active alerts
 * Demonstrates: List rendering, severity indicators, user interaction
 */

import { AlertTriangle, AlertCircle, Info, CheckCircle, X } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';

const AlertPanel = ({ alerts, stats }) => {
  const getSeverityIcon = (severity) => {
    switch (severity) {
      case 'critical':
        return <AlertTriangle className="w-5 h-5 text-danger-500" />;
      case 'high':
        return <AlertCircle className="w-5 h-5 text-warning-500" />;
      case 'medium':
        return <Info className="w-5 h-5 text-primary-500" />;
      case 'low':
        return <CheckCircle className="w-5 h-5 text-success-500" />;
      default:
        return <Info className="w-5 h-5 text-gray-500" />;
    }
  };

  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'critical':
        return 'danger';
      case 'high':
        return 'warning';
      case 'medium':
        return 'primary';
      case 'low':
        return 'success';
      default:
        return 'gray';
    }
  };

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-gray-900">Active Alerts</h2>
        {stats.total_unresolved > 0 && (
          <span className="badge badge-danger">
            {stats.total_unresolved} unresolved
          </span>
        )}
      </div>

      {/* Alert Stats */}
      <div className="grid grid-cols-2 gap-3 mb-4 pb-4 border-b border-gray-200">
        <div className="text-center p-2 bg-danger-50 rounded-lg">
          <p className="text-2xl font-bold text-danger-700">{stats.critical || 0}</p>
          <p className="text-xs text-danger-600">Critical</p>
        </div>
        <div className="text-center p-2 bg-warning-50 rounded-lg">
          <p className="text-2xl font-bold text-warning-700">{stats.high || 0}</p>
          <p className="text-xs text-warning-600">High</p>
        </div>
      </div>

      {/* Alerts List */}
      <div className="space-y-3 max-h-96 overflow-y-auto">
        {alerts.length === 0 ? (
          <div className="text-center py-8">
            <CheckCircle className="w-12 h-12 mx-auto mb-3 text-success-500" />
            <p className="text-gray-600">No active alerts</p>
            <p className="text-sm text-gray-500 mt-1">Your portfolio is looking good!</p>
          </div>
        ) : (
          alerts.map((alert) => (
            <AlertItem
              key={alert.id}
              alert={alert}
              icon={getSeverityIcon(alert.severity)}
              color={getSeverityColor(alert.severity)}
            />
          ))
        )}
      </div>

      {alerts.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <button className="w-full text-center text-sm text-primary-600 hover:text-primary-700 font-medium">
            View All Alerts →
          </button>
        </div>
      )}
    </div>
  );
};

// Alert Item Component
const AlertItem = ({ alert, icon, color }) => {
  return (
    <div className={`p-3 rounded-lg border-l-4 border-${color}-500 bg-${color}-50`}>
      <div className="flex items-start gap-3">
        <div className="flex-shrink-0">{icon}</div>
        <div className="flex-1 min-w-0">
          <div className="flex items-start justify-between gap-2">
            <div className="flex-1">
              <p className="text-sm font-semibold text-gray-900 mb-1">
                {alert.title}
              </p>
              <p className="text-xs text-gray-600 mb-2">
                {alert.company_name}
              </p>
            </div>
            <button className="text-gray-400 hover:text-gray-600">
              <X className="w-4 h-4" />
            </button>
          </div>
          <p className="text-xs text-gray-700 line-clamp-2 mb-2">
            {alert.description}
          </p>
          <div className="flex items-center justify-between">
            <span className={`badge badge-${color} text-xs`}>
              {alert.severity}
            </span>
            <span className="text-xs text-gray-500">
              {formatDistanceToNow(new Date(alert.created_at), { addSuffix: true })}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AlertPanel;

