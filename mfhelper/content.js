// Function to get the current URL
function getCurrentURL() {
    return window.location.href;
}

// Function to check if we are on a restricted page
// Function to check if we are on a restricted page
function isOnRestrictedPage() {
    const restrictedUrls = [
        'https://www.skylom.com/prizes',
        'https://www.zaptaps.com/prizes',
        'https://www.skylom.com/waitfornextday',
        'https://www.zaptaps.com/waitfornextday'
    ];
    
    const currentURL = getCurrentURL();
    
    // Check if the current URL is exactly in the restricted URLs
    if (restrictedUrls.includes(currentURL)) {
        return true;
    }
    
    // Check if the current URL starts with the restricted path for checkinflow (zaptaps or popmack)
    if (currentURL.startsWith('https://www.zaptaps.com/checkinflow/') || 
        currentURL.startsWith('https://www.popmack.com/checkinflow/')) {
        return true;
    }

    return false;
}

// Function to check and click the "Next Video" button
function clickNextVideo() {
    if (isOnRestrictedPage()) {
        console.log("On a restricted page, skipping 'Next Video' click.");
        return false; // Skip clicking if on a restricted page
    }

    const selectors = [
        'a.retention-click.themeBtn.bluebtn#nextvideo',
        '#next-video',
        '#nextvideo',
        'a.retention-click.themeBtn',
        'a.themeBtn',
        'a.try_again'
    ];

    // Check if the captcha textarea exists
    if (document.querySelector('textarea.captcha-textarea')) {
        console.log("Captcha textarea found, skipping the 'Next Video' click.");
        return false; // Skip clicking if captcha textarea is present
    }

    // Loop through the selectors and try to find and click the button
    for (let selector of selectors) {
        const nextVideoButton = document.querySelector(selector);
        if (nextVideoButton) {
            nextVideoButton.click();
            console.log("Next Video button clicked: " + selector);
            return true; // Exit once a button is clicked
        }
    }


    console.log("Next Video button not found");
    return false;
}



// Function to periodically check for the "Next Video" button every 1 second
function startCheckingForNextVideo() {
    setInterval(() => {
        clickNextVideo();
    }, 1000); // Check every 1 second
}

// Start checking for "Next Video" button
startCheckingForNextVideo();
