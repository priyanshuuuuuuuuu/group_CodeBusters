document.addEventListener('DOMContentLoaded', function () {
    const nextButton = document.getElementById('submit');
    const otpContainer = document.getElementById('otpContainer');
    const loginPart = document.querySelector('.login_part');
    const buttonContainer = document.querySelector('.button_container');

    nextButton.addEventListener('click', function () {
        // Show the OTP container with a sliding effect
        otpContainer.classList.add('visible');

        // Add class to adjust padding and create space for OTP section
        loginPart.classList.add('show_otp');

        // Change the button text to "Confirm"
        nextButton.textContent = 'Confirm';
        nextButton.classList.remove('next_button');
        nextButton.classList.add('confirm_button');

        // Add sliding effect for the button
        buttonContainer.classList.add('show_otp');
    });

    // Handle OTP input focus shift
    const otpInputs = document.querySelectorAll('.otp_input');

    otpInputs.forEach((input, index) => {
        input.addEventListener('input', function () {
            if (input.value.length === 1 && index < otpInputs.length - 1) {
                otpInputs[index + 1].focus();
            }
        });

        input.addEventListener('keydown', function (e) {
            if (e.key === 'Backspace' && input.value.length === 0 && index > 0) {
                otpInputs[index - 1].focus();
            }
        });
    });
});

