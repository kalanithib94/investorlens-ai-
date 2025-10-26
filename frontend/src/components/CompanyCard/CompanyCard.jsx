/**
 * Company Card Component - Display company summary
 * Demonstrates: Component design, conditional rendering, color coding
 */

import { Building2, TrendingUp, TrendingDown, Calendar, DollarSign } from 'lucide-react';
import { formatDistanceToNow } from 'date-fns';

const CompanyCard = ({ company }) => {
  // Determine risk level and color
  const getRiskLevel = (score) => {
    if (score < 26) return { level: 'Low', color: 'success' };
    if (score < 51) return { level: 'Medium', color: 'warning' };
    if (score < 76) return { level: 'High', color: 'warning' };
    return { level: 'Critical', color: 'danger' };
  };

  const risk = getRiskLevel(company.risk_score);

  // Format currency
  const formatCurrency = (value) => {
    if (!value) return 'N/A';
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      notation: 'compact',
      maximumFractionDigits: 1,
    }).format(value);
  };

  return (
    <div className="card hover:shadow-md transition-shadow cursor-pointer">
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-start gap-3">
          <div className="p-2 bg-primary-50 rounded-lg">
            <Building2 className="w-6 h-6 text-primary-600" />
          </div>
          <div>
            <h3 className="text-lg font-semibold text-gray-900">{company.name}</h3>
            <p className="text-sm text-gray-600">{company.industry || 'Technology'}</p>
          </div>
        </div>
        <span className={`badge badge-${risk.color}`}>
          {company.stage || 'Series A'}
        </span>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-3 gap-4 mb-4">
        <div>
          <p className="text-xs text-gray-500 mb-1">ARR</p>
          <p className="text-sm font-semibold text-gray-900">
            {formatCurrency(company.current_arr)}
          </p>
        </div>
        <div>
          <p className="text-xs text-gray-500 mb-1">Burn Rate</p>
          <p className="text-sm font-semibold text-gray-900">
            {formatCurrency(company.monthly_burn_rate)}/mo
          </p>
        </div>
        <div>
          <p className="text-xs text-gray-500 mb-1">Runway</p>
          <p className="text-sm font-semibold text-gray-900">
            {company.runway_months || 'N/A'} mo
          </p>
        </div>
      </div>

      {/* Risk Score */}
      <div className="pt-4 border-t border-gray-200">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">Risk Score:</span>
            <span className={`font-semibold text-${risk.color}-600`}>
              {company.risk_score}/100
            </span>
            <span className={`badge badge-${risk.color} text-xs`}>
              {risk.level}
            </span>
          </div>
          
          {/* Risk indicator */}
          {company.risk_score >= 50 ? (
            <TrendingUp className="w-4 h-4 text-danger-500" />
          ) : (
            <TrendingDown className="w-4 h-4 text-success-500" />
          )}
        </div>

        {/* Risk bar */}
        <div className="mt-2 w-full bg-gray-200 rounded-full h-2">
          <div
            className={`bg-${risk.color}-500 h-2 rounded-full transition-all`}
            style={{ width: `${company.risk_score}%` }}
          />
        </div>
      </div>

      {/* Footer */}
      <div className="mt-4 flex items-center justify-between text-xs text-gray-500">
        <div className="flex items-center gap-1">
          <Calendar className="w-3 h-3" />
          Updated {company.updated_at ? formatDistanceToNow(new Date(company.updated_at), { addSuffix: true }) : 'recently'}
        </div>
        <button className="text-primary-600 hover:text-primary-700 font-medium">
          View Details →
        </button>
      </div>
    </div>
  );
};

export default CompanyCard;

