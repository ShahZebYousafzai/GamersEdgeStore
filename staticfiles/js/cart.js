// var updateBtns = document.getElementsByClassName('update-cart')

// for(var i=0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function(){
//         var gameID = this.dataset.game
//         var action = this.dataset.action

//         console.log(action)

//         if(user === 'AnonymousUser'){
//             console.log('Not logged in')
//         }
//         else{
//             updateUserOrder(gameID, action)
//         }
//     })
// }

// var deleteBtns = document.getElementsByClassName('delete-cart')

// for(var i=0; i < deleteBtns.length; i++) {
//     deleteBtns[i].addEventListener('click', function(){
//         var gameID = this.dataset.game
//         var action = this.dataset.action

//         console.log(gameID)
//         console.log(action)

//         if(user === 'AnonymousUser'){
//             console.log('Not logged in')
//         }
//         else{
//             deleteUserOrder(gameID, action)
//         }
//     })
// }

// function updateUserOrder(gameID, action) {
//     console.log('User is Logged In, Sending data...')

//     var url = "/add_item/"

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//             'gameID': gameID,
//             'action': action,
//             'user': user  // Pass the user information
//         })
//     })

//     .then((response) => {
//         // Check if the response status is OK (200)
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         // Call json() method to parse the response body as JSON
//         return response.json();
//     })

//     .then((data) => {
//         console.log('Data:', data);
//         // Reload the page after updating the cart
//         location.reload();
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }

// function deleteUserOrder(gameID, action) {
//     console.log('User is Logged In, Sending data...')

//     var url = "/delete_item/"

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//             'gameID': gameID,
//             'action': action,
//             'user': user  // Pass the user information
//         })
//     })

//     .then((response) => {
//         // Check if the response status is OK (200)
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         // Call json() method to parse the response body as JSON
//         return response.json();
//     })

//     .then((data) => {
//         console.log('Data:', data);
//         // Reload the page after updating the cart
//         location.reload();
//     })
//     .catch((error) => {
//         console.error('Error:', error);
//     });
// }

function toggleCart(button) {
    var icon = button.querySelector('i');
    var gameId = button.getAttribute('data-game');
  
    // Toggle the heart icon immediately
    if (icon.classList.contains('bi-cart-plus')) {
        icon.classList.remove('bi-cart-plus');
        icon.classList.add('bi-cart-dash-fill');
    } else {
        icon.classList.remove('bi-cart-dash-fill');
        icon.classList.add('bi-cart-plus');
    }
  
    // Send an AJAX request to add or remove the game from the cart
    if (icon.classList.contains('bi-cart-dash-fill')) {
        addToCart(gameId);
    } else {
      removeFromCart(gameId);
    }
  }
  
  function addToCart(gameId) {
    // Send an AJAX request to add the game to the wishlist
    $.ajax({
        type: 'POST',
        url: '/add_to_cart/',
        data: {
            'game_id': gameId,
            'action': 'add'
        },
    });
  }
  
  function removeFromCart(gameId) {
    // Send an AJAX request to remove the game from the wishlist
    $.ajax({
        type: 'POST',
        url: '/remove_from_cart/',
        data: {
            'game_id': gameId,
            'action': 'remove'
        },
    });
  }