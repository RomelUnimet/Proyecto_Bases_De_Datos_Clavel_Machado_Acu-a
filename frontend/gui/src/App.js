import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';
import './App.css';
import 'antd/dist/antd.css';
import ProductLayout from './containers/productLayout';

function App() {
  return (
    <div className="App">
      <Router>
         <ProductLayout>
          <BaseRouter/>
        </ProductLayout>
      </Router>

      
    </div>
  );
}

export default App;
