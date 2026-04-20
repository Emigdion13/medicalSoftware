import { useState } from 'react';

const inventory = [
  { id: 1, name: 'Paracetamol 500mg', generic: 'Paracetamol', commercial: 'Dolorex', lab: 'Farmalab', stock: 12, minStock: 20, price: 3.50, expiry: '2026-08-15', supplier: 'Distribuidora Médica' },
  { id: 2, name: 'Ibuprofeno 400mg', generic: 'Ibuprofeno', commercial: 'Alivium', lab: 'Bayer', stock: 45, minStock: 15, price: 5.20, expiry: '2026-11-20', supplier: 'Bayer Bolivia' },
  { id: 3, name: 'Amoxicilina 500mg', generic: 'Amoxicilina', commercial: 'Trimox', lab: 'Roche', stock: 8, minStock: 25, price: 7.80, expiry: '2026-03-10', supplier: 'Roche Bolivia' },
  { id: 4, name: 'Omeprazol 20mg', generic: 'Omeprazol', commercial: 'Losec', lab: 'AstraZeneca', stock: 60, minStock: 20, price: 4.30, expiry: '2027-01-05', supplier: 'AstraZeneca' },
  { id: 5, name: 'Metformina 850mg', generic: 'Metformina', commercial: 'Glucophage', lab: 'BMS', stock: 3, minStock: 15, price: 6.10, expiry: '2026-06-30', supplier: 'Bristol Myers' },
  { id: 6, name: 'Loratadina 10mg', generic: 'Loratadina', commercial: 'Claritine', lab: 'Bayer', stock: 35, minStock: 10, price: 3.90, expiry: '2027-04-12', supplier: 'Bayer Bolivia' },
  { id: 7, name: 'Azitromicina 250mg', generic: 'Azitromicina', commercial: 'Zithromax', lab: 'Pfizer', stock: 18, minStock: 15, price: 9.50, expiry: '2026-09-22', supplier: 'Pfizer Bolivia' },
  { id: 8, name: 'Diclofenaco 50mg', generic: 'Diclofenaco', commercial: 'Voltaren', lab: 'Novartis', stock: 50, minStock: 20, price: 4.80, expiry: '2026-12-01', supplier: 'Novartis' },
];

export default function Farmacia() {
  const [search, setSearch] = useState('');
  
  const lowStock = inventory.filter(i => i.stock <= i.minStock);
  const totalItems = inventory.reduce((sum, i) => sum + i.stock, 0);
  
  const filtered = inventory.filter(m => 
    m.name.toLowerCase().includes(search.toLowerCase()) ||
    m.generic.toLowerCase().includes(search.toLowerCase()) ||
    m.commercial.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <div className="page-header">
        <div>
          <h2>Farmacia</h2>
          <p>Inventario y gestión de medicamentos</p>
        </div>
        <div className="page-header-actions">
          <button className="btn btn-secondary">📥 Reportes</button>
          <button className="btn btn-primary">➕ Nuevo Medicamento</button>
        </div>
      </div>

      {/* Stats */}
      <div className="stats-grid" style={{ marginBottom: 28 }}>
        <StatCard icon="💊" color="#2563eb" value={inventory.length} label="Medicamentos en catálogo" />
        <StatCard icon="📦" color="#10b981" value={totalItems} label="Total en Stock" />
        <StatCard icon="⚠️" color="#ef4444" value={lowStock.length} label="Stock Bajo" />
        <StatCard icon="📅" color="#f59e0b" value={inventory.filter(i => new Date(i.expiry) < new Date('2026-06-01')).length} label="Próx. a Vencer" />
      </div>

      {/* Search */}
      <div className="filter-bar">
        <input 
          className="form-input" 
          placeholder="🔍 Buscar medicamento..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>

      {/* Inventory Grid */}
      <div className="inventory-grid">
        {filtered.map((med, i) => {
          const isLow = med.stock <= med.minStock;
          const isCritical = med.stock <= med.minStock * 0.5;
          
          return (
            <div className="inventory-card" key={med.id} style={{ animationDelay: `${i * 0.08}s`, borderLeft: `4px solid ${isCritical ? '#ef4444' : isLow ? '#f59e0b' : '#10b981'}` }}>
              <div className="inventory-card-header">
                <h4>{med.name}</h4>
                {isCritical && <span className="badge badge-danger">Crítico</span>}
                {isLow && !isCritical && <span className="badge badge-warning">Bajo</span>}
                {!isLow && !isCritical && <span className="badge badge-success">Normal</span>}
              </div>
              <div className="inventory-details">
                <InventoryDetail label="Genérico" value={med.generic} />
                <InventoryDetail label="Comercial" value={med.commercial} />
                <InventoryDetail label="Laboratorio" value={med.lab} />
                <InventoryDetail label="Stock" value={`${med.stock} unidades`} showProgress={true} current={med.stock} max={med.minStock * 3} />
                <InventoryDetail label="Precio" value={`$${med.price.toFixed(2)}`} />
                <InventoryDetail label="Vencimiento" value={new Date(med.expiry).toLocaleDateString('es-ES')} />
                <InventoryDetail label="Proveedor" value={med.supplier} />
              </div>
              <div style={{ display: 'flex', gap: 8, marginTop: 16 }}>
                <button className="btn btn-primary" style={{ flex: 1, justifyContent: 'center', padding: '8px 12px', fontSize: 13 }}>📦 Reabastecer</button>
                <button className="btn btn-secondary" style={{ padding: '8px 12px', fontSize: 13 }}>✏️</button>
              </div>
            </div>
          );
        })}
      </div>

      {/* Low Stock Alert */}
      {lowStock.length > 0 && (
        <div className="section-card" style={{ marginTop: 28, borderLeft: '4px solid #ef4444' }}>
          <div className="section-header">
            <h3>🚨 Alerta de Stock Bajo ({lowStock.length} medicamentos)</h3>
          </div>
          <table className="data-table">
            <thead>
              <tr>
                <th>Medicamento</th>
                <th>Stock Actual</th>
                <th>Mínimo</th>
                <th>Nivel</th>
                <th>Vencimiento</th>
              </tr>
            </thead>
            <tbody>
              {lowStock.map(med => (
                <tr key={med.id}>
                  <td style={{ fontWeight: 600 }}>{med.name}</td>
                  <td><span style={{ color: '#ef4444', fontWeight: 700 }}>{med.stock}</span></td>
                  <td>{med.minStock}</td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                      <div className="progress-bar" style={{ width: 100 }}>
                        <div className="progress-bar-fill red" style={{ width: `${Math.min((med.stock / med.minStock) * 100, 100)}%` }} />
                      </div>
                      <span style={{ fontSize: 12, color: '#ef4444', fontWeight: 600 }}>
                        {Math.round((med.stock / med.minStock) * 100)}%
                      </span>
                    </div>
                  </td>
                  <td>{new Date(med.expiry).toLocaleDateString('es-ES')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function StatCard({ icon, color, value, label }: { icon: string; color: string; value: string | number; label: string }) {
  return (
    <div className="stat-card" style={{ borderTop: `4px solid ${color}` }}>
      <div className="stat-icon">{icon}</div>
      <div className="stat-info">
        <span className="stat-value">{value}</span>
        <span className="stat-label">{label}</span>
      </div>
    </div>
  );
}

function InventoryDetail({ label, value, showProgress, current, max }: { label: string; value: string; showProgress?: boolean; current?: number; max?: number }) {
  return (
    <div className="inventory-detail-row">
      <span className="label">{label}:</span>
      {showProgress && current !== undefined && max !== undefined ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1 }}>
          <div className="progress-bar" style={{ width: 80 }}>
            <div className={`progress-bar-fill ${current <= max * 0.5 ? 'red' : current <= max ? 'orange' : 'green'}`} style={{ width: `${Math.min((current / max) * 100, 100)}%` }} />
          </div>
          <span style={{ fontSize: 12, fontWeight: 600 }}>{value}</span>
        </div>
      ) : (
        <span>{value}</span>
      )}
    </div>
  );
}
