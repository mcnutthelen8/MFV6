
async function validate_ipaddress() {
  const validURLs = ["https://feyorra.site/", "https://earn-pepe.com/", "https://claimcoin.in/faucet"];
  const currentURL = window.location.href;

  // Check if the current URL matches the target pattern
  const isTargetSite = validURLs.some((url) => currentURL.startsWith(url));

  if (!isTargetSite) {
      console.log("This script only runs on the target sites.");
      return;
  }

  try {
      // Fetch the target IP from the JSON file
      const configResponse = await fetch(chrome.runtime.getURL("config.json"));
      const config = await configResponse.json();
      const targetIP = config.targetIP;

      // Stop the page from loading temporarily
      console.log(targetIP);

      // Fetch the current IP address before the page fully loads
      const response = await fetch("https://api.ipify.org?format=json");
      const data = await response.json();
      const currentIP = data.ip;

      // Log the current IP to the console
      console.log(`Current IP: ${currentIP}`);

      // Store IP check result in sessionStorage
      sessionStorage.setItem(currentIP, true);

      // Redirect to Google if IP does not match
      if (currentIP !== targetIP) {
          console.log("IP mismatch detected. Redirecting to Google.");
          window.location.href = "https://www.google.com";
      } else {
          console.log("IP matches the target");
          return currentIP;
          // Allow the page to reload after IP validation
          //window.location.reload();
      }
  } catch (error) {
      console.error("Failed to fetch IP address or validate:", error);
      // If there's an error, handle it gracefully and redirect to Google
      //window.location.href = "https://www.google.com";
  }
}


// Function to get the current URL
function getCurrentURL() {
  return window.location.href;
}

// Function to check if we are on a restricted page
function isOnRestrictedPage() {
  const restrictedUrls = [
    'https://www.popmack.com/prizes',
    'https://www.baymack.com/prizes',
    'https://www.popmack.com/waitfornextday',
    'https://www.baymack.com/waitfornextday'
  ];
  
  const currentURL = getCurrentURL();
  
  // Check if the current URL is exactly in the restricted URLs
  if (restrictedUrls.includes(currentURL)) {
    return true;
  }
  
  // Check if the current URL starts with the restricted path for checkinflow (baymack or popmack)
  if (currentURL.startsWith('https://www.baymack.com/checkinflow/') || 
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

// Function to handle Feyorra claims
function claimFeyorra() {
  const verifiedBadgeFeyorra = document.querySelector("div.mb-2.badge.bg-success");
  const successcloudfl = document.querySelector("span#success-text");
  const claimButtonFeyorra = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeFeyorra && claimButtonFeyorra || successcloudfl && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  }
  else if (successcloudfl && claimButtonFeyorra) {
    console.log(" Verified on feyorra.site - Clicking the Claim button...");
    claimButtonFeyorra.click();
    return true; // Stop the interval if the claim button is clicked
  } else {
    
  }
  return false;
}

// Function to handle Earn Pepe claims
function claimEarnPepe() {
  const verifiedBadgeEarnPepe = document.querySelector("div.mb-16.badge.hp-text-color-black-100.hp-bg-success-3");
  const claimButtonEarnPepe = document.querySelector("button#ClaimBtn");

  if (verifiedBadgeEarnPepe && claimButtonEarnPepe) {
    console.log(" Verified on earn-pepe.com - Clicking the Claim button...");
    claimButtonEarnPepe.click();
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
function createNotification(message) {
  const notification = document.createElement('div');
  notification.id = 'captcha-solver-notification';
  notification.style.cssText = `
      position: fixed;
      top: 10px;
      left: 10px;
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 15px;
      border-radius: 8px;
      z-index: 9999;
      font-family: sans-serif;
      box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
      display: flex;
      align-items: center;
  `;

  const messageSpan = document.createElement('span');
  messageSpan.textContent = message;
  notification.appendChild(messageSpan);

  const closeButton = document.createElement('button');
  closeButton.textContent = '×';
  closeButton.style.cssText = `
      margin-left: 10px;
      background: transparent;
      border: none;
      color: white;
      font-size: 1.2em;
      cursor: pointer;
  `;
  closeButton.addEventListener('click', () => notification.remove());
  notification.appendChild(closeButton);

  document.body.appendChild(notification);

  setTimeout(() => {
      if (notification.parentNode) notification.remove();
  }, 1000);
}

async function getCoins() {
  let coins = null;

  try {
      // Determine sitekey based on page URL
      const url = window.location.href;

      let sitekey = null;
      if (url.includes("earn-pepe.com")) {
          sitekey = 1;
      } else if (url.includes("feyorra.site")) {
          sitekey = 2;
      } else if (url.includes("claimcoin.in")) {
          sitekey = 3;
      } else {
          console.log("Unsupported site.");
          return false;
      }

      // Process based on sitekey
      if (sitekey === 1) {
          let selectElement = document.querySelector('small span span');
          if (selectElement) {
              coins = selectElement.textContent.trim();
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      if (sitekey === 2) {
          let selectElement = document.querySelector('select.form-select option[selected]');
          if (selectElement) {
              let selectedText = selectElement.textContent.trim();
              console.log(`Selected option text: ${selectedText}`);
              coins = selectedText;
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      if (sitekey === 3) {
          let element = document.querySelector('div.col-md-6.col-xl-3:nth-child(4) p.lh-1.mb-1.font-weight-bold');
          if (element) {
              coins = element.textContent.trim();
          } else {
              console.log(`Sitekey:${sitekey} not found`);
          }
      }

      console.log(`SiteKey${sitekey}: ${coins}`);

      // Handle specific processing for sitekey 3
      if (sitekey === 3 && coins && coins.includes('/')) {
          let numerator = coins.split('/')[0];
          return numerator;
      }

      // Extract numeric value
      let numericValue = coins && coins.match(/\d+\.\d+/);
      if (numericValue) {
          console.log(`SiteKey${sitekey}: ${coins}`);
          return parseFloat(numericValue[0]);
      }

      return false;
  } catch (error) {
      console.error(`ERR on GetCoins | ${error.message}`);
  }

  return false;
}
const iconPathList = {
  "heart": "M473.7 73.8l-2.4-2.5c-46-47-118-51.7-169.6-14.8L336 159.9l-96 64 48 128-144-144 96-64-28.6-86.5C159.7 19.6 87 24 40.7 71.4l-2.4 2.4C-10.4 123.6-12.5 202.9 31 256l212.1 218.6c7.1 7.3 18.6 7.3 25.7 0L481 255.9c43.5-53 41.4-132.3-7.3-182.1z",
  "coin": "M12.0049 4.00281C18.08 4.00281 23.0049 6.6891 23.0049 10.0028V14.0028C23.0049 17.3165 18.08 20.0028 12.0049 20.0028C6.03824 20.0028 1.18114 17.4116 1.00957 14.1797L1.00488 14.0028V10.0028C1.00488 6.6891 5.92975 4.00281 12.0049 4.00281ZM12.0049 16.0028C8.28443 16.0028 4.99537 14.9953 3.00466 13.4533L3.00488 14.0028C3.00488 15.885 6.88751 18.0028 12.0049 18.0028C17.0156 18.0028 20.8426 15.9723 20.9999 14.1207L21.0049 14.0028L21.0061 13.4525C19.0155 14.995 15.726 16.0028 12.0049 16.0028ZM12.0049 6.00281C6.88751 6.00281 3.00488 8.12061 3.00488 10.0028C3.00488 11.885 6.88751 14.0028 12.0049 14.0028C17.1223 14.0028 21.0049 11.885 21.0049 10.0028C21.0049 8.12061 17.1223 6.00281 12.0049 6.00281Z",
  "volume": "M215 71.1L126.1 160H24c-13.3 0-24 10.7-24 24v144c0 13.3 10.7 24 24 24h102.1l89 89c15 15 41 4.5 41-17V88c0-21.5-26-32-41-17zm233.3-51.1c-11.2-7.3-26.2-4.2-33.5 7-7.3 11.2-4.2 26.2 7 33.5 66.3 43.5 105.8 116.6 105.8 195.6 0 79-39.6 152.1-105.8 195.6-11.2 7.3-14.3 22.3-7 33.5 7 10.7 21.9 14.6 33.5 7C528.3 439.6 576 351.3 576 256S528.3 72.4 448.4 20zM480 256c0-63.5-32.1-121.9-85.8-156.2-11.2-7.1-26-3.8-33.1 7.5s-3.8 26.2 7.4 33.4C408.3 166 432 209.1 432 256s-23.7 90-63.5 115.4c-11.2 7.1-14.5 22.1-7.4 33.4 6.5 10.4 21.1 15.1 33.1 7.5C447.9 377.9 480 319.5 480 256zm-141.8-76.9c-11.6-6.3-26.2-2.2-32.6 9.5-6.4 11.6-2.2 26.2 9.5 32.6C328 228.3 336 241.6 336 256c0 14.4-8 27.7-20.9 34.8-11.6 6.4-15.8 21-9.5 32.6 6.4 11.7 21.1 15.8 32.6 9.5 28.2-15.6 45.8-45 45.8-76.9s-17.5-61.3-45.8-76.9z",
  "android": "M420.6 301.9a24 24 0 1 1 24-24 24 24 0 0 1 -24 24m-265.1 0a24 24 0 1 1 24-24 24 24 0 0 1 -24 24m273.7-144.5 47.9-83a10 10 0 1 0 -17.3-10h0l-48.5 84.1a301.3 301.3 0 0 0 -246.6 0L116.2 64.5a10 10 0 1 0 -17.3 10h0l47.9 83C64.5 202.2 8.2 285.6 0 384H576c-8.2-98.5-64.5-181.8-146.9-226.6",
  "chrome":"M16 8a8 8 0 0 1-7.022 7.94l1.902-7.098a3 3 0 0 0 .05-1.492A3 3 0 0 0 10.237 6h5.511A8 8 0 0 1 16 8M0 8a8 8 0 0 0 7.927 8l1.426-5.321a3 3 0 0 1-.723.255 3 3 0 0 1-1.743-.147 3 3 0 0 1-1.043-.7L.633 4.876A8 8 0 0 0 0 8m5.004-.167L1.108 3.936A8.003 8.003 0 0 1 15.418 5H8.066a3 3 0 0 0-1.252.243 2.99 2.99 0 0 0-1.81 2.59M8 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4",
  "mouse":"M15.3873 13.4975L17.9403 20.5117L13.2418 22.2218L10.6889 15.2076L6.79004 17.6529L8.4086 1.63318L19.9457 12.8646L15.3873 13.4975ZM15.3768 19.3163L12.6618 11.8568L15.6212 11.4459L9.98201 5.9561L9.19088 13.7863L11.7221 12.1988L14.4371 19.6583L15.3768 19.3163Z",
  "cursor":"M15.3873 13.4975L17.9403 20.5117L13.2418 22.2218L10.6889 15.2076L6.79004 17.6529L8.4086 1.63318L19.9457 12.8646L15.3873 13.4975ZM15.3768 19.3163L12.6618 11.8568L15.6212 11.4459L9.98201 5.9561L9.19088 13.7863L11.7221 12.1988L14.4371 19.6583L15.3768 19.3163Z",
  "truck":"M624 224h-16v-64c0-17.7-14.3-32-32-32h-73.6L419.2 24A64 64 0 0 0 369.2 0H256c-17.7 0-32 14.3-32 32v96H48c-8.8 0-16 7.2-16 16v80H16c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h16.7c29.2-38.7 75.1-64 127.3-64s98.1 25.4 127.3 64h65.5c29.2-38.7 75.1-64 127.3-64s98.1 25.4 127.3 64H624c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-336-96V64h81.2l51.2 64H288zm304 224h-5.2c-2.2-7.3-5.1-14.3-8.7-20.9l3.7-3.7c6.3-6.3 6.3-16.4 0-22.6l-22.6-22.6c-6.3-6.3-16.4-6.3-22.6 0l-3.7 3.7A110.9 110.9 0 0 0 512 277.2V272c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v5.2c-7.3 2.2-14.3 5.1-20.9 8.7l-3.7-3.7c-6.3-6.3-16.4-6.3-22.6 0l-22.6 22.6c-6.3 6.3-6.3 16.4 0 22.6l3.7 3.7A110.9 110.9 0 0 0 373.2 352H368c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h5.2c2.2 7.3 5.1 14.3 8.7 20.9l-3.7 3.7c-6.3 6.3-6.3 16.4 0 22.6l22.6 22.6c6.3 6.3 16.4 6.3 22.6 0l3.7-3.7c6.6 3.6 13.6 6.5 20.9 8.7v5.2c0 8.8 7.2 16 16 16h32c8.8 0 16-7.2 16-16v-5.2c7.3-2.2 14.3-5.1 20.9-8.7l3.7 3.7c6.3 6.3 16.4 6.3 22.6 0l22.6-22.6c6.3-6.3 6.3-16.4 0-22.6l-3.7-3.7a110.9 110.9 0 0 0 8.7-20.9h5.2c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-112 80c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm-208-80h-5.2c-2.2-7.3-5.1-14.3-8.7-20.9l3.7-3.7c6.3-6.3 6.3-16.4 0-22.6l-22.6-22.6c-6.3-6.3-16.4-6.3-22.6 0l-3.7 3.7A110.9 110.9 0 0 0 192 277.2V272c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v5.2c-7.3 2.2-14.3 5.1-20.9 8.7l-3.7-3.7c-6.3-6.3-16.4-6.3-22.6 0L58.2 304.8c-6.3 6.3-6.3 16.4 0 22.6l3.7 3.7a110.9 110.9 0 0 0 -8.7 20.9H48c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h5.2c2.2 7.3 5.1 14.3 8.7 20.9l-3.7 3.7c-6.3 6.3-6.3 16.4 0 22.6l22.6 22.6c6.3 6.3 16.4 6.3 22.6 0l3.7-3.7c6.6 3.6 13.6 6.5 20.9 8.7v5.2c0 8.8 7.2 16 16 16h32c8.8 0 16-7.2 16-16v-5.2c7.3-2.2 14.3-5.1 20.9-8.7l3.7 3.7c6.3 6.3 16.4 6.3 22.6 0l22.6-22.6c6.3-6.3 6.3-16.4 0-22.6l-3.7-3.7a110.9 110.9 0 0 0 8.7-20.9h5.2c8.8 0 16-7.2 16-16v-32C288 359.2 280.8 352 272 352zm-112 80c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48z",
  "rocket":"M4 13a8 8 0 0 1 7 7a6 6 0 0 0 3 -5a9 9 0 0 0 6 -8a3 3 0 0 0 -3 -3a9 9 0 0 0 -8 6a6 6 0 0 0 -5 3",
  "apple":"M15.778 8.20793C15.3053 8.1711 14.7974 8.28434 14.0197 8.58067C14.085 8.55577 13.2775 8.87173 13.0511 8.95077C12.5494 9.12593 12.1364 9.22198 11.6734 9.22198C11.2151 9.22198 10.7925 9.13042 10.3078 8.96683C10.1524 8.91441 9.99616 8.8564 9.80283 8.7809C9.71993 8.74852 9.41997 8.62947 9.3544 8.60379C8.70626 8.34996 8.34154 8.25434 8.03885 8.26181C6.88626 8.2765 5.79557 8.9421 5.16246 10.0442C3.87037 12.2875 4.58583 16.3428 6.47459 19.075C7.4802 20.5189 8.03062 21.035 8.25199 21.0279C8.4743 21.0183 8.63777 20.9713 9.03567 20.8026C9.11485 20.7689 9.11485 20.7689 9.202 20.7317C10.2077 20.3032 10.9118 20.114 11.9734 20.114C12.9944 20.114 13.6763 20.2997 14.6416 20.7159C14.7302 20.7542 14.7302 20.7542 14.8097 20.7884C15.2074 20.9588 15.3509 20.9962 15.6016 20.9902C15.9591 20.9846 16.4003 20.5726 17.3791 19.1362C17.6471 18.7447 17.884 18.3333 18.0895 17.9168C17.9573 17.8077 17.826 17.6917 17.6975 17.5693C16.4086 16.3408 15.6114 14.6845 15.5895 12.6391C15.5756 11.0186 16.1057 9.61487 16.999 8.45797C16.6293 8.3142 16.2216 8.23805 15.778 8.20793ZM15.9334 6.21398C16.6414 6.26198 18.6694 6.47798 19.9894 8.40998C19.8814 8.46998 17.5654 9.81397 17.5894 12.622C17.6254 15.982 20.5294 17.098 20.5654 17.11C20.5414 17.194 20.0974 18.706 19.0294 20.266C18.1054 21.622 17.1454 22.966 15.6334 22.99C14.1454 23.026 13.6654 22.114 11.9734 22.114C10.2694 22.114 9.74138 22.966 8.33738 23.026C6.87338 23.074 5.76938 21.562 4.83338 20.218C2.92538 17.458 1.47338 12.442 3.42938 9.04597C4.40138 7.35397 6.12938 6.28598 8.01338 6.26198C9.44138 6.22598 10.7974 7.22198 11.6734 7.22198C12.5374 7.22198 14.0854 6.06998 15.9334 6.21398ZM14.7934 4.38998C14.0134 5.32598 12.7414 6.05798 11.5054 5.96198C11.3374 4.68998 11.9614 3.35798 12.6814 2.52998C13.4854 1.59398 14.8294 0.897976 15.9454 0.849976C16.0894 2.14598 15.5734 3.45398 14.7934 4.38998Z",
  "thumb":"M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3",
  "bank":"M2 20H22V22H2V20ZM4 12H6V19H4V12ZM9 12H11V19H9V12ZM13 12H15V19H13V12ZM18 12H20V19H18V12ZM2 7L12 2L22 7V11H2V7ZM12 8C12.5523 8 13 7.55228 13 7C13 6.44772 12.5523 6 12 6C11.4477 6 11 6.44772 11 7C11 7.55228 11.4477 8 12 8Z",
  "database": "M12.0049 4.00281C18.08 4.00281 23.0049 6.6891 23.0049 10.0028V14.0028C23.0049 17.3165 18.08 20.0028 12.0049 20.0028C6.03824 20.0028 1.18114 17.4116 1.00957 14.1797L1.00488 14.0028V10.0028C1.00488 6.6891 5.92975 4.00281 12.0049 4.00281ZM12.0049 16.0028C8.28443 16.0028 4.99537 14.9953 3.00466 13.4533L3.00488 14.0028C3.00488 15.885 6.88751 18.0028 12.0049 18.0028C17.0156 18.0028 20.8426 15.9723 20.9999 14.1207L21.0049 14.0028L21.0061 13.4525C19.0155 14.995 15.726 16.0028 12.0049 16.0028ZM12.0049 6.00281C6.88751 6.00281 3.00488 8.12061 3.00488 10.0028C3.00488 11.885 6.88751 14.0028 12.0049 14.0028C17.1223 14.0028 21.0049 11.885 21.0049 10.0028C21.0049 8.12061 17.1223 6.00281 12.0049 6.00281Z",
  "music":"M470.4 1.5L150.4 96A32 32 0 0 0 128 126.5v261.4A139 139 0 0 0 96 384c-53 0-96 28.7-96 64s43 64 96 64 96-28.7 96-64V214.3l256-75v184.6a138.4 138.4 0 0 0 -32-3.9c-53 0-96 28.7-96 64s43 64 96 64 96-28.7 96-64V32a32 32 0 0 0 -41.6-30.5z",
  "award":"M97.1 362.6c-8.7-8.7-4.2-6.2-25.1-11.9-9.5-2.6-17.9-7.5-25.4-13.3L1.2 448.7c-4.4 10.8 3.8 22.5 15.4 22l52.7-2L105.6 507c8 8.4 22 5.8 26.4-5l52.1-127.6c-10.8 6-22.9 9.6-35.3 9.6-19.5 0-37.8-7.6-51.6-21.4zM382.8 448.7l-45.4-111.2c-7.6 5.9-15.9 10.8-25.4 13.3-21.1 5.6-16.5 3.2-25.1 11.9-13.8 13.8-32.1 21.4-51.6 21.4-12.4 0-24.5-3.6-35.3-9.6L252 502c4.4 10.8 18.4 13.4 26.4 5l36.3-38.3 52.7 2c11.6 .4 19.8-11.3 15.4-22zM263 340c15.3-15.6 17-14.2 38.8-20.1 13.9-3.8 24.8-14.8 28.5-29 7.5-28.4 5.5-25 26-45.8 10.2-10.4 14.1-25.4 10.4-39.6-7.5-28.4-7.5-24.4 0-52.8 3.7-14.1-.3-29.2-10.4-39.6-20.4-20.8-18.5-17.4-26-45.8-3.7-14.1-14.6-25.2-28.5-29-27.9-7.6-24.5-5.6-45-26.4-10.2-10.4-25-14.4-38.9-10.6-27.9 7.6-24 7.6-51.9 0-13.9-3.8-28.7 .3-38.9 10.6-20.4 20.8-17.1 18.8-44.9 26.4-13.9 3.8-24.8 14.8-28.5 29-7.5 28.4-5.5 25-26 45.8-10.2 10.4-14.2 25.4-10.4 39.6 7.5 28.4 7.5 24.4 0 52.8-3.7 14.1 .3 29.2 10.4 39.6 20.4 20.8 18.5 17.4 26 45.8 3.7 14.1 14.6 25.2 28.5 29C104.6 326 106.3 325 121 340c13.2 13.5 33.8 15.9 49.7 5.8a39.7 39.7 0 0 1 42.5 0c15.9 10.1 36.5 7.7 49.7-5.8zM97.7 176c0-53 42.2-96 94.3-96s94.3 43 94.3 96-42.2 96-94.3 96-94.3-43-94.3-96z",
  "house":"M5.793 1a1 1 0 0 1 1.414 0l.647.646a.5.5 0 1 1-.708.708L6.5 1.707 2 6.207V12.5a.5.5 0 0 0 .5.5.5.5 0 0 1 0 1A1.5 1.5 0 0 1 1 12.5V7.207l-.146.147a.5.5 0 0 1-.708-.708zm3 1a1 1 0 0 1 1.414 0L12 3.793V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v3.293l1.854 1.853a.5.5 0 0 1-.708.708L15 8.207V13.5a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 4 13.5V8.207l-.146.147a.5.5 0 1 1-.708-.708zm.707.707L5 7.207V13.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5V7.207z",
  "emo":"M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm33.8 161.7l80-48c11.6-6.9 24 7.7 15.4 18L343.6 180l33.6 40.3c8.7 10.4-3.9 24.8-15.4 18l-80-48c-7.7-4.7-7.7-15.9 0-20.6zm-163-30c-8.6-10.3 3.8-24.9 15.4-18l80 48c7.8 4.7 7.8 15.9 0 20.6l-80 48c-11.5 6.8-24-7.6-15.4-18l33.6-40.3-33.6-40.3zM398.9 306C390 377 329.4 432 256 432h-16c-73.4 0-134-55-142.9-126-1.2-9.5 6.3-18 15.9-18h270c9.6 0 17.1 8.4 15.9 18z",
  "blue":"m8.543 3.948 1.316 1.316L8.543 6.58zm0 8.104 1.316-1.316L8.543 9.42zm-1.41-4.043L4.275 5.133l.827-.827L7.377 6.58V1.128l4.137 4.136L8.787 8.01l2.745 2.745-4.136 4.137V9.42l-2.294 2.274-.827-.827zM7.903 16c3.498 0 5.904-1.655 5.904-8.01 0-6.335-2.406-7.99-5.903-7.99S2 1.655 2 8.01C2 14.344 4.407 16 7.904 16Z",
  "file":"M6 7V4C6 3.44772 6.44772 3 7 3H13.4142L15.4142 5H21C21.5523 5 22 5.44772 22 6V16C22 16.5523 21.5523 17 21 17H18V20C18 20.5523 17.5523 21 17 21H3C2.44772 21 2 20.5523 2 20V8C2 7.44772 2.44772 7 3 7H6ZM6 9H4V19H16V17H6V9ZM8 5V15H20V7H14.5858L12.5858 5H8Z",
  "build":"M5.793 1a1 1 0 0 1 1.414 0l.647.646a.5.5 0 1 1-.708.708L6.5 1.707 2 6.207V12.5a.5.5 0 0 0 .5.5.5.5 0 0 1 0 1A1.5 1.5 0 0 1 1 12.5V7.207l-.146.147a.5.5 0 0 1-.708-.708zm3 1a1 1 0 0 1 1.414 0L12 3.793V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v3.293l1.854 1.853a.5.5 0 0 1-.708.708L15 8.207V13.5a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 4 13.5V8.207l-.146.147a.5.5 0 1 1-.708-.708zm.707.707L5 7.207V13.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5V7.207z",
  "gift":"M3 8m0 1a1 1 0 0 1 1 -1h16a1 1 0 0 1 1 1v2a1 1 0 0 1 -1 1h-16a1 1 0 0 1 -1 -1z",
  "bluetooth":"m8.543 3.948 1.316 1.316L8.543 6.58zm0 8.104 1.316-1.316L8.543 9.42zm-1.41-4.043L4.275 5.133l.827-.827L7.377 6.58V1.128l4.137 4.136L8.787 8.01l2.745 2.745-4.136 4.137V9.42l-2.294 2.274-.827-.827zM7.903 16c3.498 0 5.904-1.655 5.904-8.01 0-6.335-2.406-7.99-5.903-7.99S2 1.655 2 8.01C2 14.344 4.407 16 7.904 16Z",
  "display":"M8 1a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1zm1 13.5a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0m2 0a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0M9.5 1a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM9 3.5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 0-1h-5a.5.5 0 0 0-.5.5M1.5 2A1.5 1.5 0 0 0 0 3.5v7A1.5 1.5 0 0 0 1.5 12H6v2h-.5a.5.5 0 0 0 0 1H7v-4H1.5a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .5-.5H7V2z",
  "pc":"M8 1a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1zm1 13.5a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0m2 0a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0M9.5 1a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM9 3.5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 0-1h-5a.5.5 0 0 0-.5.5M1.5 2A1.5 1.5 0 0 0 0 3.5v7A1.5 1.5 0 0 0 1.5 12H6v2h-.5a.5.5 0 0 0 0 1H7v-4H1.5a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .5-.5H7V2z",
  "university":"M2 20H22V22H2V20ZM4 12H6V19H4V12ZM9 12H11V19H9V12ZM13 12H15V19H13V12ZM18 12H20V19H18V12ZM2 7L12 2L22 7V11H2V7ZM12 8C12.5523 8 13 7.55228 13 7C13 6.44772 12.5523 6 12 6C11.4477 6 11 6.44772 11 7C11 7.55228 11.4477 8 12 8Z",
  "laptop":"M8 1a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1zm1 13.5a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0m2 0a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0M9.5 1a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM9 3.5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 0-1h-5a.5.5 0 0 0-.5.5M1.5 2A1.5 1.5 0 0 0 0 3.5v7A1.5 1.5 0 0 0 1.5 12H6v2h-.5a.5.5 0 0 0 0 1H7v-4H1.5a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .5-.5H7V2z",
  "folder":"M6 7V4C6 3.44772 6.44772 3 7 3H13.4142L15.4142 5H21C21.5523 5 22 5.44772 22 6V16C22 16.5523 21.5523 17 21 17H18V20C18 20.5523 17.5523 21 17 21H3C2.44772 21 2 20.5523 2 20V8C2 7.44772 2.44772 7 3 7H6ZM6 9H4V19H16V17H6V9ZM8 5V15H20V7H14.5858L12.5858 5H8Z",
  "space":"M4 13a8 8 0 0 1 7 7a6 6 0 0 0 3 -5a9 9 0 0 0 6 -8a3 3 0 0 0 -3 -3a9 9 0 0 0 -8 6a6 6 0 0 0 -5 3",
  "device":"M8 1a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1zm1 13.5a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0m2 0a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0M9.5 1a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM9 3.5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 0-1h-5a.5.5 0 0 0-.5.5M1.5 2A1.5 1.5 0 0 0 0 3.5v7A1.5 1.5 0 0 0 1.5 12H6v2h-.5a.5.5 0 0 0 0 1H7v-4H1.5a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .5-.5H7V2z",
  "mood":"M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm33.8 161.7l80-48c11.6-6.9 24 7.7 15.4 18L343.6 180l33.6 40.3c8.7 10.4-3.9 24.8-15.4 18l-80-48c-7.7-4.7-7.7-15.9 0-20.6zm-163-30c-8.6-10.3 3.8-24.9 15.4-18l80 48c7.8 4.7 7.8 15.9 0 20.6l-80 48c-11.5 6.8-24-7.6-15.4-18l33.6-40.3-33.6-40.3zM398.9 306C390 377 329.4 432 256 432h-16c-73.4 0-134-55-142.9-126-1.2-9.5 6.3-18 15.9-18h270c9.6 0 17.1 8.4 15.9 18z",
  "point":"M15.3873 13.4975L17.9403 20.5117L13.2418 22.2218L10.6889 15.2076L6.79004 17.6529L8.4086 1.63318L19.9457 12.8646L15.3873 13.4975ZM15.3768 19.3163L12.6618 11.8568L15.6212 11.4459L9.98201 5.9561L9.19088 13.7863L11.7221 12.1988L14.4371 19.6583L15.3768 19.3163Z",
  "home":"M5.793 1a1 1 0 0 1 1.414 0l.647.646a.5.5 0 1 1-.708.708L6.5 1.707 2 6.207V12.5a.5.5 0 0 0 .5.5.5.5 0 0 1 0 1A1.5 1.5 0 0 1 1 12.5V7.207l-.146.147a.5.5 0 0 1-.708-.708zm3 1a1 1 0 0 1 1.414 0L12 3.793V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v3.293l1.854 1.853a.5.5 0 0 1-.708.708L15 8.207V13.5a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 4 13.5V8.207l-.146.147a.5.5 0 1 1-.708-.708zm.707.707L5 7.207V13.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5V7.207z",

};
async function solveIconCaptcha() {
  try {
      const url = window.location.href;
      let sitekey = null;

      // Validate IP address
      const ipAddress = await validate_ipaddress();
      console.log("Extracted IP Address:", ipAddress);

      // Determine sitekey based on URL
      if (url.includes("earn-pepe.com")) {
          sitekey = 1;
      } else if (url.includes("feyorra.site")) {
          sitekey = 2;
      } else if (url.includes("claimcoin.in")) {
          sitekey = 3;
      } else {
          console.log("Unsupported site.");
          return false;
      }

      // Get coin value
      const coins = await getCoins();
      console.log("Extracted Coins:", coins);

      // Handle sitekey 3 (no captcha case)
      if (sitekey === 3) {
          console.log("No captcha icons found on this page.");
          const clipboardText = `${coins} and is is ${ipAddress}`;
          console.log("Clipboard Text:", clipboardText);

          // Copy to clipboard
          try {
              await navigator.clipboard.writeText(clipboardText);
              console.log("Text copied to clipboard:", clipboardText);
              createNotification(`Text copied: ${clipboardText}`);
          } catch (err) {
              console.error("Failed to copy text to clipboard:", err);
          }

          return true;
      }

      // Handle captcha-solving process
      console.log("Starting captcha solving process...");

      // Find potential captcha icons
      const captchaIcons = document.querySelectorAll('[class*="fa-"],[class*="fas fa-"],[class*="far fa-"], [class*="ri-"], [class*="ti ti-"], [class*="bi bi-"]');
      console.log(`Found ${captchaIcons.length} potential captcha icons.`);

      // Filter valid captcha icons
      const validCaptchaIcons = Array.from(captchaIcons).filter(icon => {
          return !icon.hasAttribute("style") && !icon.hasAttribute("id") && icon.tagName.toLowerCase() !== "i";
      });
      console.log("Valid captcha icons:", validCaptchaIcons.map(icon => icon.outerHTML));

      // Find SVG elements
      const svgElements = Array.from(document.querySelectorAll("svg"));
      console.log(`Found ${svgElements.length} SVG elements to check.`);

      let answerFound = false;

      // Process each SVG element
      for (const svg of svgElements) {
          const pathElement = svg.querySelector("path");
          if (pathElement && pathElement.hasAttribute("d")) {
              const pathData = pathElement.getAttribute("d");

              // Compare pathData with the iconPathList dictionary
              for (const [iconName, iconPath] of Object.entries(iconPathList)) {
                  if (pathData === iconPath) {
                      const rect = svg.getBoundingClientRect();
                      const x = rect.left + window.scrollX;
                      const y = rect.top + window.scrollY;

                      // Match icon class name
                      for (const validIcon of validCaptchaIcons) {
                          if (validIcon.className.includes(iconName)) {
                              answerFound = true;
                              console.log(`Answer found for icon: ${iconName}`);
                              console.log(`Coordinates: X=${x}, Y=${y}`);

                              //const clipboardText = `${coins}, X=${x}, Y=${y}, IP=${ipAddress}`;
                              const clipboardText = `${coins} and x is ${x} and ip is ${ipAddress}`;
                              console.log("Clipboard Text:", clipboardText);

                              // Copy to clipboard
                              try {
                                  await navigator.clipboard.writeText(clipboardText);
                                  console.log("Text copied to clipboard:", clipboardText);
                                  createNotification(`Text copied: ${clipboardText}`);
                              } catch (err) {
                                  console.error("Failed to copy text to clipboard:", err);
                              }

                              return true; // Exit function after finding an answer
                          }
                      }
                  }
              }
          } else {
              console.log(`Skipping SVG (no valid path data).`);
          }
      }

      // Log if no answer was found
      if (!answerFound) {
          console.log("No answer found after checking all SVG elements.");
      }
  } catch (error) {
      console.error("An error occurred:", error);
  }
}


// Function to handle claims on Feyorra and Earn Pepe sites
function checkAndClaim() {
  
  handleAlerts(); // Check and handle alerts
  handle404Errors(); // Check and handle 404 errors
  solveIconCaptcha();

  if (window.location.href.includes("feyorra.site")) {
    if (claimFeyorra()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-pepe.com")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  }
}

// Start checking for "Next Video" button
startCheckingForNextVideo();

// Run the check every 1 second for Feyorra and Earn Pepe claims
const claimInterval = setInterval(checkAndClaim, 1000);








