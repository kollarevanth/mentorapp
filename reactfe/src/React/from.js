import React,{Component} from 'react'


class Form extends Component{
state={
name:'',
pass:''
};
saveName=(event)=>{
const {target :{value}} = event;
       this.setState({
            name:value
        });
}
savePass=(event)=>{
const {target :{value}} = event;
       this.setState({
            name:value
        });;
}
submit = (e) =>{

        const{name,pass} = this.state;
        fetch("http://localhost:8080/token/",{

            method:'post',
            headers:{
                "Content-type":"application/x-www-form-urlencoded; charset=UTF-8"
            },

            body:'username = ${name}&password=${pass}'
            }).then(res=>res.json()).then(response=>{

                console.log('response',response);
            })
        }
    render(){

            return(<div>

                <input onChange = {this.saveName} name = "name"/>
                <br/>
                <input onChange = {this.savePass} name = "pass"/>
                <br/>

                <button onClick={this.submit}>Submit</button>
                </div>)

        }


}
export default Form