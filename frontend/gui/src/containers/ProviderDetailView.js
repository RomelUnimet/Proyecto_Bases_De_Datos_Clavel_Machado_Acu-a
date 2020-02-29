import React from 'react';
import axios from 'axios';
import { Card } from 'antd';

class ProviderDetail extends React.Component{

    state = {
        provider: {}
    }

    componentDidMount(){
        const providerID = this.props.match.params.providerID;
        axios.get(`http://127.0.0.1:8000/rest/prov/${providerID}`).then(res => {
            this.setState({
                provider: res.data
            });
        })
    }


    render(){
        return (

            <Card title={this.state.provider.name + " (" + this.state.provider.id + ")"}>
                <p>Telefono principal: {this.state.provider.main_phone}</p>
                <p>Otro telefono: {this.state.provider.phone}</p>
                <p>Direccion: {this.state.provider.address}</p>
                <p>E-mail: {this.state.provider.email}</p>
            </Card>
            

        )
    }
}

export default ProviderDetail;