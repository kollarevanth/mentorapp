import React,{ Component } from "react";
import {BrowserRouter as Router,Route,Link} from 'react-router-dom'
class CollegeListComponent extends Component{
    state={
    collegesList:[]
    }
    componentDidMount(){
    var username="rrr"
        var password="rrr"
        const hash = Buffer.from(`${username}:${password}`).toString('base64');

    fetch('http://127.0.0.1:8000/onlineapp/serialize/',
    {
        headers:{
        'Authorization': `Basic ${this.props.token}`
        }
        }

    ).then(response => response.json())
        .then(responseJson => {
        this.setState({ collegesList : responseJson});
        })
    }
    render(){
    return(
        <React.Fragment>
            <div className="container">
                <table className="table table-bordered">
                    <thead>
                        <th>Acronym</th>
                        <th>College Name</th>
                        <th>Location</th>
                        <th>Contact</th>
                    </thead>
                    <tbody>
                    {this.state.collegesList.map(item => (
                        <tr key={item.id}>
                            <td>{item.name}</td>
                            <td><Link to={'/colleges/' + item.id}>{item.acronym}</Link></td>
                            <td>{item.location}</td>
                            <td>{item.contact}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );

}
}
export default CollegeListComponent