import React,{ Component } from "react"
import CollegeListComponent from './GetCollege.js'
import StudentListComponent from './GetStudents.js'
import {BrowserRouter as Router,Route,Link} from 'react-router-dom'
import Form from './from'
class ReactApp extends Component
{

state={
value:''
}

componentWillMount()
{
var username="rrr";
var password="rrr"
const hash=Buffer.from(`${username}:${password}`).toString('base64')
this.setState({token:hash})

}


    render()
    {
    return(
    <div className="App">
    <React.Fragment>
    <Router>
    <div>
    <Route exact path="/hello" component={Form}/>
    <Route exact path="/college" render={pops=><CollegeListComponent token={this.state.token}/>}/>
    <Route exact path="/colleges/:id" render={props=><StudentListComponent{...props} token={this.state.token}/>}/>
    </div>
    </Router>
    </React.Fragment>
    </div>
    );

        }

}

export default ReactApp