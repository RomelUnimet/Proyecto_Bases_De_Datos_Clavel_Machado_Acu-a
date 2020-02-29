import React from 'react';
import axios from 'axios';
import Providers from '../components/providers';

class ProviderList extends React.Component{

    state = {
        providers: []
    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/rest/prov/').then(res => {
            this.setState({
                providers: res.data
            });
        })
    }


    render(){
        return (

            <Providers data ={this.state.providers}/>

        )
    }
}

export default ProviderList;