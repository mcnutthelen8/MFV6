// Function to check and click the "Next Video" button
function clickNextVideo() {
    const selectors = [
        'a.retention-click.themeBtn.bluebtn#nextvideo',
        '#next-video',
        '#nextvideo',
        'a.retention-click.themeBtn',
        'a.themeBtn'
    ];

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
// Function to click the "False" button or "Try Again" button
function clickFalseButton() {
    try {
        let tryAgainButton = document.querySelector('a.try_again');
        if (tryAgainButton) {
            tryAgainButton.click();
            console.log("Clicked the 'a.try_again' button.");
            return true;
        } else {
            console.log("'a.try_again' button is not visible.");
        }

        let falseButton = document.querySelector('a.themeBtn.brdr-btn');
        if (falseButton) {
            falseButton.click();
            console.log("Clicked the 'False' button.");
            return true;
        } else {
            console.log("'False' button is not visible.");
            return false;
        }
    } catch (e) {
        console.log("Exception: False button is not visible. " + e);
        return false;
    }
}

// Function to handle and click the button with the smallest numeric value
function handleRandomNumberButtons() {
    try {
        let ulElement = document.querySelector("ul.link-btn-list.vid-category-options");
        if (ulElement) {
            console.log('Numeric verification found');
            
            // Find all 'a' tags (buttons) within the 'ul'
            let buttons = ulElement.querySelectorAll("a");

            let values = [];
            buttons.forEach(button => {
                let text = button.textContent.trim();
                if (!isNaN(text)) { // Check if the text is a digit
                    values.push(parseInt(text, 10));
                    console.log("Button value: " + text);
                }
            });

            if (values.length > 0) {
                // Find the smallest value
                let minValue = Math.min(...values);
                console.log("Smallest value: " + minValue);

                // Find the button with the smallest value and click it
                buttons.forEach(button => {
                    if (button.textContent.trim() === minValue.toString()) {
                        button.click();
                        console.log("Clicked the button with the smallest value.");
                        return true;
                    }
                });
            } else {
                console.log("No numeric values found.");
                return false;
            }
        } else {
            console.log("Numeric verification element is not visible.");
            return false;
        }
    } catch (e) {
        console.log("Exception: " + e);
        return false;
    }
}

// Function to periodically check for the "False" or "Try Again" button every 2 seconds
function startCheckingForFalseButton() {
    setInterval(() => {
        clickFalseButton();
    }, 1000); // Check every 2 seconds (2000 ms)
}

// Function to periodically check for random number buttons and click the smallest value every 2 seconds
function startCheckingForRandomNumberButtons() {
    setInterval(() => {
        handleRandomNumberButtons();
    }, 1000); // Check every 2 seconds (2000 ms)
}
function startCheckingForNextVideo() {
    setInterval(() => {
        clickNextVideo();
    }, 1000); // Check every 2 seconds (2000 ms)
}
// Start checking for "False" button or "Try Again" button
startCheckingForFalseButton();
// Start checking for random number buttons and click the smallest value
startCheckingForRandomNumberButtons();
startCheckingForNextVideo();