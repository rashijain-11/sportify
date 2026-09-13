// Sportify - Interactive Store JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // 1. Auto-dismiss alerts after 4 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            try {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } catch (e) {}
        }, 4000);
    });

    // 2. Quantity selector (+ / -) in Product Details and Cart
    const qtyDecrements = document.querySelectorAll('.btn-qty-decrement');
    const qtyIncrements = document.querySelectorAll('.btn-qty-increment');

    qtyDecrements.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.closest('.input-group').querySelector('.input-qty');
            if (input) {
                let currentVal = parseInt(input.value) || 1;
                if (currentVal > 1) {
                    input.value = currentVal - 1;
                }
            }
        });
    });

    qtyIncrements.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.closest('.input-group').querySelector('.input-qty');
            if (input) {
                let currentVal = parseInt(input.value) || 1;
                const max = parseInt(input.getAttribute('max')) || 99;
                if (currentVal < max) {
                    input.value = currentVal + 1;
                }
            }
        });
    });

    // 3. Checkout payment method toggle
    const paymentRadios = document.querySelectorAll('input[name="payment_method"]');
    const cardFields = document.getElementById('card-fields');
    const upiFields = document.getElementById('upi-fields');
    const codNotice = document.getElementById('cod-notice');

    if (paymentRadios.length > 0) {
        function updatePaymentUI() {
            const selected = document.querySelector('input[name="payment_method"]:checked')?.value;
            if (cardFields) cardFields.style.display = (selected === 'card') ? 'block' : 'none';
            if (upiFields) upiFields.style.display = (selected === 'upi') ? 'block' : 'none';
            if (codNotice) codNotice.style.display = (selected === 'cod') ? 'block' : 'none';
        }

        paymentRadios.forEach(radio => {
            radio.addEventListener('change', updatePaymentUI);
        });

        // Initialize state
        updatePaymentUI();
    }
});
