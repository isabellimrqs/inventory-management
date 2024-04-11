import react from 'react';
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';
import NavBar from './components/NavBar';
import { ProductProvider } from './ProductContext';
import ProductsTable from './components/ProductsTable'
import AddProducts from './components/AddProducts';

function App() {
  return (
    <div>
      <Router>
        <Switch>
          <ProductProvider>
          <NavBar/>
          <div className="row">
            <div className="col-sm-10 col-xm-12 mr-auto ml-auto mt-4 mb-4">
              <Route exact path = "/" component={ProductsTable}/> {/*taking too long to load the page, comment if present */}
              
              <Route exact path = "/addproduct" component={AddProducts}/>
            </div>
          </div>
          </ProductProvider>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
