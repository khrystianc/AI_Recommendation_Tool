import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Recommendations from './components/Recommendations';
import ItemList from './components/ItemList';

const App = () => {
  return (
    <div>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/recommendations" component={Recommendations} />
        <Route path="/items" component={ItemList} />
      </Switch>
    </div>
  );
};

export default App;
