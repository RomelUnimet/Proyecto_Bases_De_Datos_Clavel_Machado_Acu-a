import React from 'react';
import { Route } from 'react-router-dom';
import ProductList from './containers/ProductListView';
import ProductDetail from './containers/ProductDetailView';


const BaseRouter = () => (
    <div>
        <Route exact path='/' component={ProductList}/>
        <Route exact path='/:productID' component={ProductDetail}/>
    </div>
)

export default BaseRouter;