import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Job from './Jobs.js'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    }
  }

  componentDidMount() {
    const result = fetch('http://127.0.0.1:8000/info/1/')
      .then(response => response.json())
      .then(data => this.setState({ data }))
      .then(console.log(this.state.data))
      .catch(function(e) {
        console.log(e);
      }
    )
  }

  render() {

    if(this.state.data === null) return null
    return (
      <div className="app">
        <div className='frame'>
          <div className='corners'>
            <div className='info'>
              <div className='text'>
                <h1>{ this.state.data.first_name } { this.state.data.last_name }</h1>
                <h4><span>Date of birth:</span> { this.state.data.date_of_birth } </h4>
                <h4><span>City:</span> { this.state.data.city }</h4>
                <h4><span>Phone number:</span> { this.state.data.phone_number }</h4>
                <h4><span>Email:</span> { this.state.data.email }</h4>
              </div>
              <div className='text'>
                <a href={ this.state.data.facebook_link } target="_blank">
                  <img src="http:\/\/localhost:8000/media/uploaded_images/facebook_2.png"/>
                </a>
                <a href={this.state.data.linkedin_link } target="_blank">
                  <img src="http:\/\/localhost:8000/media/uploaded_images/Linkedin_circle.svg_.png"/> 
                </a>
              </div>
            </div>    
            <div className='info'>
              <img src={"http:\/\/localhost:8000" + this.state.data.photo} height="250"  />
            </div>
          </div>
          <Job jobs_list={this.state.data.jobs} />
        </div>
      </div>
    );
  }
}

export default App;
