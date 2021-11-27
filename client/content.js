chrome.runtime.sendMessage({ todo: "showPageAction" })

window.addEventListener('load', function () {

    let body = document.querySelector('body');
    let jokes = [
        "Sorry, Google is down today!",
        "<a href='https://duckduckgo.com'>DuckDuckGo</a> is better.",
        "I'm Watching You... 😶",
        "I know you better than you know yourself. I'm google bro.",
        "I'm Sick. I've overdosed on privacy",
        "<a href='https://duckduckgo.com'>DuckDuckGo</a> is better.",
        "I've been admitted in a hospital. I've overdosed on monopoly.",
        "<span style='color:red'>Google Virus found!!</span>",
        "I'm tired.",
        "😴"
    ]
    
    body.innerHTML = `<p>${ jokes[Math.floor(Math.random() * jokes.length)] }</p>`;

}, false);



