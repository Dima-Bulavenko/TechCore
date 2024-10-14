let stripePublicKey = document
    .getElementById("id_stripe_public_key")
    .textContent.slice(1, -1);
let clientSecret = document
    .getElementById("id_client_secret")
    .textContent.slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let card = elements.create("card");
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
    let errorDiv = document.getElementById("card-errors");
    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submit
let form = document.getElementById("checkout_form");

form.addEventListener("submit", function (event) {
    event.preventDefault();
    card.update({ disabled: true });
    let submitButton = document.getElementById("complete_order_button");
    let loadSpinner = document.getElementById("payment_load_spinner");
    loadSpinner.dataset.open = "true";
    submitButton.setAttribute("disabled", true);
    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            },
        })
        .then(function (result) {
            if (result.error) {
                let errorDiv = document.getElementById("card-errors");
                errorDiv.textContent = result.error.message;
                card.update({ disabled: false });
                submitButton.removeAttribute("disabled");
                loadSpinner.dataset.open = "false";
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    form.submit();
                }
            }
        });
});
