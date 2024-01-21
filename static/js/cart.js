
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
        console.log('Add to Cart', gameId);
        addToCart(gameId);
    } else {
      removeFromCart(gameId);
    }
  }

  function deleteFromCart(button) {
    var icon = button.querySelector('i');
    var gameId = button.getAttribute('data-game');
    console.log('Delete from Cart', gameId);
    removeFromCart(gameId)
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
        success: function(data) {
            console.log(data);
            cartCount = document.getElementsByClassName('cart-count')[0];  // Assuming there is only one element with the class 'cart-count'
            cartCount.innerHTML = data.cartItems;  // Update to use the correct key
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
        success: function(data) {
            console.log(data);
            cartCount = document.getElementsByClassName('cart-count')[0];  // Assuming there is only one element with the class 'cart-count'
            cartCount.innerHTML = data.cartItems;  // Update to use the correct key
        },
    });
  }
  