interface BadgeProps {
  text: string;
  variant?: 'success' | 'warning' | 'danger' | 'info' | 'purple';
}

export default function Badge({ text, variant = 'info' }: BadgeProps) {
  return (
    <span className={`badge badge-${variant}`}>{text}</span>
  );
}
