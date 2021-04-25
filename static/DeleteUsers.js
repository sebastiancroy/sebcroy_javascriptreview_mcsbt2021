
const deleteUser = (id) => {
    console.log("here");
    fetch('/deleteUser/' + id, {
        method: 'DELETE',
        mode: 'cors',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        }
    }).then( response => {
        if(response.status === 200){
            console.log("working");
        }
        else{
            console.log("Failed");
        }
    }).catch( e => {
        console.log(e);
    });
}




