

function claimEarnPepe() {
  // Find the element with the text "Verified!"
  const verifiedBadgeFeyorra = document.evaluate(
    "//*[contains(text(), 'Verified!')]",
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;

  // Find the element with the text "Oops, wrong selection! Please refresh the page."
  const errorBadgeFeyorra = document.evaluate(
    "//*[contains(text(), 'Oops, wrong selection! Please refresh the page.')]",
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;

  const claimButtonEarn = document.querySelector("button#ClaimBtn");

  if (errorBadgeFeyorra) {
    console.log(" Error: Oops, wrong selection! Please refresh the page.");
    //window.location.reload(); // Refresh the page when the error is found
    return false; // Stop further execution
  }

  if (verifiedBadgeFeyorra && claimButtonEarn) {
    console.log(" Verified on claimEarnPepe.site - Clicking the Claim button...");
    claimButtonEarn.click();
    return true; // Stop the interval if the claim button is clicked
  }

  return false;
}

// Function to periodically check for the "Next Video" button every 1 second
function claimFeyorra() {
  // Find the element with the text "Verified!"
  const verifiedBadgeFeyorra = document.evaluate(
    "//*[contains(text(), 'Verified!')]",
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;

  // Find the element with the text "Oops, wrong selection! Please refresh the page."
  const errorBadgeFeyorra = document.evaluate(
    "//*[contains(text(), 'Oops, wrong selection! Please refresh the page.')]",
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;

  const claimButtonFeyorra = document.querySelector("button#ClaimBtn");

  if (errorBadgeFeyorra) {
    console.log(" Error: Oops, wrong selection! Please refresh the page.");
    //window.location.reload(); // Refresh the page when the error is found
    return false; // Stop further execution
  }

  if (verifiedBadgeFeyorra && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  }

  return false;
}

// Function to automatically close alerts
function handleAlerts() {
  if (window.confirm) {
    window.confirm = () => true; // Auto confirm all alerts
  }
  if (window.alert) {
    window.alert = () => {}; // Auto dismiss alerts
  }
  if (window.prompt) {
    window.prompt = () => null; // Auto dismiss prompts
  }
}

// Function to check for 404 and redirect to Google
function handle404Errors() {
  const pageTitle = document.title.toLowerCase();
  if (pageTitle.includes("404") || pageTitle.includes("not found")) {
    console.log("404 Error Detected - Redirecting to Google...");
    window.location.href = "https://feyorra.site/member/faucet";
  }
}

// Function to handle claims on Feyorra and Earn Pepe sites
function checkAndClaim() {
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors

  if (window.location.href.includes("feyorra.site")) {
    if (claimFeyorra()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-pepe.com")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-bonk.com")) {
    if (claimFeyorra()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-trump.com")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  }
}

// Run the check every 1 second for Feyorra and Earn Pepe claims
const claimInterval = setInterval(checkAndClaim, 1000);
