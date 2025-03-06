

function claimEarnPepe() {
  // Find the element with the text "Verified!"
  //const verifiedBadgeFeyorra = document.evaluate(
  //  "//*[contains(text(), 'Verified!')]",
  //  document,
   // null,
  //  XPathResult.FIRST_ORDERED_NODE_TYPE,
  //  null
  //).singleNodeValue;

  // Find error messages within the form
  // Find the claim button
  const claimButtonEarn = document.querySelector("button#ClaimBtn");

  // Base64 encoded image check
  //const wrong64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAAZCAYAAACmRqkJAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAClUlEQVRYhe2Zy2sTURjFzxmDKLjrSvNonk1o0o0gFEFwoeBCcCUiVNwJ/gUiinShiKIb6cbuREHcKIILQRFBlIrgQtMYkyamwbgRd4IiyufiTieZVybTTjEmczZz5ztzv7nz475mhvApqUwIoAEkAA2AfmRP2ckfpA7YJ4+Lb8R681p81zx2n/EF+uHhebEs7xDbzUYYoLV9jF3vy8jVlOXt4nqzMQK4VmbsqiMrzRneNnEDO66Sz2ccmdgASnlrCM9F0jlrY2MCKOVICM9D0jlnYmQAlPKWEN6Aks55g5XjHBhqcGkAIGUG2vtYaIL5RpAph07SuSAAEPFbkdPfnBNW4xtsUvBi8i4AQFpzzn5iUfnt0+u+h2+AUpkAoIHTX9X5h52wzgRSTev7qtGXb4BeYqFllOVjrhvPV1SsNgNOvVPl+u6un3ttyiMr+7pe5pnZax5S8fQjdf7piDpP3VfnraNg8l63fvKOiq+e9P08XtKkjEDnP6km+/qcet8t597qxzeqbn0WsrJXxbIv1DHzXHmNA5DGQRVLP/ZuR+tYT3kOsnpisAfwIfkyLxGWwKAhrlfMLf3rJvgSd80z8CHsJanNAKAxjE1efdbyrrvJbWmfwgDfU/pqKPeBzL40hnBgOSdvg5O3zLHEIpi4uaG8gQJkoW1aRJivg/maZz2p71HX55bA7CsV0xcRaexXXuYpmHmiYvoiIs3Dyks9BFMP7Hlbx5W/iYuI0X/Vq5zTZ6bwc5ZTHUYvEhjSIfw/yQDI0p/x2PkGoLXeB1h6IEu/Q4geYvSSiZFtCLP0K4ToIkYv29g4zoEs/gwhWsTYFUcmrhtpFn8Q0P/KjbEYu9a3M3m+ibD43ZRA/RceXTF+w9fo+wsjErFwOeJlIQAAAABJRU5ErkJggg==";

  //const base64Src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAAAZCAYAAACvrQlzAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACt0lEQVRoge2Zz6tMYRjHv8+YSFkpKfN7zox7ppmIjZRiw45SUtdCKf4HIt0FEVnIhpJbUnI3REpuZCGSsppx586dMedeRmSrRPRYnDk/3jnv+TlNI3M+m5nn13nevr3ve857DiEk/H49AwmACEACgO2XBmwknD5pjk+NZ78gOR41PmOizDUKo49vMjfWsbPp5Ag6mEPpK56auQa5sZbdm06uoIZN6UtS7RJyMdewm9AxOvzppFQjh6BcXx2LGRDunXJoJQjK9WQsZki4d1rQzBSU66tiMSPCvTOmdtI9NCY6CQDgOv1Ts5NKr0GlV/KY8gykzIOUp85Y4SGo8CB63+wNUPZ6pFrunWVgiBlKlW+gyleb3QOpH6NeLlhP5TkAgDt7dbv4ZKT9opAc9wBkcHsn/M4c3NnXfza0+boHMO5dbGSCktoVbF5Udf/mhiOXl7ZbdeU3lr+9K3i/4iOrrntQjOXvif2Wj1qx3K3APYKQ4Doi7Z+8sMHpa2YAAKRqfVsBL5Z131RTzG1tAbe26rHyO8u/tEPaj5QXtv/zzt4f9svr8nN6XJsGa0d0X+52/3dWj60cB6+ckNaHgT/PcJJqoKii+kFqx38QrW39Y55PXmePKaqxh4YaS/5u6JrQPTbN0NBLnipfXGPcVAbOwOODtWmIZ/nRMNSVeWGj7X/KNY+mWo4lPy4od8dc8qNgJDclbuZBqiYseeOm5AWV34p26aVe297tXVd8LNqF+3pd9xBYOwzKz8G+5I2bEi8fA+VmQdmbvmMLirl56UfPoK/B4td3g/0odY6AcW9s/yGmoFT7E+pVf4yFMTuBgRlKtd+xqCGh1HlBM8eSp9qvWNSAUOqCQyvpHkrVn7GoPlD6olQj18cmqv4gwPjqGWNA6cuek833OZSq34UL6N/lJwfKXA21Wv8CNLm9CSlHmuUAAAAASUVORK5CYII=";
  //const timeoutb64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAAAZCAYAAACvrQlzAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACkklEQVRoge2ZzWsTQRjGn2cNiuBJ8GLSNGnSJCWhB8FDBUEQQRA8iUIRT4L/gqJID4qieBCP9iQi6EURBEEUQbGIICiJxny0aTGCeBVEUV4Ps9lks5v9Mqux2ecyM+87887sj/nY2SV8St5tFUADSAAagJ6UfWVoVpttHZc2jv15qePQxmVMnLhGP3xcK0tli1g7HR+g/XWYuOLIbKBTKptlcKfjC7RTZuKSLTvNHuYmGQQ6kpJ8PGnLyAJUyhsjmB4l7VMWViagUo5FMH1K2qdNzAygUt4QwQwoaZ8x2NnuoZGCSwMAKTOU2clCE8zXwwg9cpL2WQGAWNAAnPliH7iaDBoyNDF1GwAgrXl7f3JR+ddO/HFfgYHK+20ANHDms16O6+9qPXWqGYttvSswUDexsGLk5UOua89VlK02C+beqHx9R9c//dIURxq7u77ME7Nveb+yTz1Q5ZWDqpy+q5cPgak73fapW8q+esz/A3mUJmWEsn9KNe3oZ+5tNz/9Wk9fqbaNOUhjl7Jln6k081T5mnshzX3KNvXQfRytwz35ecjqUY9P4F/yaUFiLIFhQQ0qZpf+9RACidsXGNqSd5PUZgHQWPYmX2MO5rt1yGNZOz60fkb6xGD2ubHkhxZz8iY4ecNsSy6CyetDiR8KUBZapkOJ+RqYr7q2k/pOVT+7BGZfKJt+KElzj/JlHoOZR8qmH0qyfED50vfB9D1r3NYR5f8Lh5Ixz9XV0+tnsOjzXX9/jJ8jMOJL/n+UAZSlX+Hv/utUndkJ9M1Qln5GUH2K8fMmZpYlz9KPCKpHMX7Bwsp2D2XxewTVRUxctGU08MWexW8EOn89I3XExGXHyeZ6U2LxqymA+i8/PuLEVV+r9TeO4rFjvkpYjgAAAABJRU5ErkJggg==";

  //const imageExists = [...document.querySelectorAll("img")].some(img => img.src === base64Src);
  //const imageExists2 = [...document.querySelectorAll("img")].some(img => img.src === timeoutb64);
  //const imageExists3 = [...document.querySelectorAll("img")].some(img => img.src === timeoutb64);
  //console.log("imageExists: ", imageExists);
  //console.log("imageExists2: ", imageExists2);
  //console.log("imageExists3: ", imageExists3);
  function checkFormForIcons() {
      let xpathExpression = `//form[@method="POST"]//*[contains(@class, "bxs-") or 
          contains(@class, "bx-") or contains(@class, "la-") or 
          contains(@class, "fa-") or contains(@class, "fas fa-") or 
          contains(@class, "far fa-") or contains(@class, "ri-") or 
          contains(@class, "ti ti-") or contains(@class, "bi bi-") or 
          contains(text(), "Pick the one clear, similar icon from above.")]`;

      // Evaluate XPath expression
      let matchingElements = document.evaluate(xpathExpression, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);

      let filteredElements = [];
      console.log("All matching elements with computed styles:");

      for (let i = 0; i < matchingElements.snapshotLength; i++) {
          let element = matchingElements.snapshotItem(i);
          let style = window.getComputedStyle(element);

          let opacity = parseFloat(style.opacity); // Convert opacity to a number
          let filter = style.filter.trim(); // Trim spaces

          //console.log(`Element ${i}:`, element);
          //console.log(`  Opacity: ${opacity}`);
          //console.log(`  Filter: ${filter}`);

          // Extract opacity from filter if it exists
          let filterOpacityMatch = filter.match(/opacity\(([\d.]+)\)/);
          let filterOpacity = filterOpacityMatch ? parseFloat(filterOpacityMatch[1]) : null;

          // Keep elements where opacity is > 0.5 OR no filter opacity is applied
          if ((filterOpacity === null || filterOpacity > 0.5) && opacity > 0.5) {
              filteredElements.push(element);
          }
      }

      ///onsole.log("Filtered elements (opacity > 0.5):", filteredElements);

      // Return false if more than 6 elements, otherwise true
      return filteredElements.length <= 6;
  }


  const checkFormFor = checkFormForIcons();
  console.log("checkFormForIcons: ",checkFormFor); // Returns true if found, otherwise false

  const base64Images = [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZElEQVRYhc1YSxbDIAjEvt4p99/hqezC15QCAqJJO6tEh8+AT02grQERFz3cEAK25OEinahhKKdG5KjIlXLGbfGNIJM6N6ymO7lrfcb7sOKz46blehGYqqTIG/aV7ZA5w2jalXeRftXtVGISH5GzxnE+AADwJQNvuMxZzxKPM9hxHCBQSimlyGeJWqs7cg52Pz3L/qySI0BEnxQvVYTPtvXFDrgI+nnm6kdb2khDZHXP8dYaa1etlS4fyjQCscEQqGK1A0A6KevHwqsFlq9nFVhcwzASaASdQdWOUmGV6nmr9xWZyig5VSQLxCLmRcrArPBdj5pfRGT3EBRpcLaJtGOrq4hBSlLJcg27gRh/p8imtdeoOt2HbIcjplplOT5CkTb/D7Ytu3iw9/ShnEDw/iAxpRBgx4mcw3WfbHLqDpH2p2Pk8r1YkaHIqf8Of4ivo37W4LdIZIKI/rUu7T1ou7eCqrcXOd5OshXZ9OEAAAAASUVORK5CYII=",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXB",
    ];
    const base64Images2 = [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUgAAAAXCAIAAADm2UHyAAAACXB",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI"
    ];
  //Check if any image on the page matches a base64 image from the list
  const imageExists = [...document.querySelectorAll("img")].some(img => {
    return base64Images.some(prefix => img.src.startsWith(prefix));
  });
  const imageExists2 = [...document.querySelectorAll("img")].some(img => {
    return base64Images2.some(prefix => img.src.startsWith(prefix));
  });

  console.log("imageExists: ", imageExists);
  console.log("imageExists2: ", imageExists2);
  // If there's an error message, log and stop execution
  //if (imageExists2  && claimButtonEarn || imageExists3  && claimButtonEarn || imageExists  && claimButtonEarn) {
  if (imageExists && claimButtonEarn) {
    console.log("verified on ");
    claimButtonEarn.click();
    return true; // Stop further execution
  }
  if (checkFormFor && imageExists2) {
    console.log("Error: Oops, wrong selection! Please refresh the page.");
    location.reload();

    return false; // Stop further execution
  }
  // If CAPTCHA is still loading, do not proceed
  //if (loadingCaptcha) {
  //  console.log("Loading CAPTCHA, please wait...");
  //  return false; // Stop execution until CAPTCHA is loaded
  //}

  // If the verification badge is found and the claim button exists, click it
  //if (verifiedBadgeFeyorra && claimButtonEarn) {
  //  console.log("Verified on claimEarnPepe.site - Clicking the Claim button...");
  //  claimButtonEarn.click();
  //  return true; // Stop the interval if the claim button is clicked
  //}

  return false;
}

//data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZUlEQVRYhc1XS7IDIQjsyaXm/js81WSRCkUQENFM0otXLwzStPhBXH8MIuK/3tcMkHfdAiLqGZM5lFNFbZhHuThlu2ZcxamL3JXEt5cSEc2JVAntLWYwUG7OQvyBSI5489YtM5obHisRb0C5ehLj5bo+owAATYQ35BC2JEnNyEYC+ShBxNlU2KI+eRTeWZBM6Q6RQXLDwyaZXuxcFAmB3uItQjOsMpqeZsFNfxMPhOhpABzHIbW9firB0qjAn5RPn71JpIwKrTVbhoK8Nl514IheaK84Xt0CanQV47Ug/4/j6ARMpv5s5HBMo1sn4eCJ5PvAS07ZTbeKyMx1H3B7lYyvkIJIk6heySH3JaoR8+ETwdGPDr3dc94jUiE+r2ebh0KzMTvki6+Q+LG7d6biOCmRmX37k+432/1lxq8L+O0DILtcpzRvfCUV4vQ4Lutkk2itnecZ+/w5Bm0dgFih3UYtY2/YJ2n06l2xShOUAAAAAElFTkSuQmCC


//data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABW0lEQVRYhc1YSRICIQzM+Kn5/y28Cg+xqJhtwqp9sJiYpRsyCAIi1lrpcwwtdibJVsASZjvk6ZzDVWC45BkM1NUhWZFjDLjDD5u5Q+QYy5NRHqZWMo/fSoUg13yNP9lvr1orbMZ1XQAgCpFR2E3P3swar8csjQ0fT4KTy+cspYyVexBpVuotRj2T+crzpIr3fYOSiohZBh50bRq31O2tM9NyBl5aYTQ9hb1LAiLaHnzD4CLpK6LejOTsTYf3GOg0H9s4KOQh4fEtslrt1Izmdqqp8GnSnl537BUpJp6PBaEgQ2wx7cFq6/aJJAiuGZaiXYG9/Znw6i+7uZJi3LWSn7kIPLgkk+XjpJr9Zop89NQrLDwD9B3r4svn397aXJFnLhBx5pVnV5Exn/oMxd5sWsjILUQ37dp/QJY3TmrjOUNlBjFJ+Rsdx6yqfSCcx2avWqUUOh/vAz+Fr8Ubw0ctwQSEWrUAAAAASUVORK5CYII=
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
    "//form[@id='Claimformx']//div[contains(text(), '0')]",
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

  if (window.location.href.includes("feyorra.site/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-pepe.com/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-bonk.com/member/faucet")) {
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  } else if (window.location.href.includes("earn-trump.com/member/faucet")) {
    console.log("earn-trump.com.");
    if (claimEarnPepe()) {
      clearInterval(claimInterval); // Stop the loop if claimed
    }
  }
  console.log("checkAndClaim");
}

// Run the check every 1 second for Feyorra and Earn Pepe claims
const claimInterval = setInterval(checkAndClaim, 1000);
