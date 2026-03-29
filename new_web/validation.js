// js/validation.js
document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            event.preventDefault(); 
            
            const emailInput = document.getElementById('reg-email');
            const passwordInput = document.getElementById('reg-password');
            const emailError = document.getElementById('email-error');
            const passwordError = document.getElementById('password-error');
            
            let isValid = true;
            
            // Email Validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailInput.value || !emailRegex.test(emailInput.value)) {
                emailError.textContent = 'Please enter a valid email address.';
                isValid = false;
            } else {
                emailError.textContent = '';
            }

            // Password Validation
            const minLength = 8;
            if (passwordInput.value.length < minLength) {
                passwordError.textContent = `Password must be at least ${minLength} characters long.`;
                isValid = false;
            } else {
                passwordError.textContent = '';
            }

            if (isValid) {
                alert('Sign Up Successful! (Pretending to submit data)');
                signupForm.reset();
            }
        });
    }
});