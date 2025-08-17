const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const { check, validationResult } = require('express-validator');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Middleware for form validation
const validateForm = [
  check('name')
    .notEmpty()
    .withMessage('Name is required'),
  check('email')
    .isEmail()
    .withMessage('Invalid email address'),
  check('password')
    .isLength({ min: 8 })
    .withMessage('Password must be at least 8 characters long')
];

// Route for the form page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route for handling form submission
app.post('/submit', validateForm, (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  // Process the form data
  const { name, email, password } = req.body;
  console.log('Form data:', { name, email, password });

  // Redirect or send a success response
  res.status(200).json({ message: 'Form submitted successfully' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

FILENAME: public/index.html