// When the html document is ready (rendered)
$(document).ready(function () {
    // Take markup element with id jq-notification for ajax notifications into a variable
    var successMessage = $("#jq-notification");

    // Catch the event of a click on the add to cart button
    $(document).on("click", ".add-to-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // We take the counter element in the cart icon and take the value from there
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Get product id from data-product-id attribute
        var product_id = $(this).data("product-id");

        // From the href attribute we take the link to the django controller
        var add_to_cart_url = $(this).attr("href");

        // Make post request via ajax without reloading the page
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // After 7 seconds, clear the message
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Increase the number of items in the cart (rendering in the template)
                cartCount++;
                goodsInCartCount.text(cartCount);

                // Change the contents of the cart to the response from django (new rendered fragment of the cart markup)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Error when adding an item to cart");
            },
        });
    });
    // Take element by id from markup - django alerts
    var notification = $('#notification');
    // And after 7 seconds, we're out.
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // Clicking on the cart icon opens a pop-up (modal) window
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Click on the button to close the cart windows
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Delivery method selection radio button event handler
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Hide or show shipping address inputs
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});