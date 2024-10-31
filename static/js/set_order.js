const SORT_ELEMENT = document.getElementById("order_list");

function setOrder(event) {
    let value = event.target.value;
    if (value === "reset") {
        Cookies.remove("order");
    } else {
        Cookies.set("order", value, { expires: 7 });
    }
    location.reload();
}

if (SORT_ELEMENT) {
    SORT_ELEMENT.addEventListener("change", setOrder);
}
