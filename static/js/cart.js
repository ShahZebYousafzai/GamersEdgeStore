var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var gameID = this.dataset.game
        var action = this.dataset.action

        console.log(action)

        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            updateUserOrder(gameID, action)
        }
    })
}

function updateUserOrder(gameID, action) {
    console.log('User is Logged In, Sending data...')

    var url = "/update-item/"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'gameID': gameID,
            'action': action,
            'user': user  // Pass the user information
        })
    })

    .then((response) => {
        // Check if the response status is OK (200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Call json() method to parse the response body as JSON
        return response.json();
    })

    .then((data) => {
        console.log('Data:', data);
        // Reload the page after updating the cart
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
