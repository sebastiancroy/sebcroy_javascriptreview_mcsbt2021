"use strict";

const createUser = ()=>{
    console.log("Here", document.getElementById('inputfirstname').value);
    let new_event = {
        'firstname': document.getElementById('inputfirstname').value,
        'lastname': document.getElementById('inputlastname').value,
        'birthday': document.getElementById('inputbirthday').value,
        'role': document.getElementById('inputrole').value,
        'about': document.getElementById('inputabout').value,
    };
    fetch('/addUser', {
        method: 'POST',
        mode: 'cors',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(new_event)
    }).then( response => {
        if (response.status === 200){
            console.log("Working");
        }
    }).catch( e => {
        console.log(e);
    })
}



