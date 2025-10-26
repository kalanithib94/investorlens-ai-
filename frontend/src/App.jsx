import { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard/Dashboard';
import { healthCheck } from './services/api';
import './index.css';

function App() {
  const [backendStatus, setBackendStatus] = useState('checking');

  useEffect(() => {
    // Check backend connection
    checkBackend();
  }, []);

  const checkBackend = async () => {
    try {
      await healthCheck();
      setBackendStatus('connected');
    } catch (error) {
      console.error('Backend connection failed:', error);
      setBackendStatus('disconnected');
    }
  };

  return (
    <div className="App">
      {backendStatus === 'disconnected' && (
        <div className="bg-warning-100 border-l-4 border-warning-500 p-4 mb-4">
          <p className="text-sm text-warning-700">
            ⚠️ Backend connection unavailable. Using demo mode.
          </p>
        </div>
      )}
      <Dashboard />
    </div>
  );
}

export default App;

