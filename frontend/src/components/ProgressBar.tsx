interface ProgressBarProps {
  value: number;
  max?: number;
  color?: 'blue' | 'green' | 'orange' | 'red';
}

export default function ProgressBar({ value, max = 100, color = 'blue' }: ProgressBarProps) {
  const percentage = Math.min((value / max) * 100, 100);
  
  return (
    <div className="progress-bar">
      <div 
        className={`progress-bar-fill ${color}`} 
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
}
