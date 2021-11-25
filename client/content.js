chrome.runtime.sendMessage({ todo: "showPageAction" })


window.addEventListener('load', function () {

    let body = document.querySelector('body');
    let author = `<span class="author"> - just kidding</span`;

    body.innerHTML = `Google is down today! ${author}`;


}, false);



