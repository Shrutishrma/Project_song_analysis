// Define a variable to keep track of the current state
var currentState = 'main';

document.getElementById('getStartedBtn').addEventListener('click', function () {
    console.log('Get Started button clicked');
    fadeOutAndHide('main-content', function () {
        fadeIn('new-content');
        // Update the current state
        currentState = 'new';
    });
});

document.getElementById('goBackBtn').addEventListener('click', function () {
    console.log('Go Back button clicked');
    if (currentState === 'new') {
        fadeOutAndHide('new-content', function () {
            fadeIn('main-content');
            // Update the current state
            currentState = 'main';
        });
    }
});

document.getElementById('nextBtn').addEventListener('click', function () {
    console.log('Next button clicked');
    // Replace the following URL with the actual path to the new HTML file
    window.location.href = '/recommend/';
});

document.getElementById('goBackFromNewPageBtn').addEventListener('click', function () {
    console.log('Go Back from New Page button clicked');
    // Check if the user is on the first page
    if (document.referrer.includes('home.html')) {
        // Navigate back to index.html
        history.back();
    } else {
        // If the user is on a different page or the first page, navigate to index.html
        window.location.href = 'home.html';
    }
});


function fadeOutAndHide(elementId, callback) {
    var element = document.getElementById(elementId);
    element.style.transition = 'opacity 0.5s ease-in-out';
    element.style.opacity = 0;

    setTimeout(function () {
        element.style.display = 'none';
        element.style.transition = '';
        if (callback) callback();
    }, 500);
}

function fadeIn(elementId) {
    var element = document.getElementById(elementId);
    element.style.transition = 'opacity 0.5s ease-in-out';
    element.style.display = 'flex';
    element.style.flexDirection = 'column';

    setTimeout(function () {
        element.style.opacity = 1;
        element.style.transition = '';
    }, 10);
}