interface StatCardComponentProps {
  icon: string;
  iconColor?: 'blue' | 'green' | 'red' | 'orange' | 'purple' | 'cyan';
  value: string | number;
  label: string;
  trend?: { value: number; up: boolean };
  borderColor?: string;
}

export default function StatCardComponent({ 
  icon, 
  iconColor = 'blue', 
  value, 
  label,
  trend,
  borderColor 
}: StatCardComponentProps) {
  return (
    <div className="stat-card" style={{ borderTop: `4px solid ${borderColor || 'var(--primary)'}` }}>
      <div className={`stat-icon ${iconColor}`}>{icon}</div>
      <div className="stat-info">
        <span className="stat-value">{value}</span>
        <span className="stat-label">{label}</span>
        {trend && (
          <div className={`stat-trend ${trend.up ? 'up' : 'down'}`}>
            {trend.up ? '↑' : '↓'} {Math.abs(trend.value)}%
          </div>
        )}
      </div>
    </div>
  );
}
