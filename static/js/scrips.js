document.addEventListener("DOMContentLoaded", () => {
    // Simulated cart count (replace with actual API logic if needed)
    const cartCount = document.getElementById("cart-count");
    let totalItems = 0; // Replace with actual data from the server

    // Example: Increment cart count on some event (replace with actual logic)
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", () => {
            totalItems += 1; // Increment the cart count
            cartCount.textContent = totalItems;
        });
    });
});
