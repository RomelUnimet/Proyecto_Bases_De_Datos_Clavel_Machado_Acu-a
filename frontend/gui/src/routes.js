import React from 'react';
import { Route } from 'react-router-dom';
import ProductList from './containers/ProductListView';
import ProductDetail from './containers/ProductDetailView';
import ProviderList from './containers/ProviderListView';
import ProviderDetail from './containers/ProviderDetailView';


const BaseRouter = () => (
    <div>
        <Route exact path='/prov' component={ProviderList}/>
        <Route exact path='/' component={ProductList}/>
        <Route exact path='/prod/:productID' component={ProductDetail}/>
        <Route exact path='/prov/:providerID' component={ProviderDetail}/>
        
    </div>
)

export default BaseRouter;