import React from 'react';
import './App.css';
import UserList from './components/user.js'
import Footer from './components/footer.js'
import axios from 'axios'
import Header from "./components/header";
import Button from 'react-bootstrap/Button';


// const home = 'http://127.0.0.1:8000/api/';
// const get_url = (url) => '${home}${url}';

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

  componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
}


   render () {
       return (
           <div style={{background: '#32CD32',
                        textAlign: "center"}}>
               <Header/>
               <UserList users={this.state.users} />
               <Footer/>
           </div>

       )
   }
}


export default App;