// Example to handle messages, if you need it for more complex scenarios
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'clickPlayButton') {
      // Possibly interact with content scripts or other background tasks
      console.log("Message received to click play button");
    }
  });
  