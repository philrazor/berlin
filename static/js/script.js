function filterModels() {
    const brandSelect = document.getElementById("brand");
    const modelSelect = document.getElementById("model");
    const selectedBrandId = brandSelect.value;

    modelSelect.disabled = !selectedBrandId;
    
    for (const option of modelSelect.options) {
        option.style.display = option.dataset.brand === selectedBrandId ? 'block' : 'none';
    }
    modelSelect.value = "";  // Reset the model selection
}




const texts = document.querySelectorAll('.text-content');
console.log(texts)
const searchSection = document.querySelector('.search-section');

// Array of images
const backgrounds = [
        '{% static "images/mercedes.jpg" %}', // Background image for the first text
        '{% static "images/mustang.jpg" %}',   // Background image for the second text
        '{% static "images/mercedes-blink.jpg" %}'    // Background image for the third text
];

let index = 0;

function showNextText() {
        texts[index].classList.remove('active');
        index = (index + 1) % texts.length; // Move to the next index
        texts[index].classList.add('active'); // Show next text
        searchSection.style.backgroundImage = `url(${backgrounds[index]})`; // Change background image
    }

// Show the first text immediately
texts[index].classList.add('active');
searchSection.style.backgroundImage = `url(${backgrounds[index]})`; // Set initial background

// Change text and background every 4 seconds
setInterval(showNextText, 4000);

