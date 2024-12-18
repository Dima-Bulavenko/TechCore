let stripePublicKey = document
    .getElementById("id_stripe_public_key")
    .textContent.slice(1, -1);
let stripe = Stripe(stripePublicKey);
const classes = {
    base: "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
    invalid: "border-red-500 text-red-500",
    complete: "border-green-500 text-green-500",
};
let elements = stripe.elements();
let cardNumber = elements.create("cardNumber", {
    showIcon: true,
    classes,
});
let cardExpiry = elements.create("cardExpiry", {
    classes,
});
let cardCvc = elements.create("cardCvc", {
    classes,
});

let errorDiv = document.getElementById("card-errors");
let submitButton = document.getElementById("complete_order_button");
let loadSpinner = document.getElementById("payment_load_spinner");

cardNumber.mount("#cardNumber");
cardExpiry.mount("#cardExpiry");
cardCvc.mount("#cardCvc");

// Handle realtime validation errors on the card element
function addErrorMessage(event) {
    let errorDiv = document.getElementById(
        event.elementType
    ).nextElementSibling;
    if (event.error) {
        errorDiv.classList.remove("hidden");
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.classList.add("hidden");
        errorDiv.textContent = "";
    }
}

cardNumber.on("change", addErrorMessage);
cardExpiry.on("change", addErrorMessage);
cardCvc.on("change", addErrorMessage);

function showLoading(flag) {
    if (flag) {
        loadSpinner.dataset.open = "true";
        submitButton.setAttribute("disabled", true);
    } else {
        loadSpinner.dataset.open = "false";
        submitButton.removeAttribute("disabled");
    }
}

// Handle form submit
let form = document.getElementById("checkout_form");

form.addEventListener("htmx:confirm", async (event) => {
    showLoading(true);
    if (!form.querySelector('input[name="payment_intent_id"]')) {
        event.preventDefault();
        const { paymentMethod, error } = await stripe.createPaymentMethod({
            type: "card",
            card: cardNumber,
        });
        if (error) {
            event.preventDefault();
            errorDiv.textContent = error.message;
            showLoading(false);
        } else {
            var hiddenInput = document.createElement("input");
            hiddenInput.setAttribute("type", "hidden");
            hiddenInput.setAttribute("name", "payment_method_id");
            hiddenInput.setAttribute("value", paymentMethod.id);
            form.appendChild(hiddenInput);
            event.detail.issueRequest();
        }
    }
});

form.addEventListener("htmx:afterRequest", async (event) => {
    let statusParams = document.getElementById("status_params").textContent;
    const { cardError, clientSecret, requiredAction, isFormValid } =
        JSON.parse(statusParams);

    if (!isFormValid) return showLoading(false);

    if (cardError) {
        errorDiv.textContent = cardError;
        showLoading(false);
        return;
    }

    if (requiredAction) {
        const { error: errorAction, paymentIntent } =
            await stripe.handleCardAction(clientSecret);
        if (errorAction) {
            errorDiv.textContent = errorAction.message;
            showLoading(false);
            return;
        } else {
            var hiddenInput = document.createElement("input");
            hiddenInput.setAttribute("type", "hidden");
            hiddenInput.setAttribute("name", "payment_intent_id");
            hiddenInput.setAttribute("value", paymentIntent.id);
            form.appendChild(hiddenInput);
            htmx.trigger(`#${form.id}`, "submit");
        }
        return;
    }
});
