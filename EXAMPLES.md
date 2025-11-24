# Code Examples

This file contains example code snippets that work great with the Gradio Winter Hack Code Editor.

## Example 1: Animated Card Component

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animated Card</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="card">
        <div class="card-image">
            <img src="https://via.placeholder.com/400x250" alt="Card image">
        </div>
        <div class="card-content">
            <h2>Amazing Feature</h2>
            <p>This card has a beautiful hover animation and gradient effects.</p>
            <button class="btn">Learn More</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
body {
    margin: 0;
    padding: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Arial', sans-serif;
}

.card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    max-width: 400px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.card-image img {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.card-content {
    padding: 30px;
}

.card-content h2 {
    margin: 0 0 15px 0;
    color: #333;
}

.card-content p {
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
}

.btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 25px;
    cursor: pointer;
    font-size: 16px;
    transition: opacity 0.3s ease;
}

.btn:hover {
    opacity: 0.9;
}
```

### JavaScript
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const btn = document.querySelector('.btn');
    
    btn.addEventListener('click', function() {
        this.textContent = 'Loading...';
        
        setTimeout(() => {
            this.textContent = 'Learn More';
            alert('Feature clicked!');
        }, 1000);
    });
});
```

## Example 2: Interactive Navigation Bar

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navigation Bar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo">MyBrand</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
        <button class="hamburger">☰</button>
    </nav>
    <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background: #f5f5f5;
}

.navbar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 15px 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.logo {
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 30px;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-size: 16px;
    transition: opacity 0.3s ease;
}

.nav-links a:hover {
    opacity: 0.8;
}

.hamburger {
    display: none;
    background: none;
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
}

@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    
    .hamburger {
        display: block;
    }
}
```

### JavaScript
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    hamburger.addEventListener('click', function() {
        if (navLinks.style.display === 'flex') {
            navLinks.style.display = 'none';
        } else {
            navLinks.style.display = 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '60px';
            navLinks.style.right = '50px';
            navLinks.style.background = '#764ba2';
            navLinks.style.padding = '20px';
            navLinks.style.borderRadius = '10px';
        }
    });
});
```

## Example 3: Countdown Timer

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Launch Countdown</h1>
        <div class="timer">
            <div class="time-box">
                <span id="days">00</span>
                <label>Days</label>
            </div>
            <div class="time-box">
                <span id="hours">00</span>
                <label>Hours</label>
            </div>
            <div class="time-box">
                <span id="minutes">00</span>
                <label>Minutes</label>
            </div>
            <div class="time-box">
                <span id="seconds">00</span>
                <label>Seconds</label>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Arial', sans-serif;
}

.container {
    text-align: center;
    color: white;
}

h1 {
    font-size: 48px;
    margin-bottom: 40px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.timer {
    display: flex;
    gap: 20px;
    justify-content: center;
}

.time-box {
    background: rgba(255, 255, 255, 0.2);
    padding: 30px 40px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.time-box span {
    display: block;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

.time-box label {
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 2px;
}
```

### JavaScript
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Set launch date (7 days from now)
    const launchDate = new Date().getTime() + (7 * 24 * 60 * 60 * 1000);
    
    function updateCountdown() {
        const now = new Date().getTime();
        const distance = launchDate - now;
        
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        document.getElementById('days').textContent = String(days).padStart(2, '0');
        document.getElementById('hours').textContent = String(hours).padStart(2, '0');
        document.getElementById('minutes').textContent = String(minutes).padStart(2, '0');
        document.getElementById('seconds').textContent = String(seconds).padStart(2, '0');
        
        if (distance < 0) {
            clearInterval(timer);
            document.querySelector('h1').textContent = 'Launched!';
        }
    }
    
    updateCountdown();
    const timer = setInterval(updateCountdown, 1000);
});
```

## Example 4: Dark Mode Toggle

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Mode Toggle</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Dark Mode Toggle</h1>
        <p>Click the button below to switch between light and dark mode.</p>
        <button class="theme-toggle">🌙 Toggle Theme</button>
        <div class="content">
            <h2>Welcome!</h2>
            <p>This is a demonstration of a dark mode toggle feature.</p>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### CSS
```css
:root {
    --bg-color: #ffffff;
    --text-color: #333333;
    --card-bg: #f5f5f5;
    --button-bg: #667eea;
}

[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: #ffffff;
    --card-bg: #2a2a2a;
    --button-bg: #764ba2;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Arial', sans-serif;
    padding: 40px;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

h1 {
    margin-bottom: 20px;
}

.theme-toggle {
    background: var(--button-bg);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    cursor: pointer;
    font-size: 16px;
    margin: 20px 0;
    transition: opacity 0.3s ease;
}

.theme-toggle:hover {
    opacity: 0.9;
}

.content {
    background: var(--card-bg);
    padding: 30px;
    border-radius: 15px;
    margin-top: 30px;
    transition: background-color 0.3s ease;
}

.content h2 {
    margin-bottom: 15px;
}
```

### JavaScript
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.theme-toggle');
    const htmlElement = document.documentElement;
    
    // Check for saved theme preference or default to 'light'
    const currentTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-theme', currentTheme);
    updateButtonText(currentTheme);
    
    toggleButton.addEventListener('click', function() {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateButtonText(newTheme);
    });
    
    function updateButtonText(theme) {
        toggleButton.textContent = theme === 'light' ? '🌙 Toggle Dark' : '☀️ Toggle Light';
    }
});
```

## Tips for Using These Examples

1. **Copy Each Section**: Copy the HTML, CSS, and JavaScript into their respective tabs
2. **Click Generate Preview**: See the live result instantly
3. **Modify Values**: Change colors, sizes, and content to customize
4. **Experiment**: Try combining elements from different examples
5. **Use AI Assistant**: Ask the AI to modify or enhance these examples

## AI Prompts for Similar Designs

Try these prompts in the AI Assistant:

- "Create a card component similar to Example 1 but with a flip animation"
- "Make a navigation bar like Example 2 but add dropdown menus"
- "Build a countdown timer for a specific date with confetti animation"
- "Design a dark mode toggle with smooth transitions and icons"
