import React from 'react';
import { List} from 'antd';
import InfiniteScroll from 'react-infinite-scroller';

const Providers = (props) => {
    return (
        <div className="demo-infinite-container">
          <InfiniteScroll
            initialLoad={false}
            pageStart={0}
            useWindow={false}
          >
            <h2>Proveedores:</h2>
            <List
              dataSource={props.data}
              renderItem={item => (
                <List.Item key={item.id}>
                  <List.Item.Meta
                    title={<a href={`prov/${item.id}`}>{item.name}</a>}
                  />
                </List.Item>
              )}
            >
            </List>
          </InfiniteScroll>
        </div>
    );
}



export default Providers;