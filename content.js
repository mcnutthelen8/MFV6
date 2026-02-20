(function () {
    // Blocked host keywords
    const blockedHosts = [
        "huggingface.co",
        "huggingface",
        "mediafire.com",
        "gamemodding.com",
        "gamemodding",
        "gta5-mods.com",
        "gta5-mods",
        "aether.mom",
"limewire",
"dogegamer",
        "hianime.to",
        "hianime",
        "4anime.gg",
        "4anime",
        "simkl.com",
        "simkl",
        "aliexpress",
        "animekai.me",
        "animekai.to",
        "animekai",
        "animetosho.org",
        "codepen.io",
        "github.com",
        "megaup.site",
        "pastebin.com",
        "simkl.com",
        "vikingf1le.us.to",
        "vikingfile.com",

        "explore.org",
        "dynamicslab",
        "demo.dynamicslab.ai",
        "learn-anything",
        "hacksplaining",
        "ifixit.com",
        "human.biodigital",
        "photoskop.com",
        "typingclub",
        "myemulator",
        "remove.photos",
        "secretflixcodes",
        "3dtuning",
        "workout.cool",
        "x-minus",
        "buildcores",
        "yoprintables",
        "remusic.ai",
        "chronas",
        "faceonlive",

        "pointerpointer.com",
        "neal.fun",
        "onemillioncheckboxes.com",
        "staggeringbeauty.com",
        "eelslap.com",
        "shademap.co",
        "homicide.watch",
        "worldometers.info",
        "webwithoutwords.com",
        "cookingforengineers.com",
        "notalwaysright.com",
        "artofmanliness.com",
        "cracked.com",
        "quickdraw.withgoogle.com",
        "play2048.co",
        "9gag.com",
        "iwastesomuchtime.com",
        "stellarium-web.org",
        "fallingfalling.com",
        "zoomquilt.org",
        'mediafire',
        'filebin',
        "patreon.com",
        "getintopc.com",
        "mega.nz",
        "drive.google.com",
        "vidu.com",
        "drive.usercontent.google.com",
        "gtaxscripting.blogspot.com",

        "moewalls.com",
        "cursify.vercel.app",
        'contentcore.xyz',
        'pixelmotion.art',
        'catbox.moe',
        'litterbox.catbox.moe',
        'napkin.ai',
        'wolframalpha.com',
        'spline.design',
        'freesewing.eu',
        'chefgpt.xyz',
        'asciiart.eu',

        "docs.google.com",
        "thenewscasts.com"
        
    ];

    // Function to check if current hostname matches blocked list
    function shouldClose(hostname) {
        return blockedHosts.some(domain => hostname.includes(domain));
    }

    const currentHost = window.location.hostname.toLowerCase();

    if (shouldClose(currentHost)) {
        console.log("Blocked domain detected:", currentHost);



        // Close the tab (requires background.js to handle tab closing)
        chrome.runtime.sendMessage({ action: "closeTab" });
    }
})();
(function() {
  // 🔹 Define reusable site groups
  const siteGroups = {
    common: [
      'pubnotepad.com','telegram.org','reddit.com','quora.com','tiktok.com',
      'facebook.com','codepen.io','discourse.julialang.org','pinpaste.com','pinterest.com'
    ],
    anime: [
      'pubnotepad.com','animeforums.net','forums.animeuknews.net','telegram.org',
      'novanon.net','pinpaste.com','reddit.com','quora.com','site.trooporiginals.cloud',
      'discussions.unity.com','anime-planet.com','animekai.to','animetsu.to',
      'tiktok.com','blog.discoveruniversal.com'
    ],
    gaming: [
      'pubnotepad.com','telegram.org','novanon.net','pinpaste.com','reddit.com',
      'tiktok.com','memoryhackers.org','hey-gamer.com','joyfreak.com','hardforum.com'
    ],
  };

  // 🔹 Define links by type
  const linkTypes = {
    link1: [
{ url: 'https://gplinks.co/RrybixVq', sites: siteGroups.common },
{ url: 'https://gplinks.co/poPc7UDt', sites: siteGroups.common },
{ url: 'https://gplinks.co/B5ZRb', sites: siteGroups.common },
{ url: 'https://gplinks.co/BBzFo2Zj', sites: siteGroups.common },
{ url: 'https://gplinks.co/YrTaT', sites: siteGroups.common },
{ url: 'https://gplinks.co/WXiJT8V5', sites: siteGroups.common },
{ url: 'https://gplinks.co/Tm0V9Gh', sites: siteGroups.common },
{ url: 'https://gplinks.co/gGEhA2Rx', sites: siteGroups.common },
{ url: 'https://gplinks.co/mbhlzihK', sites: siteGroups.common },
{ url: 'https://gplinks.co/UBqgI3G', sites: siteGroups.common },
{ url: 'https://gplinks.co/VQZuFFpY', sites: siteGroups.common },
{ url: 'https://gplinks.co/fp7jnWT', sites: siteGroups.common },
    ],
    link2: [


{ url: 'https://shortxlinks.in/9rPEK', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/5iQXS', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/fOUX', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/SSUXU', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/i83Zv5S7', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/evnTk', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/zzOm', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/K0u1eM', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/NIjX', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/Q6LL8', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/DPLGfq', sites: siteGroups.common },
{ url: 'https://shortxlinks.in/DL5R', sites: siteGroups.common },



    ],
    link3: [
        { url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/High-Probability-Trading', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/Crypto-vs-Forex-vs-Stocks-Choosing-Your-Battlefield', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/index?filter=strategies', sites: siteGroups.common },

{ url: 'https://hyperhustle.online/The-Triple-Threat-Strategy', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/Deploy-Applications', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/tools', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/which-exchange-has-the-best-liquidity-for-small-caps', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/which-exchange-has-the-best-liquidity-for-small-caps', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/', sites: siteGroups.common },
{ url: 'https://hyperhustle.online/?page=2', sites: siteGroups.common },


    ],
    link4: [
{ url: 'https://indiaearnx.com/rvad9V5', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/4JwV', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/4fZ', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/z8AB1', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/CIYG3D', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/GsDUC', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/UKh8', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/VDiSM', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/WkvBti', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/bu13X0Sz', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/yPbxqt', sites: siteGroups.common },
{ url: 'https://indiaearnx.com/0dHmw', sites: siteGroups.common },
    ],
    link8: [
{ url: 'https://adurl.io/CJRsBh7', sites: siteGroups.common },
{ url: 'https://adurl.io/U5LX', sites: siteGroups.common },
{ url: 'https://adurl.io/5J4gSO', sites: siteGroups.common },
{ url: 'https://adurl.io/pKOOQL', sites: siteGroups.common },
{ url: 'https://adurl.io/HQRQ', sites: siteGroups.common },
{ url: 'https://adurl.io/rpol8zKw', sites: siteGroups.common },
{ url: 'https://adurl.io/Jf2TCPBm', sites: siteGroups.common },
{ url: 'https://adurl.io/9gSTGpJ', sites: siteGroups.common },
{ url: 'https://adurl.io/uq8UimT8', sites: siteGroups.common },
{ url: 'https://adurl.io/z8GV', sites: siteGroups.common },
    ],
    link5: [
{ url: 'https://link.adlink.click/vai0', sites: siteGroups.common },
{ url: 'https://link.adlink.click/mC9o', sites: siteGroups.common },
{ url: 'https://link.adlink.click/3Vud', sites: siteGroups.common },
{ url: 'https://link.adlink.click/nBAQ', sites: siteGroups.common },
{ url: 'https://link.adlink.click/iaiL', sites: siteGroups.common },
{ url: 'https://link.adlink.click/t1x3', sites: siteGroups.common },
{ url: 'https://link.adlink.click/1xVN', sites: siteGroups.common },
{ url: 'https://link.adlink.click/ARwt', sites: siteGroups.common },
{ url: 'https://link.adlink.click/hwNa', sites: siteGroups.common },
{ url: 'https://link.adlink.click/ZUVQ', sites: siteGroups.common },
    ],

  };

  // 🔹 Get current site
  const currentHost = window.location.hostname.toLowerCase();

  // 🔹 Extract hash from URL (e.g., #link1)
  const hash = window.location.hash.replace('#', '').toLowerCase();

  if (hash && linkTypes[hash]) {
    // Filter links that are valid for currentHost
    const validLinks = linkTypes[hash].filter(entry => {
      return entry.sites.some(site => currentHost.includes(site));
    });

    if (validLinks.length > 0) {
      // Pick random link
      const randomIndex = Math.floor(Math.random() * validLinks.length);
      const chosen = validLinks[randomIndex];

      console.log("Valid links:", validLinks);
      console.log("Random index:", randomIndex);
      console.log("Chosen link:", chosen.url);
      // 🔹 If current host is pinpaste → direct redirect
      if (currentHost.includes('pinpaste.com')) {
        const a = document.createElement('a');
        a.href = chosen.url;
        a.rel = "noreferrer"; // hides referrer
        a.target = "_self";    // open in same tab
        document.body.appendChild(a);
        a.click();
        a.remove();

        return;
      }
      // Redirect via a simulated click
      const a = document.createElement('a');
      a.href = chosen.url;
      a.style.position = 'fixed';
      a.style.left = '-9999px';
      a.style.top = '-9999px';
      a.style.opacity = '0';
      a.target = '_self';
      document.body.appendChild(a);

      const clickEvent = new MouseEvent('click', { bubbles: true, cancelable: true, view: window });
      a.dispatchEvent(clickEvent);

      setTimeout(() => a.remove(), 1000);
    }
  }
})();



function handleButtonClicks() {
    let el = document.querySelector("h5.title i.fas.fa-bolt + span");
    const logoImg = document.querySelector('img[src*="shrinkme"]');

    if (el && el.textContent.trim() === "Breaking") {
        console.log("Found! earns");
    } else if (logoImg) {
        console.log("Found! Seime");
    } else {
        console.log("Not found.");
        return;
    }

    let canClick = true;
    const clickedButtons = new WeakSet();


    function isClickable(el) {
        if (!el) return false;

        const style = window.getComputedStyle(el);
        if (style.display === "none" || style.visibility === "hidden" || style.opacity === "0") {
            return false;
        }

        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return false;

        const midX = rect.left + rect.width / 2;
        const midY = rect.top + rect.height / 2;

        const topEl = document.elementFromPoint(midX, midY);
        return el.contains(topEl) || topEl === el;
    }


    function simulateClick(button) {
        const rect = button.getBoundingClientRect();
        const randomX = rect.left + Math.random() * rect.width;
        const randomY = rect.top + Math.random() * rect.height;

        ["mousedown", "mouseup", "click"].forEach(evt => {
            button.dispatchEvent(new MouseEvent(evt, {
                bubbles: true,
                cancelable: true,
                clientX: randomX,
                clientY: randomY,
                buttons: 1
            }));
        });

        console.log("[ButtonClick] Simulated click on:", button.textContent.trim() || button.id);
    }

    const allSelectors = [
        '#btn1',
        '#btn2',
        '#tp-snp2',
        'button.tp-btn',
        'button.tp-blue'
    ];

    function checkAndClickButtons() {
        if (!canClick) return setTimeout(checkAndClickButtons, 500);

        const waitingDiv = document.querySelector("#newtimer");
        if (waitingDiv && isClickable(waitingDiv)) {
            console.log("[ButtonClick] Waiting for timer...");
            return setTimeout(checkAndClickButtons, 1000);
        }

        for (const selector of allSelectors) {
            const buttons = document.querySelectorAll(selector);

            for (const button of buttons) {
                if (!isClickable(button)) {
                    console.log("[ButtonClick] Found but not clickable yet:", selector);
                    continue;
                }
                if (clickedButtons.has(button)) continue;

                simulateClick(button);
                clickedButtons.add(button);

                canClick = false;
                setTimeout(() => {
                    canClick = true;
                    console.log("[ButtonClick] Ready for next after 5s");
                }, 5000);

                return setTimeout(checkAndClickButtons, 500);
            }
        }

        setTimeout(checkAndClickButtons, 500);
    }

    checkAndClickButtons();
}

setTimeout(handleButtonClicks, 2000);


function handleMdTimerSite() {
    const mdTimer = document.querySelector("#mdtimer");
    if (!mdTimer) {
        console.log("[MDTimer] Not this site.");
        return;
    }
    console.log("[MDTimer] Correct site detected.");

    let canClick = true;
    const clickedButtons = new WeakSet();

    // Visibility check
    function isVisuallyVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        if (style.display === "none" || style.visibility === "hidden" || style.opacity === "0") {
            return false;
        }
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return false;
        return true;
    }

    // Simulate realistic click
    function simulateClick(button) {
        const rect = button.getBoundingClientRect();
        const randomX = rect.left + Math.random() * rect.width;
        const randomY = rect.top + Math.random() * rect.height;

        button.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, clientX: randomX, clientY: randomY, buttons: 1 }));
        button.dispatchEvent(new MouseEvent("mouseup", { bubbles: true, clientX: randomX, clientY: randomY, buttons: 1 }));
        button.dispatchEvent(new MouseEvent("click", { bubbles: true, clientX: randomX, clientY: randomY, buttons: 1 }));

        console.log("[MDTimer] Clicked:", button.id || button.textContent.trim());
    }

    function checkMdTimer() {
        if (!canClick) return setTimeout(checkMdTimer, 500);

        // If timer visible -> wait
        if (isVisuallyVisible(mdTimer)) {
            console.log("[MDTimer] Waiting for countdown...");
            return setTimeout(checkMdTimer, 1000);
        }

        const selectors = ["#next", "#nextbutton","#nexthead"];
        for (const selector of selectors) {
            const btn = document.querySelector(selector);
            if (!btn || !isVisuallyVisible(btn)) continue;
            if (clickedButtons.has(btn)) continue;

            simulateClick(btn);
            clickedButtons.add(btn);

            canClick = false;
            setTimeout(() => {
                canClick = true;
                console.log("[MDTimer] Ready for next after 5s");
            }, 10000);

            return setTimeout(checkMdTimer, 500);
        }

        setTimeout(checkMdTimer, 500);
    }

    checkMdTimer();
}

// Start after delay
setTimeout(handleMdTimerSite, 2000);


// Start with longer random initial delay
setTimeout(handleButtonClicks, 2000);
function handleMrProBloggerSite() {
    if (!window.location.href.includes("en.mrproblogger.com")) {
        console.log("[MrProBlogger] Not the target site.");
        return;
    }
    console.log("[MrProBlogger] Target site detected.");

    const getLinkSelector = "a.get-link[href*='adobe-photoshop-2023-free-download']";
    const countdownSelector = "#countdown #timer";

    function isVisuallyVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        if (style.display === "none" || style.visibility === "hidden" || style.opacity === "0") return false;
        const rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
    }

    function scrollToLink() {
        const link = document.querySelector(getLinkSelector);
        if (link && isVisuallyVisible(link)) {
            console.log("[MrProBlogger] Scrolling to Get Link button...");
            link.scrollIntoView({ behavior: "smooth", block: "center" });
        } else {
            console.log("[MrProBlogger] Link not visible yet, retrying...");
            setTimeout(scrollToLink, 500); // retry until visible
        }
    }

    function checkTimer() {
        const timerEl = document.querySelector(countdownSelector);
        if (!timerEl) {
            console.log("[MrProBlogger] Timer not found, stopping.");
            return;
        }

        const timeValue = parseInt(timerEl.textContent.trim(), 10);
        if (timeValue === 0) {
            scrollToLink(); // start looping scroll until visible
        } else {
            console.log("[MrProBlogger] Waiting for timer, current:", timeValue);
            setTimeout(checkTimer, 500);
        }
    }

    checkTimer();
}

setTimeout(handleMrProBloggerSite, 2000);







function handleBlogButtons() {

    if (!window.location.hostname.includes("blogspot") || !window.location.hostname.includes("blog") || !window.location.hostname.includes("zyrox")) {
        return;
    }

    function isVisible(el) {
        return el && el.offsetParent !== null && window.getComputedStyle(el).display !== "none";
    }


    function scrollAndClick(button) {
        button.scrollIntoView({ behavior: "smooth", block: "center" });
        console.log("Scrolled to continue button.");
        button.click();
        console.log("Clicked continue button.");
    }

    const intervalId = setInterval(() => {
        const timerDiv = document.querySelector("#timer");
        const continueBtn = document.querySelector("#continueBtn");

        if (timerDiv && isVisible(timerDiv) && timerDiv.textContent.includes("Scroll down and click continue")) {
            if (continueBtn && isVisible(continueBtn)) {
                scrollAndClick(continueBtn);
                clearInterval(intervalId); // stop after clicking
            } else {
                console.log("Continue button not visible yet, waiting...");
            }
        } else {
            console.log("Timer div not found or not visible, waiting...");
        }
    }, 1000); // check every 1 second
}

// Start the function
handleBlogButtons();
/**
 * SCRIPT 1: THE JANITOR (gpscroll)
 * Focused on finding "Scroll Only" targets and clearing obstacles (ads).
 */
function gpscroll() {
    const scrollOnlySelectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];
    const styleId = 'ui-helper-styles';

    if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.innerHTML = `
            .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
            .obstacle-ghost { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
        `;
        document.head.appendChild(style);
    }

    const processedElements2 = new WeakSet();

    function rescueAndPrepare(btn) {
        if (!btn || processedElements2.has(btn)) return;
        const rect = btn.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;

        let topEl = document.elementFromPoint(x, y);
        let loopLimit = 0;
        while (topEl && topEl !== btn && !btn.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
            topEl.classList.add('obstacle-ghost');
            topEl = document.elementFromPoint(x, y);
            loopLimit++; 
        }
        btn.classList.add('btn-rescue-active');
        processedElements2.add(btn);
        setTimeout(() => {
            processedElements2.delete(btn);
            btn.classList.remove('btn-rescue-active');
        }, 10000);
    }

    function isVisible(el) {
        if (!el) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0);
    }

    setInterval(() => {
        for (const selector of scrollOnlySelectors) {
            const btn = document.querySelector(selector);
            if (isVisible(btn)) {
                const btnText = (btn.innerText || "").toLowerCase();
                if (btnText.includes("wait") || btnText.includes("...")) continue;

                const rect = btn.getBoundingClientRect();
                if (rect.top < 0 || rect.bottom > window.innerHeight) {
                    btn.scrollIntoView({ behavior: "smooth", block: "center" });
                }
                rescueAndPrepare(btn);
                break; 
            }
        }
    }, 1500);
}

/**
 * SCRIPT 2: THE EXECUTOR (indi)
 * Focused strictly on sorting and clicking "Active" buttons.
 */
function indi() {
    const clickSelectors = ["#robotButton", "#robot", "#robot2", "#rtgli1", "#rtg-generate", "#robotContinueButton", "#open-continue-btn", "#rtg-snp2"];
    const blacklisted = new WeakSet(); 
    let isLocked = false;

    function isVisible(el) {
        if (!el || blacklisted.has(el)) return false;
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        return (style.display !== 'none' && rect.width > 0);
    }

    async function naturalClick(element) {
        blacklisted.add(element); 
        const props = { view: window, bubbles: true, cancelable: true, buttons: 1 };
        element.dispatchEvent(new PointerEvent('pointerdown', props));
        element.dispatchEvent(new MouseEvent('mousedown', props));
        await new Promise(r => setTimeout(r, 100));
        element.dispatchEvent(new PointerEvent('pointerup', props));
        element.dispatchEvent(new MouseEvent('mouseup', props));
        element.dispatchEvent(new MouseEvent('click', props));
        setTimeout(() => blacklisted.delete(element), 15000);
    }

    setInterval(() => {
        if (isLocked) return;
        let foundButtons = [];

        clickSelectors.forEach(selector => {
            document.querySelectorAll(selector).forEach(el => {
                if (isVisible(el)) foundButtons.push(el);
            });
        });

        if (foundButtons.length === 0) return;

        // Sort by bottom-most first
        foundButtons.sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top);

        const btn = foundButtons[0];
        const rect = btn.getBoundingClientRect();
        
        // Scroll if needed
        if (rect.top < 0 || rect.bottom > window.innerHeight) {
            btn.scrollIntoView({ behavior: "smooth", block: "center" });
            return; 
        }

        // Click logic
        isLocked = true;
        setTimeout(async () => {
            await naturalClick(btn);
            isLocked = false;
        }, 1000);
    }, 1500);
}

// Start both
gpscroll();
indi();
function setupDeadEndRedirect() {
    if (!window.location.href.includes("powergam.online")) return;

    let secondsMissing = 0;

    const checkStatus = () => {
        // SAFETY: If the browser is still spinning/loading, don't count yet
        if (document.readyState !== 'complete') return; 

        const timerDiv = document.querySelector("#myTimerDiv");
        const scrollSelectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];
        
        const anyButtonVisible = scrollSelectors.some(selector => {
            const el = document.querySelector(selector);
            return el && el.offsetHeight > 0; // Check if it's actually drawn on screen
        });

        // If something is happening, reset the timer
        if (timerDiv || anyButtonVisible) {
            secondsMissing = 0; 
        } else {
            secondsMissing++;
        }

        if (secondsMissing >= 5) {
            window.location.href = "https://web.telegram.org/a/get#link1";
        }
    };

    setInterval(checkStatus, 1000);
}
setupDeadEndRedirect()
