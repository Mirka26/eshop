function performSearch() {
  var searchTerm = document.getElementById('searchInput').value;
  alert('Vyhľadávanie: ' + searchTerm);
    }


document.getElementById('searchInput').addEventListener('input', performSearch);


function displayNextImage() {
  x = (x === images.length - 1) ? 0 : x + 1;
  document.getElementById("img").src = images[x];
}


function displayPreviousImage() {
  x = (x <= 0) ? images.length - 1 : x - 1;
  document.getElementById("img").src = images[x];
}


function startTimer() {
  setInterval(displayNextImage, 3000);
}


var images = [], x = -1;
images[0] = "HP.webp";
images[1] = "sony.webp";
images[2] = "startpictures.webp";

function redirectToHomePage() {
  window.location.href = "index.html"; 
}

function removeProduct(button) {
    var productDiv = button.parentElement;
    productDiv.remove();
    checkEmptyCart();
}

function removeAllProducts() {
    var cart = document.getElementById('cart');
    cart.innerHTML = '';
    checkEmptyCart();
}

function checkEmptyCart() {
    var cart = document.getElementById('cart');
    if (cart.children.length === 0) {
        window.location.href = 'cart.html';
    }
}


