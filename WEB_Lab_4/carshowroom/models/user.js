var mongoose = require("mongoose");

var Schema = mongoose.Schema;

var UserSchema = new Schema({
    first_name: { type: String, required: true, max: 100 },
    family_name: { type: String, required: true, max: 100 },
    date_of_birth: { type: Date, validate: { validator: isAdult, message: 'User must be at least 18 years old' } },
    email: { type: String, required: true, unique: true, validate: { validator: isEmailValid, message: 'Invalid email address' } },
    phone: { type: String, validate: { validator: isPhoneValid, message: 'Invalid phone number' } },
});

function isPhoneValid(phone) {
    // Regular expression to validate phone number format
    // Adjust the regular expression according to your desired phone number format
    const phoneRegex = /^\d{10}$/; // Example: 10-digit phone number format
    return phoneRegex.test(phone);
}

function isEmailValid(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isAdult(dateOfBirth) {
    const today = new Date();
    const age = today.getFullYear() - dateOfBirth.getFullYear();
    const monthDiff = today.getMonth() - dateOfBirth.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dateOfBirth.getDate())) {
        age--;
    }
    return age >= 18;
}

//Export model
module.exports = mongoose.model("User", UserSchema);

