document.addEventListener('DOMContentLoaded', function () {
    const promoForm = document.getElementById('promoForm');
    const btnCheckPromo = document.getElementById('promocheckbtn');

    btnCheckPromo.addEventListener('click', function () {
        const promoCode = inputPromo.value;

        fetch(`/information/check_promo/${promoCode}`, {
            method: 'GET',
        })
            .then(response => response.json())
            .then(data => {
                if (data.valid) {
                    const discount = data.description;

                    alert(`Промокод применен. При заказе вы получите: ${discount}`);
                } else {
                    alert('Промокод недействителен.');
                }
            })
            .catch(error => {
                console.error('Ошибка при проверке промокода:', error);
            });
    });
});